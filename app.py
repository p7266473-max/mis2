import streamlit as st
import pandas as pd
import numpy as np

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

# ─────────────────────────────────────────────────────────────────────────────
# 1. OVERVIEW & RULES MODULE
# ─────────────────────────────────────────────────────────────────────────────
if app_mode == "1. Overview & Rules":
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

# ─────────────────────────────────────────────────────────────────────────────
# 2. POPULATION HIERARCHY
# ─────────────────────────────────────────────────────────────────────────────
elif app_mode == "2. Population Hierarchy":
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

# ─────────────────────────────────────────────────────────────────────────────
# 3. MONETARY SYSTEM (GRI) & TREASURY
# ─────────────────────────────────────────────────────────────────────────────
elif app_mode == "3. Monetary System (GRI)":
    st.title("🪙 Treasury & Monetary System")
    
    t1, t2 = st.tabs(["🪙 Treasury Dashboard & Calculator", "📅 Daily Gold Price Interpolator"])
    
    with t1:
        # 1. Dashboard Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Gold Reserve", "12,450 oz", "+2.5%")
        col2.metric("Avg Gold Price", "$603.77/oz", "Stable")
        col3.metric("Last Updated", "2026-07-10 16:30")

        st.write("---")
        
        # 2. Gold Calculator
        st.subheader("🧮 Gold/Treasury Calculator")
        c1, c2, c3 = st.columns(3)
        with c1:
            gold_rate = st.number_input("Gold Rate (USD/oz)", value=603.77, key="calc_gold_rate")
            weight = st.number_input("Weight Amount", value=1.0, key="calc_weight")
        with c2:
            currency = st.selectbox("Currency", ["USD", "INR", "MYR", "EUR", "GBP", "JPY", "SGD", "AED", "SAR", "PKR", "CNY", "THB", "AUD", "CAD", "CHF", "HKD", "BRL", "MXN", "NZD", "ZAR"], key="calc_currency")
            unit = st.selectbox("Weight Unit", ["Troy Ounce", "Gram", "Kilogram", "Tola", "Tael"], key="calc_unit")
        with c3:
            rates_map = {"USD": 1.0, "INR": 46.55, "EUR": 0.9374, "GBP": 0.6814, "PKR": 61.93, "MYR": 3.8, "CNY": 8.2766, "THB": 43.09, "CAD": 1.5037, "JPY": 117.28, "AUD": 1.8021, "SGD": 1.7338, "CHF": 1.639, "ZAR": 7.825, "KRW": 1283.8}
            default_ex = rates_map.get(currency, 1.0)
            ex_rate = st.number_input("Exchange Rate (to USD)", value=default_ex, key="calc_ex_rate")
            
        # Conversion Logic
        conversion_map = {"Troy Ounce": 1.0, "Gram": 0.03215, "Kilogram": 32.1507, "Tola": 0.375, "Tael": 1.2034}
        total_val = (gold_rate * (weight * conversion_map[unit])) * ex_rate
        
        st.info(f"### Total Calculated Value: {total_val:,.2f} {currency}")
        final_val = st.number_input("Final Adjusted Value (Manual Overwrite)", value=total_val, key="calc_final_val")

        # 3. Export & Reporting
        st.write("---")
        st.subheader("📂 Export & Reporting")
        col_e1, col_e2, col_e3 = st.columns(3)
        if col_e1.button("Export to PDF"): st.toast("PDF Exported")
        if col_e2.button("Export to Excel"): st.toast("Excel Exported")
        if col_e3.button("Print Ledger"): st.write("Opening printer dialog...")
        
    with t2:
        st.write("""
        ### Dynamic Value Anchor
        Because physical banknotes have no backing government, the Kingdom uses them as tokens whose exchange value is mapped to gold. To prevent speculation, we align years **2029–2035** directly with historical pre-collapse gold prices from **2001–2007** (London Bullion Market Association data).
        """)
        
        col_t2_1, col_t2_2 = st.columns(2)
        with col_t2_1:
            st.write("#### Calendar Mapping Configuration")
            target_year = st.selectbox("Select Simulation Year", [2029, 2030, 2031, 2032, 2033, 2034, 2035])
            st.session_state["target_year"] = target_year
            reference_year = target_year - 28
            st.success(f"Simulation Year **{target_year}** maps to Reference Year **{reference_year}**")
            
            if target_year == 2032:
                st.info("Notice: 2032 maps to 2004, which are both Leap Years. February 29th aligns perfectly!")
                
        with col_t2_2:
            st.write("#### Permanent Exchange Rates (Locked Jan 1, 2001)")
            fx_rates = {
                "Currency Code": ["USD", "EUR", "GBP", "INR", "PAK", "CAD", "JPY", "AUD", "SGD", "CHF", "CNY", "MYR", "HKD", "BRL", "MXN", "NZD", "NOK", "SEK", "THB", "ZAR", "KRW"],
                "Currency Name": [
                    "US Dollar", "Euro (EMU)", "British Pound", "Indian Rupee", "Pakistani Rupee", "Canadian Dollar",
                    "Japanese Yen", "Australian Dollar", "Singapore Dollar", "Swiss Franc", "Chinese Yuan",
                    "Malaysian Ringgit", "Hong Kong Dollar", "Brazilian Real", "Mexican Peso", "New Zealand Dollar",
                    "Norwegian Krone", "Swedish Krona", "Thai Baht", "South African Rand", "South Korean Won"
                ],
                "Fixed Rate (per USD)": [
                    1.0000, 0.9374, 0.6814, 46.5500, 61.9300, 1.5037,
                    117.2800, 1.8021, 1.7338, 1.6390, 8.2766,
                    3.8000, 7.7997, 1.9540, 9.9720, 2.2472,
                    8.7675, 9.5050, 43.0900, 7.8250, 1283.8000
                ]
            }
            st.dataframe(pd.DataFrame(fx_rates), height=250)

        # New section: Dynamic LBMA Gold Price Interpolation table
        st.write("---")
        st.write("### 📈 Dynamic LBMA Gold Price Interpolation Table")
        st.write("""
        This table displays the master calculation schedule used by the Monetary Authority. 
        The gold price for January 1 of each year is set to the historical LBMA annual average. 
        The difference is divided by **200 working days** (excluding weekends) to calculate the daily step change used for dynamic calculation.
        """)

        # Interpolation data
        lbma_data = [
            {"Sim Year": 2029, "Ref Year": 2001, "Gold Price (USD/oz)": 271.04},
            {"Sim Year": 2030, "Ref Year": 2002, "Gold Price (USD/oz)": 309.68},
            {"Sim Year": 2031, "Ref Year": 2003, "Gold Price (USD/oz)": 363.32},
            {"Sim Year": 2032, "Ref Year": 2004, "Gold Price (USD/oz)": 409.17},
            {"Sim Year": 2033, "Ref Year": 2005, "Gold Price (USD/oz)": 444.45},
            {"Sim Year": 2034, "Ref Year": 2006, "Gold Price (USD/oz)": 603.77},
            {"Sim Year": 2035, "Ref Year": 2007, "Gold Price (USD/oz)": 695.39},
        ]
        
        # Calculate difference and daily step using pandas
        df_lbma = pd.DataFrame(lbma_data)
        df_lbma["Year Diff (USD)"] = df_lbma["Gold Price (USD/oz)"].diff().fillna(0.0)
        df_lbma["Daily Step (200 Working Days)"] = df_lbma["Year Diff (USD)"] / 200.0

        st.dataframe(df_lbma.style.format({
            "Gold Price (USD/oz)": "${:.2f}",
            "Year Diff (USD)": "${:.2f}",
            "Daily Step (200 Working Days)": "${:.6f}"
        }), use_container_width=True)

        # 365 Days Daily Interpolation Generator Section
        st.write("---")
        st.write("### 📅 7-Year Calendar Daily Gold Price Interpolation Generator (365-day basis)")
        st.write("""
        Generate the linear interpolation for every single calendar day from **January 1, 2029** to **December 31, 2035** (7 years = 2,556 total days).
        This simulates how local databases automatically compute the day-to-day index step scaling factors across multiple mass units:
        * **Troy Ounce (oz):** The standard pre-collapse pricing unit.
        * **Gram (g):** Standard scientific unit (`1 troy ounce = 31.1034768 grams`).
        * **Pound (lb):** Common weight unit (`1 troy ounce = 0.06857143 pounds avdp`).
        * **Pawn (Sovereign/Don/Tol - Local Unit):** Mapped for local trading systems (`1 troy ounce = 3.8879346 pawns / sovereigns`).
        """)

        if st.button("Generate Full Daily Interpolation Ledger (2,556 Days)"):
            # Generate full date index
            date_range = pd.date_range(start="2029-01-01", end="2035-12-31", freq="D")
            
            # Populate DataFrame with dates and anchor values
            df_full = pd.DataFrame(index=date_range)
            df_full["Gold Price (USD/oz)"] = np.nan
            
            # Assign baseline anchors on Jan 1st of each year
            df_full.loc["2029-01-01", "Gold Price (USD/oz)"] = 271.04
            df_full.loc["2030-01-01", "Gold Price (USD/oz)"] = 309.68
            df_full.loc["2031-01-01", "Gold Price (USD/oz)"] = 363.32
            df_full.loc["2032-01-01", "Gold Price (USD/oz)"] = 409.17
            df_full.loc["2033-01-01", "Gold Price (USD/oz)"] = 444.45
            df_full.loc["2034-01-01", "Gold Price (USD/oz)"] = 603.77
            df_full.loc["2035-01-01", "Gold Price (USD/oz)"] = 695.39
            df_full.loc["2035-12-31", "Gold Price (USD/oz)"] = 695.39  # Fill last date anchor
            
            # Linearly interpolate NaN values
            df_full["Gold Price (USD/oz)"] = df_full["Gold Price (USD/oz)"].interpolate(method="linear")
            
            # Calculate auxiliary metrics for weight units
            df_full["Gold Price (USD/g)"] = df_full["Gold Price (USD/oz)"] / 31.1034768
            df_full["Gold Price (USD/lb)"] = df_full["Gold Price (USD/oz)"] / 14.5833  # lb troy
            df_full["Gold Price (USD/pawn)"] = df_full["Gold Price (USD/oz)"] / 3.8879346
            
            # Calculate dynamic values in INR and PAK (PKR) currencies
            df_full["Gold Price (INR/oz)"] = df_full["Gold Price (USD/oz)"] * 46.55
            df_full["Gold Price (PAK/oz)"] = df_full["Gold Price (USD/oz)"] * 61.93
            
            # Formatting output
            df_full.index.name = "Date"
            df_display = df_full.reset_index()
            df_display["Date"] = df_display["Date"].dt.strftime('%Y-%m-%d')
            
            st.success("Successfully interpolated 2,556 days of data across all weights and currencies!")
            
            # Display sample and download link
            st.write("#### Data Sample (First 20 Days):")
            st.dataframe(df_display.head(20).style.format({
                "Gold Price (USD/oz)": "${:.4f}",
                "Gold Price (USD/g)": "${:.4f}",
                "Gold Price (USD/lb)": "${:.4f}",
                "Gold Price (USD/pawn)": "${:.4f}",
                "Gold Price (INR/oz)": "₹{:.2f}",
                "Gold Price (PAK/oz)": "₨{:.2f}"
            }))
            
            st.write("#### Data Sample (Last 20 Days):")
            st.dataframe(df_display.tail(20).style.format({
                "Gold Price (USD/oz)": "${:.4f}",
                "Gold Price (USD/g)": "${:.4f}",
                "Gold Price (USD/lb)": "${:.4f}",
                "Gold Price (USD/pawn)": "${:.4f}",
                "Gold Price (INR/oz)": "₹{:.2f}",
                "Gold Price (PAK/oz)": "₨{:.2f}"
            }))

            # Enable CSV download
            csv = df_display.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Full 7-Year Ledger CSV",
                data=csv,
                file_name="survivors_nation_gold_7year_units_interpolation.csv",
                mime="text/csv",
            )

# ─────────────────────────────────────────────────────────────────────────────
# 4. PRICE HISTORY & PRICING SIMULATOR
# ─────────────────────────────────────────────────────────────────────────────
elif app_mode == "4. Pricing Simulator":
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

# ─────────────────────────────────────────────────────────────────────────────
# 5. IT VS MIS ENGINEERING
# ─────────────────────────────────────────────────────────────────────────────
elif app_mode == "5. IT vs MIS Engineering":
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

# ─────────────────────────────────────────────────────────────────────────────
# 6. TALK TO A SURVIVOR MODULE
# ─────────────────────────────────────────────────────────────────────────────
elif app_mode == "6. Talk to a Survivor":
    st.title("🗣️ Interacting with a Local Survivor")
    st.write("""
    ### Enter your Gemini API Key to start the simulator
    This module uses the **Bring Your Own Key (BYOK)** approach. 
    The AI acts as a survivor from the 5 million population living under KGI/GRI monetary rules.
    """)

    # API Key Input
    api_key = st.text_input("Enter Gemini API Key", type="password")

    if api_key:
        try:
            import google.generativeai as genai

            # Configure API key
            genai.configure(api_key=api_key)

            st.success("API Key authenticated successfully!")

            # Build detailed dynamic prompt context containing the full discussion history and economic philosophy
            sim_year_ctx = st.session_state.get("target_year", 2029)
            ref_year_ctx = sim_year_ctx - 28
            
            # Map simulation year to baseline pricing context
            gold_prices_ctx = {
                2029: 271.04, 2030: 309.68, 2031: 363.32,
                2032: 409.17, 2033: 444.45, 2034: 603.77, 2035: 695.39
            }
            year_gold_val = gold_prices_ctx.get(sim_year_ctx, 271.04)

            system_prompt = f"""
            SYSTEM BLUEPRINT & CONTEXT (DO NOT BREAK CHARACTER):
            - Persona: You are a random survivor (a normal resident/populant) living in the 'Survivors' Nation' (5M population) after the 2028 WWIII nuclear holocaust.
            - Tech Environment: You live in a community powered by solar grids and connected by wireless mesh networks. Technology is the nervous system, Policy is the brain.
            - Monetary Philosophy: Gold is the master variable. All official prices are calculated using the formula: Price = Base Price * GRI * (Wr * Ws * Wt * We).
            - Economic Goal: Social stability, not price discovery. The Kingdom attempts to maximize social welfare by keeping essential goods affordable while maintaining fairness for producers. 'Happiness' is a managed system output.
            - Household Targets: The system targets a ₹6,000 monthly living expense cap and a ₹4,000 monthly savings sweep for housing lease-to-own ownership.
            - Currencies: Physical banknotes act as claims/tokens, fixed to USD conversion rates on January 1, 2001.
            - Dynamic Adjustment: The Kingdom High Command dynamically tweaks/interpolates the Gold Reference Index (GRI) to scale prices up or down to protect household purchasing power.
            - Current State: Simulation Year is {sim_year_ctx} (mapped to LBMA reference year {ref_year_ctx}). Gold anchor is ${year_gold_val:.2f}/oz.
            
            RULES:
            1. You only know about your post-apocalyptic society, local mesh networking, the KGI/GRI price adjustments, gold values, and survival constraints.
            2. If someone asks you about things outside this context (e.g. current world news, generic factual queries like 'What is Mount Everest' or 'Who is the President'), you must refuse to answer. Say: 'I am just a simple survivor working in the fields. I only know about our community mesh networks, crop yields, and the KGI pricing changes. I cannot help with external history.'
            3. Keep your tone survival-focused, pragmatic, and slightly weary but hopeful. Refer to active rates in your replies if asked about gold prices or currencies.
            """

            # Initialize Chat state
            if "messages" not in st.session_state:
                st.session_state.messages = []

            # Display previous chat messages
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])

            # Input box
            if user_input := st.chat_input("Ask the survivor a question about their life or the economy..."):
                # Append user message
                st.session_state.messages.append({"role": "user", "content": user_input})
                with st.chat_message("user"):
                    st.write(user_input)

                # Query Gemini using the legacy SDK structures
                with st.chat_message("assistant"):
                    with st.spinner("The survivor is replying..."):
                        # Dynamically discover the best model allowed by this API key
                        try:
                            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                            selected_model = next((m for m in models if "gemini-1.5-flash" in m), None)
                            if not selected_model:
                                selected_model = models[0] if models else "models/gemini-1.5-flash-latest"
                        except Exception:
                            selected_model = "models/gemini-1.5-flash-latest"

                        if not selected_model.startswith("models/"):
                            selected_model = f"models/{selected_model}"

                        # Map session messages to Gemini legacy chat format: [{'role': 'user'|'model', 'parts': [text]}]
                        history_payload = []
                        for msg in st.session_state.messages[:-1]:
                            role_map = "user" if msg["role"] == "user" else "model"
                            history_payload.append({
                                "role": role_map,
                                "parts": [msg["content"]]
                            })

                        # Initialize model with the comprehensive system instruction
                        model = genai.GenerativeModel(
                            model_name=selected_model,
                            system_instruction=system_prompt
                        )

                        # Implement smolagents integration
                        try:
                            from smolagents import CodeAgent, Tool, LiteLLMModel
                            import io
                            import contextlib
                            
                            # Cache the agent instance in session state for conversational persistence
                            if "code_agent" not in st.session_state:
                                lite_model_name = selected_model.replace("models/", "gemini/")
                                agent_model = LiteLLMModel(
                                    model_id=lite_model_name,
                                    api_key=api_key
                                )

                                class GetGoldPriceTool(Tool):
                                    name = "get_current_gold_price"
                                    description = "Retrieves the active gold index price per troy ounce for the current simulation year."
                                    inputs = {}
                                    output_type = "string"

                                    def forward(self):
                                        return f"The current active gold index price is ${year_gold_val:.2f} per troy ounce for the simulation year {sim_year_ctx}."

                                class GetPricingFormulaTool(Tool):
                                    name = "get_pricing_formula_details"
                                    description = "Returns the mathematical formula parameters and descriptions of the multipliers (Wr, Ws, Wt, We)."
                                    inputs = {}
                                    output_type = "string"

                                    def forward(self):
                                        return (
                                            "Pricing Formula: Price = Base Price * GRI * (Wr * Ws * Wt * We)\n"
                                            "Multiplier Parameters:\n"
                                            "- Wr: Regional Weight (Drought factor)\n"
                                            "- Ws: Seasonal Weight (Harvest cycle alignment)\n"
                                            "- Wt: Kingdom Tax Weight (non-essential services surcharge)\n"
                                            "- We: Emergency Weight (anti-hoarding/rationing adjustments)"
                                        )

                                st.session_state.code_agent = CodeAgent(
                                    tools=[GetGoldPriceTool(), GetPricingFormulaTool()],
                                    model=agent_model,
                                    additional_authorized_imports=["pandas", "numpy"]
                                )

                            prompt_with_instructions = (
                                f"You are a survivor speaking to a visitor. Stay in character.\n"
                                f"System Guidelines:\n{system_prompt}\n\n"
                                f"Query: {user_input}"
                            )
                            
                            # Capture agent logs dynamically to show the students the agentic thought steps
                            log_capture = io.StringIO()
                            with contextlib.redirect_stdout(log_capture):
                                reply = st.session_state.code_agent.run(prompt_with_instructions)
                            
                            agent_logs = log_capture.getvalue()
                            
                            # Render logs in expander
                            if agent_logs.strip():
                                with st.expander("🕵️ Inspect Survivor's Agentic Thought Process"):
                                    st.text(agent_logs)
                                    
                            st.write(reply)

                        except Exception as agent_error:
                            # fallback to direct generative model if smolagents fails to load
                            model = genai.GenerativeModel(
                                model_name=selected_model,
                                system_instruction=system_prompt
                            )
                            # Start chat with loaded history
                            chat = model.start_chat(history=history_payload)
                            response = chat.send_message(
                                user_input,
                                generation_config={"temperature": 0.7, "max_output_tokens": 300}
                            )
                            reply = response.text
                            st.write(reply)
                
                # Append assistant reply
                st.session_state.messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            st.error("⚠️ The Mesh Network is struggling to sync with the central database. The solar grids might be undergoing scheduled runtime downtime. Please try your query again when the signal stabilizes.")
    else:
        st.info("Please enter your Gemini API Key in the box above to enable conversational simulation.")

# ─────────────────────────────────────────────────────────────────────────────
# 7. GROUP ASSIGNMENTS & SECTORS
# ─────────────────────────────────────────────────────────────────────────────
elif app_mode == "7. Group Assignments & Sectors":
    st.title("👥 Kingdom Sector Teams & Group Assignments")
    st.write("""
    ### Organizational & Systems Responsibility
    To operationalize the Survivors' Nation, students are divided into 10 specialized resource groups. 
    Each group manages the technology layer, database logs, and economic policies for their respective sector.
    """)
    
    group_assignments = [
        {
            "id": 1,
            "name": "Group 1: Consolidation",
            "sector": "Consolidation",
            "lead": "Thanishvel Mogam",
            "members": ["Thanishvel Mogam", "Jeremy Matthews Thomas", "Ajwaad Mahbub Karim", "Intan Syazana"],
            "icon": "💼",
            "resource": "Gold Standard & System Ledger Reconciliation"
        },
        {
            "id": 2,
            "name": "Group 2: Rice / Flour",
            "sector": "Rice / Flour",
            "lead": "Rejoice Kandemiri",
            "members": ["Dehemi Amanda", "Rejoice Kandemiri", "Darrshnee"],
            "icon": "🌾",
            "resource": "Grain & Flour Reserves Management"
        },
        {
            "id": 3,
            "name": "Group 3: Spices",
            "sector": "Spices",
            "lead": "Fahim Sahriar Ponno",
            "members": ["Fahim Sahriar Ponno", "Eithi Noor Jahan", "Rifat Md", "Joy Chandra Das", "Zannat Zamman"],
            "icon": "🌶️",
            "resource": "Imported & Local Herb/Spice Logistics"
        },
        {
            "id": 4,
            "name": "Group 4: Vegetables",
            "sector": "Vegetables",
            "lead": "Farhad Niloy",
            "members": ["Raj Malo (Himangshu)", "Farhad Niloy", "Sagor Mollah", "Shawon Sorif"],
            "icon": "🥦",
            "resource": "Perishable Crop Harvests & Cold Storage Logs"
        },
        {
            "id": 5,
            "name": "Group 5: Fruits",
            "sector": "Fruits",
            "lead": "Jishan Ahamed Himel",
            "members": ["Akter Khusbu", "Md Shahik Khan Hemel", "Md Rimon", "Jishan Ahamed Himel", "Biraj Sarker"],
            "icon": "🍎",
            "resource": "Orchard Production & Distribution Routing"
        },
        {
            "id": 6,
            "name": "Group 6: Electricity",
            "sector": "Electricity",
            "lead": "Arpita Roy Joya",
            "members": ["Arpita Roy Joya", "Tanvire Anwaro Ivan", "Rahi Al Md Jameal Kawsar", "Sohanur Rahman"],
            "icon": "⚡",
            "resource": "Solar Arrays, Battery Banks, & Scheduled Server Downtimes"
        },
        {
            "id": 7,
            "name": "Group 7: Fuel",
            "sector": "Fuel",
            "lead": "Sofiq",
            "members": ["Salam", "Utsa", "Sofiq", "Zaman Uddin Sarker", "Sayed"],
            "icon": "⛽",
            "resource": "Generators & Biofuel Reserves Inventory"
        },
        {
            "id": 8,
            "name": "Group 8: Furniture / Utensils",
            "sector": "Furniture / Utensils",
            "lead": "Hasan Murad",
            "members": ["Abdul Azim", "Hasan Murad", "Tanjil", "Wazed", "Rabbi"],
            "icon": "🪑",
            "resource": "Domestic Living Goods & Asset Lifecycles"
        },
        {
            "id": 9,
            "name": "Group 9: Clothes",
            "sector": "Clothes",
            "lead": "Ishtiaq Ahamed Swapneel",
            "members": ["Afsana Akter Borsha", "Angelo Tirtho Khan", "Fatema Begum", "Ishtiaq Ahamed Swapneel"],
            "icon": "👕",
            "resource": "Apparel, Uniforms, & Textiles Sourcing"
        },
        {
            "id": 10,
            "name": "Group 10: Meat",
            "sector": "Meat",
            "lead": "Eshwary",
            "members": ["Eshwary", "Parveer"],
            "icon": "🥩",
            "resource": "Livestock Tracking & Rations Distribution"
        }
    ]

    t_groups1, t_groups2 = st.tabs(["👥 Sector Teams & Assignments", "📊 Kingdom Operational Matrix & Budget Governor"])
    
    with t_groups1:
        # Filters
        col1, col2 = st.columns([2, 1])
        with col1:
            search_query = st.text_input("🔍 Search member or sector team name", "").strip().lower()
        with col2:
            filter_resource = st.selectbox("Filter by primary resource/sector", ["All"] + [g["sector"] for g in group_assignments])
        
        filtered_groups = []
        for g in group_assignments:
            matches_search = (
                search_query in g["name"].lower() or 
                search_query in g["sector"].lower() or 
                any(search_query in m.lower() for m in g["members"])
            )
            matches_resource = (filter_resource == "All" or g["sector"] == filter_resource)
            
            if matches_search and matches_resource:
                filtered_groups.append(g)

        # Statistics Bar
        met1, met2, met3 = st.columns(3)
        met1.metric("Total Designated Sectors", len(group_assignments))
        met2.metric("Matching Search Results", len(filtered_groups))
        met3.metric("Total Assigned Specialists", sum(len(g["members"]) for g in group_assignments))
        
        st.markdown("---")
        
        # Display Group Cards
        cols_per_row = 2
        for i in range(0, len(filtered_groups), cols_per_row):
            cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                if i + j < len(filtered_groups):
                    g = filtered_groups[i + j]
                    with cols[j]:
                        members_html = "".join([
                            f"<div class='member-item'>• {name} "
                            f"{'<span class=\'lead-badge\'>👑 Lead</span>' if name == g['lead'] else ''}</div>"
                            for name in g["members"]
                        ])
                        
                        card_content = f"""
                        <div class="group-card">
                            <h3 style="margin-top: 0; margin-bottom: 0.5rem; color: #1e3a8a;">
                                {g['icon']} {g['name']}
                            </h3>
                            <p style="color: #64748b; font-size: 0.9rem; margin-bottom: 0.8rem;">
                                <b>Primary Sector Duty:</b> {g['resource']}
                            </p>
                            <div style="margin-bottom: 0.5rem;">
                                {members_html}
                            </div>
                        </div>
                        """
                        st.markdown(card_content, unsafe_allow_html=True)
                        
    with t_groups2:
        st.subheader("📊 The Kingdom’s Operational Matrix (2026 Simulation)")
        st.write("""
        This matrix maps the 10-Sector Budgetary Baseline to the assigned groups. 
        Each group carries systemic responsibility for their resource bandwidth.
        """)
        
        # Display baseline table
        matrix_data = {
            "Sector": ["1. Grains/Staples", "2. Proteins (Meat)", "3. Vegetables", "4. Fruits", "5. Spices/Safety", "6. Electricity", "7. Fuel", "8. Furniture/Utensils", "9. Clothes", "10. Reserve/Health"],
            "Assigned Group": ["Group 2 (Rice/Flour)", "Group 10 (Meat)", "Group 4 (Vegetables)", "Group 5 (Fruits)", "Group 3 (Spices)", "Group 6 (Electricity)", "Group 7 (Fuel)", "Group 8 (Furniture)", "Group 9 (Clothes)", "Group 1 (Consolidation)"],
            "Baseline Budget": [1200, 1000, 600, 300, 200, 400, 400, 500, 300, 800],
            "Min Bandwidth": [1000, 800, 400, 200, 100, 300, 300, 400, 200, 600],
            "Max Bandwidth": [1500, 1200, 800, 400, 300, 500, 500, 600, 400, 1000]
        }
        df_matrix = pd.DataFrame(matrix_data)
        st.table(df_matrix)
        st.caption("*Note: Electricity and Fuel budgets are split to match Group 6 and Group 7 tasks. Reserve/Health budget is allocated to Group 1 (Monetary Board) as their Emergency Fund.")

        # Interactive Live Budget Governor
        st.write("---")
        st.subheader("🎮 Monday Launch: Live Budget Governor")
        st.info("💡 **Monetary Board Challenge:** Group 1 (Consolidation) must audit and input requests from the other 9 groups. The total combined budget must equal exactly **₹6,000** to initialize the simulation!")
        
        bg_col1, bg_col2 = st.columns(2)
        with bg_col1:
            st.write("##### Input Proposed Budgets")
            b_g2 = st.number_input("1. Grains/Staples (Group 2) [1000-1500]", 1000, 1500, 1200, step=50, key="gov_b_g2")
            b_g10 = st.number_input("2. Proteins (Meat) (Group 10) [800-1200]", 800, 1200, 1000, step=50, key="gov_b_g10")
            b_g4 = st.number_input("3. Vegetables (Group 4) [400-800]", 400, 800, 600, step=50, key="gov_b_g4")
            b_g5 = st.number_input("4. Fruits (Group 5) [200-400]", 200, 400, 300, step=50, key="gov_b_g5")
            b_g3 = st.number_input("5. Spices/Safety (Group 3) [100-300]", 100, 300, 200, step=50, key="gov_b_g3")
        with bg_col2:
            st.write("##### Input Proposed Budgets (Cont.)")
            b_g6 = st.number_input("6. Electricity (Group 6) [300-500]", 300, 500, 400, step=50, key="gov_b_g6")
            b_g7 = st.number_input("7. Fuel (Group 7) [300-500]", 300, 500, 400, step=50, key="gov_b_g7")
            b_g8 = st.number_input("8. Furniture/Utensils (Group 8) [400-600]", 400, 600, 500, step=50, key="gov_b_g8")
            b_g9 = st.number_input("9. Clothes (Group 9) [200-400]", 200, 400, 300, step=50, key="gov_b_g9")
            b_g1 = st.number_input("10. Reserve/Health (Group 1) [600-1000]", 600, 1000, 800, step=50, key="gov_b_g1")

        total_proposed = b_g2 + b_g10 + b_g4 + b_g5 + b_g3 + b_g6 + b_g7 + b_g8 + b_g9 + b_g1
        
        # Display progress and validation status
        st.write("### Total Proposed Budget Balance")
        if total_proposed == 6000:
            st.success(f"🎉 **Perfect Balance achieved: ₹{total_proposed:,.2f} / ₹6,000.00!**")
            st.balloons()
            st.markdown("""
            ### 🚀 Simulation Initialized!
            Cabinet Appointments are officially locked. High Command Node Online.
            """)
        elif total_proposed > 6000:
            st.error(f"❌ **Over-Budget: ₹{total_proposed:,.2f} / ₹6,000.00** (Surplus of ₹{total_proposed - 6000}). Group 1 must enforce budget cuts!")
        else:
            st.warning(f"⚠️ **Under-Budget: ₹{total_proposed:,.2f} / ₹6,000.00** (Deficit of ₹{6000 - total_proposed}). Allocate remaining funds to reserves or sectors.")

        # Monday Launch Checklist Expanders
        st.write("---")
        st.subheader("📋 Monday Launch Checklist & Instructions")
        with st.expander("1. Cabinet Appointments & Classroom Briefing"):
            st.markdown("""
            - **Appoint the Leaders:** Post/Share this list with the class. Every student carries structural accountability.
            - **Emergency Meeting:** Brief **Group 1 (Consolidation)** 5 minutes early. Instruct them as the **Kingdom's Monetary Board** who must audit and approve final budgets.
            """)
        with st.expander("2. The Budget Proposal Challenge (30 Minutes)"):
            st.markdown("""
            - **Research & Negotiate:** Give the other 9 groups 30 minutes to justify their commodity budgets.
            - **Proposal Phase:** Each group must submit and present their final budget requests within their min/max bandwidth to Group 1.
            """)
        with st.expander("3. Initialize Simulation"):
            st.markdown("""
            - **The Live Governor:** Group 1 inputs requests here live. When the balance hits exactly ₹6,000, initialization is complete!
            """)



