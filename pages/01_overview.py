import streamlit as st
import plotly.graph_objects as go
from utils.styling import apply_custom_css

st.set_page_config(page_title="Overview", layout="wide")
apply_custom_css()

st.title("Understanding Cross-Regional Generalization")
st.markdown("### The Problem: Geographic Domain Shift")

st.markdown("""
Machine Learning models are typically evaluated using a **Random Train-Test Split**. 
This means training and testing data are randomly shuffled together. If the dataset spans multiple geographic regions, the model learns the specific visual features (soil color, terrain, typical weather) of *every* region.

However, in the real world, we want to deploy our model to **Unseen Regions**.
""")

col1, col2 = st.columns(2)

with col1:
    st.info("**Conventional Random Split (In-Domain)**")
    fig1 = go.Figure(data=[
        go.Sankey(
            node = dict(
              pad = 15,
              thickness = 20,
              line = dict(color = "black", width = 0.5),
              label = ["Region A", "Region B", "Region C", "Region D", "Mixed Training Data", "Mixed Testing Data", "Model Evaluation"],
              color = ["#3498db", "#3498db", "#3498db", "#3498db", "#9b59b6", "#e74c3c", "#2ecc71"]
            ),
            link = dict(
              source = [0, 1, 2, 3, 0, 1, 2, 3, 4, 5],
              target = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6],
              value =  [80, 80, 80, 80, 20, 20, 20, 20, 320, 80]
          ))])
    fig1.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.error("**Cross-Regional Split (Out-of-Domain Deployment)**")
    fig2 = go.Figure(data=[
        go.Sankey(
            node = dict(
              pad = 15,
              thickness = 20,
              line = dict(color = "black", width = 0.5),
              label = ["Region A", "Region B", "Region C", "Region D (Unseen)", "Training Data", "AI Model", "Generalization Test"],
              color = ["#3498db", "#3498db", "#3498db", "#e74c3c", "#9b59b6", "#f1c40f", "#2ecc71"]
            ),
            link = dict(
              source = [0, 1, 2, 4, 3, 5],
              target = [4, 4, 4, 5, 6, 6],
              value =  [100, 100, 100, 300, 100, 300]
          ))])
    fig2.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
### The Workflow
In this dashboard, we will evaluate models by explicitly isolating a region from the training process:

1. **Step 1:** Select **Training Regions** (e.g., UP, Rajasthan, Odisha).
2. **Step 2:** Hold out an **Unseen Deployment Region** (e.g., Bihar).
3. **Step 3:** Evaluate the model on the unseen region.
4. **Step 4:** Measure the **Generalization Gap** (the drop in accuracy compared to a random split).
""")
