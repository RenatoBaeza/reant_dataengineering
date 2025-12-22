# Backend Data Pipeline

This directory contains the Python data pipeline that fetches weather data from the Open-Meteo API, processes it with pandas, and stores it in Supabase.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

3. Add your Supabase credentials to `.env`:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
```

## Running the Pipeline

Run the pipeline locally:
```bash
python pipeline.py
```

## Supabase Table Schema

Make sure you have created the following table in your Supabase project:

```sql
CREATE TABLE weather_data (
  id SERIAL PRIMARY KEY,
  location VARCHAR(255),
  temperature FLOAT,
  humidity FLOAT,
  wind_speed FLOAT,
  timestamp TIMESTAMP DEFAULT NOW()
);
```

## API Used

This project uses the [Open-Meteo API](https://open-meteo.com/), which is free and doesn't require an API key.

