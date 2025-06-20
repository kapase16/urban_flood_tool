# app.py
import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("🌧️ Urban Flood Risk Mapping Tool (MVP)")

# Rainfall Input
rainfall = st.number_input("Enter Rainfall (mm)", min_value=0.0, step=1.0)

# Upload GeoJSON and Curve Number table
geojson_file = st.file_uploader("Upload Land Use GeoJSON", type=["geojson"])
cn_file = st.file_uploader("Upload Curve Number Table (CSV)", type=["csv"])

if geojson_file and cn_file:
    gdf = gpd.read_file(geojson_file)
    cn_df = pd.read_csv(cn_file)

    # Merge on land_use
    merged = gdf.merge(cn_df, on='land_use')

    # SCS Runoff calculation
    def scs_runoff(P, CN):
        S = (25400 / CN) - 254
        if P <= 0.2 * S:
            return 0
        return ((P - 0.2*S)**2) / (P + 0.8*S)

    merged["runoff_mm"] = merged["CN"].apply(lambda cn: scs_runoff(rainfall, cn))

    # Map
    center = [merged.geometry.centroid.y.mean(), merged.geometry.centroid.x.mean()]
    m = folium.Map(location=center, zoom_start=13)

    folium.GeoJson(
        merged,
        style_function=lambda x: {
            'fillColor': '#ff4d4d' if x['properties']['runoff_mm'] > 50 else '#a3f7bf',
            'color': 'black',
            'weight': 0.3,
            'fillOpacity': 0.7,
        },
        tooltip=folium.GeoJsonTooltip(fields=['land_use', 'CN', 'runoff_mm'])
    ).add_to(m)

    st_folium(m, width=800, height=500)
