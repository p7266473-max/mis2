import streamlit as st
import pandas as pd

# Standardized commodity item catalogs for all sectors
COMMODITY_CATALOG = {
    "Rice / Flour": {
        "Rice (20 kg)": 320.00,
        "Flour (5 kg)": 65.00
    },
    "Spices": {
        "Garlic (Fresh) (1.2 kg)": 37.15,
        "Ginger (Fresh) (1.2 kg)": 46.44,
        "Chili Powder (Morich) (1.0 kg)": 61.92,
        "Cumin (Jeera) (250g)": 23.22,
        "Coriander Powder (Dhaniya) (250g)": 11.61,
        "Turmeric Powder (Holud) (300g)": 16.25,
        "Black Pepper (Gol Morich) (50g)": 11.61,
        "Cardamom (Elachi) (50g)": 23.22,
        "Cinnamon (Daruchini) (50g)": 6.19,
        "Cloves (Labango) (25g)": 7.74
    },
    "Vegetables": {
        "Potato (15 kg)": 116.11,
        "Onion (10 kg)": 139.33,
        "Pumpkin (6 kg)": 46.44,
        "Cabbage (5 kg)": 46.44,
        "Eggplant (5 kg)": 69.67,
        "Carrot (4 kg)": 61.93,
        "Beetroot (2 kg)": 34.06,
        "Tomato (6 kg)": 92.89,
        "Lady Fingers (4 kg)": 49.54,
        "Radish (3 kg)": 27.87
    },
    "Fruits": {
        "Apples (15 kg)": 450.00,
        "Oranges (12 kg)": 180.00,
        "Papaya (8 kg)": 96.00,
        "Banana (per pc)": 4.00,
        "Jackfruit (per kg)": 10.00,
        "Mango (per kg)": 15.00,
        "Pineapple (per kg)": 15.00,
        "Watermelon (per kg)": 6.00,
        "Guava (per kg)": 10.00,
        "Orange (per kg)": 15.00,
        "Lemon (per kg)": 10.00
    },
    "Meat": {
        "Chicken (10 kg)": 600.00,
        "Fish (6 kg)": 300.00,
        "Lamb (4 kg)": 400.00,
        "Tilapia (per kg)": 50.00,
        "Catfish (per kg)": 40.00,
        "Carp (per kg)": 35.00,
        "Milkfish (per kg)": 35.00,
        "Snakehead (per kg)": 60.00
    },
    "Clothes": {
        "Husband Shirt (Monthly portion)": 67.00,
        "Wife Skirt/Dress (Monthly portion)": 67.00,
        "Grandfather Panjabi/Shirt (Monthly portion)": 50.00,
        "Grandmother Saree/Dress (Monthly portion)": 50.00,
        "Boy T-shirt + Shorts (Monthly portion)": 33.00,
        "Girl Dress (Monthly portion)": 33.00
    },
    "Furniture / Utensils": {
        "Chairs (6 pcs)": 60.00,
        "Table (1 pc)": 40.00,
        "Bed (2 pcs)": 160.00,
        "Fan (2 pcs)": 120.00
    },
    "Fuel": {
        "Petrol (12 ltr)": 169.19,
        "Diesel (9 ltr)": 188.30,
        "Kerosene (10 ltr)": 141.00,
        "Mustard Oil (2 ltr)": 145.54,
        "Raw Cow Fat (2 kg)": 36.39,
        "Raw Sheep Fat (2 kg)": 54.58
    },
    "Electricity": {
        "Electricity (250 kWh @ ₹8/unit)": 2000.00
    }
}

def show_groups():
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
            "members": ["Thanishvel Mogam", "Jeremy Mattews Thomas", "Ajwaad Mahbub Karim", "Intan Syazana"],
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
            "lead": "Fahim Sahriar Punno",
            "members": ["Fahim Sahriar Punno", "Md Rifat", "Eithi Nur Jahan", "Zannat Zaman", "Joy Chandra Das"],
            "icon": "🌶️",
            "resource": "Imported & Local Herb/Spice Logistics"
        },
        {
            "id": 4,
            "name": "Group 4: Vegetables",
            "sector": "Vegetables",
            "lead": "MOHAMMAD FARHAD HASAN NILOY",
            "members": ["HIMANGSHU RAJ MALO", "SHAWON SORIF", "HASAN MD SAKIB", "MD SAGOR MOLLAH", "MOHAMMAD FARHAD HASAN NILOY"],
            "icon": "🥦",
            "resource": "Perishable Crop Harvests & Cold Storage Logs"
        },
        {
            "id": 5,
            "name": "Group 5: Fruits",
            "sector": "Fruits",
            "lead": "Jishan Ahmed Himel",
            "members": ["Akter Khusbu", "Shahik khan Himel", "MD Rimon", "Jishan Ahmed Himel", "Biraj Sarker"],
            "icon": "🍎",
            "resource": "Orchard Production & Distribution Routing"
        },
        {
            "id": 6,
            "name": "Group 6: Electricity",
            "sector": "Electricity",
            "lead": "Arpita Roy",
            "members": ["Arpita Roy", "Tanvir anwar Ivan", "Rahi Jame UL kawser", "Islam siyam"],
            "icon": "⚡",
            "resource": "Solar Arrays, Battery Banks, & Scheduled Server Downtimes"
        },
        {
            "id": 7,
            "name": "Group 7: Fuel",
            "sector": "Fuel",
            "lead": "MD.Shofiqul Islam",
            "members": ["MD.Shofiqul Islam", "Abu sayed", "Mansur", "Salam", "Utsha"],
            "icon": "⛽",
            "resource": "Generators & Biofuel Reserves Inventory"
        },
        {
            "id": 8,
            "name": "Group 8: Furniture / Utensils",
            "sector": "Furniture / Utensils",
            "lead": "Murad hasan",
            "members": ["Murad hasan", "Abdul Azim", "Wazed", "Tanjil hossain", "Jihad rabbi"],
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
        st.subheader("📝 Draft Your Budget Proposal")
        st.write("Each sector team must draft their proposed resource budget by selecting items below and generating their formal proposal PDF.")
        
        c_prop1, c_prop2 = st.columns([1, 2])
        with c_prop1:
            sector_choice = st.selectbox("Select Your Sector", list(COMMODITY_CATALOG.keys()))
        
        with c_prop2:
            selected_items = st.multiselect(
                f"Select items for {sector_choice}", 
                list(COMMODITY_CATALOG[sector_choice].keys()),
                default=list(COMMODITY_CATALOG[sector_choice].keys())
            )
        
        # All item values are already monthly allocations — simple sum for all sectors
        total_cost = sum([COMMODITY_CATALOG[sector_choice][item] for item in selected_items])
        
        st.markdown(f"### 💰 Monthly Basket Allocation — **{sector_choice}**: **₹{total_cost:,.2f}**")
        
        # Min/max boundaries check (±~20% flex around baseline)
        boundaries = {
            "Rice / Flour":        (308, 462),
            "Spices":              (196, 294),
            "Vegetables":          (547, 821),
            "Fruits":              (581, 871),
            "Meat":                (1064, 1596),
            "Clothes":             (240, 360),
            "Furniture / Utensils":(304, 456),
            "Fuel":                (588, 882),
            "Electricity":         (1600, 2400)
        }
        
        min_b, max_b = boundaries.get(sector_choice, (0, 99999))
        if min_b <= total_cost <= max_b:
            st.success(f"✅ Budget is within allowed bandwidth: **₹{min_b} – ₹{max_b}**")
        else:
            st.warning(f"⚠️ Budget exceeds or is below allowed bandwidth: **₹{min_b} – ₹{max_b}**")
            
        if st.button("Generate Formal Proposal PDF", key="btn_pdf_gen"):
            from fpdf import FPDF
            
            pdf = FPDF()
            pdf.add_page()
            pdf.set_margins(20, 20, 20)
            
            # Header block
            pdf.set_fill_color(15, 23, 42)
            pdf.rect(0, 0, 210, 40, "F")
            
            pdf.ln(5)
            pdf.set_text_color(255, 255, 255)
            pdf.set_font("Helvetica", 'B', 16)
            pdf.cell(170, 10, "SURVIVORS' NATION - CABINET OF MINISTERS", ln=True, align='C')
            pdf.set_font("Helvetica", size=11)
            pdf.cell(170, 8, "OFFICIAL ECONOMIC BUDGET PROPOSAL LEDGER", ln=True, align='C')
            
            # Body
            pdf.set_text_color(15, 23, 42)
            pdf.ln(15)
            pdf.set_font("Helvetica", 'B', 13)
            pdf.cell(170, 10, f"Sector Proposal: {sector_choice}", ln=True)
            pdf.line(20, pdf.get_y(), 190, pdf.get_y())
            pdf.ln(5)
            
            pdf.set_font("Helvetica", size=10)
            pdf.cell(100, 8, "Monthly Allocation Line Items", 'B')
            pdf.cell(70, 8, "Monthly Cost (INR)", 'B', ln=True, align='R')
            
            pdf.set_font("Helvetica", size=9)
            for item in selected_items:
                cost = COMMODITY_CATALOG[sector_choice][item]
                pdf.cell(100, 8, f"- {item}")
                pdf.cell(70, 8, f"INR {cost:,.2f}", ln=True, align='R')
                
            pdf.ln(5)
            pdf.set_font("Helvetica", 'B', 11)
            pdf.cell(100, 10, "Total Monthly Basket Allocation", 'T')
            pdf.cell(70, 10, f"INR {total_cost:,.2f}", 'T', ln=True, align='R')
            
            pdf.ln(10)
            pdf.set_font("Helvetica", 'I', 8)
            pdf.multi_cell(170, 5, "By downloading this ledger, the designated sector team formally submits this request to Group 1 (Monetary Board). Audits will be conducted offline via wireless mesh sync nodes.")
            
            # Signatures
            pdf.ln(15)
            pdf.set_font("Helvetica", 'B', 10)
            pdf.cell(85, 10, "Sector Lead Representative:")
            pdf.cell(85, 10, "Monetary Board Representative:", ln=True)
            pdf.ln(5)
            pdf.cell(85, 5, "___________________________")
            pdf.cell(85, 5, "___________________________", ln=True)
            
            pdf_output = "proposal.pdf"
            pdf.output(pdf_output)
            
            with open(pdf_output, "rb") as f:
                st.download_button("Download Proposal PDF File", f, file_name=f"Budget_Proposal_{sector_choice.replace(' ', '')}.pdf")

        st.write("---")
        st.subheader("📊 The Kingdom’s Operational Matrix — Validated Basket Architecture (Family of 6)")
        st.write("""
        This matrix reflects the **validated ₹6,000 monthly basket** for a family of six, grounded in 2001 Tamil Nadu market prices.
        Each group's sector budget is locked to the baseline. The Monetary Board (Group 1) audits all allocations.
        """)
        
        # Validated basket matrix — all 9 sectors sum to exactly Rs.6,785.63
        matrix_data = {
            "Sector": [
                "1. Rice / Flour",
                "2. Spices",
                "3. Vegetables",
                "4. Fruits",
                "5. Meat",
                "6. Clothes",
                "7. Furniture / Utensils",
                "8. Fuel (Diesel + Oil)",
                "9. Electricity"
            ],
            "Assigned Group": [
                "Group 2 — Rice/Flour",
                "Group 3 — Spices",
                "Group 4 — Vegetables",
                "Group 5 — Fruits",
                "Group 10 — Meat",
                "Group 9 — Clothes",
                "Group 8 — Furniture",
                "Group 7 — Fuel",
                "Group 6 — Electricity"
            ],
            "Baseline (₹/month)": [385.00, 245.34, 684.29, 726.00, 1330.00, 300.00, 380.00, 735.00, 2000.00],
            "Min Bandwidth (₹)": [308.00, 196.27, 547.43, 580.80, 1064.00, 240.00, 304.00, 588.00, 1600.00],
            "Max Bandwidth (₹)": [462.00, 294.41, 821.15, 871.20, 1596.00, 360.00, 456.00, 882.00, 2400.00]
        }
        df_matrix = pd.DataFrame(matrix_data)
        st.table(df_matrix)
        
        # Grand total verification
        grand_total = sum(matrix_data["Baseline (₹/month)"])
        if abs(grand_total - 6785.63) < 0.1:
            st.success(f"✅ **Basket Total Verified: ₹{grand_total:,.2f} / ₹6,785.63 — Architecture Locked.**")
        else:
            st.error(f"❌ Basket total mismatch: ₹{grand_total:,.2f} ≠ ₹6,785.63. Check sector allocations!")
        
        st.caption("""
        *Baseline prices are anchored to 2001 post-apocalyptic base pricing data. 
        Min/Max Bandwidth = ±20% flex for regional and seasonal GRI adjustments. 
        Group 1 (Consolidation/Monetary Board) does not hold a commodity sector — they audit and approve all 9 proposals.
        """)

        # Interactive Live Budget Governor
        st.write("---")
        st.subheader("🎮 Live Budget Governor")
        st.info("💡 **Monetary Board Challenge:** Group 1 (Consolidation) must audit and input requests from the other 9 groups. The total combined budget must equal exactly **₹6,785.63** to initialize the simulation!")
        
        bg_col1, bg_col2 = st.columns(2)
        with bg_col1:
            st.write("##### Input Proposed Budgets")
            b_g2 = st.slider("1. Rice / Flour (Group 2) [308.00 - 462.00]", min_value=0.0, max_value=1000.0, value=385.00, step=1.0, key="gov_b_g2")
            b_g3 = st.slider("2. Spices (Group 3) [196.27 - 294.41]", min_value=0.0, max_value=1000.0, value=245.34, step=0.01, key="gov_b_g3")
            b_g4 = st.slider("3. Vegetables (Group 4) [547.43 - 821.15]", min_value=0.0, max_value=2000.0, value=684.29, step=0.01, key="gov_b_g4")
            b_g5 = st.slider("4. Fruits (Group 5) [580.80 - 871.20]", min_value=0.0, max_value=2000.0, value=726.00, step=1.0, key="gov_b_g5")
            b_g10 = st.slider("5. Proteins (Meat) (Group 10) [1064.00 - 1596.00]", min_value=0.0, max_value=3000.0, value=1330.00, step=1.0, key="gov_b_g10")
        with bg_col2:
            st.write("##### Input Proposed Budgets (Cont.)")
            b_g9 = st.slider("6. Clothes (Group 9) [240.00 - 360.00]", min_value=0.0, max_value=1000.0, value=300.00, step=1.0, key="gov_b_g9")
            b_g8 = st.slider("7. Furniture / Utensils (Group 8) [304.00 - 456.00]", min_value=0.0, max_value=1000.0, value=380.00, step=1.0, key="gov_b_g8")
            b_g7 = st.slider("8. Fuel (Group 7) [588.00 - 882.00]", min_value=0.0, max_value=2000.0, value=735.00, step=1.0, key="gov_b_g7")
            b_g6 = st.slider("9. Electricity (Group 6) [1600.00 - 2400.00]", min_value=0.0, max_value=4000.0, value=2000.00, step=5.0, key="gov_b_g6")

        total_proposed = b_g2 + b_g3 + b_g4 + b_g5 + b_g10 + b_g9 + b_g8 + b_g7 + b_g6
        
        # Display progress and validation status
        st.write("### Total Proposed Budget Balance")
        if abs(total_proposed - 6785.63) < 0.5:
            st.success(f"🎉 **Perfect Balance achieved: ₹{total_proposed:,.2f} / ₹6,785.63!**")
            st.balloons()
            st.markdown("""
            ### 🚀 Simulation Initialized!
            Cabinet Appointments are officially locked. High Command Node Online.
            """)
        elif total_proposed > 6785.63:
            st.error(f"❌ **Over-Budget: ₹{total_proposed:,.2f} / ₹6,785.63** (Surplus of ₹{total_proposed - 6785.63:.2f}). Group 1 must enforce budget cuts!")
        else:
            st.warning(f"⚠️ **Under-Budget: ₹{total_proposed:,.2f} / ₹6,785.63** (Deficit of ₹{6785.63 - total_proposed:.2f}). Allocate remaining funds to reserves or sectors.")
