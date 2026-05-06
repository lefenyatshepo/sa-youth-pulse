# ============================================================
# SA YOUTH PULSE DASHBOARD
# Notebook 01 — Employment Data Download & Clean
# Source: World Bank Open Data API
# ============================================================

import pandas as pd
import requests
import os

# ── Create folders if they don't exist ──────────────────────
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

print("Folders ready...")

# ── Download SA Youth Unemployment from World Bank API ──────
# Indicator: SL.UEM.1524.ZS = Youth unemployment 15-24
# Indicator: SL.UEM.TOTL.ZS = Total unemployment

indicators = {
    "youth_unemployment": "SL.UEM.1524.ZS",
    "total_unemployment": "SL.UEM.TOTL.ZS",
    "youth_not_in_education": "SL.UEM.NEET.ZS",
}

all_data = []

for name, code in indicators.items():
    print(f"Downloading {name}...")
    
    url = (
        f"https://api.worldbank.org/v2/country/ZA/indicator/{code}"
        f"?format=json&per_page=100&mrv=20"
    )
    
    response = requests.get(url)
    data = response.json()
    
    records = data[1]
    for r in records:
        all_data.append({
            "indicator": name,
            "year": r["date"],
            "value": r["value"],
            "country": r["country"]["value"]
        })

# ── Build DataFrame ─────────────────────────────────────────
df = pd.DataFrame(all_data)
df = df.dropna(subset=["value"])
df["year"] = df["year"].astype(int)
df["value"] = df["value"].astype(float).round(2)
df = df.sort_values(["indicator", "year"])

# ── Save raw + processed ────────────────────────────────────
df.to_csv("data/raw/worldbank_unemployment_raw.csv", index=False)
df.to_csv("data/processed/unemployment_clean.csv", index=False)

print("Done! Files saved.")
print(f"Total records: {len(df)}")
print("\nPreview:")
print(df.tail(10))