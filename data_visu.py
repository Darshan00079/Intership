import pandas as pd
import plotly.express as px

def load_dataset(file_path):
    try:
        a = pd.read_csv(file_path)
        return a
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def generate_visualizations(a):
    if a is None:
        print("No dataset loaded.")
        return


    graph_fig = px.scatter(a, x=a.columns[0], y=a.columns[1], title="Graph Plot")
    graph_fig.show()


    bar_fig = px.bar(a, x=a.columns[0], y=a.columns[1], title="Bar Plot")
    bar_fig.show()


    line_fig = px.line(a, x=a.columns[0], y=a.columns[1], title="Line Plot")
    line_fig.show()


    hist_fig = px.histogram(a, x=a.columns[0], title="Histogram")
    hist_fig.show()

if __name__ == "__main__":
    file_path = input("Enter the path to the dataset (CSV file): ")
    a = load_dataset(file_path)
    generate_visualizations(a)


