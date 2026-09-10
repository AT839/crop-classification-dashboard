import streamlit as st
import plotly.graph_objects as go
from utils.styling import apply_custom_css

st.set_page_config(page_title="Research Roadmap", layout="wide")
apply_custom_css()

st.title("🚀 Research Evolution & Roadmap")
st.markdown("Visualizing the trajectory of this AI research project.")

stages = [
    {"Phase": "PHASE 1", "Title": "Baseline Machine Learning", "Desc": "Random Forest, XGBoost"},
    {"Phase": "PHASE 2", "Title": "Deep Learning", "Desc": "3D CNN, Spatial ResNet"},
    {"Phase": "PHASE 3", "Title": "Cross-Regional Generalization", "Desc": "Domain Adversarial Networks (DANN), Hybrid CNN-LSTM"},
    {"Phase": "PHASE 4", "Title": "Advanced Research", "Desc": "Vision Transformers, Self-Supervised Learning, Explainable AI"}
]

for stage in stages:
    st.markdown(f"### {stage['Phase']}: {stage['Title']}")
    st.markdown(f"*{stage['Desc']}*")
    st.markdown("---")
    
st.success("Currently executing Phase 3: Solving Geographic Generalization via Advanced Architectures.")
