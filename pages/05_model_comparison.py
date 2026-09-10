import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.styling import apply_custom_css
from utils.data_loader import get_models, load_experiment_results

st.set_page_config(page_title="Model Comparison", layout="wide")
apply_custom_css()

st.title("📈 Model Comparison")
st.markdown("Compare baseline Machine Learning models against advanced Deep Learning and Domain Generalization models.")

if 'exp_train' not in st.session_state:
    st.warning("Please configure an experiment in **03 Experiment Lab** first.")
    st.stop()

train_regs = st.session_state['exp_train']
test_reg = st.session_state['exp_test']

st.write(f"**Experiment Configuration:** Train on `{', '.join(train_regs)}`, Test on `{test_reg}`")

models = get_models()
results_list = []

for m in models:
    res = load_experiment_results(train_regs, test_reg, m)
    results_list.append({
        "Model": m,
        "Random Split Acc": round(res['source_acc']*100, 1),
        "Unseen Region Acc": round(res['target_acc']*100, 1),
        "Generalization Gap": round(res['generalization_gap']*100, 1)
    })

df_res = pd.DataFrame(results_list)

st.markdown("### Performance Comparison Table")
st.dataframe(df_res, use_container_width=True)

st.markdown("---")
st.markdown("### Generalization Gap Comparison")

fig = go.Figure()
fig.add_trace(go.Bar(
    x=df_res['Model'],
    y=df_res['Random Split Acc'],
    name='Random Split (In-Domain)',
    marker_color='#3498db'
))
fig.add_trace(go.Bar(
    x=df_res['Model'],
    y=df_res['Unseen Region Acc'],
    name='Unseen Region (Cross-Domain)',
    marker_color='#e74c3c'
))

fig.update_layout(barmode='group', title="In-Domain vs Cross-Domain Accuracy", yaxis_title="Accuracy (%)")
st.plotly_chart(fig, use_container_width=True)

st.info("**Research Insight:** Notice how advanced models like **3D DANN** (Domain Adversarial Neural Network) and **Hybrid CNN-LSTM** reduce the generalization gap compared to Baseline models!")
