from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

colors = {
    'background': '#111111',
    'text': '#111111'
}


#load in data
df = pd.read_csv('clean_data.csv', skipinitialspace=True)
df = df.sort_values(by='date')
print(df.columns)
#create line chart
fig = px.line(df, x="date", y="sales", title="Price Visualisation")
graph = dcc.Graph(
            id='pink-morsel-graph',
            figure=fig,
            style={
                "height":"70vh"
            }
    )

#create header
header = html.H1(
    "Pink Morsels Price Trend Over Time",
    id = "header",
)

filters = dcc.RadioItems(
    ['North', 'South', 'East', 'West', 'All'],
    id = 'radio-input',
    value='All',
    inline=True
)

#create app layout (header, graph)
app.layout = html.Div(
    [
        header,
        graph,
        filters
    ]
)

@callback(
        Output(component_id='pink-morsel-graph', component_property='figure'),
        Input(component_id='radio-input', component_property='value')
)

def update_figure(selected_region):
    if selected_region == 'All':
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region.lower()]

    fig = px.line(filtered_df, x="date", y="sales", title="Price Visualisation")
    fig.update_layout(transition_duration=1000)
    return fig

if __name__ == '__main__':
    app.run(debug=True)

