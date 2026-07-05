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
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR NAVIGATION
# ─────────────────────────────────────────────────────────────────────────────
st.sidebar.title("Survivors' Nation")
st.sidebar.markdown("*MIS & IT Case Study (Week 3)*")

app_mode = st.sidebar.selectbox("Choose Module", [
    "1. Overview & Rules", 
    "2. Population Hierarchy", 
    "3. Monetary System (GRI)", 
    "4. Pricing Simulator", 
    "5. IT vs MIS Engineering",
    "6. Talk to a Survivor"
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
# 3. MONETARY SYSTEM (GRI)
# ─────────────────────────────────────────────────────────────────────────────
elif app_mode == "3. Monetary System (GRI)":
    st.title("🪙 The Gold Reference Index (GRI)")
    st.write("""
    ### Dynamic Value Anchor
    Because physical banknotes have no backing government, the Kingdom uses them as tokens whose exchange value is mapped to gold. To prevent speculation, we align years **2029–2035** directly with historical pre-collapse gold prices from **2001–2007** (London Bullion Market Association data).
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### Calendar Mapping Configuration")
        target_year = st.selectbox("Select Simulation Year", [2029, 2030, 2031, 2032, 2033, 2034, 2035])
        st.session_state["target_year"] = target_year
        reference_year = target_year - 28
        st.success(f"Simulation Year **{target_year}** maps to Reference Year **{reference_year}**")
        
        if target_year == 2032:
            st.info("Notice: 2032 maps to 2004, which are both Leap Years. February 29th aligns perfectly!")
            
    with col2:
        st.write("#### Permanent Exchange Rates (Locked Jan 1, 2001)")
        fx_rates = {
            "Currency Code": ["USD", "EUR", "GBP", "INR", "CAD", "JPY", "AUD", "SGD", "CHF", "CNY", "MYR", "HKD", "BRL", "MXN", "NZD", "NOK", "SEK", "THB", "ZAR", "KRW"],
            "Currency Name": [
                "US Dollar", "Euro (EMU)", "British Pound", "Indian Rupee", "Canadian Dollar",
                "Japanese Yen", "Australian Dollar", "Singapore Dollar", "Swiss Franc", "Chinese Yuan",
                "Malaysian Ringgit", "Hong Kong Dollar", "Brazilian Real", "Mexican Peso", "New Zealand Dollar",
                "Norwegian Krone", "Swedish Krona", "Thai Baht", "South African Rand", "South Korean Won"
            ],
            "Fixed Rate (per USD)": [
                1.0000, 0.9374, 0.6814, 46.5500, 1.5037,
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
        
        # Formatting output
        df_full.index.name = "Date"
        df_display = df_full.reset_index()
        df_display["Date"] = df_display["Date"].dt.strftime('%Y-%m-%d')
        
        st.success("Successfully interpolated 2,556 days of data across all weights!")
        
        # Display sample and download link
        st.write("#### Data Sample (First 20 Days):")
        st.dataframe(df_display.head(20).style.format({
            "Gold Price (USD/oz)": "${:.4f}",
            "Gold Price (USD/g)": "${:.4f}",
            "Gold Price (USD/lb)": "${:.4f}",
            "Gold Price (USD/pawn)": "${:.4f}"
        }))
        
        st.write("#### Data Sample (Last 20 Days):")
        st.dataframe(df_display.tail(20).style.format({
            "Gold Price (USD/oz)": "${:.4f}",
            "Gold Price (USD/g)": "${:.4f}",
            "Gold Price (USD/lb)": "${:.4f}",
            "Gold Price (USD/pawn)": "${:.4f}"
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
# 4. PRICING SIMULATOR
# ─────────────────────────────────────────────────────────────────────────────
elif app_mode == "4. Pricing Simulator":
    st.title("🧮 Algorithmic Pricing Simulator")
    
    st.write("""
    ### The Commodity Pricing Model
    Official prices are computed as: `Price = Base Price * GRI * (W_r * W_s * W_t * W_e)`
    Use the controls below to simulate how local environmental and policy factors scale the price of commodities, and how the Monetary Board can adjust the GRI to keep the basket affordable.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### Input Parameters")
        base_price = st.number_input("Base Commodity Price (INR)", min_value=10.0, max_value=1000.0, value=100.0)
        gri = st.slider("Gold Reference Index (GRI Multiplier)", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
        
        w_r = st.slider("Regional Weight (Wr - e.g. Drought = 1.3)", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
        w_s = st.slider("Seasonal Weight (Ws - e.g. Winter = 1.2)", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
        w_t = st.slider("Kingdom Tax Weight (Wt)", min_value=1.0, max_value=1.5, value=1.0, step=0.05)
        w_e = st.slider("Emergency Weight (We)", min_value=1.0, max_value=2.0, value=1.0, step=0.1)
        
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
                            
                            # Map the discovered Gemini model to LiteLLM configuration for smolagents
                            # e.g., selected_model = "models/gemini-1.5-flash" -> gemini/gemini-1.5-flash
                            lite_model_name = selected_model.replace("models/", "gemini/")
                            
                            # Initialize LiteLLM model using the key
                            agent_model = LiteLLMModel(
                                model_id=lite_model_name,
                                api_key=api_key
                            )

                            # Define tools for the agent to query the system state
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

                            # Create agent instance
                            agent = CodeAgent(
                                tools=[GetGoldPriceTool(), GetPricingFormulaTool()],
                                model=agent_model,
                                additional_authorized_imports=["pandas", "numpy"]
                            )

                            # Build complete instruction payload
                            prompt_with_instructions = (
                                f"You are a survivor speaking to a visitor. Stay in character.\n"
                                f"System Guidelines:\n{system_prompt}\n\n"
                                f"Query: {user_input}"
                            )
                            
                            # Run reasoning loop
                            reply = agent.run(prompt_with_instructions)
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
            st.error(f"Error communicating with Gemini API: {e}")
    else:
        st.info("Please enter your Gemini API Key in the box above to enable conversational simulation.")


