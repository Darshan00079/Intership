import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import sys

# --- Load CSV ---
file_path = input("Enter the path to your CSV file: ")

try:
    df = pd.read_csv(file_path)
except Exception as e:
    print("Error loading file:", e)
    sys.exit()

print("\n✅ File loaded successfully!")
print(f"🔍 Columns: {list(df.columns)}\n")

# --- Column selection ---
target = input("Enter the column you want to visualize: ")

if target not in df.columns:
    print("❌ Column not found.")
    sys.exit()

# --- Data types ---
numeric_cols = df.select_dtypes(include='number').columns.tolist()
cat_cols = df.select_dtypes(include='object').columns.tolist()
datetime_cols = df.select_dtypes(include='datetime').columns.tolist()

# --- Recommend chart ---
def recommend_chart(col):
    if col in numeric_cols:
        return "Histogram"
    elif col in cat_cols:
        return "Bar"
    elif col in datetime_cols:
        return "Line"
    else:
        return "Table"

chart = recommend_chart(target)

# --- Explain ---
chart_explanations = {
    "Histogram": "Visualizes the distribution of numeric values.",
    "Bar": "Compares frequency of categorical values.",
    "Line": "Shows trends over time (datetime column).",
    "Table": "Fallback display for unsupported types."
}

print(f"\n📊 Recommended Chart: {chart}")
print(f"💡 Why: {chart_explanations[chart]}")

# --- Offer alternates ---
alt_types = {
    "Histogram": ["Histogram", "Box", "Violin"],
    "Bar": ["Bar", "Pie"],
    "Line": ["Line", "Area", "Scatter"],
    "Table": ["Table"]
}

print(f"\nAvailable alternate chart types: {alt_types[chart]}")
chart_choice = input("Choose chart type (press Enter to accept recommended): ") or chart

# --- Optional grouping ---
group_by = input("Enter a column to group by (or press Enter to skip): ")
if group_by == "":
    group_by = None

# --- Plotting ---
print("\n📈 Generating chart...")

try:
    if chart_choice == "Histogram":
        fig = px.histogram(df, x=target, color=group_by)
        fig.show()
    elif chart_choice == "Box":
        fig = px.box(df, x=group_by, y=target) if group_by else px.box(df, y=target)
        fig.show()
    elif chart_choice == "Violin":
        fig = px.violin(df, x=group_by, y=target, box=True, points="all") if group_by else px.violin(df, y=target)
        fig.show()
    elif chart_choice == "Bar":
        bar_data = df[target].value_counts().reset_index()
        bar_data.columns = [target, "Count"]
        fig = px.bar(bar_data, x=target, y="Count", color=group_by)
        fig.show()
    elif chart_choice == "Pie":
        pie_data = df[target].value_counts().reset_index()
        pie_data.columns = [target, "Count"]
        fig = px.pie(pie_data, names=target, values="Count")
        fig.show()
    elif chart_choice == "Line":
        fig = px.line(df, x=df.index, y=target, color=group_by)
        fig.show()
    elif chart_choice == "Area":
        fig = px.area(df, x=df.index, y=target, color=group_by)
        fig.show()
    elif chart_choice == "Scatter":
        y_col = input("Enter Y-axis column for scatter plot: ")
        fig = px.scatter(df, x=target, y=y_col, color=group_by)
        fig.show()
    elif chart_choice == "Table":
        print(df[[target]].head())
    else:
        print("❌ Unsupported chart type.")
except Exception as e:
    print("❌ Failed to plot chart:", e)
