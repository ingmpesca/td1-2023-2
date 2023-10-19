import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random
import time

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='area-graph'),
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0),
])

@app.callback(
    Output('area-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n_intervals):
    x = list(range(n_intervals))
    y = [random.random() for _ in x]

    data = [go.Scatter(x=x, y=y, fill='tozeroy', fillcolor='rgba(0,100,80,0.2)', mode='none')]
    layout = go.Layout(title='Gráfico de Área Animado', xaxis=dict(range=[max(0, n_intervals - 10), n_intervals]),
                       yaxis=dict(range=[0, 1]))

    return {'data': data, 'layout': layout}

if __name__ == '__main__':
    app.run_server(debug=True)
