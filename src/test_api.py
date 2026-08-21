import os
from pathlib import Path

import requests
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)

api_key = os.getenv("NLR_API_KEY")
email = os.getenv("NLR_EMAIL")

url = "https://developer.nlr.gov/api/wind-toolkit/v2/wind/india-wind-download.csv"

parameters = {
    "api_key": api_key,
    "wkt": "POINT(75.36621 24.72687)",
    "attributes": "windspeed_100m,winddirection_100m,temperature_100m,pressure_100m",
    "names": "2014",
    "interval": 60,
    "utc": "true",
    "leap_day": "false",
    "email": email
}

response = requests.get(url, params=parameters)

print("Status code:", response.status_code)
print("Content type:", response.headers.get("Content-Type"))
print("Response preview:", response.text[:500])