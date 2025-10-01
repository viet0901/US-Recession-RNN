import os
import pandas as pd
from fredapi import Fred

# FRED API key
api_key = 'a8b15880b3822995f0e2e4f970cd86e3'
if not api_key:
    raise ValueError("Please set the FRED_API_KEY environment variable")

# Connect to FRED
fred = Fred(api_key=api_key)

# List of FRED series to download
series_ids = [
    "USRECP", "GDPC1", "UNRATE", "INDPRO",
    "DSPIC96", "FPCPITOTLZGUSA", "CPIAUCSL", "USSLIND", "CCNSA"
]

# Output directory: top-level data/raw/
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
raw_dir = os.path.join(project_root, "data", "raw")
os.makedirs(raw_dir, exist_ok=True)

# Download each series and save CSV
for series_id in series_ids:
    try:
        data = fred.get_series(series_id)
        df = pd.DataFrame(data, columns=[series_id])
        df.index.name = "DATE"
        file_path = os.path.join(raw_dir, f"{series_id}.csv")
        df.to_csv(file_path)
        print(f"Saved {series_id} to {file_path}")
    except Exception as e:
        print(f"Failed to download {series_id}: {e}")

print("All series downloaded successfully!")
