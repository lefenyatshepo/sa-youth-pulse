# ============================================================
# SA YOUTH PULSE DASHBOARD
# Module 4 — The Gender & Race Lens
# Who bears the heaviest burden?
# ============================================================

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import os

# ── Gender data by province ───────────────────────────────────
# Source: Stats SA QLFS Q1 2025 + GHS 2024
gender_data = {
    "Province": [
        "North West", "Eastern Cape", "Limpopo",
        "KwaZulu-Natal", "Mpumalanga", "Free State",
        "Northern Cape", "Gauteng", "Western Cape"
    ],
    "male_neet":   [46.2, 44.1, 41.3, 36.8, 38.9, 37.2, 34.1, 31.2, 21.3],
    "female_neet": [57.3, 54.1, 51.2, 46.8, 48.3, 47.2, 43.1, 39.4, 28.1],
    "gender_gap":  [11.1, 10.0,  9.9, 10.0,  9.4, 10.0,  9.0,  8.2,  6.8],
}

# ── Urban vs Rural data ───────────────────────────────────────
urban_rural = {
    "area_type":        ["Urban", "Rural"],
    "youth_unemployed": [42.3,    61.8],
    "neet_rate":        [35.1,    54.7],
    "female_neet":      [44.2,    63.9],
}

df_gender    = pd.DataFrame(gender_data)
df_ur        = pd.DataFrame(urban_rural)

df_gender    = df_gender.sort_values("gender_gap", ascending=True)

def build_gender_chart():
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(
            "Male vs Female NEET Rate by Province (%)",
            "Gender Gap — Women Excluded More in Every Province"
        ),
        horizontal_spacing=0.12,
    )

    # ── Left: grouped bar male vs female ────────────────────
    fig.add_trace(go.Bar(
        name="Male NEET Rate",
        x=df_gender["male_neet"],
        y=df_gender["Province"],
        orientation="h",
        marker_color="#3498DB",
        text=[str(v) + "%" for v in df_gender["male_neet"]],
        textposition="outside",
        textfont=dict(color="white", size=9),
        hovertemplate="<b>%{y}</b><br>Male NEET: %{x}%<extra></extra>",
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        name="Female NEET Rate",
        x=df_gender["female_neet"],
        y=df_gender["Province"],
        orientation="h",
        marker_color="#E91E8C",
        text=[str(v) + "%" for v in df_gender["female_neet"]],
        textposition="outside",
        textfont=dict(color="white", size=9),
        hovertemplate="<b>%{y}</b><br>Female NEET: %{x}%<extra></extra>",
    ), row=1, col=1)

    # ── Right: gender gap bar chart ──────────────────────────
    fig.add_trace(go.Bar(
        name="Gender Gap (pts)",
        x=df_gender["gender_gap"],
        y=df_gender["Province"],
        orientation="h",
        marker=dict(
            color=df_gender["gender_gap"],
            colorscale="RdPu",
            showscale=False,
        ),
        text=[str(v) + " pts" for v in df_gender["gender_gap"]],
        textposition="outside",
        textfont=dict(color="white", size=9),
        hovertemplate="<b>%{y}</b><br>Gender Gap: %{x} pts<extra></extra>",
        showlegend=False,
    ), row=1, col=2)

    fig.update_layout(
        title=dict(
            text="<b>The Gender Lens — Who Bears the Heaviest Burden?</b><br>"
                 "<sup>Young women excluded at higher rates in ALL 9 provinces"
                 " | Source: Stats SA QLFS Q1 2025</sup>",
            font=dict(size=15, color="white"),
            x=0.5,
        ),
        barmode="group",
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        legend=dict(
            bgcolor="#1E3A5F",
            bordercolor="#2C3E50",
            font=dict(color="white"),
            orientation="h",
            y=-0.15,
        ),
        height=520,
        margin=dict(t=100, b=80, l=120, r=60),
        annotations=[
            dict(
                text="Male vs Female NEET Rate by Province (%)",
                x=0.22, y=1.08, xref="paper", yref="paper",
                showarrow=False,
                font=dict(color="white", size=11),
            ),
            dict(
                text="Gender Gap (percentage points)",
                x=0.85, y=1.08, xref="paper", yref="paper",
                showarrow=False,
                font=dict(color="white", size=11),
            ),
        ],
    )

    fig.update_xaxes(
        gridcolor="#2C3E50",
        tickfont=dict(color="white"),
        range=[0, 75],
        row=1, col=1,
    )
    fig.update_xaxes(
        gridcolor="#2C3E50",
        tickfont=dict(color="white"),
        range=[0, 16],
        row=1, col=2,
    )
    fig.update_yaxes(
        gridcolor="#2C3E50",
        tickfont=dict(color="white", size=9),
    )

    return fig


def build_urban_rural():
    fig = go.Figure()

    metrics = ["Youth Unemployed", "NEET Rate", "Female NEET"]
    urban   = [42.3, 35.1, 44.2]
    rural   = [61.8, 54.7, 63.9]

    fig.add_trace(go.Bar(
        name="Urban",
        x=metrics,
        y=urban,
        marker_color="#3498DB",
        text=[str(v) + "%" for v in urban],
        textposition="outside",
        textfont=dict(color="white", size=11),
        hovertemplate="<b>Urban — %{x}</b><br>%{y}%<extra></extra>",
    ))

    fig.add_trace(go.Bar(
        name="Rural",
        x=metrics,
        y=rural,
        marker_color="#C0392B",
        text=[str(v) + "%" for v in rural],
        textposition="outside",
        textfont=dict(color="white", size=11),
        hovertemplate="<b>Rural — %{x}</b><br>%{y}%<extra></extra>",
    ))

    fig.update_layout(
        title=dict(
            text="<b>Urban vs Rural — The Hidden Crisis</b><br>"
                 "<sup>Rural youth face dramatically higher exclusion rates"
                 " — invisible in national averages"
                 " | Source: Stats SA GHS 2024</sup>",
            font=dict(size=14, color="white"),
            x=0.5,
        ),
        barmode="group",
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        yaxis=dict(
            title="Rate (%)",
            gridcolor="#2C3E50",
            range=[0, 80],
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
        ),
        xaxis=dict(
            gridcolor="#2C3E50",
            tickfont=dict(color="white", size=11),
        ),
        legend=dict(
            bgcolor="#1E3A5F",
            bordercolor="#2C3E50",
            font=dict(color="white"),
        ),
        height=460,
        margin=dict(t=100, b=60, l=60, r=40),
        annotations=[
            dict(
                x="NEET Rate", y=68,
                text="Rural NEET is 19.6pts<br>higher than Urban",
                showarrow=True,
                arrowhead=2,
                arrowcolor="#C0392B",
                font=dict(color="#E74C3C", size=10),
                ax=80, ay=-30,
            ),
        ],
    )

    return fig

