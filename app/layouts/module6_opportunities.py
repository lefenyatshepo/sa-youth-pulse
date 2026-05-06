# ============================================================
# SA YOUTH PULSE DASHBOARD
# Module 6 — The Opportunity & Intervention Engine
# Here's the problem. Here's who's solving it.
# Here's what can be built here.
# ============================================================

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import os

# ── Province opportunity data ─────────────────────────────────
opportunity_data = {
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
    "tier": [
        "Crisis", "Crisis", "High Concern",
        "High Concern", "High Concern", "High Concern",
        "High Concern", "Stabilise", "Stabilise"
    ],
    "top_sector": [
        "Mining Services", "Agri-Processing",
        "Eco-Tourism", "Port Logistics",
        "Renewable Energy", "Agri-Logistics",
        "Solar Energy", "Tech and Fintech",
        "Blue Economy"
    ],
    "job_creation_score": [78, 82, 71, 85, 69, 74, 65, 92, 88],
    "programme_count":    [3,  4,  3,  4,  3,  3,  2,  5,  4],
    "funding_available": [
        "IDC, NEF, NYDA",
        "IDC, Jobs Fund, NYDA",
        "IDC, Mining SETA",
        "IDC, Jobs Fund, NEF",
        "IDC, Energy SETA",
        "AgriSETA, Jobs Fund",
        "IDC, NYDA",
        "IDC, NEF, Microsoft",
        "IDC, Jobs Fund"
    ],
}

# ── Programme reach data ──────────────────────────────────────
programme_data = {
    "Programme": [
        "YES", "Harambee", "NYDA",
        "SAYouth.mobi", "Jobs Fund",
        "Presidential PYEI", "IDC/NEF"
    ],
    "youth_reached": [
        185557, 876131, 320000,
        4500000, 180000,
        890000, 45000
    ],
    "focus": [
        "Work experience + B-BBEE",
        "First-job seekers",
        "Youth entrepreneurship",
        "Digital job matching",
        "Grant funding",
        "Multi-programme coordination",
        "Enterprise funding"
    ],
    "color": [
        "#F5A623", "#3498DB", "#27AE60",
        "#9B59B6", "#E67E22",
        "#1ABC9C", "#C0392B"
    ],
}

df_opp  = pd.DataFrame(opportunity_data)
df_prog = pd.DataFrame(programme_data)
df_opp  = df_opp.sort_values(
    "youth_unemployment_rate", ascending=False
).reset_index(drop=True)

tier_colors = {
    "Crisis":       "#C0392B",
    "High Concern": "#E67E22",
    "Stabilise":    "#27AE60",
}


def build_opportunity_matrix():
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(
            "Job Creation Score by Province",
            "Active Programme Count"
        ),
        horizontal_spacing=0.15,
    )

    colors = [tier_colors[t] for t in df_opp["tier"]]

    fig.add_trace(go.Bar(
        x=df_opp["job_creation_score"],
        y=df_opp["Province"],
        orientation="h",
        marker_color=colors,
        text=[
            str(s) + " | " + sec
            for s, sec in zip(
                df_opp["job_creation_score"],
                df_opp["top_sector"]
            )
        ],
        textposition="outside",
        textfont=dict(color="white", size=8),
        hovertemplate="<b>%{y}</b><br>Job Creation Score: %{x}/100<extra></extra>",
        name="Job Creation Score",
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        x=df_opp["programme_count"],
        y=df_opp["Province"],
        orientation="h",
        marker=dict(
            color=df_opp["programme_count"],
            colorscale="Blues",
            showscale=False,
        ),
        text=df_opp["programme_count"],
        textposition="outside",
        textfont=dict(color="white", size=10),
        hovertemplate="<b>%{y}</b><br>Active Programmes: %{x}<extra></extra>",
        name="Active Programmes",
    ), row=1, col=2)

    fig.update_layout(
        title=dict(
            text="<b>Province Opportunity Matrix</b><br>"
                 "<sup>Job creation potential + active programme coverage"
                 " by province and crisis tier</sup>",
            font=dict(size=15, color="white"),
            x=0.5,
        ),
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        showlegend=False,
        height=500,
        margin=dict(t=100, b=60, l=120, r=120),
    )

    fig.update_xaxes(
        gridcolor="#2C3E50",
        tickfont=dict(color="white"),
        range=[0, 115],
        row=1, col=1,
    )
    fig.update_xaxes(
        gridcolor="#2C3E50",
        tickfont=dict(color="white"),
        range=[0, 7],
        row=1, col=2,
    )
    fig.update_yaxes(
        gridcolor="#2C3E50",
        tickfont=dict(color="white", size=9),
    )

    return fig


def build_programme_reach():
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_prog["Programme"],
        y=df_prog["youth_reached"],
        marker_color=df_prog["color"],
        text=[
            str(int(v/1000)) + "K" if v < 1000000
            else str(round(v/1000000, 1)) + "M"
            for v in df_prog["youth_reached"]
        ],
        textposition="outside",
        textfont=dict(color="white", size=11),
        hovertemplate="<b>%{x}</b><br>Youth Reached: %{y:,}<extra></extra>",
    ))

    fig.update_layout(
        title=dict(
            text="<b>Programme Reach — Who Is Already Solving This</b><br>"
                 "<sup>Total youth supported by each active programme"
                 " | Sources: YES, Harambee, NYDA, SAYouth.mobi 2025</sup>",
            font=dict(size=14, color="white"),
            x=0.5,
        ),
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        xaxis=dict(
            gridcolor="#2C3E50",
            tickfont=dict(color="white", size=10),
        ),
        yaxis=dict(
            title="Youth Reached",
            gridcolor="#2C3E50",
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
        ),
        height=460,
        margin=dict(t=100, b=60, l=70, r=40),
        annotations=[
            dict(
                x="SAYouth.mobi", y=4800000,
                text="4.5M registered work-seekers",
                showarrow=True,
                arrowhead=2,
                arrowcolor="#9B59B6",
                font=dict(color="#9B59B6", size=10),
                ax=-80, ay=-30,
            ),
            dict(
                x="Harambee", y=1100000,
                text="876K income opportunities created",
                showarrow=True,
                arrowhead=2,
                arrowcolor="#3498DB",
                font=dict(color="#3498DB", size=10),
                ax=80, ay=-40,
            ),
        ],
    )

    return fig


def build_business_opportunities():
    businesses = {
        "Business Type": [
            "Agri-Processing Co-ops",
            "Solar Installation SMEs",
            "Mining Services",
            "Port Logistics SMEs",
            "Eco-Tourism Enterprises",
            "Timber Value Chain",
            "BPO and Call Centres",
            "Tech Startups",
            "Township Retail Hubs",
            "Recycling Enterprises",
        ],
        "Best Province": [
            "Eastern Cape",
            "Northern Cape",
            "North West",
            "KwaZulu-Natal",
            "Limpopo",
            "Mpumalanga",
            "KwaZulu-Natal",
            "Gauteng",
            "Gauteng",
            "North West",
        ],
        "jobs_per_100k": [45, 38, 52, 61, 34, 41, 67, 89, 73, 29],
        "startup_cost": [
            "R50K-R200K",
            "R80K-R300K",
            "R100K-R500K",
            "R200K-R1M",
            "R30K-R150K",
            "R80K-R400K",
            "R150K-R800K",
            "R20K-R100K",
            "R50K-R250K",
            "R15K-R80K",
        ],
        "funding_source": [
            "IDC, Jobs Fund",
            "IDC, NEF",
            "IDC, Mining SETA",
            "IDC, NEF",
            "NYDA, Jobs Fund",
            "IDC, AgriSETA",
            "IDC, BPO SETA",
            "IDC, NEF, Microsoft",
            "NYDA, NEF",
            "NYDA, Jobs Fund",
        ],
    }

    df_biz = pd.DataFrame(businesses)
    df_biz = df_biz.sort_values(
        "jobs_per_100k", ascending=True
    ).reset_index(drop=True)

    hover_texts = [
        "Best Province: " + p + "<br>Startup Cost: " + c + "<br>Funding: " + f
        for p, c, f in zip(
            df_biz["Best Province"],
            df_biz["startup_cost"],
            df_biz["funding_source"],
        )
    ]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_biz["jobs_per_100k"],
        y=df_biz["Business Type"],
        orientation="h",
        marker=dict(
            color=df_biz["jobs_per_100k"],
            colorscale="YlOrRd",
            showscale=True,
            colorbar=dict(
                title=dict(
                    text="Jobs per R100K",
                    font=dict(color="white"),
                ),
                tickfont=dict(color="white"),
            ),
        ),
        text=[
            str(j) + " jobs | " + p + " | " + c
            for j, p, c in zip(
                df_biz["jobs_per_100k"],
                df_biz["Best Province"],
                df_biz["startup_cost"],
            )
        ],
        textposition="outside",
        textfont=dict(color="white", size=8),
        customdata=hover_texts,
        hovertemplate="<b>%{y}</b><br>%{customdata}<extra></extra>",
    ))

    fig.update_layout(
        title=dict(
            text="<b>Strategic Business Opportunities by Province</b><br>"
                 "<sup>Ranked by job creation per R100K invested"
                 " | With startup costs and funding sources</sup>",
            font=dict(size=14, color="white"),
            x=0.5,
        ),
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        xaxis=dict(
            title="Jobs Created per R100K Invested",
            gridcolor="#2C3E50",
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
            range=[0, 110],
        ),
        yaxis=dict(
            gridcolor="#2C3E50",
            tickfont=dict(color="white", size=9),
        ),
        height=520,
        margin=dict(t=100, b=60, l=160, r=60),
    )

    return fig


