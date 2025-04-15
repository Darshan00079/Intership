import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import sys

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def create_charts(df):
    charts = {}

    x_col = df.columns[0]
    y_col = df.columns[1]

    # Scatter Plot
    charts["Scatter Plot"] = px.scatter(df, x=x_col, y=y_col, title="Scatter Plot")

    # Bar Plot
    charts["Bar Plot"] = px.bar(df, x=x_col, y=y_col, title="Bar Plot")

    # Line Plot
    charts["Line Plot"] = px.line(df, x=x_col, y=y_col, title="Line Plot")

    # Histogram
    charts["Histogram"] = px.histogram(df, x=x_col, title="Histogram")

    # Animated Bar Plot (if valid frame column exists)
    possible_frames = [col for col in df.columns if df[col].nunique() > 1 and df[col].nunique() < 100]
    if len(df.columns) >= 3 and len(possible_frames) > 0:
        frame_col = possible_frames[0]
        try:
            charts["Animated Bar Plot"] = px.bar(
                df,
                x=x_col,
                y=y_col,
                color=x_col,
                animation_frame=frame_col,
                title=f"Animated Bar Plot (by {frame_col})"
            )
        except Exception as e:
            print(f"Animated plot failed: {e}")

    return charts

def launch_dashboard(charts):
    app = Dash(__name__)
    app.title = "Data Visualization Dashboard"

    app.layout = html.Div([
        html.H1("📊 Data Visualization Dashboard", style={'textAlign': 'center'}),
        html.Div([
            html.Div([
                html.H3(chart_name),
                dcc.Graph(figure=fig)
            ], style={'padding': '20px', 'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'})
            for chart_name, fig in charts.items()
        ])
    ])

    app.run_server(debug=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <path_to_csv>")
    else:
        file_path = sys.argv[1]
        df = load_dataset(file_path)
        if df is not None:
            charts = create_charts(df)
            launch_dashboard(charts)
