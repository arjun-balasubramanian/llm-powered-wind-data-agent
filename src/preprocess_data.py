#Read the raw CSV.
#Skip the API metadata row.
#Combine Year, Month, Day, Hour, and Minute into one timestamp.
#Remove the five original time columns.
#Rename the weather columns to clean Python-friendly names.
#Sort chronologically.


from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "india_wind_site_83343_15min_2014.csv"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = PROCESSED_DIR / "india_wind_site_83343_15min_2014_clean.csv"

# Create processed directory if it doesn't exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


# Load raw data
df = pd.read_csv(RAW_FILE, skiprows=1)

print(f"Raw dataset shape: {df.shape}")


# Create a single timestamp column
df["timestamp"] = pd.to_datetime(
    df[["Year", "Month", "Day", "Hour", "Minute"]]
)

# Rename measurement columns
df = df.rename(
    columns={
        "wind speed at 100m (m/s)": "wind_speed_100m",
        "wind direction at 100m (deg)": "wind_direction_100m",
        "temperature at 100m (C)": "temperature_100m",
        "air pressure at 100m (Pa)": "pressure_100m",
    }
)

# Keep only the useful columns
df = df[
    [
        "timestamp",
        "wind_speed_100m",
        "wind_direction_100m",
        "temperature_100m",
        "pressure_100m",
    ]
]

# Sort chronologically
df = df.sort_values("timestamp").reset_index(drop=True)

# Save processed dataset
df.to_csv(OUTPUT_FILE, index=False)


print(f"Processed dataset shape: {df.shape}")
print(f"Saved to: {OUTPUT_FILE}")
print("\nFirst 5 rows:")
print(df.head())