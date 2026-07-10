import streamlit as st
import pandas as pd

def show_population():
    st.title("📊 Hierarchical Population Structure")
    
    st.write("""
    ### System Design & Governance Scale
    To manage logistics, communications, and database synchronization efficiently without a global network, the population of 5 million is structured into nested, self-contained units. This hierarchy prevents network traffic bottlenecks and establishes localized lines of authority.
    """)
    
    # Interactive Table
    hierarchy_data = {
        "Level": ["Family", "Circle", "Community", "Region", "Settlement", "Nation"],
        "Structure Scale": ["5–6 Members", "10 Families (~50 Pax)", "10 Circles (~500 Pax)", "10 Communities (~5,000 Pax)", "100 Regions (~500,000 Pax)", "10 Settlements (~5,000,000 Pax)"],
        "IT Infrastructure Layer": ["Single salvages devices", "Circle LAN (Wired Hub)", "Mesh Router Node", "Regional Cache Server", "Settlement Backbone Node", "High Command Data Directory"],
        "MIS Governance Scope": ["Domestic allocation", "Circle Representative", "Community Council", "Regional Council Board", "Settlement Director", "Monetary Board"]
    }
    df = pd.DataFrame(hierarchy_data)
    st.table(df)
