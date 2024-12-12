import streamlit as st

# App Title
st.title("StatQuestJourney Hub Salary Management System")
st.markdown(
    "<h3 style='color: skyblue; text-align: center;'>Salary Management Made Simple</h3>",
    unsafe_allow_html=True
)

# Input Total Revenue
total_revenue = st.number_input("Enter Total Revenue (KES):", min_value=0, step=1000)

# Default Percentages
savings_percent = 25
tax_percent = 16
rent_and_charges = 9000
roles = {
    "Data Scientist": 27,
    "Administrator": 24,
    "Marketing Specialist": 20,
    "CEO": 15,
    "Operational Expenses": 14
}

# Calculate Salaries and Other Amounts
if st.button("Generate Salaries"):
    if total_revenue > 0:
        # Calculate Savings and Tax
        savings = (savings_percent / 100) * total_revenue
        tax = (tax_percent / 100) * total_revenue

        # Remaining after savings and tax
        remaining_after_tax_savings = total_revenue - savings - tax - rent_and_charges

        if remaining_after_tax_savings < 0:
            st.error("The revenue is insufficient to cover basic expenses.")
        else:
            # Calculate salaries for each role
            st.markdown(
                "<h4 style='color: skyblue; text-align: center;'>Generated Salary Breakdown</h4>",
                unsafe_allow_html=True
            )

            st.write(f"**Savings (KES):** {savings:.2f}")
            st.write(f"**Tax (KES):** {tax:.2f}")
            st.write(f"**Rent and Charges (KES):** {rent_and_charges:.2f}")
            st.write(f"**Remaining After Deductions (KES):** {remaining_after_tax_savings:.2f}")

            for role, percent in roles.items():
                salary = (percent / 100) * remaining_after_tax_savings
                st.write(f"**{role}:** {salary:.2f} KES")
    else:
        st.warning("Please enter a valid total revenue.")
