#Creating Dashboard using Plotly and Dash

#Import Libraries
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

data = pd.read_csv('avocado-prices.csv')

#We create a Dash object named 'app'
app = Dash()

#Setting up the Layout
geography_dropdown = dcc.Dropdown(options=data['geography'].unique(), 
                                  value='New York')

app.layout = html.Div(children=[
    html.H1(children='Average Price Dashboard'),
    geography_dropdown,
    dcc.Graph(id='price_graph')
])

#decorator, which starts with @app.callback
#function itself, which begins with def

#Callback function to make the plotly figure dependent on the dropdown
@app.callback(
    Output(component_id='price_graph', component_property= 'figure'),
    Input(component_id=geography_dropdown, component_property='value')
)

def update_graph(selected_place):
  selected_avocado = data[data['geography']== selected_place]
  line_figure = px.line(
      selected_avocado,
      x = 'date', y = 'average_pice',
      color = 'type',
      title = f'Prices of Avocado in {selected_place}')
      
  return line_figure

#Running the App in Local Server
if __name__== '__main__':
    app.run_server(port = 8080, debug = True)