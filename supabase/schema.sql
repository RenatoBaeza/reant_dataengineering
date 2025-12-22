-- Weather Data Table Schema
-- Run this in your Supabase SQL Editor

CREATE TABLE IF NOT EXISTS weather_data (
  id SERIAL PRIMARY KEY,
  location VARCHAR(255) NOT NULL,
  temperature FLOAT,
  humidity FLOAT,
  wind_speed FLOAT,
  timestamp TIMESTAMP DEFAULT NOW()
);

-- Create an index on timestamp for faster queries
CREATE INDEX IF NOT EXISTS idx_weather_data_timestamp ON weather_data(timestamp DESC);

-- Create an index on location for faster filtering
CREATE INDEX IF NOT EXISTS idx_weather_data_location ON weather_data(location);

-- Enable Row Level Security (RLS) - optional but recommended
ALTER TABLE weather_data ENABLE ROW LEVEL SECURITY;

-- Create a policy that allows anyone to read data (for public dashboard)
CREATE POLICY "Allow public read access" ON weather_data
  FOR SELECT USING (true);

-- Create a policy that allows insert (for your backend pipeline)
-- Note: In production, you should use a service role key for inserts
-- This policy allows inserts with the anon key for development
CREATE POLICY "Allow public insert access" ON weather_data
  FOR INSERT WITH CHECK (true);

