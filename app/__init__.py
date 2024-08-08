from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = Flask(__name__)
app.secret_key = 'your_secret_key'

dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

dash_app.layout = html.Div(children=[
    html.H1(children='Real-time Stock Market Dashboard'),

    dcc.Input(id='stock-input', value='AAPL', type='text'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),

    dcc.Graph(id='stock-graph')
])

from app import routes
