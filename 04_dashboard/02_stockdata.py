import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go


def fetch_financial_data(ticker='AAPL'):
    """
    This function fetch stock market quotations.
    """
    import yfinance as yf
    df = yf.download(ticker, start="2023-01-01")
    return df


df = fetch_financial_data()
df.columns = [col[0] for col in df.columns]
df.info()
df.index = pd.date_range(start='2023-01-01', periods = 818, name = 'Date')
df = df.reset_index()
df = df[df.Date > '2019-01-01']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H4('Notowania spółki Amazon'),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x=df.Date,
                    y=df.Close,
                    mode='lines',
                    fill='tozeroy',
                    name='Amazon'
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=500,
                title_text='Wykres ceny',
                showlegend=True
            )
        )
    ),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=df.Date,
                    y=df.Volume,
                    name='Wolumen'
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=300,
                title_text='Wykres wolumenu',
                showlegend=True
            )
        )
    )
])

if __name__ == '__main__':
    app.run(debug=True)