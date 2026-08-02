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

import streamlit.components.v1 as components

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

/* Hide Streamlit bottom footer, bottom container, and viewer/host badges */
footer {visibility: hidden !important; display: none !important;}
[data-testid="stFooter"] {visibility: hidden !important; display: none !important;}
[data-testid="stBottom"] {visibility: hidden !important; display: none !important;}
[data-testid="stBottomBlockContainer"] {visibility: hidden !important; display: none !important;}
.viewerBadge_container__16g3m {visibility: hidden !important; display: none !important;}
[class*="viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="styles_viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="ViewerBadge"] {visibility: hidden !important; display: none !important;}
.stActionButton {visibility: hidden !important; display: none !important;}
</style>
""", unsafe_allow_html=True)

components.html("""
<script>
function cleanupStreamlitUI() {
    const targetSelectors = [
        'footer', '[data-testid="stFooter"]', '[data-testid="stDecoration"]',
        '[data-testid="stStatusWidget"]', '[data-testid="stToolbar"]', '#MainMenu',
        'header', '.stAppDeployButton', '#stDecoration', '.viewerBadge_container__16g3m',
        '[class*="viewerBadge"]', '[class*="styles_viewerBadge"]', '[class*="ViewerBadge"]',
        '.stActionButton', '[data-testid="stBottom"]', '[data-testid="stBottomBlockContainer"]',
        'button[title*="Streamlit"]', 'div[class*="StatusWidget"]'
    ];

    [document, window.parent.document].forEach(doc => {
        try {
            targetSelectors.forEach(selector => {
                doc.querySelectorAll(selector).forEach(el => {
                    el.style.setProperty('display', 'none', 'important');
                    el.style.setProperty('visibility', 'hidden', 'important');
                    el.style.setProperty('opacity', '0', 'important');
                });
            });
        } catch (err) {}
    });
}
cleanupStreamlitUI();
setInterval(cleanupStreamlitUI, 250);
</script>
""", height=0, width=0)


# Apply CSS styling for premium look
import streamlit.components.v1 as components

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

/* Hide Streamlit bottom footer, bottom container, and viewer/host badges */
footer {visibility: hidden !important; display: none !important;}
[data-testid="stFooter"] {visibility: hidden !important; display: none !important;}
[data-testid="stBottom"] {visibility: hidden !important; display: none !important;}
[data-testid="stBottomBlockContainer"] {visibility: hidden !important; display: none !important;}
.viewerBadge_container__16g3m {visibility: hidden !important; display: none !important;}
[class*="viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="styles_viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="ViewerBadge"] {visibility: hidden !important; display: none !important;}
.stActionButton {visibility: hidden !important; display: none !important;}
</style>
""", unsafe_allow_html=True)

components.html("""
<script>
function cleanupStreamlitUI() {
    const targetSelectors = [
        'footer', '[data-testid="stFooter"]', '[data-testid="stDecoration"]',
        '[data-testid="stStatusWidget"]', '[data-testid="stToolbar"]', '#MainMenu',
        'header', '.stAppDeployButton', '#stDecoration', '.viewerBadge_container__16g3m',
        '[class*="viewerBadge"]', '[class*="styles_viewerBadge"]', '[class*="ViewerBadge"]',
        '.stActionButton', '[data-testid="stBottom"]', '[data-testid="stBottomBlockContainer"]',
        'button[title*="Streamlit"]', 'div[class*="StatusWidget"]'
    ];

    [document, window.parent.document].forEach(doc => {
        try {
            targetSelectors.forEach(selector => {
                doc.querySelectorAll(selector).forEach(el => {
                    el.style.setProperty('display', 'none', 'important');
                    el.style.setProperty('visibility', 'hidden', 'important');
                    el.style.setProperty('opacity', '0', 'important');
                });
            });
        } catch (err) {}
    });
}
cleanupStreamlitUI();
setInterval(cleanupStreamlitUI, 250);
</script>
""", height=0, width=0)

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
