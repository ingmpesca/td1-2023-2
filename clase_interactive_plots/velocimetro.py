import dash
import dash_daq as daq
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import time

app = dash.Dash(__name__)

app.layout = html.Div([
    daq.Gauge(
        id='gauge',
        label="Velocímetro",
        value=0,
        max=50,
        min=0,
        color="#FF5E5E"
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # Actualiza cada 1 segundo
        n_intervals=0
    )
])

increment = 10
current_value = 0
incrementing = True

@app.callback(
    Output('gauge', 'value'),
    Input('interval-component', 'n_intervals')
)
def update_gauge(n):
    global current_value, incrementing

    if incrementing:
        current_value += increment
        if current_value >= 50:
            incrementing = False
    else:
        current_value -= increment
        if current_value <= 0:
            incrementing = True

    return current_value

if __name__ == '__main__':
    app.run_server(debug=True)

