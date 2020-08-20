import pandas as pd
import plotly.express as px  # (version 4.7.0)
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv("/Users/sreenivas/PycharmProjects/covid-19.csv")
print(df[:5])

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("COVID-19 analysis for some of the states in USA using Dash framework ", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_state",
                 options=[
                     {"label": "Alabama", "value": 'Alabama'},
                     {"label": "Alaska", "value": 'South Carolina'},
                     {"label": "Arizona", "value": 'Arizona'},
                     {"label": "Arkansas", "value": 'Arkansas'},
                     {"label": "California", "value": 'California'},
                     {"label": "Idaho", "value": 'Idaho'},
                     {"label": "Illinois", "value": 'Illinois'},
                     {"label": "Indiana", "value": 'Indiana'},
                     {"label": "Louisiana", "value": 'Louisiana'},
                     {"label": "Michigan", "value": 'Michigan'},
                     {"label": "Minnesota", "value": 'Minnesota'},
                     {"label": "Missouri", "value": 'Missouri'},
                     {"label": "Texas", "value": 'Texas'},
                     {"label": "Virginia", "value": 'Virginia'}
                 ],
                 multi=False,
                 value="Arkansas",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='my_covid_map', figure={})

])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_covid_map', component_property='figure')],
    [Input(component_id='slct_state', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))
    container = "The State chosen by user was: {}".format(option_slctd)
    dff = df.copy()
    dff = dff[dff["Province_State"] == option_slctd]
    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
