import streamlit as st

st.markdown("""
<style>
/* Hide Streamlit top header, toolbar, GitHub fork badges, menu, and decoration */
#MainMenu {visibility: hidden !important; display: none !important;}
header {visibility: hidden !important; display: none !important;}
[data-testid="stHeader"] {visibility: hidden !important; display: none !important;}
[data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
[data-testid="stDecoration"] {visibility: hidden !important; display: none !important;}
[data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
.stAppDeployButton {visibility: hidden !important; display: none !important;}
#stDecoration {visibility: hidden !important; display: none !important;}

/* Hide Streamlit bottom footer and bottom-right viewer/host badges */
footer {visibility: hidden !important; display: none !important;}
[data-testid="stFooter"] {visibility: hidden !important; display: none !important;}
.viewerBadge_container__16g3m {visibility: hidden !important; display: none !important;}
[class*="viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="styles_viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="ViewerBadge"] {visibility: hidden !important; display: none !important;}
.stActionButton {visibility: hidden !important; display: none !important;}
</style>
""", unsafe_allow_html=True)

def show_overview():
    st.title("🕸️ The Survivors' Nation — Case Scenario")
    st.subheader("Designing Resilient Systems for a Post-Apocalyptic Economy")
    
    st.write("""
    ### The Narrative Context
    It is the year **2028**. A global six-month nuclear conflict has completely shattered the civilized world. 
    Major capital cities are destroyed, borders are wiped out, and traditional currencies have zero value. 
    The remaining world population is scattered, and we are focusing on a subset of **5 million survivors** who migrate to a geographically protected region with a reliable freshwater source. 
    The objective is not to study the war itself, but to study how to rebuild a functioning society from scratch using Systems Thinking and Information Systems.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.error("#### Constraint 1: No Internet\nOnly local Area Networks (LAN) and wireless mesh grids are salvageable. Offline synchronization is mandatory.")
    with col2:
        st.warning("#### Constraint 2: Scarce Power\nNo centralized power grids. Rely strictly on salvaged solar arrays and battery banks. Scheduled server downtimes.")
    with col3:
        st.info("#### Constraint 3: No Government\nNo central banks, cloud databases, or security institutions. Governance processes must be designed completely from scratch.")
