from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__, title="Price Visualiser")

colors = {
    'background': '#161A1D',
    'text': '#7FDBFF'
}


#load in data
df = pd.read_csv('clean_data.csv')
df = df.sort_values(by='date')

#create line chart
fig = px.line(df, x="date", y="sales", title="Price Visualisation")
graph = dcc.Graph(
            id='pink-morsel-graph',
            figure=fig
    )

#create header
header = html.H1(
    "Pink Morsels Price Trend Over Time",
    id = "header",
    style={
            'paddingTop': '0px',
            'textAlign': 'center',
            'color': colors['text']
        }
)

#create app layout (header, graph)
app.layout = html.Div(
    [
        header,
        graph
    ]
)

if __name__ == '__main__':
    app.run(debug=True)


