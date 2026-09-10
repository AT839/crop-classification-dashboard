import streamlit as st
import plotly.express as px
from utils.styling import apply_custom_css
from utils.data_loader import load_experiment_results, generate_mock_confusion_matrix

st.set_page_config(page_title="Which Crops Fail?", layout="wide")
apply_custom_css()

st.title("❌ Which Crops Fail?")
st.markdown("Analyze class-level errors to answer: **Which crop classes are most difficult to generalize geographically?**")

if 'exp_model' not in st.session_state:
    st.warning("Please configure an experiment in **03 Experiment Lab** first.")
    st.stop()

train_regs = st.session_state['exp_train']
test_reg = st.session_state['exp_test']
model = st.session_state['exp_model']

results = load_experiment_results(train_regs, test_reg, model)
df_per_class = results['per_class']
cm = generate_mock_confusion_matrix()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Per-Class F1-Score (Unseen Region)")
    fig_f1 = px.bar(df_per_class, x='Crop', y='F1_Score', color='F1_Score', color_continuous_scale="RdYlGn")
    fig_f1.update_yaxes(range=[0, 1])
    st.plotly_chart(fig_f1, use_container_width=True)

with col2:
    st.subheader("Confusion Matrix")
    fig_cm = px.imshow(cm, text_auto=True, color_continuous_scale="Blues", labels=dict(x="Predicted Crop", y="Actual Crop", color="Count"))
    st.plotly_chart(fig_cm, use_container_width=True)

st.markdown("---")
st.subheader("Most Confused Crop Pairs")
st.error("**Actual: Rice ➡️ Predicted: Maize**")
st.write("The model frequently misclassifies Rice as Maize in the unseen region. This suggests their phenological signatures or spectral reflectances overlap significantly in the deployment geography.")
