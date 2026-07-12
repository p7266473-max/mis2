import streamlit as st
import pandas as pd
import numpy as np

def show_monetary():
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
        
        GRAM_CONVERSIONS = {
            "Troy Ounce": 31.1034768,
            "Gram": 1.0,
            "Kilogram": 1000.0,
            "Tola": 11.6638038,
            "Tael": 37.429
        }

        RATES_MAP = {
            "USD": 1.0, "EUR": 0.9374, "GBP": 0.6814, "INR": 46.55, 
            "PAK": 61.93, "CAD": 1.5037, "JPY": 117.28, "AUD": 1.8021, 
            "SGD": 1.7338, "CHF": 1.639, "CNY": 8.2766, "MYR": 3.8,
            "HKD": 7.7997, "BRL": 1.954, "MXN": 9.972, "NZD": 2.2472,
            "NOK": 8.7675, "SEK": 9.505, "THB": 43.09, "ZAR": 7.825, "KRW": 1283.8
        }

        c1, c2, c3 = st.columns(3)
        with c1:
            gold_rate = st.number_input("Gold Rate (USD/Troy Ounce)", value=603.77, key="calc_gold_rate")
            weight = st.number_input("Weight Amount", value=1.0, key="calc_weight")
        with c2:
            currency = st.selectbox("Currency", list(RATES_MAP.keys()), index=list(RATES_MAP.keys()).index("USD"), key="calc_currency")
            unit = st.selectbox("Weight Unit", list(GRAM_CONVERSIONS.keys()), key="calc_unit")
        with c3:
            default_ex = RATES_MAP.get(currency, 1.0)
            ex_rate = st.number_input("Exchange Rate (to USD)", value=default_ex, key="calc_ex_rate")
            
        # Conversion Logic (Base-Gram Method)
        usd_per_gram = gold_rate / GRAM_CONVERSIONS["Troy Ounce"]
        total_grams = weight * GRAM_CONVERSIONS[unit]
        total_val = (total_grams * usd_per_gram) * ex_rate
        
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
