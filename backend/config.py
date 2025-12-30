import os
from dotenv import load_dotenv

# Load .env file if it exists (for local development)
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "").strip()

# Validate configuration
if not SUPABASE_URL:
    raise ValueError(
        "SUPABASE_URL environment variable is not set. "
        "Please set it in your environment or GitHub Secrets."
    )
if not SUPABASE_KEY:
    raise ValueError(
        "SUPABASE_KEY environment variable is not set. "
        "Please set it in your environment or GitHub Secrets."
    )

# Validate URL format
if not SUPABASE_URL.startswith("https://"):
    raise ValueError(
        f"SUPABASE_URL must start with 'https://'. Got: {SUPABASE_URL[:20]}..."
    )

# API configuration
WEATHER_API_BASE_URL = "https://api.open-meteo.com/v1/forecast"

# Default locations to fetch weather data for
DEFAULT_LOCATIONS = [
    {"name": "New York", "latitude": 40.7128, "longitude": -74.0060},
    {"name": "London", "latitude": 51.5074, "longitude": -0.1278},
    {"name": "Tokyo", "latitude": 35.6762, "longitude": 139.6503},
    {"name": "Sydney", "latitude": -33.8688, "longitude": 151.2093},
    {"name": "Paris", "latitude": 48.8566, "longitude": 2.3522},
]

