# import packages 
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Load Data - Keep only infant mortality
data = pd.read_csv("fusion_CME_UNICEF_1.0_all.csv", low_memory=False)
data = data[(data.Indicator == 'Infant mortality rate')]

# Options lists
countries = data.Country.unique()

# Dash app
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([

    html.Label('Country'),
    #div for dropdown
    dcc.Dropdown(
        id='country',
        options=[{'label': country, 'value': country} for country in countries],
        value=countries[0]
    ),

    html.Label('Infant Mortality Rates by Country'),
    #div for chart question 1
    html.Div(
        dcc.Graph(id='graphic')
    )
])

#call backs
@app.callback(dash.dependencies.Output('graphic', 'figure'),
              [dash.dependencies.Input('country', 'value')]
              )

#update graphic
def update_fig(input_value):

    #filter out dataset by selected values
    data_filtered = data[data['Country'] == input_value]



    
    fig = px.line(data_filtered,x='TIME_PERIOD',y='OBS_VALUE',color='Sex')


    return fig


if __name__ == '__main__':
    app.run_server(debug=True)