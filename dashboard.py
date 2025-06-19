import streamlit as st
import plotly.express as px

def show_dashboard(df):
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if len(numeric_cols) < 2:
        st.warning("Need at least two numeric columns for dashboard.")
        return

    x_axis = st.selectbox("📊 Select X-axis", numeric_cols, index=0)
    y_axis = st.selectbox("📊 Select Y-axis", numeric_cols, index=1)

    chart_type = st.radio("Choose chart type", ["Scatter", "Line", "Bar"])

    if chart_type == "Scatter":
        fig = px.scatter(df, x=x_axis, y=y_axis)
    elif chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)
    elif chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis)

    st.plotly_chart(fig, use_container_width=True)
