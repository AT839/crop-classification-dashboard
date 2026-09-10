import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from utils.styling import apply_custom_css
from utils.data_loader import load_feature_distribution

st.set_page_config(page_title="Domain Shift Explorer", layout="wide")
apply_custom_css()

st.title("🕵️ Why Did The Model Fail?")
st.markdown("### Domain Shift Explorer")

st.info("A difference in feature distributions between training and deployment regions may indicate geographic domain shift and may contribute to reduced model performance.")

if 'exp_train' not in st.session_state:
    st.warning("Please configure an experiment in **03 Experiment Lab** first.")
    st.stop()

train_regs = st.session_state['exp_train']
test_reg = st.session_state['exp_test']

st.markdown(f"**Comparing:** {', '.join(train_regs)} 🆚 **{test_reg}**")

feature = st.selectbox("Select Feature to Compare", ["NDVI", "NDWI", "NIR Band", "SWIR Band"])
crop = st.selectbox("Select Crop Class", ["Rice", "Wheat", "Mustard", "Maize"])

# Load mock distributions
train_df = load_feature_distribution(train_regs[0], feature)
train_df['Region Type'] = "Training"
test_df = load_feature_distribution(test_reg, feature)
test_df['Region Type'] = "Unseen Test"

combined_df = pd.concat([train_df, test_df])

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{feature} Histogram")
    fig1 = px.histogram(combined_df, x=feature, color="Region Type", barmode="overlay", nbins=50, opacity=0.7)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader(f"{feature} Box Plot")
    fig2 = px.box(combined_df, x="Region Type", y=feature, color="Region Type")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.markdown("### Observation")
st.write(f"The distribution of {feature} for {crop} in the unseen region ({test_reg}) is visibly shifted compared to the training regions. Baseline models rely strictly on the training distribution, causing them to fail when presented with this shifted data. Domain Adaptation models (like DANN) attempt to align these distributions internally.")
