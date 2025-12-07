import streamlit as st

st.title('My First Streamlit App')  
st.subheader('Brewed with Streamlit')
st.text('Welcome to my first Streamlit application!')
st.write('This is a simple app to demonstrate Streamlit capabilities.')

chai = st.selectbox('Your fav chai', ["Masala Chai", "Adrak Chai", "Elaichi Chai", "Kesar Chai"])

st.write(f"You selected {chai} as your favorite chai!")
st.success('Your chai has been brewed. Enjoy!')