import streamlit as st
import pandas as pd

def user_cleaning_ui(df):
    columns = st.multiselect("Select columns to clean manually", df.columns)
    for col in columns:
        st.markdown(f"**{col} Cleaning Options**")
        action = st.selectbox(f"Choose action for {col}", ["None", "Drop NA", "Fill with Mean", "Fill with Mode"])

        if action == "Drop NA":
            df = df.dropna(subset=[col])
        elif action == "Fill with Mean":
            if df[col].dtype in ['float64', 'int64']:
                df[col] = df[col].fillna(df[col].mean())
        elif action == "Fill with Mode":
            df[col] = df[col].fillna(df[col].mode()[0])

    return df
