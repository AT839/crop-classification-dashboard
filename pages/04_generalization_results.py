import streamlit as st
import plotly.graph_objects as go
from utils.styling import apply_custom_css
from utils.data_loader import load_experiment_results

st.set_page_config(page_title="Generalization Results", layout="wide")
apply_custom_css()

st.title("📊 Generalization Results")

if 'exp_model' not in st.session_state:
    st.warning("Please configure an experiment in **03 Experiment Lab** first.")
    st.stop()

train_regs = st.session_state['exp_train']
test_reg = st.session_state['exp_test']
model = st.session_state['exp_model']

st.markdown(f"### Results for **{model}**")
st.write(f"**Trained on:** {', '.join(train_regs)}")
st.write(f"**Evaluated on:** {test_reg}")

# Load results
results = load_experiment_results(train_regs, test_reg, model)

st.markdown("---")
st.subheader("Performance Drop-off (The Generalization Gap)")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"<div class='metric-card'><h3>Conventional Random Split Accuracy</h3><h1>{results['source_acc']*100:.1f}%</h1></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-card'><h3>Cross-Regional Accuracy (Unseen)</h3><h1>{results['target_acc']*100:.1f}%</h1></div>", unsafe_allow_html=True)
with col3:
    gap_class = "gap-positive" if results['generalization_gap'] > 0 else "gap-negative"
    st.markdown(f"<div class='metric-card'><h3>Generalization Gap</h3><h1 class='{gap_class}'>{results['generalization_gap']*100:.1f} pts</h1></div>", unsafe_allow_html=True)

st.markdown("---")
st.subheader("Visualizing the Gap")

fig = go.Figure(go.Waterfall(
    name = "20", orientation = "h",
    measure = ["absolute", "relative", "total"],
    y = ["Random Split", "Performance Drop", "Unseen Region"],
    x = [results['source_acc']*100, -results['generalization_gap']*100, results['target_acc']*100],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
    decreasing = {"marker":{"color":"#d9534f"}},
    totals = {"marker":{"color":"#3498db"}},
    textposition = "outside",
    text = [f"{results['source_acc']*100:.1f}%", f"-{results['generalization_gap']*100:.1f}%", f"{results['target_acc']*100:.1f}%"]
))

fig.update_layout(title="Accuracy Degradation", showlegend=False, height=400)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Detailed Evaluation Metrics (Unseen Region)")
m1, m2, m3 = st.columns(3)
m1.metric("Precision", f"{results['precision']:.3f}")
m2.metric("Recall", f"{results['recall']:.3f}")
m3.metric("Weighted F1-Score", f"{results['f1']:.3f}")
