import streamlit as st
from modules.overview import show_overview
from modules.population import show_population
from modules.monetary import show_monetary
from modules.simulator import show_simulator
from modules.engineering import show_engineering
from modules.survivor import show_survivor
from modules.groups import show_groups

# Set page layout and configurations
st.set_page_config(
    page_title="The Survivors' Nation MIS/IT Suite",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS styling for premium look
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
        color: #0f172a;
        font-family: 'Outfit', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #0f172a;
    }
    h1, h2, h3 {
        color: #0f172a;
        font-weight: 700;
    }
    .stAlert {
        border-radius: 8px;
    }
    .group-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    .group-card:hover {
        border-color: #3b82f6;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .lead-badge {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: #ffffff;
        font-weight: bold;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        font-size: 0.8rem;
        display: inline-block;
        margin-left: 0.5rem;
        vertical-align: middle;
    }
    .member-item {
        color: #334155;
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR NAVIGATION
# ─────────────────────────────────────────────────────────────────────────────
st.sidebar.title("Survivors' Nation")
st.sidebar.markdown("*MIS & IT Case Study*")

app_mode = st.sidebar.selectbox("Choose Module", [
    "1. Overview & Rules", 
    "2. Population Hierarchy", 
    "3. Monetary System (GRI)", 
    "4. Pricing Simulator", 
    "5. IT vs MIS Engineering",
    "6. Talk to a Survivor",
    "7. Group Assignments & Sectors"
])

st.sidebar.info("""
**System Status:** Running Offline  
**Power Grid Output:** 78% (Solar peak)  
**Mesh Network Sync:** 10,000 Communities connected
""")

# Route to corresponding module function
if app_mode == "1. Overview & Rules":
    show_overview()
elif app_mode == "2. Population Hierarchy":
    show_population()
elif app_mode == "3. Monetary System (GRI)":
    show_monetary()
elif app_mode == "4. Pricing Simulator":
    show_simulator()
elif app_mode == "5. IT vs MIS Engineering":
    show_engineering()
elif app_mode == "6. Talk to a Survivor":
    show_survivor()
elif app_mode == "7. Group Assignments & Sectors":
    show_groups()
