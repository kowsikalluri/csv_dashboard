import streamlit as st
import pandas as pd
from auto_cleaning import auto_clean
from user_cleaning import user_cleaning_ui
from insights import generate_report
from dashboard import show_dashboard
from ml_model import train_model

st.set_page_config(layout="wide")

st.title("📊 Smart CSV Dashboard Generator")

file = st.file_uploader("📁 Upload a CSV file", type="csv")

if file:
    df = pd.read_csv(file)
    st.subheader("🧾 Raw Data Preview")
    st.dataframe(df.head())

    st.subheader("🧼 Auto Data Cleaning")
    df_clean = auto_clean(df)
    st.dataframe(df_clean.head())

    st.subheader("🛠️ Custom User Cleaning")
    df_custom = user_cleaning_ui(df_clean.copy())

    st.subheader("📈 Dashboard")
    show_dashboard(df_custom)

    st.subheader("📋 Generate Insights Report")
    generate_report(df_custom)

    st.subheader("📥 Download Final Cleaned CSV")

    csv = df_custom.to_csv(index=False).encode('utf-8')
    st.download_button(
    label="📁 Download Cleaned Data as CSV",
    data=csv,
    file_name='cleaned_data.csv',
    mime='text/csv',
)
    if 'df_custom' in locals():
        st.subheader("🤖 ML Prediction on Cleaned Data")
        target_col = st.selectbox("🎯 Select target column to predict", df_custom.columns)

    

    if st.button("Train ML Model"):
        with st.spinner("Training model..."):
            try:
                model, X_test, y_test, y_pred, score, is_classification, class_names = train_model(df_custom, target_col)
                st.success("Model trained successfully!")
                if is_classification:
                    st.write(f"🔍 Accuracy Score: {score:.2f}")
                else:
                    st.write(f"🔍 RMSE (Regression): {score:.2f}")

                # Show prediction sample
                pred_df = pd.DataFrame(X_test)
                pred_df['Actual'] = y_test
                pred_df['Predicted'] = y_pred
                st.dataframe(pred_df.head())

                csv_pred = pred_df.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Download Predictions as CSV", data=csv_pred, file_name='predictions.csv', mime='text/csv')
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
    else:
        st.warning("⚠️ Please upload and clean a CSV file first.")

    

