# ============================================================
# SA YOUTH PULSE DASHBOARD
# Module 2 — The Education to Employment Funnel
# How much does education actually help?
# ============================================================

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os

# ── Education vs Unemployment data ───────────────────────────
# Source: Stats SA QLFS Q1 2025
education_data = {
    "level": [
        "No Matric",
        "Matric Only",
        "Vocational/\nDiploma",
        "University\nDegree"
    ],
    "unemployment_rate": [51.6, 47.6, 37.3, 23.9],
    "employed_rate":     [48.4, 52.4, 62.7, 76.1],
    "youth_population":  [2100000, 3800000, 1200000, 890000],
    "color": ["#C0392B", "#E67E22", "#F5A623", "#27AE60"],
}

df_edu = pd.DataFrame(education_data)

# ── Skills mismatch data ──────────────────────────────────────
skills_gap = {
    "skill": [
        "Digital Literacy",
        "Numeracy",
        "Communication",
        "Problem Solving",
        "Work Readiness",
        "Technical Skills",
    ],
    "employer_demand": [87, 82, 91, 78, 95, 71],
    "school_output":   [34, 41, 52, 38, 29, 45],
}
df_skills = pd.DataFrame(skills_gap)
df_skills["gap"] = df_skills["employer_demand"] - df_skills["school_output"]

def build_funnel():
    fig = go.Figure()

    # ── Funnel bars ──────────────────────────────────────────
    fig.add_trace(go.Bar(
        name="Unemployment Rate",
        x=df_edu["level"],
        y=df_edu["unemployment_rate"],
        marker_color=df_edu["color"],
        text=[str(v) + "%" for v in df_edu["unemployment_rate"]],
        textposition="outside",
        textfont=dict(color="white", size=13, family="Arial Black"),
        hovertemplate="<b>%{x}</b><br>Unemployment: %{y}%<extra></extra>",
    ))

    # ── Employed rate line ───────────────────────────────────
    fig.add_trace(go.Scatter(
        name="Employment Rate",
        x=df_edu["level"],
        y=df_edu["employed_rate"],
        mode="lines+markers+text",
        line=dict(color="#27AE60", width=2, dash="dot"),
        marker=dict(size=8, color="#27AE60"),
        text=[str(v) + "%" for v in df_edu["employed_rate"]],
        textposition="top center",
        textfont=dict(color="#27AE60", size=11),
        hovertemplate="<b>%{x}</b><br>Employment Rate: %{y}%<extra></extra>",
        yaxis="y",
    ))

    fig.update_layout(
        title=dict(
            text="<b>The Education-to-Employment Funnel</b><br>"
                 "<sup>Does education actually help? "
                 "Youth unemployment by education level | "
                 "Source: Stats SA QLFS Q1 2025</sup>",
            font=dict(size=16, color="white"),
            x=0.5,
        ),
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        xaxis=dict(
            title="Education Level",
            gridcolor="#2C3E50",
            tickfont=dict(color="white", size=11),
            title_font=dict(color="white"),
        ),
        yaxis=dict(
            title="Rate (%)",
            gridcolor="#2C3E50",
            range=[0, 75],
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
        ),
        legend=dict(
            bgcolor="#1E3A5F",
            bordercolor="#2C3E50",
            font=dict(color="white"),
        ),
        height=500,
        margin=dict(t=100, b=60, l=60, r=40),
        annotations=[
            dict(
                x="No Matric", y=55,
                text="51.6% unemployed<br>— more than 1 in 2",
                showarrow=True, arrowhead=2,
                arrowcolor="#C0392B",
                font=dict(color="#E74C3C", size=10),
                ax=60, ay=-40,
            ),
            dict(
                x="University\nDegree", y=28,
                text="Degree = 27.7pt<br>improvement",
                showarrow=True, arrowhead=2,
                arrowcolor="#27AE60",
                font=dict(color="#27AE60", size=10),
                ax=-70, ay=-30,
            ),
        ],
    )
    return fig


def build_skills_gap():
    fig = go.Figure()

    fig.add_trace(go.Bar(
        name="Employer Demand (%)",
        x=df_skills["skill"],
        y=df_skills["employer_demand"],
        marker_color="#F5A623",
        text=[str(v) + "%" for v in df_skills["employer_demand"]],
        textposition="outside",
        textfont=dict(color="white", size=10),
        hovertemplate="<b>%{x}</b><br>Employers need: %{y}%<extra></extra>",
    ))

    fig.add_trace(go.Bar(
        name="School Output (%)",
        x=df_skills["skill"],
        y=df_skills["school_output"],
        marker_color="#2C3E50",
        text=[str(v) + "%" for v in df_skills["school_output"]],
        textposition="outside",
        textfont=dict(color="white", size=10),
        hovertemplate="<b>%{x}</b><br>Schools produce: %{y}%<extra></extra>",
    ))

    fig.update_layout(
        title=dict(
            text="<b>The Skills Mismatch — What Employers Want vs What Schools Produce</b><br>"
                 "<sup>Gap between employer demand and school output | "
                 "Source: HSRC / Harambee Employer Survey 2024</sup>",
            font=dict(size=14, color="white"),
            x=0.5,
        ),
        barmode="group",
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        xaxis=dict(
            gridcolor="#2C3E50",
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
        ),
        yaxis=dict(
            title="% of Youth with Skill",
            gridcolor="#2C3E50",
            range=[0, 110],
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
        ),
        legend=dict(
            bgcolor="#1E3A5F",
            bordercolor="#2C3E50",
            font=dict(color="white"),
        ),
        height=480,
        margin=dict(t=100, b=60, l=60, r=40),
    )
    return fig


