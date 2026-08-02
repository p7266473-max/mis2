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

/* Hide Streamlit bottom footer and viewer/host badges */
footer {visibility: hidden !important; display: none !important;}
[data-testid="stFooter"] {visibility: hidden !important; display: none !important;}
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
        '.stActionButton', 'button[title*="Streamlit"]', 'div[class*="StatusWidget"]'
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

def show_survivor():
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

            # Build detailed prompt context
            sim_year_ctx = st.session_state.get("target_year", 2029)
            ref_year_ctx = sim_year_ctx - 28
            
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
                st.session_state.messages.append({"role": "user", "content": user_input})
                with st.chat_message("user"):
                    st.write(user_input)

                with st.chat_message("assistant"):
                    with st.spinner("The survivor is replying..."):
                        try:
                            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                            selected_model = next((m for m in models if "gemini-1.5-flash" in m), None)
                            if not selected_model:
                                selected_model = models[0] if models else "models/gemini-1.5-flash-latest"
                        except Exception:
                            selected_model = "models/gemini-1.5-flash-latest"

                        if not selected_model.startswith("models/"):
                            selected_model = f"models/{selected_model}"

                        history_payload = []
                        for msg in st.session_state.messages[:-1]:
                            role_map = "user" if msg["role"] == "user" else "model"
                            history_payload.append({
                                "role": role_map,
                                "parts": [msg["content"]]
                            })

                        # Implement smolagents integration
                        try:
                            from smolagents import CodeAgent, Tool, LiteLLMModel
                            import io
                            import contextlib
                            
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
                            
                            log_capture = io.StringIO()
                            with contextlib.redirect_stdout(log_capture):
                                reply = st.session_state.code_agent.run(prompt_with_instructions)
                            
                            agent_logs = log_capture.getvalue()
                            
                            if agent_logs.strip():
                                with st.expander("🕵️ Inspect Survivor's Agentic Thought Process"):
                                    st.text(agent_logs)
                                    
                            st.write(reply)

                        except Exception as agent_error:
                            model = genai.GenerativeModel(
                                model_name=selected_model,
                                system_instruction=system_prompt
                            )
                            chat = model.start_chat(history=history_payload)
                            response = chat.send_message(
                                user_input,
                                generation_config={"temperature": 0.7, "max_output_tokens": 300}
                            )
                            reply = response.text
                            st.write(reply)
                
                st.session_state.messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            st.error("⚠️ The Mesh Network is struggling to sync with the central database. The solar grids might be undergoing scheduled runtime downtime. Please try your query again when the signal stabilizes.")
    else:
        st.info("Please enter your Gemini API Key in the box above to enable conversational simulation.")
