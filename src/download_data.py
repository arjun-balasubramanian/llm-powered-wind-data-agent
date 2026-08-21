import os
from pathlib import Path

import requests
from dotenv import load_dotenv


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

# Load environment variables
load_dotenv(ENV_FILE)

api_key = os.getenv("NLR_API_KEY")
email = os.getenv("NLR_EMAIL")

# API endpoint
url = "https://developer.nlr.gov/api/wind-toolkit/v2/wind/india-wind-download.csv"

# Request parameters
parameters = {
    "api_key": api_key,
    "wkt": "POINT(75.36621 24.72687)",
    "attributes": "windspeed_100m,winddirection_100m,temperature_100m,pressure_100m",
    "names": "2014",
    "interval": 15,
    "utc": "true",
    "leap_day": "false",
    "email": email
}

# Make API request
response = requests.get(url, params=parameters)

# Check response
response.raise_for_status()

# Create raw data directory if it doesn't exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Save CSV
output_file = RAW_DATA_DIR / "india_wind_site_83343_15min_2014.csv"

with open(output_file, "wb") as file:
    file.write(response.content)

print(f"Data downloaded successfully.")
print(f"Saved to: {output_file}")