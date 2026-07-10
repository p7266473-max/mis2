import streamlit as st
import pandas as pd

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
