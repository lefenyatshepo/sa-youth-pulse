# ============================================================
# SA YOUTH PULSE DASHBOARD
# Notebook 02 — Province Data + SA Map Boundaries
# Sources: StatsSA + GADM GeoJSON
# ============================================================

import pandas as pd
import requests
import json
import os

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)
os.makedirs("data/geojson", exist_ok=True)

print("Starting province data build...")

# ── Province unemployment data (Stats SA QLFS 2025) ─────────
# Manually structured from Stats SA Q1 2025 report
# Source: statssa.gov.za

province_data = {
    "Province": [
        "North West", "Eastern Cape", "Limpopo",
        "KwaZulu-Natal", "Mpumalanga", "Free State",
        "Northern Cape", "Gauteng", "Western Cape"
    ],
    "youth_unemployment_rate": [
        58.8, 54.3, 47.2,
        42.1, 44.3, 43.1,
        40.2, 38.4, 27.3
    ],
    "neet_rate": [
        52.1, 49.8, 46.3,
        41.2, 43.5, 42.1,
        38.9, 35.2, 24.6
    ],
    "female_neet_rate": [
        57.3, 54.1, 51.2,
        46.8, 48.3, 47.2,
        43.1, 39.4, 28.1
    ],
    "labour_participation_rate": [
        43.0, 45.2, 48.1,
        52.3, 50.1, 49.8,
        54.2, 58.9, 67.4
    ],
    "tier": [
        "Crisis", "Crisis", "High Concern",
        "High Concern", "High Concern", "High Concern",
        "High Concern", "Stabilise", "Stabilise"
    ],
    "economic_strength": [
        "Mining (platinum, gold, chrome)",
        "Automotive, Agriculture, Tourism",
        "Mining, Agriculture, Kruger Tourism",
        "Agriculture, Manufacturing, Port Logistics",
        "Mining, Timber, Tourism",
        "Agriculture (Maize), Logistics",
        "Mining (Diamonds), Solar, SKA Tourism",
        "Finance, Tech, Retail, BPO",
        "Finance, Wine Tourism, Tech, Blue Economy"
    ],
    "top_business_opportunity": [
        "Mining services, Solar installation, Recycling",
        "Agri-processing, Auto supply SMEs, Eco-tourism",
        "Safari tourism, Avocado export, Mining services",
        "Port logistics, Textile manufacturing, BPO",
        "Timber value chain, Renewable energy, Tourism",
        "Maize processing, Road freight, Solar farms",
        "Solar farms, Astro-tourism, Desert eco-tourism",
        "Tech startups, Township retail, Fintech",
        "AgriTourism, Blue economy, Silicon Cape tech"
    ],
    "key_programmes": [
        "YES, Harambee, NYDA Mahikeng",
        "YES, Harambee, NYDA, EC TVET Colleges",
        "YES, NYDA, Mining SETA",
        "YES, Harambee Durban, NYDA",
        "YES, NYDA, Energy SETA",
        "YES, NYDA Bloemfontein, AgriSETA",
        "YES, NYDA Kimberley, Mining SETA",
        "Harambee, YES, Microsoft AI Platform, NYDA",
        "YES, Harambee, NYDA Cape Town, WeThinkCode"
    ]
}

df_provinces = pd.DataFrame(province_data)

# ── Add severity score (composite) ──────────────────────────
df_provinces["severity_score"] = (
    df_provinces["youth_unemployment_rate"] * 0.5 +
    df_provinces["neet_rate"] * 0.3 +
    df_provinces["female_neet_rate"] * 0.2
).round(2)

df_provinces = df_provinces.sort_values(
    "severity_score", ascending=False
).reset_index(drop=True)

# ── Save province data ───────────────────────────────────────
df_provinces.to_csv("data/raw/province_data_raw.csv", index=False)
df_provinces.to_csv("data/processed/province_data_clean.csv", index=False)
print("Province data saved.")

# ── Download SA GeoJSON map boundaries ──────────────────────
print("Downloading SA province map boundaries...")

geojson_url = (
    "https://raw.githubusercontent.com/nvkelso/"
    "natural-earth-vector/master/geojson/"
    "ne_10m_admin_1_states_provinces.geojson"
)

response = requests.get(geojson_url, timeout=30)
all_provinces = response.json()

# Filter only South Africa
sa_geojson = {
    "type": "FeatureCollection",
    "features": [
        f for f in all_provinces["features"]
        if f["properties"].get("admin") == "South Africa"
    ]
}

print(f"SA provinces found in GeoJSON: "
      f"{len(sa_geojson['features'])}")

# Show province names from GeoJSON
for f in sa_geojson["features"]:
    print(" -", f["properties"].get("name"))

# Save GeoJSON
with open("data/geojson/sa_provinces.geojson", "w") as file:
    json.dump(sa_geojson, file)

print("GeoJSON saved.")

# ── Final summary ────────────────────────────────────────────
print("\n Province Severity Ranking:")
print(df_provinces[["Province","youth_unemployment_rate",
                     "severity_score","tier"]].to_string(index=False))
print("\nAll done. Week 1 data foundation complete.")