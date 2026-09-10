import streamlit as st
from utils.styling import apply_custom_css

st.set_page_config(
    page_title="Cross-Regional Crop AI Lab",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

st.title("🌾 Cross-Regional Crop AI Lab")
st.subheader("Understanding and Evaluating Geographic Generalization in AI-Based Crop Classification")

st.markdown("""
---
### The Central Research Question:
**"Can an AI model trained on crop data from certain geographic regions accurately classify crops in a completely unseen region?"**

Welcome to the interactive research demonstrator. This dashboard is designed to help researchers and non-technical stakeholders visually understand:
1. What cross-regional geographic generalization is.
2. Why models fail when deployed to new regions (Domain Shift).
3. How advanced AI techniques (DANN, CNN-LSTM) solve these failures.

### Navigation
Please use the sidebar to navigate through the research workflow:
*   **01 Overview**: Understand the structural problem of domain shift.
*   **02 Regional Explorer**: Explore the dataset geographically.
*   **03 Experiment Lab**: Build and test custom cross-regional training runs.
*   **04 Generalization Results**: Observe the performance degradation gaps.
*   **05 Model Comparison**: Compare ML vs DL approaches.
*   **06 Error Analysis**: Discover which crops cause the most confusion.
*   **07 Domain Shift**: Analyze the underlying feature shifts.
*   **08 Sample Inspector**: Look at individual model predictions.
*   **09 Roadmap**: The future of this AI research.
""")

st.info("👈 Please select a module from the sidebar to begin.")
