import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file = st.file_uploader("Upload your chai sales CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.header("Sales Data")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    cities = df["City"].unique()
    selected_city = st.selectbox("Select City", cities)
    filtered_data = df[df["City"] == selected_city]
    st.dataframe(filtered_data)