import streamlit as st
import pandas as pd
import random

# Title and Description
st.title("Green Finance Optimization Platform")
st.markdown("""
Welcome to the **Green Finance Optimization Platform**! 
This platform evaluates, prioritizes, and optimizes green finance investments to help financial institutions make sustainable and impactful decisions.

**Note:** The dataset used here is a small dataset for the time being. We are working on a larger dataset with more features for a greater impact and we don't want to rush on the process of making a good dataset which directly impacts the qaulity..
""")

# Load Dataset

def load_data():
    # Generate mock data
    project_types = [
        "Solar Farm",
        "Wind Power Plant",
        "Reforestation Initiative",
        "Urban Tree Plantation",
        "Biofuel Facility"
    ]
    data = []
    for _ in range(20):
        project = random.choice(project_types)
        carbon_reduction = random.randint(30, 100)  # in tons/year
        social_impact_score = random.randint(7, 10)  # 1-10 scale
        cost = random.randint(50000, 500000)  # in USD
        roi = round(random.uniform(5, 15), 2)  # in percentage
        data.append([project, carbon_reduction, social_impact_score, cost, roi])
    columns = ["Project Name", "Carbon Reduction (tons)", "Social Impact Score", "Cost (USD)", "ROI (%)"]
    df = pd.DataFrame(data, columns=columns)

    # Calculate ESG Score
    df["ESG Score"] = (
        (0.5 * df["Carbon Reduction (tons)"]) +
        (0.3 * df["Social Impact Score"]) -
        (0.2 * df["Cost (USD)"] / 1000)
    )
    return df

mock_data = load_data()

# Dataset Overview
st.subheader("Dataset Overview")
st.dataframe(mock_data)
st.markdown("""
- **Carbon Reduction:** Measured in tons/year.
- **Social Impact Score:** A score between 1 and 10.
- **Cost:** In USD.
- **ROI:** Return on Investment as a percentage.
- **ESG Score:** Calculated using a formula combining all these metrics.
""")

# Visualizations
st.subheader("Project Rankings")
st.bar_chart(mock_data.set_index("Project Name")["ESG Score"])

# Scenario Analysis
st.subheader("Scenario Analysis")
budget_filter = st.slider("Set a Budget Constraint (in USD)", min_value=50000, max_value=500000, step=50000)
filtered_data = mock_data[mock_data["Cost (USD)"] <= budget_filter]
st.markdown(f"Projects within a budget of **${budget_filter}**:")
st.dataframe(filtered_data)

# Future Enhancements
st.subheader("Future Enhancements")
st.markdown("""
We are actively working on:
- **User Interface and data Collection System** wil add different metrics to cater different investment strategies or even for different investment options and their feature inputs.
- **Incorporating additional data points** like climate metrics, economic data, and project-specific KPIs.
- **Predicting future risks** using advanced AI models.
- **Building a robust optimization engine** for resource allocation.
- **Enhancing the visualization dashboard** for better insights.
""")

# Highlighted Message
st.subheader("Future Dataset")
st.markdown("""
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 1px solid #ddd;">
    <h4 style="color: #007bff; text-align: center;">Sneakpeek of the dataset we are currently working on</h4>
</div>
""", unsafe_allow_html=True)

# Upload and Display CSV
file_path = "green_finance_extended_dataset.csv"  # Replace with your CSV file path
df = pd.read_csv(file_path)

st.dataframe(df)
