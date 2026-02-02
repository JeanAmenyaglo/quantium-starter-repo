import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load cleaned data
df = pd.read_csv("pink_morsel_sales.csv")

# Ensure date is datetime
df['date'] = pd.to_datetime(df['date'])

# Aggregate total sales per day
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Create line chart
fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Daily Sales of Pink Morsels',
    labels={'date': 'Date', 'sales': 'Total Sales ($)'}
)

# Add vertical line for price increase date
fig.add_vline(
    x=pd.Timestamp("2021-01-15"),
    line_width=2,
    line_dash="dash",
    line_color="red"
)

# Build Dash app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(
        children="Pink Morsel Sales Before and After Price Increase",
        style={'textAlign': 'center'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)