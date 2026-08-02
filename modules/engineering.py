import streamlit as st

st.markdown("""
<style>
#MainMenu {visibility: hidden; display: none !important;}
header {visibility: hidden; display: none !important;}
footer {visibility: hidden; display: none !important;}
[data-testid="stHeader"] {visibility: hidden; display: none !important;}
[data-testid="stFooter"] {visibility: hidden; display: none !important;}
[data-testid="stToolbar"] {visibility: hidden; display: none !important;}
[data-testid="stDecoration"] {visibility: hidden; display: none !important;}
[data-testid="stStatusWidget"] {visibility: hidden; display: none !important;}
.stAppDeployButton {display: none !important;}
#stDecoration {display: none !important;}
</style>
""", unsafe_allow_html=True)

def show_engineering():
    st.title("🏗️ Systems Architecture & Subject Roles")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 💻 IT Engineering Scope")
        st.write("""
        * **Physical Mesh Networking:** Setting up antennas, configuring routers, routing algorithms.
        * **Database Schema Execution:** Writing tables, columns, indexes, and handling replication.
        * **Cryptographic Code:** Implementing SHA-256 signatures, verifying public/private keys.
        * **Power Management:** scheduled runtime triggers, low-power state configurations.
        """)
    with col2:
        st.write("### 🏢 MIS Analysis Scope")
        st.write("""
        * **Economic Logic & Policies:** Planning the GRI link mechanism, freezing FX tables.
        * **Process Modeling:** Designing weekend pricing sync and audit processes.
        * **Data Governance:** Defining role authorities (Monetary Board vs Local Council Officers).
        * **Ethical Assessment:** Evaluating algorithmic overrides, emergency policies, and housing milestones.
        """)
