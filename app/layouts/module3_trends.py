# ============================================================
# SA YOUTH PULSE DASHBOARD
# Module 3 — The Decade of Decline
# 20-year unemployment trend with annotations
# ============================================================

import pandas as pd
import plotly.graph_objects as go
import os

df = pd.read_csv("data/processed/unemployment_clean.csv")

df_youth = df[df["indicator"] == "youth_unemployment"].sort_values("year")
df_total = df[df["indicator"] == "total_unemployment"].sort_values("year")

def build_trend_chart():

    fig = go.Figure()

    # ── Youth unemployment line ──────────────────────────────
    fig.add_trace(go.Scatter(
        x=df_youth["year"],
        y=df_youth["value"],
        mode="lines+markers",
        name="Youth Unemployment (15-24)",
        line=dict(color="#F5A623", width=3),
        marker=dict(size=6, color="#F5A623"),
        hovertemplate="<b>%{x}</b><br>Youth Unemployment: %{y}%<extra></extra>",
    ))

    # ── Total unemployment line ──────────────────────────────
    fig.add_trace(go.Scatter(
        x=df_total["year"],
        y=df_total["value"],
        mode="lines+markers",
        name="Total Unemployment (all ages)",
        line=dict(color="#BDC3C7", width=2, dash="dot"),
        marker=dict(size=5, color="#BDC3C7"),
        hovertemplate="<b>%{x}</b><br>Total Unemployment: %{y}%<extra></extra>",
    ))

    # ── Peak marker ──────────────────────────────────────────
    peak_year = df_youth.loc[df_youth["value"].idxmax(), "year"]
    peak_val  = df_youth["value"].max()

    fig.add_trace(go.Scatter(
        x=[peak_year],
        y=[peak_val],
        mode="markers",
        name="Peak (2021)",
        marker=dict(size=14, color="#C0392B", symbol="star"),
        hovertemplate="<b>PEAK: " + str(peak_year) + "</b><br>" +
                      str(peak_val) + "% youth unemployment<extra></extra>",
    ))

    # ── Annotations ─────────────────────────────────────────
    annotations = [
        dict(x=2008, y=48, text="Global Financial Crisis", showarrow=True,
             arrowhead=2, arrowcolor="#BDC3C7", font=dict(color="#BDC3C7", size=10),
             ax=40, ay=-40),
        dict(x=2020, y=59.61, text="COVID-19 Hits", showarrow=True,
             arrowhead=2, arrowcolor="#E74C3C", font=dict(color="#E74C3C", size=10),
             ax=-60, ay=-30),
        dict(x=2021, y=peak_val, text="PEAK: " + str(round(peak_val, 1)) + "%",
             showarrow=True, arrowhead=2, arrowcolor="#C0392B",
             font=dict(color="#F5A623", size=11, family="Arial Black"),
             ax=50, ay=-20),
        dict(x=2022, y=32, text="Load shedding intensifies", showarrow=True,
             arrowhead=2, arrowcolor="#BDC3C7", font=dict(color="#BDC3C7", size=10),
             ax=40, ay=30),
    ]

    # ── Forecast zone (shaded) ───────────────────────────────
    last_val = df_youth.iloc[-1]["value"]
    last_year = int(df_youth.iloc[-1]["year"])

    forecast_years = list(range(last_year + 1, last_year + 4))
    forecast_vals  = [last_val - 0.5, last_val - 1.0, last_val - 1.5]

    fig.add_trace(go.Scatter(
        x=forecast_years,
        y=forecast_vals,
        mode="lines",
        name="Forecast (if trend holds)",
        line=dict(color="#F5A623", width=2, dash="dash"),
        hovertemplate="<b>%{x} (forecast)</b><br>Projected: %{y}%<extra></extra>",
    ))

    # ── 50% danger line ──────────────────────────────────────
    fig.add_hline(
        y=50,
        line_dash="dot",
        line_color="#C0392B",
        annotation_text="50% danger threshold",
        annotation_position="top right",
        annotation_font_color="#C0392B",
    )

    # ── Layout ───────────────────────────────────────────────
    fig.update_layout(
        title=dict(
            text="<b>SA Youth Unemployment — The Decade of Decline</b><br>"
                 "<sup>Youth (15-24) vs Total Unemployment 2005-2025 | "
                 "Source: World Bank / Stats SA</sup>",
            font=dict(size=16, color="white"),
            x=0.5,
        ),
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        xaxis=dict(
            title="Year",
            gridcolor="#2C3E50",
            tickmode="linear",
            dtick=2,
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
        ),
        yaxis=dict(
            title="Unemployment Rate (%)",
            gridcolor="#2C3E50",
            range=[0, 75],
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
        ),
        legend=dict(
            bgcolor="#1E3A5F",
            bordercolor="#2C3E50",
            borderwidth=1,
            font=dict(color="white"),
        ),
        annotations=annotations,
        hovermode="x unified",
        height=550,
        margin=dict(t=100, b=60, l=60, r=40),
    )

    return fig

