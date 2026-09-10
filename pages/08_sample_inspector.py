import streamlit as st
import plotly.express as px
import pandas as pd
from utils.styling import apply_custom_css

st.set_page_config(page_title="Sample Inspector", layout="wide")
apply_custom_css()

st.title("🔬 Sample-Level Model Inspector")
st.markdown("Deep dive into a specific agricultural satellite chip prediction.")

if 'exp_model' not in st.session_state:
    st.warning("Please configure an experiment in **03 Experiment Lab** first.")
    st.stop()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Satellite Chip Viewer")
    st.info("Visual representation of a randomly selected 224x224 chip from the unseen region.")
    
    # Mock image representation
    st.image("https://via.placeholder.com/400x400.png?text=Sentinel-2+Agriculture+Chip", use_container_width=True)
    
    st.write("**Region:**", st.session_state['exp_test'])
    st.write("**Lat/Lon:**", "25.09, 85.31")
    st.write("**Actual Crop:**", "Rice")

with col2:
    st.subheader("Model Prediction Output")
    st.write(f"**Model:** {st.session_state['exp_model']}")
    
    is_correct = False
    predicted = "Maize"
    confidence = 0.62
    
    if st.session_state['exp_model'] in ["3D DANN", "Hybrid CNN-LSTM"]:
        is_correct = True
        predicted = "Rice"
        confidence = 0.78
        
    if is_correct:
        st.success(f"**✓ Correct Prediction**: {predicted} (Confidence: {confidence*100:.0f}%)")
    else:
        st.error(f"**✗ Misclassification**: {predicted} (Confidence: {confidence*100:.0f}%)")
        
    # Mock probability distribution
    probs = pd.DataFrame({
        "Crop": ["Rice", "Maize", "Wheat", "Mustard", "Other"],
        "Probability": [0.78, 0.12, 0.05, 0.03, 0.02] if is_correct else [0.24, 0.62, 0.08, 0.04, 0.02]
    })
    
    fig = px.bar(probs, x="Probability", y="Crop", orientation='h', color="Probability", color_continuous_scale="Viridis")
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)
    
st.markdown("---")
st.info("🧠 Explainability visualization (Grad-CAM, Attention Maps) will be available for compatible Deep Learning models in a future update.")
