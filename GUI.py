import dash
import datetime
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px

# Load data from CSV file
data = pd.read_csv('cansat_test.csv')

# Initialize Dash app
app = dash.Dash(__name__)

def serve_layout():
    return html.H1('The time is: ' + str(datetime.datetime.now()))


# Define layout
app.layout = html.Div([
    dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000,  # in milliseconds
            n_intervals=0
        ),
])

@app.callback(
    Output('live-update-graph','figure'),
    [Input('interval-component','n_intervals')]
)
def update_graph(n):
    updated_data = pd.read_csv('cansat_test.csv')

    fig = px.line(updated_data, x='Time', y='Altitude',title='Update Graph')

    fig.update_layout(
        xaxis=dict(range=[0, 200]),  # Set x-axis range from 0 to 1000
        yaxis=dict(range=[0, 1400]),  # Set y-axis range from 0 to 1000
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
