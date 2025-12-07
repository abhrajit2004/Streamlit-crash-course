import streamlit as st

st.title('My Second Streamlit App')  
st.subheader('Brewed with Streamlit')
st.text('Welcome to my second Streamlit application!')
st.write('This is a simple app to demonstrate Streamlit capabilities.')

lang = st.selectbox('Your fav programming language', ["C", "C++", "Java", "Python", "JavaScript"])

st.write(f"You selected {lang} as your favorite language!")
st.success('Your language has been selected. Enjoy!')