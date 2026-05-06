# SA Youth Economic Pulse Dashboard
### by Sankwela Solutions

> "Where are South Africa's youth being left behind — and where do the opportunities lie?"

*Intelligence. Trust. Modernity. Strategic Clarity.*

---

## 🌍 Live Dashboard

🔗 *[View Live Dashboard](https://web-production-ae6fa.up.railway.app)*

---

## What This Is

The SA Youth Economic Pulse Dashboard is a multi-module data intelligence
platform that maps South Africa's youth unemployment crisis — and provides
actionable, province-specific solutions for government, corporates, NGOs,
and investors.

This is not just a data dashboard. It is a decision-making engine.

---

## The Problem

- *46.1%* of South African youth (ages 15-34) are unemployed (Stats SA Q1 2025)
- *34%* are NEET — Not in Employment, Education, or Training
- *48.1%* of young women are excluded from the economy
- *58.7%* of unemployed youth have zero work experience
- The crisis is structural, provincial, and gendered — and it has never been
  mapped this comprehensively in one place

---

## The 7 Modules

| Module | What It Shows |
|--------|--------------|
| 1 — Crisis Map | Interactive choropleth map of all 9 provinces — 5 metric views |
| 2 — Education Funnel | Does education help? Unemployment by education level + skills mismatch |
| 3 — Decade of Decline | 20-year trend with COVID annotation, forecast, and danger threshold |
| 4 — Gender Lens | Male vs female exclusion by province + urban vs rural divide |
| 5 — Crime Correlation | Unemployment vs crime scatter plot — the story behind the numbers |
| 6 — Opportunities | Province intelligence briefs — situation, solutions, funding, contacts |
| 7 — Redistribution Engine | 9 sectors stress-tested — market size, ROI, export opportunity, skills pipeline |

---

## The Redistribution Engine — 9 Sectors

| Sector | Market 2025 | Market 2030 | Angel Verdict |
|--------|------------|------------|---------------|
| AgriTech & Precision Farming | $1.1B | $50B | STRONG BUY |
| Solar Manufacturing & Renewables | $2.1B | $15B | STRONG BUY |
| Electric Vehicles & Automotive | $4.8B | $33.1B | BUY |
| EdTech & Private TVET Colleges | $1.25B | $3.26B | STRONG BUY |
| Agri-Export Value Chains | $13.7B | $22B | STRONG BUY |
| Blue Economy | $0.8B | $6.5B | EARLY STAGE BUY |
| Mining Services SMEs | $55B | $60B | BUY |
| Township Retail & E-Commerce | $8.5B | $18B | BUY |
| Water Economy | $3.2B | $12B | STRONG BUY |

---

## Province Intelligence Briefs

Each of South Africa's 9 provinces has a full intelligence card covering:
- Crisis severity score and tier (Crisis / High Concern / Stabilise)
- The situation in plain language
- What is already working (YES, Harambee, NYDA, SETAs)
- What needs to happen — specific business opportunities
- Funding available (IDC, NEF, Jobs Fund, municipal PPPs)
- Key contact numbers

---

## Data Sources

All data is free, credible, and cited:

| Source | Data |
|--------|------|
| Stats SA ISIbalo | QLFS Q1 2025, NEET, GHS |
| DataFirst UCT | PALMS harmonised labour data |
| SAPS Annual Report | Crime statistics 2023/24 |
| World Bank | Youth unemployment time series |
| HSRC Spatial Insights | NEET mapping + Census 2022 |
| OpenData SA | Schools, health, housing |
| PoliceData.online | Pre-cleaned SAPS station data |

---

## Tech Stack

| Layer | Tool |
|-------|------|
| Dashboard Framework | Plotly Dash |
| Visualisations | Plotly |
| Data Processing | Python, Pandas, GeoPandas |
| Maps | Folium + GeoJSON |
| Deployment | Railway |
| Version Control | GitHub |

---

## Who This Is For

- *Government departments* — DPME, DHET, NYDA, provincial offices
- *Development Finance Institutions* — IDC, NEF, Jobs Fund
- *Corporate CSI teams* — B-BBEE investment targeting
- *NGOs and social enterprises* — YES, Harambee, SAYouth.mobi
- *Impact investors* — sector opportunity identification
- *Media* — data journalism on youth unemployment
- *Researchers* — academic and policy analysis

---

## About Sankwela Solutions

Sankwela Solutions is a data intelligence and analytics company
delivering strategic clarity through evidence-based insights.

*Intelligence. Trust. Modernity. Strategic Clarity.*

📧 Contact: tshepolefenya71@gmail.com

---

## Running Locally

```bash
git clone https://github.com/lefenyatshepo/sa-youth-pulse.git
cd sa-youth-pulse
pip install -r requirements.txt
python -c "import sys; sys.path.insert(0, '.'); from app.main import app; app.run(debug=False, port=8050)"