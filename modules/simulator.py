import streamlit as st

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
import pandas as pd
import numpy as np

def show_simulator():
    st.title("📈 Price History & Pricing Simulator")
    
    t_sim1, t_sim2 = st.tabs(["📊 Price Trend Chart", "🧮 Algorithmic Pricing Simulator"])
    
    with t_sim1:
        st.subheader("📈 Gold Price Trend Graph")
        view = st.radio("Display View", ["Weekly", "Monthly"], horizontal=True, key="sim_trend_view")
        
        # Generate dummy data for the graph
        chart_data = pd.DataFrame(np.random.randn(20, 1), columns=['Gold Price Trend'])
        st.line_chart(chart_data)
        
    with t_sim2:
        st.write("""
        ### The Commodity Pricing Model
        Official prices are computed as: `Price = Base Price * GRI * (W_r * W_s * W_t * W_e)`
        Use the controls below to simulate how local environmental and policy factors scale the price of commodities, and how the Monetary Board can adjust the GRI to keep the basket affordable.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("#### Input Parameters")
            base_price = st.number_input("Base Commodity Price (INR)", min_value=10.0, max_value=1000.0, value=100.0, key="sim_base_price")
            gri = st.slider("Gold Reference Index (GRI Multiplier)", min_value=0.5, max_value=2.0, value=1.0, step=0.1, key="sim_gri")
            
            w_r = st.slider("Regional Weight (Wr - e.g. Drought = 1.3)", min_value=0.5, max_value=2.0, value=1.0, step=0.1, key="sim_w_r")
            w_s = st.slider("Seasonal Weight (Ws - e.g. Winter = 1.2)", min_value=0.5, max_value=2.0, value=1.0, step=0.1, key="sim_w_s")
            w_t = st.slider("Kingdom Tax Weight (Wt)", min_value=1.0, max_value=1.5, value=1.0, step=0.05, key="sim_w_t")
            w_e = st.slider("Emergency Weight (We)", min_value=1.0, max_value=2.0, value=1.0, step=0.1, key="sim_w_e")
            
        with col2:
            st.write("#### Output Calculations")
            final_price = base_price * gri * (w_r * w_s * w_t * w_e)
            st.metric("Computed Official Price", f"₹ {final_price:.2f}")

