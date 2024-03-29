import dash
import datetime
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import webbrowser
import subprocess

print("YO")

# Execute the command and capture its output
result = subprocess.run("lsof -i :8050 | awk 'NR>1 {print $2}' | head -n 1", shell=True, capture_output=True, text=True)

# Check if the output is not empty
if result.stdout:
    # Print the output, stripping any trailing newlines
    print(result.stdout.strip())
    PIDstring = result.stdout.strip()
    subprocess.run(f"kill {PIDstring}", shell=True, capture_output=True, text=True)
else:
    print("No process found on port 8050")


# Execute the command and capture its output
result = subprocess.run("lsof -i :8050 | awk 'NR>1 {print $2}' | head -n 1", shell=True, capture_output=True, text=True)

# Check if the output is not empty
if result.stdout:
    # Print the output, stripping any trailing newlines
    print(result.stdout.strip())
    PIDstring = result.stdout.strip()
    subprocess.run(f"kill {PIDstring}", shell=True, capture_output=True, text=True)
else:
    print("No process found on port 8050")

#rowNum = 1
# Load data from CSV file
data = pd.read_csv('cansat_test.csv')

# Initialize Dash app
app = dash.Dash(__name__)

def serve_layout():
    return html.H1('The time is: ' + str(datetime.datetime.now()))



@app.callback(
    Output('live-update-graph','figure'),
    [Input('interval-component','n_intervals')]
)
def update_graph(n):
    #global rowNum
    
    #Reading the CSV data into "updated_data"
    updated_data = pd.read_csv('cansat_test.csv')

    # if rowNum >= len(updated_data) - 1:
    #     rowNum = 0  # Reset rowNum to 0 or another appropriate value based on your needs
    # else:
    #     rowNum += 1
        
    #Updating the line
    fig = px.line(updated_data, x='Packet Count', y='Altitude',title='Update Graph')

    #Updating the max and min
    # xMax = updated_data.loc[rowNum,"Mission Time"]
    # yMax = updated_data.loc[rowNum,"Altitude"]

    fig.update_layout(
        xaxis=dict(range=[0, 200]),  # Set x-axis range from 0 to 1000
        yaxis=dict(range=[0, 1000]),  # Set y-axis range from 0 to 1000
    )

    return fig


# Define layout
app.layout = html.Div([
    dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000,  # in milliseconds
            n_intervals=0
        ),
])

url = "http://127.0.0.1:8050/"
webbrowser.open(url)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
