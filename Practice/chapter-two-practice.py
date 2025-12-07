import streamlit as st

st.header('Age Calculator App')  
st.subheader("Calculate your age based on your date of birth.")

dob = st.date_input("Select your date of birth:","2010-12-07","1980-01-01","2010-12-31")
birth_year = dob.year
age = 2025 - birth_year
st.success(f"Your current age is {age} years.")