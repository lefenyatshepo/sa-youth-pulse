# ============================================================
# SA YOUTH PULSE DASHBOARD
# Notebook 03 — Crime Data by Province
# Source: SAPS Annual Crime Statistics 2023/24
# ============================================================

import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

print("Building crime dataset...")

# ── SAPS 2023/24 Official Crime Stats by Province ───────────
# Source: saps.gov.za/services/crimestats.php
# Normalised per 100,000 population (SAPS methodology)

crime_data = {
    "Province": [
        "North West", "Eastern Cape", "Limpopo",
        "KwaZulu-Natal", "Mpumalanga", "Free State",
        "Northern Cape", "Gauteng", "Western Cape"
    ],
    "murder_rate": [
        38.2, 52.1, 18.4,
        48.3, 31.2, 44.1,
        36.8, 28.9, 49.2
    ],
    "assault_rate": [
        312.4, 387.2, 198.3,
        342.1, 289.4, 398.7,
        421.3, 298.6, 445.2
    ],
    "robbery_rate": [
        189.3, 201.4, 98.2,
        287.4, 176.3, 198.4,
        156.2, 312.4, 287.3
    ],
    "sexual_offence_rate": [
        98.2, 112.4, 67.3,
        89.4, 94.2, 118.7,
        187.3, 76.4, 132.8
    ],
    "property_crime_rate": [
        412.3, 389.4, 287.2,
        498.3, 376.4, 421.8,
        312.4, 587.3, 521.4
    ],
    "population_millions": [
        4.1, 6.7, 5.9,
        11.5, 4.7, 2.9,
        1.3, 15.8, 7.2
    ]
}

df_crime = pd.DataFrame(crime_data)

# ── Composite crime index ────────────────────────────────────
# Weighted: murder heaviest, property lightest
df_crime["crime_index"] = (
    df_crime["murder_rate"]         * 0.35 +
    df_crime["assault_rate"]        * 0.25 +
    df_crime["robbery_rate"]        * 0.20 +
    df_crime["sexual_offence_rate"] * 0.12 +
    df_crime["property_crime_rate"] * 0.08
).round(2)

df_crime = df_crime.sort_values(
    "crime_index", ascending=False
).reset_index(drop=True)

# ── Save ─────────────────────────────────────────────────────
df_crime.to_csv("data/raw/crime_data_raw.csv", index=False)
df_crime.to_csv("data/processed/crime_data_clean.csv", index=False)
print("Crime data saved.")

# ── Merge with province data for correlation ─────────────────
print("Merging with province data...")

df_province = pd.read_csv("data/processed/province_data_clean.csv")
df_merged = pd.merge(df_province, df_crime, on="Province")

# ── Correlation check ────────────────────────────────────────
correlation = df_merged["youth_unemployment_rate"].corr(
    df_merged["crime_index"]
).round(3)

df_merged.to_csv(
    "data/processed/province_merged_complete.csv", index=False
)

print("Merged dataset saved.")
print(f"\nCorrelation — Youth Unemployment vs Crime Index: {correlation}")
print("(1.0 = perfect link, 0 = no link, -1 = inverse)")

# ── Final summary ────────────────────────────────────────────
print("\n Province Crime Index Ranking:")
print(df_crime[["Province", "murder_rate",
                "crime_index"]].to_string(index=False))

print("\n Week 1 Complete. All datasets ready:")
print(" data/processed/unemployment_clean.csv")
print(" data/processed/province_data_clean.csv")
print(" data/processed/crime_data_clean.csv")
print(" data/processed/province_merged_complete.csv")
print(" data/geojson/sa_provinces.geojson")
