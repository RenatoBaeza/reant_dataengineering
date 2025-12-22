"""
Data Engineering Pipeline
Fetches weather data from Open-Meteo API, processes it with pandas, and stores in Supabase
"""

import requests
import pandas as pd
from datetime import datetime
from supabase import create_client, Client
from config import (
    SUPABASE_URL,
    SUPABASE_KEY,
    WEATHER_API_BASE_URL,
    DEFAULT_LOCATIONS,
)


def fetch_weather_data(location: dict) -> dict:
    """
    Fetch weather data from Open-Meteo API for a given location
    
    Args:
        location: Dictionary with name, latitude, and longitude
        
    Returns:
        Dictionary containing weather data
    """
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto",
    }
    
    try:
        response = requests.get(WEATHER_API_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        current = data.get("current", {})
        
        return {
            "location": location["name"],
            "temperature": current.get("temperature_2m", None),
            "humidity": current.get("relative_humidity_2m", None),
            "wind_speed": current.get("wind_speed_10m", None),
            "timestamp": datetime.now().isoformat(),
        }
    except Exception as e:
        print(f"Error fetching data for {location['name']}: {str(e)}")
        return None


def process_data(weather_records: list) -> pd.DataFrame:
    """
    Process weather data using pandas
    
    Args:
        weather_records: List of weather data dictionaries
        
    Returns:
        Processed pandas DataFrame
    """
    # Filter out None values
    valid_records = [record for record in weather_records if record is not None]
    
    if not valid_records:
        print("No valid records to process")
        return pd.DataFrame()
    
    # Create DataFrame
    df = pd.DataFrame(valid_records)
    
    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    
    # Round numeric columns
    numeric_columns = ["temperature", "humidity", "wind_speed"]
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").round(2)
    
    # Add derived metrics
    df["temperature_fahrenheit"] = (df["temperature"] * 9/5) + 32
    df["wind_speed_kmh"] = df["wind_speed"] * 3.6
    
    return df


def save_to_supabase(df: pd.DataFrame, supabase: Client):
    """
    Save processed data to Supabase
    
    Args:
        df: Processed pandas DataFrame
        supabase: Supabase client instance
    """
    if df.empty:
        print("No data to save")
        return
    
    # Convert DataFrame to list of dictionaries
    records = df.to_dict("records")
    
    # Prepare data for Supabase (only include columns that exist in the table)
    supabase_records = []
    for record in records:
        supabase_records.append({
            "location": record["location"],
            "temperature": record.get("temperature"),
            "humidity": record.get("humidity"),
            "wind_speed": record.get("wind_speed"),
            "timestamp": record["timestamp"].isoformat() if pd.notna(record["timestamp"]) else None,
        })
    
    try:
        # Insert data into Supabase
        result = supabase.table("weather_data").insert(supabase_records).execute()
        print(f"Successfully inserted {len(supabase_records)} records into Supabase")
        return result
    except Exception as e:
        print(f"Error saving to Supabase: {str(e)}")
        raise


def main():
    """
    Main pipeline execution function
    """
    print("Starting data pipeline...")
    
    # Validate Supabase configuration
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in environment variables")
    
    # Initialize Supabase client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Fetch weather data for all locations
    print("Fetching weather data...")
    weather_records = []
    for location in DEFAULT_LOCATIONS:
        print(f"Fetching data for {location['name']}...")
        data = fetch_weather_data(location)
        if data:
            weather_records.append(data)
    
    # Process data with pandas
    print("Processing data with pandas...")
    df = process_data(weather_records)
    
    if df.empty:
        print("No data to process")
        return
    
    print(f"Processed {len(df)} records")
    print("\nData Summary:")
    print(df[["location", "temperature", "humidity", "wind_speed"]].to_string())
    
    # Save to Supabase
    print("\nSaving to Supabase...")
    save_to_supabase(df, supabase)
    
    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()

