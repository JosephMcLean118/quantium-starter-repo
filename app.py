from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__, title="Price Visualiser")

colors = {
    'background': '#161A1D',
    'text': '#7FDBFF'
}

df = pd.read_csv('clean_data.csv')

fig = px.line(df, x="date", y="sales", title="Price Visualisation")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(
    style={
        'backgroundColor': colors['background'],
        'fontFamily': 'Open Sans, verdana, arial, sans-serif',
        'margin': '20',
        'padding': '20',
        'height': '50vh'}, children=[
    html.H1(
        children='Pink Morsels Price Trend Over Time',
        style={
            'paddingTop': '0px',
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='pink-morsel-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
