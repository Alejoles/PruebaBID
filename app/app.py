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
                        #config={"displayModeBar": False},
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
def update_chart(countries, request_type):
    """
        Callback function to update the graph in the front.
        Returns the chart that is going to be showed in the front.
        Inputs:
            - countries: Is an input showed in the front that brings
                         the countries to us.
            - request_type: Another input that selects which of the
                            macrofiscal data will be used.
        Output:
            - A graph showing the requested data.
    """
    data = MacroFiscalData()
    if request_type == "Macro - Gross Domestic Product": # Each if represents which data set will be used
        gdp = data.gdp
        graphs = []
        for i in countries:
            graphs.append({
                    "x": list(gdp[i].keys()),
                    "y": list(gdp[i].values()),
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                    "name": str(i)
                })
        gdp_chart_figure = {
            "data": graphs,
            "layout": {
                "title": {
                    "text": "Gross Domestic Product Per Capita (US$)",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": str(data.gdp["Currency"]), "fixedrange": True},
            },
        }
    if request_type == "Macro - Inflation":
        if data.inflation == {}:
            data.get_inflation()
        macrofiscal = data.inflation
        graphs = []
        for i in countries:
            graphs.append({
                    "x": list(macrofiscal[i].keys()),
                    "y": list(macrofiscal[i].values()),
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                    "name": str(i)
                })
        gdp_chart_figure = {
            "data": graphs,
            "layout": {
                "title": {
                    "text": "Inflation (Annual %)",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": str(data.inflation["Currency"]), "fixedrange": True},
            },
        }
    if request_type == "Macro - Unemployment":
        if data.unemploy == {}:
            data.get_uem()
        macrofiscal = data.unemploy
        graphs = []
        for i in countries:
            graphs.append({
                    "x": list(macrofiscal[i].keys()),
                    "y": list(macrofiscal[i].values()),
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                    "name": str(i)
                })
        gdp_chart_figure = {
            "data": graphs,
            "layout": {
                "title": {
                    "text": "Unemployment (% of total labor force)",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": str(data.unemploy["Currency"]), "fixedrange": True},
            },
        }
    if request_type == "Fiscal - Central Gov Debt":
        if data.debt == {}:
            data.get_public_debt()
        macrofiscal = data.debt
        graphs = []
        for i in countries:
            graphs.append(
                    go.Bar(x=list(macrofiscal[i].keys()), y=list(macrofiscal[i].values()), name=str(i))
                )
        gdp_chart_figure = {
            "data": graphs,
            "layout": {
                "title": {
                    "text": "Central Government debt (% of GDP)",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": str(data.debt["Currency"]), "fixedrange": True},
            },
        }
    if request_type == "Fiscal - Gross National Income":
        if data.incomes == {}:
            data.get_incomes()
        macrofiscal = data.incomes
        graphs = []
        for i in countries:
            graphs.append(
                go.Bar(x=list(macrofiscal[i].keys()), y=list(macrofiscal[i].values()), name=str(i))
            )
        gdp_chart_figure = {
            "data": graphs,
            "layout": {
                "title": {
                    "text": "Gross National Income (US$)",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": str(data.incomes["Currency"]), "fixedrange": True},
                "legend" :{"asd":"asd"}
            },
        }
    if request_type == "Fiscal - Tax Expenses":
        if data.expenses == {}:
            data.get_tax_expenses()
        macrofiscal = data.expenses
        graphs = []
        for i in countries:
            graphs.append(
                go.Bar(x=list(macrofiscal[i].keys()), y=list(macrofiscal[i].values()), name=str(i))
            )
        gdp_chart_figure = {
            "data": graphs,
            "layout": {
                "title": {
                    "text": "Expense (% of GDP)",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": str(data.expenses["Currency"]), "fixedrange": True},
            },
        }

    return gdp_chart_figure


if __name__ == '__main__':
    # Running the server
    app.run_server(host='0.0.0.0', port=8050, debug=True)

