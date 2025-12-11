
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

# Load data
data_path = 'data/border_killing_locations.json'
with open(data_path, 'r') as f:
    data = json.load(f)

# Ensure docs directory exists
if not os.path.exists('docs'):
    os.makedirs('docs')

# --- 1. Enhanced Map of Incidents ---
incidents = data['incidents']
df_incidents = pd.DataFrame(incidents)

# Extract year for color coding
df_incidents['Year'] = pd.to_datetime(df_incidents['date']).dt.year.astype(str)

fig_map = px.scatter_mapbox(
    df_incidents,
    lat="lat",
    lon="lon",
    color="Year",
    hover_name="name",
    hover_data={
        "date": True, 
        "location": True, 
        "description": True, 
        "lat": False, 
        "lon": False,
        "Year": False
    },
    color_discrete_sequence=px.colors.qualitative.Bold, # Vivid colors
    zoom=6,
    height=600,
    title="<b>Recent Border Killing Incidents (2022-2024)</b>"
)

fig_map.update_traces(marker=dict(size=14, opacity=0.8)) # Larger, semi-transparent markers

fig_map.update_layout(
    mapbox_style="carto-positron", # Cleaner, high-contrast map style
    margin={"r":0,"t":50,"l":0,"b":0},
    title_x=0.5,
    title_font_size=20,
    legend_title_text='Year',
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        bgcolor="rgba(255, 255, 255, 0.9)"
    )
)

map_output_path = 'docs/border_killing_map.html'
fig_map.write_html(map_output_path)
print(f"Enhanced map saved to {map_output_path}")

# --- 2. Enhanced Trend Chart ---
stats = data['yearly_stats']
df_stats = pd.DataFrame(stats)

# Highlight 2024
colors = ['#EF553B' if x == 2024 else '#636EFA' for x in df_stats['year']]

fig_trend = go.Figure()

fig_trend.add_trace(go.Bar(
    x=df_stats['year'],
    y=df_stats['killed'],
    text=df_stats['killed'],
    textposition='auto',
    marker_color=df_stats['killed'], # Gradient color based on value
    marker=dict(colorscale='Reds')   # Red gradient
))

fig_trend.update_layout(
    title="<b>Border Killing Trends (2013-2024)</b>",
    title_x=0.5,
    xaxis_title="Year",
    yaxis_title="Number of Deaths",
    xaxis=dict(type='category'),
    template="plotly_white",
    margin={"r":20,"t":60,"l":20,"b":20},
    hovermode="x unified"
)

trend_output_path = 'docs/border_killing_trend.html'
fig_trend.write_html(trend_output_path)
print(f"Enhanced trend chart saved to {trend_output_path}")
