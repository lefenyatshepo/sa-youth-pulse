# ============================================================
# SA YOUTH PULSE DASHBOARD
# Module 5 — The Crime Correlation Engine
# What happens when youth have no future?
# ============================================================

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import os

# ── Load merged dataset ──────────────────────────────────────
df = pd.read_csv("data/processed/province_merged_complete.csv")

def build_scatter():
    fig = go.Figure()

    # ── Colour by tier ───────────────────────────────────────
    tier_colors = {
        "Crisis":    "#C0392B",
        "High Concern": "#E67E22",
        "Stabilise": "#27AE60",
    }

    for tier, group in df.groupby("tier"):
        fig.add_trace(go.Scatter(
            x=group["youth_unemployment_rate"],
            y=group["crime_index"],
            mode="markers+text",
            name=tier,
            marker=dict(
                size=group["population_millions"] * 3,
                color=tier_colors.get(tier, "#BDC3C7"),
                opacity=0.85,
                line=dict(width=1, color="white"),
            ),
            text=group["Province"],
            textposition="top center",
            textfont=dict(color="white", size=9),
            hovertemplate=(
                "<b>%{text}</b><br>"
                "Youth Unemployment: %{x}%<br>"
                "Crime Index: %{y}<br>"
                "<extra></extra>"
            ),
        ))

    # ── Correlation annotation ───────────────────────────────
    corr = df["youth_unemployment_rate"].corr(
        df["crime_index"]
    ).round(3)

    fig.update_layout(
        title=dict(
            text="<b>Unemployment vs Crime — The Correlation Story</b><br>"
                 "<sup>Bubble size = province population | "
                 "Correlation: " + str(corr) +
                 " | Source: SAPS 2023/24 + Stats SA QLFS Q1 2025</sup>",
            font=dict(size=15, color="white"),
            x=0.5,
        ),
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        xaxis=dict(
            title="Youth Unemployment Rate (%)",
            gridcolor="#2C3E50",
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
            range=[20, 65],
        ),
        yaxis=dict(
            title="Composite Crime Index",
            gridcolor="#2C3E50",
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
        ),
        legend=dict(
            bgcolor="#1E3A5F",
            bordercolor="#2C3E50",
            font=dict(color="white"),
            title=dict(text="Crisis Tier", font=dict(color="white")),
        ),
        height=540,
        margin=dict(t=100, b=60, l=70, r=40),
        annotations=[
            dict(
                x=54.3, y=df[df["Province"]=="Eastern Cape"]["crime_index"].values[0],
                text="Eastern Cape:<br>High unemployment<br>+ High crime",
                showarrow=True, arrowhead=2,
                arrowcolor="#C0392B",
                font=dict(color="#E74C3C", size=9),
                ax=-80, ay=-40,
            ),
            dict(
                x=27.3, y=df[df["Province"]=="Western Cape"]["crime_index"].values[0],
                text="Western Cape:<br>Low unemployment<br>BUT high crime<br>(urbanisation effect)",
                showarrow=True, arrowhead=2,
                arrowcolor="#F5A623",
                font=dict(color="#F5A623", size=9),
                ax=80, ay=-50,
            ),
            dict(
                x=47.2, y=df[df["Province"]=="Limpopo"]["crime_index"].values[0],
                text="Limpopo:<br>High unemployment<br>lower crime<br>(rural buffer)",
                showarrow=True, arrowhead=2,
                arrowcolor="#27AE60",
                font=dict(color="#27AE60", size=9),
                ax=70, ay=30,
            ),
        ],
    )
    return fig


def build_crime_ranking():
    df_sorted = df.sort_values("crime_index", ascending=True)

    tier_colors = {
        "Crisis":       "#C0392B",
        "High Concern": "#E67E22",
        "Stabilise":    "#27AE60",
    }

    colors = [tier_colors.get(t, "#BDC3C7") for t in df_sorted["tier"]]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_sorted["crime_index"],
        y=df_sorted["Province"],
        orientation="h",
        marker_color=colors,
        text=[str(v) for v in df_sorted["crime_index"]],
        textposition="outside",
        textfont=dict(color="white", size=10),
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Crime Index: %{x}<br>"
            "Murder Rate: " +
            df_sorted["murder_rate"].astype(str) +
            " per 100K<extra></extra>"
        ),
    ))

    fig.update_layout(
        title=dict(
            text="<b>Province Crime Index Ranking</b><br>"
                 "<sup>Composite index: murder (35%) + assault (25%) "
                 "+ robbery (20%) + sexual offences (12%) "
                 "+ property crime (8%)<br>"
                 "Normalised per 100,000 population "
                 "| Source: SAPS Annual Report 2023/24</sup>",
            font=dict(size=13, color="white"),
            x=0.5,
        ),
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        xaxis=dict(
            title="Composite Crime Index",
            gridcolor="#2C3E50",
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
        ),
        yaxis=dict(
            gridcolor="#2C3E50",
            tickfont=dict(color="white", size=10),
        ),
        height=460,
        margin=dict(t=120, b=60, l=120, r=60),
    )
    return fig


