import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div(children=[

    html.H2(children='Hello Dash!'),

    dcc.Graph(
        figure=go.Figure(
            data=[go.Bar(
                x=['2017','2018','2019'],
                y=[150,160,156],
                name='lokalnie'
            ),
            go.Bar(
                x=['2017','2018','2019'],
                y=[160,190,254],
                name='online'
            )]
        ))
])

if __name__ == '__main__':
    app.run(debug=True)