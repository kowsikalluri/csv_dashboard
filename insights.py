# insights.py

import streamlit as st
import pandas as pd
import plotly.express as px

def generate_report(df):
    st.markdown("### 🧠 Quick Insights")

    # Dataset Overview
    st.markdown("#### 🔹 Dataset Shape")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Data Types
    st.markdown("#### 🔹 Column Types")
    st.write(df.dtypes)

    # Missing Values
    st.markdown("#### 🔹 Missing Values per Column")
    st.write(df.isnull().sum())

    # Descriptive Stats for Numeric Columns
    st.markdown("#### 🔹 Descriptive Statistics")
    st.write(df.describe())

    # Plot: Histogram for numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if numeric_cols:
        selected_col = st.selectbox("📊 Select numeric column to plot histogram", numeric_cols)
        fig = px.histogram(df, x=selected_col, nbins=30, title=f"Distribution of {selected_col}")
        st.plotly_chart(fig, use_container_width=True)

    # Value counts for categorical
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    if cat_cols:
        selected_cat = st.selectbox("📊 Select categorical column to view value counts", cat_cols)
        st.write(df[selected_cat].value_counts())
