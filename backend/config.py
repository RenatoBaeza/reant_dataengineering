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

# Validate API key format (JWT tokens start with 'eyJ' and have 3 parts separated by dots)
if not SUPABASE_KEY.startswith("eyJ"):
    raise ValueError(
        f"SUPABASE_KEY appears to be invalid. JWT tokens should start with 'eyJ'. "
        f"Got key starting with: {SUPABASE_KEY[:10] if len(SUPABASE_KEY) >= 10 else SUPABASE_KEY} "
        f"(length: {len(SUPABASE_KEY)})"
    )

# Check JWT format (should have 3 parts: header.payload.signature)
key_parts = SUPABASE_KEY.split(".")
if len(key_parts) != 3:
    raise ValueError(
        f"SUPABASE_KEY appears to be malformed. JWT tokens should have 3 parts separated by dots. "
        f"Found {len(key_parts)} parts. Key length: {len(SUPABASE_KEY)}"
    )

# Debug output (safe - only shows lengths and first/last few chars)
print(f"✓ SUPABASE_URL configured (length: {len(SUPABASE_URL)})")
print(f"✓ SUPABASE_KEY configured (length: {len(SUPABASE_KEY)}, starts with: {SUPABASE_KEY[:10]}...)")

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

