import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .metric-card h3 {
        margin: 0;
        font-size: 1.2rem;
        color: #6c757d;
    }
    .metric-card h1 {
        margin: 10px 0 0 0;
        font-size: 2.5rem;
        color: #212529;
    }
    .gap-positive {
        color: #d9534f;
    }
    .gap-negative {
        color: #5cb85c;
    }
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
