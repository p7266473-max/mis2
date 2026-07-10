import streamlit as st
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
            
            st.write("#### The Closed-Loop Feedback Goal")
            st.write("Desired Monthly living expenditure target: **₹ 6,000**")
            estimated_basket_cost = final_price * 60  # assume 60 units of baseline commodities
            st.metric("Estimated Household Basket Cost", f"₹ {estimated_basket_cost:.2f}")
            
            if estimated_basket_cost > 6000:
                st.error("System Alert: Basket cost exceeds the ₹6,000 limit. The Monetary Authority must decrease KGI/GRI to restore purchasing power!")
            else:
                st.success("Normal Status: Basket cost is within the ₹6,000 limit. Household savings of ₹4,000 are protected.")
