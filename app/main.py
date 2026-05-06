import sys
import os
import datetime

sys.path.insert(0, os.path.abspath("."))

import dash
from dash import dcc, html, Input, Output

from app.layouts.module1_map import build_map
from app.layouts.module2_education import build_funnel, build_skills_gap
from app.layouts.module3_trends import build_trend_chart
from app.layouts.module4_gender import build_gender_chart, build_urban_rural
from app.layouts.module5_crime import build_scatter, build_crime_ranking
from app.layouts.module6_opportunities import (
    build_opportunity_matrix,
    build_programme_reach,
    build_business_opportunities,
)
from app.layouts.module7_redistribution import (
    build_sector_market_map,
    build_roi_matrix,
    build_export_opportunity,
    build_skills_pipeline,
    get_sector_detail,
    get_all_sectors,
)
from app.layouts.module6_intelligence import (
    get_intelligence_card,
    get_all_provinces,
)

DATA_UPDATED = "Q1 2025 - Stats SA QLFS + SAPS 2023/24 + World Bank 2025"
BUILD_DATE = datetime.datetime.now().strftime("%d %B %Y")

app = dash.Dash(
    "sa_youth_pulse",
    title="SA Youth Economic Pulse",
    suppress_callback_exceptions=True,
    assets_folder=os.path.abspath("assets"),
)

NAVY  = "#1E3A5F"
AMBER = "#F5A623"
RED   = "#C0392B"
GREEN = "#27AE60"
GREY  = "#2C3E50"
WHITE = "#FFFFFF"

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "220px",
    "padding": "20px 10px",
    "backgroundColor": GREY,
    "overflowY": "auto",
    "zIndex": 1000,
}

CONTENT_STYLE = {
    "marginLeft": "240px",
    "padding": "20px",
    "backgroundColor": NAVY,
    "minHeight": "100vh",
}

NAV_ITEM = {
    "display": "block",
    "padding": "10px 15px",
    "marginBottom": "6px",
    "borderRadius": "6px",
    "color": WHITE,
    "fontSize": "13px",
    "cursor": "pointer",
    "border": "1px solid #3D5A7A",
    "backgroundColor": NAVY,
}

CARD_STYLE = {
    "backgroundColor": "#152C47",
    "borderRadius": "8px",
    "padding": "15px",
    "marginBottom": "15px",
    "border": "1px solid #2C3E50",
}

KPI_STYLE = {
    "backgroundColor": RED,
    "borderRadius": "8px",
    "padding": "15px",
    "textAlign": "center",
    "margin": "5px",
    "flex": "1",
}

KPI_GREEN  = {**KPI_STYLE, "backgroundColor": GREEN}
KPI_ORANGE = {**KPI_STYLE, "backgroundColor": "#E67E22"}
KPI_NAVY   = {**KPI_STYLE, "backgroundColor": "#1A5276"}


def kpi_card(value, label, style=None):
    if style is None:
        style = KPI_STYLE
    return html.Div([
        html.H2(value, style={
            "color": AMBER, "margin": "0",
            "fontSize": "24px", "fontWeight": "bold",
        }),
        html.P(label, style={
            "color": WHITE, "margin": "5px 0 0 0",
            "fontSize": "11px", "lineHeight": "1.3",
        }),
    ], style=style)


HEADER_CONTENT = html.Div([
    html.Div([
        html.Div([
            html.H1(
                "SA Youth Economic Pulse Dashboard",
                style={
                    "color": WHITE, "margin": "0",
                    "fontSize": "20px", "fontWeight": "bold",
                }
            ),
            html.P(
                "Where are South Africa's youth being left behind "
                "- and where do the opportunities lie?",
                style={
                    "color": AMBER, "margin": "4px 0 0 0",
                    "fontSize": "11px", "fontStyle": "italic",
                }
            ),
        ], style={"flex": "1"}),
        html.Div([
            html.P("Powered by", style={
                "color": "#BDC3C7", "fontSize": "8px",
                "margin": "0", "textAlign": "right",
            }),
            html.P("SANKWELA SOLUTIONS", style={
                "color": AMBER, "fontSize": "11px",
                "fontWeight": "bold", "margin": "0",
                "textAlign": "right", "letterSpacing": "1px",
            }),
            html.P(
                "Intelligence. Trust. Modernity. Strategic Clarity.",
                style={
                    "color": "#BDC3C7", "fontSize": "7px",
                    "margin": "0", "textAlign": "right",
                    "fontStyle": "italic",
                }
            ),
        ]),
    ], style={
        "display": "flex",
        "justifyContent": "space-between",
        "alignItems": "center",
    }),
], style={
    "backgroundColor": NAVY,
    "padding": "15px 20px",
    "marginBottom": "15px",
    "borderBottom": "3px solid " + AMBER,
    "borderRadius": "8px",
})

KPI_ROW = html.Div([
    kpi_card("46.1%", "Youth Unemployment (ages 15-34, Q1 2025)"),
    kpi_card("34%",   "NEET Rate (ages 15-24)", KPI_ORANGE),
    kpi_card("48.1%", "Female NEET (ages 15-34)"),
    kpi_card("58.7%", "Youth with Zero Work Experience"),
    kpi_card("27.5pt","Youth vs National Unemployment Gap", KPI_NAVY),
    kpi_card("23.9%", "Degree Holders Unemployed", KPI_GREEN),
], style={
    "display": "flex",
    "flexWrap": "wrap",
    "marginBottom": "15px",
    "gap": "5px",
})

sidebar = html.Div([
    html.Img(
        src="/assets/sankwela_logo.png",
        style={
            "width": "160px",
            "marginBottom": "6px",
            "display": "block",
        }
    ),
    html.P(
        "INTELLIGENCE. TRUST. MODERNITY. STRATEGIC CLARITY.",
        style={
            "color": AMBER, "fontSize": "7px",
            "margin": "0 0 4px 0",
            "letterSpacing": "0.5px",
        }
    ),
    html.Hr(style={"borderColor": AMBER, "margin": "6px 0"}),
    html.P("SA Youth Economic Pulse", style={
        "color": WHITE, "fontSize": "11px",
        "fontWeight": "bold", "margin": "0 0 12px 0",
    }),
    html.Hr(style={"borderColor": "#3D5A7A"}),
    html.P("MODULES", style={
        "color": "#BDC3C7", "fontSize": "10px",
        "fontWeight": "bold", "marginBottom": "8px",
    }),
    html.Div(id="nav-module1",
             children="Module 1 - Crisis Map",
             n_clicks=0, style=NAV_ITEM),
    html.Div(id="nav-module2",
             children="Module 2 - Education Funnel",
             n_clicks=0, style=NAV_ITEM),
    html.Div(id="nav-module3",
             children="Module 3 - Decade of Decline",
             n_clicks=0, style=NAV_ITEM),
    html.Div(id="nav-module4",
             children="Module 4 - Gender Lens",
             n_clicks=0, style=NAV_ITEM),
    html.Div(id="nav-module5",
             children="Module 5 - Crime Correlation",
             n_clicks=0, style=NAV_ITEM),
    html.Div(id="nav-module6",
             children="Module 6 - Opportunities",
             n_clicks=0, style=NAV_ITEM),
    html.Div(id="nav-module7",
             children="Module 7 - Redistribution Engine",
             n_clicks=0, style=NAV_ITEM),
    html.Hr(style={"borderColor": "#3D5A7A"}),
    html.P("DATA SOURCES", style={
        "color": "#BDC3C7", "fontSize": "10px",
        "fontWeight": "bold", "marginBottom": "4px",
    }),
    html.P("Stats SA QLFS Q1 2025",
           style={"color": "#7F8C8D", "fontSize": "9px", "margin": "2px 0"}),
    html.P("SAPS Annual Report 2023/24",
           style={"color": "#7F8C8D", "fontSize": "9px", "margin": "2px 0"}),
    html.P("World Bank 2025",
           style={"color": "#7F8C8D", "fontSize": "9px", "margin": "2px 0"}),
    html.P("DataFirst UCT",
           style={"color": "#7F8C8D", "fontSize": "9px", "margin": "2px 0"}),
    html.Hr(style={"borderColor": "#3D5A7A"}),
    html.P("Last updated: " + BUILD_DATE,
           style={"color": "#7F8C8D", "fontSize": "9px", "margin": "4px 0"}),
    html.P(DATA_UPDATED,
           style={"color": "#7F8C8D", "fontSize": "8px", "margin": "2px 0"}),
], style=SIDEBAR_STYLE)

app.layout = html.Div([
    dcc.Store(id="active-module", data="module1"),
    sidebar,
    html.Div(id="page-content", style=CONTENT_STYLE),
])


@app.callback(
    Output("active-module", "data"),
    [Input("nav-module1", "n_clicks"),
     Input("nav-module2", "n_clicks"),
     Input("nav-module3", "n_clicks"),
     Input("nav-module4", "n_clicks"),
     Input("nav-module5", "n_clicks"),
     Input("nav-module6", "n_clicks"),
     Input("nav-module7", "n_clicks")],
    prevent_initial_call=False,
)
def update_active_module(n1, n2, n3, n4, n5, n6, n7):
    ctx = dash.callback_context
    if not ctx.triggered:
        return "module1"
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    mapping = {
        "nav-module1": "module1",
        "nav-module2": "module2",
        "nav-module3": "module3",
        "nav-module4": "module4",
        "nav-module5": "module5",
        "nav-module6": "module6",
        "nav-module7": "module7",
    }
    return mapping.get(button_id, "module1")


@app.callback(
    Output("page-content", "children"),
    Input("active-module", "data"),
)
def render_page(module):

    if module == "module1":
        return html.Div([
            HEADER_CONTENT, KPI_ROW,
            html.Div([
                html.H3("The Crisis Map", style={
                    "color": AMBER, "margin": "0 0 5px 0",
                    "fontSize": "16px",
                }),
                html.P(
                    "Select a metric to explore the provincial crisis landscape.",
                    style={"color": "#BDC3C7", "fontSize": "12px",
                           "margin": "0 0 10px 0"}
                ),
                dcc.Dropdown(
                    id="map-metric-dropdown",
                    options=[
                        {"label": "Youth Unemployment Rate",
                         "value": "youth_unemployment_rate"},
                        {"label": "NEET Rate",
                         "value": "neet_rate"},
                        {"label": "Female NEET Rate",
                         "value": "female_neet_rate"},
                        {"label": "Overall Severity Score",
                         "value": "severity_score"},
                        {"label": "Labour Participation Rate",
                         "value": "labour_participation_rate"},
                    ],
                    value="youth_unemployment_rate",
                    clearable=False,
                    style={
                        "backgroundColor": GREY,
                        "color": NAVY,
                        "width": "350px",
                        "marginBottom": "10px",
                    },
                ),
                dcc.Graph(id="map-chart"),
            ], style=CARD_STYLE),
        ])

    elif module == "module2":
        return html.Div([
            HEADER_CONTENT, KPI_ROW,
            html.Div([
                html.H3("Education to Employment Funnel",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_funnel()),
            ], style=CARD_STYLE),
            html.Div([
                html.H3("The Skills Mismatch",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_skills_gap()),
            ], style=CARD_STYLE),
        ])

    elif module == "module3":
        return html.Div([
            HEADER_CONTENT, KPI_ROW,
            html.Div([
                html.H3("The Decade of Decline",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_trend_chart()),
            ], style=CARD_STYLE),
        ])

    elif module == "module4":
        return html.Div([
            HEADER_CONTENT, KPI_ROW,
            html.Div([
                html.H3("The Gender Lens",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_gender_chart()),
            ], style=CARD_STYLE),
            html.Div([
                html.H3("Urban vs Rural - The Hidden Crisis",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_urban_rural()),
            ], style=CARD_STYLE),
        ])

    elif module == "module5":
        return html.Div([
            HEADER_CONTENT, KPI_ROW,
            html.Div([
                html.H3("Unemployment vs Crime Correlation",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_scatter()),
            ], style=CARD_STYLE),
            html.Div([
                html.H3("Province Crime Index Ranking",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_crime_ranking()),
            ], style=CARD_STYLE),
        ])

    elif module == "module6":
        provinces = get_all_provinces()
        return html.Div([
            HEADER_CONTENT, KPI_ROW,
            html.Div([
                html.H3("Province Intelligence Brief",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 5px 0"}),
                html.P(
                    "Select a province for the full intelligence brief - "
                    "situation, what is working, opportunities, and funding.",
                    style={"color": "#BDC3C7", "fontSize": "12px",
                           "margin": "0 0 10px 0"}
                ),
                dcc.Dropdown(
                    id="province-dropdown",
                    options=[{"label": p, "value": p} for p in provinces],
                    value="North West",
                    clearable=False,
                    style={
                        "backgroundColor": GREY,
                        "color": NAVY,
                        "width": "300px",
                        "marginBottom": "15px",
                    },
                ),
                html.Div(id="intelligence-card"),
            ], style=CARD_STYLE),
            html.Div([
                html.H3("Province Opportunity Matrix",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_opportunity_matrix()),
            ], style=CARD_STYLE),
            html.Div([
                html.H3("Programme Reach",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_programme_reach()),
            ], style=CARD_STYLE),
            html.Div([
                html.H3("Strategic Business Opportunities",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_business_opportunities()),
            ], style=CARD_STYLE),
        ])

    elif module == "module7":
        sectors = get_all_sectors()
        return html.Div([
            HEADER_CONTENT, KPI_ROW,
            html.Div([
                html.H3("The Redistribution Engine",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 5px 0"}),
                html.P(
                    "9 sectors stress-tested by an angel investor. "
                    "Market size, ROI, export opportunity, and the "
                    "skills pipeline. Select a sector for the full brief.",
                    style={"color": "#BDC3C7", "fontSize": "12px",
                           "margin": "0 0 10px 0"}
                ),
                dcc.Dropdown(
                    id="sector-dropdown",
                    options=[{"label": s, "value": s} for s in sectors],
                    value="Water Economy",
                    clearable=False,
                    style={
                        "backgroundColor": GREY,
                        "color": NAVY,
                        "width": "400px",
                        "marginBottom": "15px",
                    },
                ),
                html.Div(id="sector-detail-card"),
            ], style=CARD_STYLE),
            html.Div([
                html.H3("9 Sectors - Market Size and Viability",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_sector_market_map()),
            ], style=CARD_STYLE),
            html.Div([
                html.H3("Corporate and SME ROI Matrix",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_roi_matrix()),
            ], style=CARD_STYLE),
            html.Div([
                html.H3("International Export Opportunity",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_export_opportunity()),
            ], style=CARD_STYLE),
            html.Div([
                html.H3("Skills Pipeline - Cost Per Youth by Sector",
                        style={"color": AMBER, "fontSize": "16px",
                               "margin": "0 0 10px 0"}),
                dcc.Graph(figure=build_skills_pipeline()),
            ], style=CARD_STYLE),
        ])

    return html.Div([
        HEADER_CONTENT,
        html.P("Select a module from the sidebar.",
               style={"color": WHITE}),
    ])


@app.callback(
    Output("map-chart", "figure"),
    Input("map-metric-dropdown", "value"),
)
def update_map(metric):
    return build_map(metric)


@app.callback(
    Output("intelligence-card", "children"),
    Input("province-dropdown", "value"),
)
def update_intelligence_card(province):
    card = get_intelligence_card(province)
    if not card:
        return html.P("No data available.", style={"color": WHITE})
    tier_color = card["tier_color"]
    return html.Div([
        html.Div([
            html.H2(province + " - " + card["tier"] + " TIER",
                    style={"color": WHITE, "margin": "0",
                           "fontSize": "18px", "fontWeight": "bold"}),
            html.Div([
                html.Span("Unemployment: " + card["unemployment"],
                          style={"color": AMBER, "fontSize": "12px",
                                 "marginRight": "20px"}),
                html.Span("NEET Rate: " + card["neet"],
                          style={"color": AMBER, "fontSize": "12px",
                                 "marginRight": "20px"}),
                html.Span("Female NEET: " + card["female_neet"],
                          style={"color": AMBER, "fontSize": "12px"}),
            ], style={"marginTop": "5px"}),
        ], style={
            "backgroundColor": tier_color,
            "padding": "12px 15px",
            "borderRadius": "6px 6px 0 0",
        }),
        html.Div([
            html.Div([
                html.H4("THE SITUATION",
                        style={"color": AMBER, "fontSize": "12px",
                               "fontWeight": "bold", "margin": "0 0 6px 0",
                               "letterSpacing": "1px"}),
                html.P(card["situation"],
                       style={"color": WHITE, "fontSize": "12px",
                              "lineHeight": "1.7", "margin": "0"}),
            ], style={"marginBottom": "15px"}),
            html.Div([
                html.H4("WHAT IS ALREADY WORKING",
                        style={"color": GREEN, "fontSize": "12px",
                               "fontWeight": "bold", "margin": "0 0 6px 0",
                               "letterSpacing": "1px"}),
                html.P(card["working"],
                       style={"color": WHITE, "fontSize": "12px",
                              "lineHeight": "1.7", "margin": "0"}),
            ], style={"marginBottom": "15px"}),
            html.Div([
                html.H4("WHAT NEEDS TO HAPPEN - OPPORTUNITIES",
                        style={"color": "#3498DB", "fontSize": "12px",
                               "fontWeight": "bold", "margin": "0 0 6px 0",
                               "letterSpacing": "1px"}),
                html.P(card["opportunities"],
                       style={"color": WHITE, "fontSize": "12px",
                              "lineHeight": "1.7", "margin": "0"}),
            ], style={"marginBottom": "15px"}),
            html.Div([
                html.H4("FUNDING AVAILABLE",
                        style={"color": AMBER, "fontSize": "12px",
                               "fontWeight": "bold", "margin": "0 0 4px 0",
                               "letterSpacing": "1px"}),
                html.P(card["funding"],
                       style={"color": WHITE, "fontSize": "12px",
                              "margin": "0 0 10px 0"}),
                html.H4("KEY CONTACTS",
                        style={"color": AMBER, "fontSize": "12px",
                               "fontWeight": "bold", "margin": "0 0 4px 0",
                               "letterSpacing": "1px"}),
                html.P(card["key_contact"],
                       style={"color": "#3498DB", "fontSize": "12px",
                              "margin": "0"}),
            ]),
        ], style={
            "backgroundColor": "#152C47",
            "padding": "15px",
            "borderRadius": "0 0 6px 6px",
            "border": "1px solid " + tier_color,
            "borderTop": "none",
        }),
    ])


@app.callback(
    Output("sector-detail-card", "children"),
    Input("sector-dropdown", "value"),
)
def update_sector_card(sector):
    card = get_sector_detail(sector)
    if not card:
        return html.P("No data.", style={"color": WHITE})
    verdict_color = card["verdict_color"]
    return html.Div([
        html.Div([
            html.H2(sector,
                    style={"color": WHITE, "margin": "0",
                           "fontSize": "17px", "fontWeight": "bold"}),
            html.Div([
                html.Span("Angel Verdict: " + card["angel_verdict"],
                          style={"color": AMBER, "fontSize": "12px",
                                 "fontWeight": "bold",
                                 "marginRight": "20px"}),
                html.Span("CAGR: " + str(card["cagr_pct"]) + "%",
                          style={"color": WHITE, "fontSize": "12px",
                                 "marginRight": "20px"}),
                html.Span("Startup: " + card["startup_cost"],
                          style={"color": WHITE, "fontSize": "12px"}),
            ], style={"marginTop": "5px"}),
        ], style={
            "backgroundColor": verdict_color,
            "padding": "12px 15px",
            "borderRadius": "6px 6px 0 0",
        }),
        html.Div([
            html.Div([
                html.H4("MARKET OPPORTUNITY",
                        style={"color": AMBER, "fontSize": "11px",
                               "fontWeight": "bold", "margin": "0 0 5px 0",
                               "letterSpacing": "1px"}),
                html.P(card["description"],
                       style={"color": WHITE, "fontSize": "12px",
                              "lineHeight": "1.7", "margin": "0"}),
            ], style={"marginBottom": "12px"}),
            html.Div([
                html.Div([
                    html.H4("BEST PROVINCES",
                            style={"color": GREEN, "fontSize": "11px",
                                   "fontWeight": "bold",
                                   "margin": "0 0 4px 0",
                                   "letterSpacing": "1px"}),
                    html.P(", ".join(card["best_provinces"]),
                           style={"color": WHITE, "fontSize": "12px",
                                  "margin": "0"}),
                ], style={"flex": "1", "marginRight": "20px"}),
                html.Div([
                    html.H4("EXPORT MARKETS",
                            style={"color": "#3498DB", "fontSize": "11px",
                                   "fontWeight": "bold",
                                   "margin": "0 0 4px 0",
                                   "letterSpacing": "1px"}),
                    html.P(", ".join(card["export_markets"]),
                           style={"color": WHITE, "fontSize": "12px",
                                  "margin": "0"}),
                ], style={"flex": "1"}),
            ], style={"display": "flex", "marginBottom": "12px"}),
            html.Div([
                html.Div([
                    html.H4("YOUTH JOBS CREATED",
                            style={"color": AMBER, "fontSize": "11px",
                                   "fontWeight": "bold",
                                   "margin": "0 0 4px 0",
                                   "letterSpacing": "1px"}),
                    html.P(", ".join(card["youth_jobs"]),
                           style={"color": WHITE, "fontSize": "12px",
                                  "margin": "0"}),
                ], style={"flex": "1", "marginRight": "20px"}),
                html.Div([
                    html.H4("FUNDING AVAILABLE",
                            style={"color": AMBER, "fontSize": "11px",
                                   "fontWeight": "bold",
                                   "margin": "0 0 4px 0",
                                   "letterSpacing": "1px"}),
                    html.P(card["funding"],
                           style={"color": WHITE, "fontSize": "12px",
                                  "margin": "0"}),
                ], style={"flex": "1"}),
            ], style={"display": "flex", "marginBottom": "12px"}),
            html.Div([
                html.H4("SKILLS PIPELINE",
                        style={"color": GREEN, "fontSize": "11px",
                               "fontWeight": "bold",
                               "margin": "0 0 4px 0",
                               "letterSpacing": "1px"}),
                html.P(
                    "SETA: " + str(card.get("seta", "N/A")) +
                    " | NPO: " + str(card.get("npo", "N/A")) +
                    " | Programme: " + str(card.get("programme", "N/A")) +
                    " | Duration: " + str(card.get("duration", "N/A")) +
                    " | Cost per youth: R" + str(card.get("cost_per_youth", 0)),
                    style={"color": WHITE, "fontSize": "12px", "margin": "0"}
                ),
            ]),
        ], style={
            "backgroundColor": "#152C47",
            "padding": "15px",
            "borderRadius": "0 0 6px 6px",
            "border": "1px solid " + verdict_color,
            "borderTop": "none",
        }),
    ])


app.run(debug=False, port=8050)