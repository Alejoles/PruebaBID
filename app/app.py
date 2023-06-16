from dash import Dash, Input, Output, dcc, html
import plotly.graph_objs as go
from commands import MacroFiscalData
from constants import COUNTRIES, FLAGS

# Crear la aplicación Dash
external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Macro-Economic Dashboard"


# Diseño de la interfaz con estilos CSS
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src="assets/money-growth.png", className="header-emoji"),
                html.H1(
                    children="Macro-Fiscal Dashboard", className="header-title"
                ),
                html.P(
                    children=(
                        "Analyze the behavior of macrofiscal changes in Latam"
                        " between 2002 and 2021"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Request", className="menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                "Macro - Gross Domestic Product",
                                "Macro - Inflation",
                                "Macro - Unemployment",
                                "Fiscal - Central Gov Debt",
                                "Fiscal - Gross National Income",
                                "Fiscal - Tax Expenses"
                            ],
                            value="Macro - Gross Domestic Product",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Checklist(
                            [
                                {
                                    "label": [
                                        html.Img(src=f"assets/1x1/{FLAGS[country]}.svg", className="flags"),
                                        html.Span(country, style={"font-size": 20, "padding-left": 10}),
                                    ],
                                    "value": COUNTRIES[country],
                                }
                                for country in COUNTRIES
                            ],
                            id="country-filter",
                            value=["CO"],
                            className="checklist"
                        )
                    ],
                    className="side-menu"
                ),
                html.Div(
                    children=dcc.Graph(
                        id="gdp-chart",
                        config={"displayModeBar": False},
                        style={'width': '80vw'}
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

@app.callback(
    Output("gdp-chart", "figure"),
    Input("country-filter", "value"),
    Input("type-filter", "value"),
)
def update_chart(country, request_type):
    print(country, request_type)
    MacroFiscalData
    gdp_chart_figure = ""
    return gdp_chart_figure


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)

