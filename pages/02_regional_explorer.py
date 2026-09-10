import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from utils.styling import apply_custom_css
from utils.data_loader import load_regional_stats, get_real_crop_distribution

st.set_page_config(page_title="Regional Explorer", layout="wide")
apply_custom_css()

st.title("🌍 Regional Data Explorer")
st.markdown("Understand the geographic distribution of our agricultural dataset.")

stats = load_regional_stats()
regions = list(stats.keys())

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Geographic Distribution")
    # Interactive Map
    m = folium.Map(location=[24.0, 80.0], zoom_start=5)
    for reg, data in stats.items():
        folium.CircleMarker(
            location=[data["lat"], data["lon"]],
            radius=data["samples"] / 500,
            popup=f"{reg}: {data['samples']} samples",
            color="#3186cc",
            fill=True,
            fill_color="#3186cc"
        ).add_to(m)
    st_folium(m, height=400, width=700)

with col2:
    st.subheader("Region Statistics")
    selected_region = st.selectbox("Select a Region to inspect:", regions)
    
    r_stats = stats[selected_region]
    
    c1, c2 = st.columns(2)
    c1.markdown(f"<div class='metric-card'><h3>Total Samples</h3><h1>{r_stats['samples']}</h1></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric-card'><h3>Crop Classes</h3><h1>{r_stats['classes']}</h1></div>", unsafe_allow_html=True)

st.markdown("---")
st.subheader(f"Crop Distribution in {selected_region}")

# Real crop distribution chart
dist = get_real_crop_distribution(selected_region, r_stats['samples'])

fig = px.bar(dist, x="Crop", y="Count", color="Crop", title=f"Sample Count by Crop ({selected_region})")
st.plotly_chart(fig, use_container_width=True)
