import streamlit as st
from utils.styling import apply_custom_css
from utils.data_loader import load_regional_stats, get_models

st.set_page_config(page_title="Experiment Lab", layout="wide")
apply_custom_css()

st.title("🧪 Build Your Cross-Regional Experiment")
st.markdown("Configure a virtual experiment. Choose which regions the model trains on, and which unseen region it deploys to.")

stats = load_regional_stats()
all_regions = list(stats.keys())

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Training Regions")
    st.write("Select the regions the model will learn from:")
    train_selections = []
    for reg in all_regions:
        if st.checkbox(reg, value=True if reg != "Bihar" else False):
            train_selections.append(reg)

with col2:
    st.subheader("2. Unseen Test Region")
    st.write("Select the region to evaluate the model on:")
    test_region = st.radio("Hold-out Region", all_regions, index=all_regions.index("Bihar"))

with col3:
    st.subheader("3. Select Model architecture")
    models = get_models()
    selected_model = st.selectbox("AI Model", models)

st.markdown("---")

if test_region in train_selections:
    st.warning("⚠️ The Test Region is also in the Training Regions. This is an **In-Domain** test, not a Cross-Regional test!")
else:
    st.success("✅ Valid Cross-Regional Experiment Configuration!")

if st.button("Run Cross-Regional Analysis", type="primary"):
    if len(train_selections) == 0:
        st.error("Please select at least one training region.")
    else:
        # Save experiment state to session
        st.session_state['exp_train'] = train_selections
        st.session_state['exp_test'] = test_region
        st.session_state['exp_model'] = selected_model
        
        st.info("Loading precomputed experiment results... Please navigate to **04 Generalization Results**.")
