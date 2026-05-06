import pandas as pd
import plotly.express as px
import json
import os

df = pd.read_csv("data/processed/province_data_clean.csv")

with open("data/geojson/sa_provinces.geojson") as f:
    sa_geojson = json.load(f)

for feature in sa_geojson["features"]:
    feature["properties"]["Province"] = feature["properties"].get("name", "")

METRICS = {
    "youth_unemployment_rate": {
        "label": "Youth Unemployment Rate (%)",
        "color": "Reds",
    },
    "neet_rate": {
        "label": "NEET Rate (%)",
        "color": "Oranges",
    },
    "female_neet_rate": {
        "label": "Female NEET Rate (%)",
        "color": "RdPu",
    },
    "severity_score": {
        "label": "Overall Severity Score",
        "color": "YlOrRd",
    },
    "labour_participation_rate": {
        "label": "Labour Participation Rate (%)",
        "color": "Blues",
    },
}


def build_map(metric="youth_unemployment_rate"):
    meta = METRICS[metric]

    fig = px.choropleth(
        df,
        geojson=sa_geojson,
        locations="Province",
        featureidkey="properties.Province",
        color=metric,
        color_continuous_scale=meta["color"],
        hover_name="Province",
        hover_data={
            "youth_unemployment_rate": True,
            "neet_rate": True,
            "female_neet_rate": True,
            "severity_score": True,
            "tier": True,
            metric: False,
        },
        labels={
            "youth_unemployment_rate": "Youth Unemployment",
            "neet_rate": "NEET Rate",
            "female_neet_rate": "Female NEET",
            "severity_score": "Severity Score",
            "tier": "Crisis Tier",
        },
        title="SA Youth Crisis Map — " + meta["label"],
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False,
        bgcolor="#1E3A5F",
    )

    fig.update_layout(
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#1E3A5F",
        font_color="white",
        font_family="Arial",
        title_font_size=16,
        title_x=0.5,
        margin={"r": 0, "t": 60, "l": 0, "b": 0},
        height=600,
        coloraxis_colorbar=dict(
            thickness=15,
            len=0.7,
            bgcolor="#1E3A5F",
            tickfont=dict(color="white"),
        ),
    )

    return fig