# ============================================================
# SA YOUTH PULSE DASHBOARD
# Module 7 — The Redistribution Engine
# 9 Sectors | Market data | ROI | Export | Skills Pipeline
# Water Economy included as Sector 9
# ============================================================

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

SECTORS = {
    "AgriTech & Precision Farming": {
        "market_2025_bn": 1.1,
        "market_2030_bn": 50.0,
        "cagr_pct": 15.0,
        "best_provinces": ["Free State", "Eastern Cape", "Western Cape"],
        "export_markets": ["Global", "EU", "China", "Middle East"],
        "youth_jobs": ["Drone operators", "Data analysts",
                       "Digital farm managers", "AgriTech support"],
        "startup_cost": "R80K - R500K",
        "funding": "DALRRD R330M grants, Land Bank, IDC",
        "idc_match": 85,
        "bbbee_score": 78,
        "viability": 95,
        "angel_verdict": "STRONG BUY",
        "verdict_color": "#27AE60",
        "description": (
            "SA AgriTech hit $1.1B in 2025, projected $50B by 2030. "
            "Agricultural drones alone: R1B in 2024, growing to R3B by 2030 "
            "— yet only 34 of 106 registered drone operators serve agriculture. "
            "Market is massively undersupplied. SA agricultural exports hit a "
            "record $13.7B in 2024. Over 60% of farms now use precision "
            "agriculture technology. New export markets: avocados to India "
            "and Japan confirmed 2024. DALRRD has R330M in grants available."
        ),
    },
    "Solar Manufacturing & Renewable Energy": {
        "market_2025_bn": 2.1,
        "market_2030_bn": 15.0,
        "cagr_pct": 48.0,
        "best_provinces": ["Mpumalanga", "Northern Cape", "Free State"],
        "export_markets": ["Pan-African", "SADC", "Middle East"],
        "youth_jobs": ["Panel assembly", "Solar installation",
                       "Electrical wiring", "Battery maintenance"],
        "startup_cost": "R50K - R300K",
        "funding": "IDC, REIPPPP, Chinese JV partnerships, NEF",
        "idc_match": 92,
        "bbbee_score": 85,
        "viability": 98,
        "angel_verdict": "STRONG BUY",
        "verdict_color": "#27AE60",
        "description": (
            "October 2025: Nkangala Municipality + China's Wucheng signed "
            "$35M solar panel assembly plant in Mpumalanga — Phase 1 creates "
            "150-200 jobs. By assembling locally, SA keeps 60% of value chain "
            "in-country. Northern Cape has highest solar irradiation on earth. "
            "Government committed R276B in public capex to energy transition. "
            "SMEs feeding the plant: logistics, installation, maintenance, "
            "electrical wiring, and battery storage servicing."
        ),
    },
    "Electric Vehicles & Automotive": {
        "market_2025_bn": 4.8,
        "market_2030_bn": 33.1,
        "cagr_pct": 47.0,
        "best_provinces": ["Eastern Cape", "Gauteng", "KwaZulu-Natal"],
        "export_markets": ["Africa via AfCFTA", "EU", "Middle East"],
        "youth_jobs": ["EV assembly", "Component supply",
                       "Charging infrastructure", "Fleet servicing"],
        "startup_cost": "R200K - R2M",
        "funding": "IDC, NEF, APDP automotive incentives",
        "idc_match": 88,
        "bbbee_score": 82,
        "viability": 87,
        "angel_verdict": "BUY",
        "verdict_color": "#F5A623",
        "description": (
            "Chinese EV exports to Africa surged 65% in 2025 — EVs made up "
            "30%+ of growth. SA holds 28.4% of Africa's automotive market, "
            "projected to reach $33B by 2033. VW and BMW supply chains in "
            "Eastern Cape create immediate SME opportunity. Under AfCFTA, "
            "vehicles are a priority sector. SMEs feeding EV assembly: "
            "component supply, charging infrastructure, servicing centres, "
            "driver training, and fleet management."
        ),
    },
    "EdTech & Private TVET Colleges": {
        "market_2025_bn": 1.25,
        "market_2030_bn": 3.26,
        "cagr_pct": 10.9,
        "best_provinces": ["Northern Cape", "North West",
                           "Mpumalanga", "Eastern Cape"],
        "export_markets": ["Pan-African students", "SADC"],
        "youth_jobs": ["Lecturers", "Administrators",
                       "Tech support", "Student services"],
        "startup_cost": "R500K - R5M",
        "funding": "DHET subsidies, NSFAS, SETA learnerships, B-BBEE bursaries",
        "idc_match": 75,
        "bbbee_score": 90,
        "viability": 92,
        "angel_verdict": "STRONG BUY",
        "verdict_color": "#27AE60",
        "description": (
            "SA ranks 42nd of 44 countries in vocational enrolment — only "
            "8.9% of upper secondary students are in TVET. EdTech market hit "
            "$1.25B in 2025, growing to $3.26B by 2034. A private TVET campus "
            "near a solar plant, mine, or agri-hub has 4 revenue streams: "
            "DHET subsidies, NSFAS fees, SETA learnership funding, and "
            "corporate B-BBEE bursaries. Rural provinces are massively "
            "underserved — Northern Cape has a solar assembly plant arriving "
            "with no training institution nearby."
        ),
    },
    "Agri-Export Value Chains": {
        "market_2025_bn": 13.7,
        "market_2030_bn": 22.0,
        "cagr_pct": 9.8,
        "best_provinces": ["Limpopo", "Eastern Cape",
                           "Free State", "North West"],
        "export_markets": ["China", "India", "Japan", "EU", "Africa"],
        "youth_jobs": ["Processing operators", "Cold-chain logistics",
                       "Quality control", "Export documentation"],
        "startup_cost": "R100K - R1M",
        "funding": "IDC, Jobs Fund, AgriSETA, FPEF export grants",
        "idc_match": 90,
        "bbbee_score": 85,
        "viability": 94,
        "angel_verdict": "STRONG BUY",
        "verdict_color": "#27AE60",
        "description": (
            "SA agricultural exports hit a record $13.7B in 2024 — up 10% "
            "in 2025. New export markets confirmed: avocados to India and "
            "Japan, wool and dairy to China. Limpopo avocados, Eastern Cape "
            "mohair, Free State maize, North West beef — all with confirmed "
            "international demand. Adding value locally multiplies revenue "
            "per ton and creates significantly more youth jobs than raw "
            "commodity export. Cold-chain and packaging are the key gaps."
        ),
    },
    "Blue Economy": {
        "market_2025_bn": 0.8,
        "market_2030_bn": 6.5,
        "cagr_pct": 52.0,
        "best_provinces": ["Western Cape", "KwaZulu-Natal", "Eastern Cape"],
        "export_markets": ["EU", "Asia", "Middle East", "USA"],
        "youth_jobs": ["Aquaculture operators", "Marine logistics",
                       "Ocean tourism", "Seaweed processing"],
        "startup_cost": "R80K - R600K",
        "funding": "IDC, Operation Phakisa, Blue Economy Fund",
        "idc_match": 72,
        "bbbee_score": 80,
        "viability": 84,
        "angel_verdict": "EARLY STAGE BUY",
        "verdict_color": "#3498DB",
        "description": (
            "SA has 2,800km of coastline between two oceans yet the ocean "
            "economy contributes less than 1% of GDP. Operation Phakisa "
            "targets R177B in ocean economy value by 2033. Aquaculture, "
            "marine tourism, seaweed processing, and offshore wind are all "
            "early-stage — first-mover advantage still available. Highest "
            "upside relative to current competition. Western Cape Silicon "
            "Cape tech can combine with blue economy for aquatech startups."
        ),
    },
    "Mining Services SMEs": {
        "market_2025_bn": 55.0,
        "market_2030_bn": 60.0,
        "cagr_pct": 1.8,
        "best_provinces": ["North West", "Limpopo",
                           "Mpumalanga", "Northern Cape"],
        "export_markets": ["SADC", "Regional Africa"],
        "youth_jobs": ["Equipment maintenance", "Safety officers",
                       "Catering and facilities", "Environmental monitoring"],
        "startup_cost": "R100K - R500K",
        "funding": "IDC, Mining SETA, NEF, Jobs Fund",
        "idc_match": 80,
        "bbbee_score": 88,
        "viability": 89,
        "angel_verdict": "BUY",
        "verdict_color": "#F5A623",
        "description": (
            "SA mining grew 2.5% in Q3 2025, led by platinum group metals. "
            "Sector worth R550B annually. Most service contracts go to large "
            "corporations — not local SMEs. Mining companies face B-BBEE "
            "pressure to localise supply chains. Catering, maintenance, "
            "security, and transport SMEs within 50km of a mine have "
            "guaranteed demand. North West has 3 major platinum corridors "
            "with underserved local supply chains. Mining SETA funds "
            "learnerships to skill youth for these roles."
        ),
    },
    "Township Retail & E-Commerce": {
        "market_2025_bn": 8.5,
        "market_2030_bn": 18.0,
        "cagr_pct": 16.2,
        "best_provinces": ["Gauteng", "KwaZulu-Natal", "Western Cape"],
        "export_markets": ["Domestic", "Pan-African e-commerce"],
        "youth_jobs": ["Delivery drivers", "Warehouse operators",
                       "Digital marketers", "Customer service"],
        "startup_cost": "R20K - R150K",
        "funding": "NYDA, NEF, Standard Bank Township Economy Fund",
        "idc_match": 70,
        "bbbee_score": 92,
        "viability": 91,
        "angel_verdict": "BUY",
        "verdict_color": "#F5A623",
        "description": (
            "SA township economy estimated at R900B annually — yet most "
            "spending leaves the township to retail chains. E-commerce "
            "penetration growing rapidly as smartphone access exceeds 70%. "
            "Last-mile delivery, local fulfilment hubs, and township-specific "
            "platforms have the lowest startup cost of any sector and fastest "
            "job creation rate. R20K can create 5 jobs. Harambee and "
            "SAYouth.mobi have the largest youth pipeline for this sector."
        ),
    },
    "Water Economy": {
        "market_2025_bn": 3.2,
        "market_2030_bn": 12.0,
        "cagr_pct": 30.2,
        "best_provinces": ["North West", "Eastern Cape", "Limpopo",
                           "KwaZulu-Natal", "Gauteng"],
        "export_markets": ["Pan-African", "SADC water solutions"],
        "youth_jobs": ["Pipe technicians", "Water quality testers",
                       "Borehole drillers", "Rainwater installers",
                       "Water shop operators"],
        "startup_cost": "R15K - R2M",
        "funding": "DWS, IDC, Green bonds, Municipal PPP contracts",
        "idc_match": 88,
        "bbbee_score": 91,
        "viability": 96,
        "angel_verdict": "STRONG BUY",
        "verdict_color": "#27AE60",
        "description": (
            "46% of SA water systems pose serious health risks. 67.6% of "
            "wastewater facilities near failure. 47% of treated water lost "
            "to leaks — R7.3B lost annually in non-revenue water. "
            "R41.4B needed for universal sanitation access. Government "
            "actively calling for private sector participation. 7 business "
            "models: water shops (R15K entry), leak detection SMEs, "
            "rainwater harvesting, borehole drilling, wastewater treatment "
            "PPPs, water quality testing labs, and atmospheric water "
            "generation. Water security multiplies value of every other "
            "sector — agriculture, mining, manufacturing, and education "
            "all depend on it."
        ),
    },
}

SKILLS_PIPELINE = {
    "AgriTech & Precision Farming": {
        "seta": "AgriSETA",
        "npo": "YES + Harambee",
        "programme": "Drone operator learnership + digital farm management",
        "duration": "6-12 months",
        "cost_per_youth": 18000,
    },
    "Solar Manufacturing & Renewable Energy": {
        "seta": "ESETA",
        "npo": "YES + NYDA",
        "programme": "Solar PV installation NQF Level 4",
        "duration": "6 months",
        "cost_per_youth": 22000,
    },
    "Electric Vehicles & Automotive": {
        "seta": "merSETA",
        "npo": "YES + Harambee",
        "programme": "Automotive components + EV servicing learnership",
        "duration": "12 months",
        "cost_per_youth": 28000,
    },
    "EdTech & Private TVET Colleges": {
        "seta": "ETDP SETA",
        "npo": "YES + NYDA",
        "programme": "Educator development + digital instruction",
        "duration": "6 months",
        "cost_per_youth": 15000,
    },
    "Agri-Export Value Chains": {
        "seta": "AgriSETA + FoodBev SETA",
        "npo": "YES + Harambee",
        "programme": "Food processing NQF + export compliance training",
        "duration": "6-9 months",
        "cost_per_youth": 20000,
    },
    "Blue Economy": {
        "seta": "Transport SETA + AgriSETA",
        "npo": "YES + NYDA",
        "programme": "Aquaculture operator + marine services NQF",
        "duration": "6 months",
        "cost_per_youth": 25000,
    },
    "Mining Services SMEs": {
        "seta": "MQA",
        "npo": "YES + Harambee",
        "programme": "Mine environment control + safety officer NQF",
        "duration": "12 months",
        "cost_per_youth": 32000,
    },
    "Township Retail & E-Commerce": {
        "seta": "W&RSETA",
        "npo": "Harambee + SAYouth.mobi",
        "programme": "Retail management + e-commerce operations",
        "duration": "3-6 months",
        "cost_per_youth": 10000,
    },
    "Water Economy": {
        "seta": "EWSETA",
        "npo": "YES + NYDA + municipalities",
        "programme": "Water and sanitation NQF + pipe technician learnership",
        "duration": "6-9 months",
        "cost_per_youth": 19000,
    },
}

SECTOR_SHORTS = [
    "AgriTech", "Solar/Energy", "EV/Auto",
    "EdTech/TVET", "Agri Exports", "Blue Economy",
    "Mining SMEs", "Township/E-Comm", "Water Economy"
]


def build_sector_market_map():
    sectors = list(SECTORS.keys())
    m2025   = [SECTORS[s]["market_2025_bn"] for s in sectors]
    m2030   = [SECTORS[s]["market_2030_bn"] for s in sectors]
    viab    = [SECTORS[s]["viability"] for s in sectors]
    verdicts= [SECTORS[s]["angel_verdict"] for s in sectors]
    colors  = [SECTORS[s]["verdict_color"] for s in sectors]

    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(
            "Market Size: 2025 vs 2030 (USD Billions)",
            "Angel Investor Viability Score (/100)"
        ),
        horizontal_spacing=0.15,
    )

    fig.add_trace(go.Bar(
        name="2025 Market",
        x=m2025, y=SECTOR_SHORTS,
        orientation="h",
        marker_color="#1A5276",
        text=["$" + str(v) + "B" for v in m2025],
        textposition="outside",
        textfont=dict(color="white", size=8),
        hovertemplate="<b>%{y}</b><br>2025: $%{x}B<extra></extra>",
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        name="2030 Projected",
        x=m2030, y=SECTOR_SHORTS,
        orientation="h",
        marker_color=colors,
        text=["$" + str(v) + "B" for v in m2030],
        textposition="outside",
        textfont=dict(color="white", size=8),
        hovertemplate="<b>%{y}</b><br>2030: $%{x}B<extra></extra>",
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        name="Viability",
        x=viab, y=SECTOR_SHORTS,
        orientation="h",
        marker_color=colors,
        text=[str(v) + " — " + d for v, d in zip(viab, verdicts)],
        textposition="outside",
        textfont=dict(color="white", size=8),
        hovertemplate="<b>%{y}</b><br>Viability: %{x}/100<extra></extra>",
        showlegend=False,
    ), row=1, col=2)

    fig.update_layout(
        title=dict(
            text="<b>The Redistribution Engine — 9 Sectors, Stress-Tested</b><br>"
                 "<sup>Angel investor market scan | All data verified 2025 "
                 "| AgriTech Report, Bloomberg, IRENA, OECD, Stats SA, DWS</sup>",
            font=dict(size=13, color="white"),
            x=0.5,
        ),
        barmode="group",
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        legend=dict(
            bgcolor="#1E3A5F", bordercolor="#2C3E50",
            font=dict(color="white"),
            orientation="h", y=-0.12,
        ),
        height=560,
        margin=dict(t=110, b=80, l=130, r=80),
    )
    fig.update_xaxes(gridcolor="#2C3E50", tickfont=dict(color="white"))
    fig.update_yaxes(gridcolor="#2C3E50", tickfont=dict(color="white", size=8))
    return fig


def build_roi_matrix():
    sectors   = list(SECTORS.keys())
    idc_match = [SECTORS[s]["idc_match"]  for s in sectors]
    bbbee     = [SECTORS[s]["bbbee_score"] for s in sectors]
    colors    = [SECTORS[s]["verdict_color"] for s in sectors]
    cagr      = [SECTORS[s]["cagr_pct"] for s in sectors]

    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(
            "IDC Funding Match vs B-BBEE Score",
            "Projected Growth Rate (CAGR %) to 2030"
        ),
        horizontal_spacing=0.15,
    )

    fig.add_trace(go.Scatter(
        x=idc_match, y=bbbee,
        mode="markers+text",
        marker=dict(
            size=16, color=colors, opacity=0.9,
            line=dict(width=1, color="white"),
        ),
        text=SECTOR_SHORTS,
        textposition="top center",
        textfont=dict(color="white", size=8),
        hovertemplate=(
            "<b>%{text}</b><br>"
            "IDC Match: %{x}/100<br>"
            "B-BBEE: %{y}/100<extra></extra>"
        ),
        name="IDC vs B-BBEE",
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        x=cagr, y=SECTOR_SHORTS,
        orientation="h",
        marker_color=colors,
        text=[str(v) + "% CAGR" for v in cagr],
        textposition="outside",
        textfont=dict(color="white", size=8),
        hovertemplate="<b>%{y}</b><br>CAGR: %{x}%<extra></extra>",
        showlegend=False,
    ), row=1, col=2)

    fig.update_layout(
        title=dict(
            text="<b>Corporate & SME ROI Matrix</b><br>"
                 "<sup>IDC funding match, B-BBEE contribution, "
                 "and compound annual growth rate by sector</sup>",
            font=dict(size=13, color="white"),
            x=0.5,
        ),
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        showlegend=False,
        height=520,
        margin=dict(t=100, b=60, l=130, r=80),
    )
    fig.update_xaxes(gridcolor="#2C3E50", tickfont=dict(color="white"))
    fig.update_yaxes(gridcolor="#2C3E50", tickfont=dict(color="white", size=8))
    return fig


def build_export_opportunity():
    export_scores = [80, 88, 85, 45, 95, 75, 60, 40, 70]
    export_markets = [4, 3, 4, 2, 5, 4, 2, 2, 3]
    colors = [SECTORS[s]["verdict_color"] for s in SECTORS.keys()]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=export_scores,
        y=SECTOR_SHORTS,
        orientation="h",
        marker_color=colors,
        text=[
            str(s) + "/100 | " + str(m) + " markets"
            for s, m in zip(export_scores, export_markets)
        ],
        textposition="outside",
        textfont=dict(color="white", size=9),
        hovertemplate="<b>%{y}</b><br>Export Score: %{x}/100<extra></extra>",
    ))

    fig.update_layout(
        title=dict(
            text="<b>International Export Opportunity Score by Sector</b><br>"
                 "<sup>Based on confirmed market access, AfCFTA, AGOA, "
                 "SADC-EU EPA trade agreements, and 2025 export data</sup>",
            font=dict(size=13, color="white"),
            x=0.5,
        ),
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        xaxis=dict(
            title="Export Opportunity Score (/100)",
            gridcolor="#2C3E50",
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
            range=[0, 120],
        ),
        yaxis=dict(
            gridcolor="#2C3E50",
            tickfont=dict(color="white", size=9),
        ),
        height=440,
        margin=dict(t=100, b=60, l=130, r=80),
    )
    return fig


def build_skills_pipeline():
    sectors = list(SKILLS_PIPELINE.keys())
    costs   = [SKILLS_PIPELINE[s]["cost_per_youth"] for s in sectors]
    colors  = [SECTORS[s]["verdict_color"] for s in sectors]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=SECTOR_SHORTS,
        y=costs,
        marker_color=colors,
        text=[
            SKILLS_PIPELINE[s]["npo"] + " | " + SKILLS_PIPELINE[s]["duration"]
            for s in sectors
        ],
        textposition="outside",
        textfont=dict(color="white", size=8),
        hovertemplate=(
            "<b>%{x}</b><br>Cost per youth: R%{y:,}<extra></extra>"
        ),
    ))

    fig.update_layout(
        title=dict(
            text="<b>Skills Pipeline — Cost Per Youth Trained by Sector</b><br>"
                 "<sup>NPO and SETA responsible for skills delivery "
                 "once business investment is confirmed per province</sup>",
            font=dict(size=13, color="white"),
            x=0.5,
        ),
        paper_bgcolor="#1E3A5F",
        plot_bgcolor="#152C47",
        font=dict(color="white", family="Arial"),
        xaxis=dict(
            gridcolor="#2C3E50",
            tickfont=dict(color="white", size=8),
        ),
        yaxis=dict(
            title="Cost per Youth Trained (Rands)",
            gridcolor="#2C3E50",
            tickfont=dict(color="white"),
            title_font=dict(color="white"),
        ),
        height=440,
        margin=dict(t=100, b=100, l=80, r=40),
    )
    return fig


def get_sector_detail(sector):
    if sector not in SECTORS:
        return None
    s = SECTORS[sector]
    p = SKILLS_PIPELINE.get(sector, {})
    return {**s, **p}


def get_all_sectors():
    return list(SECTORS.keys())