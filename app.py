import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page title
st.set_page_config(page_title="Simple Data Dashboard")
st.title("📊 Simple Python Web App")

# Sidebar for user input
st.sidebar.header("Settings")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# Logic to load data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    # Default sample data
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.info("Showing sample data. Upload a CSV in the sidebar to use your own!")

# Display Data Table
st.subheader("Data Preview")
st.dataframe(df.head())

# Visualize Data
st.subheader("Quick Visualization")
column_to_plot = st.selectbox("Select column to visualize", df.columns)
fig = px.histogram(df, x=column_to_plot, title=f"Distribution of {column_to_plot}")
st.plotly_chart(fig)