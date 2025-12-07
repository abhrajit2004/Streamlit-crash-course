import streamlit as st

st.title('Chai Taste Poll')  

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/5946612/pexels-photo-5946612.jpeg", width=150)
    vote1 = st.button("Vote for Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/6962415/pexels-photo-6962415.jpeg", width=250)
    vote2 = st.button("Vote for Adrak Chai")

if vote1:
    st.success("Thanks for voting Masala Chai!")

elif vote2:
    st.success("Thanks for voting Adrak Chai!")

name = st.sidebar.text_input("Enter your name to record your vote:")
tea = st.sidebar.selectbox("Select your favorite chai type:", ["Masala Chai", "Adrak Chai"])

# st.sidebar.write(f"Voter Name: {name}")
st.write(f"Voter Name: {name}")
st.write(f"Favorite Chai Type: {tea}")

with st.expander("Show chai making instructions"):
    st.write("""
    1. Boil water/milk in a pot.
    2. Add tea leaves and let it simmer.
    3. Add spices like cardamom, ginger, and cinnamon for masala chai.
    4. Strain the tea into cups.
    5. Add sugar to taste and enjoy your chai!
""")


st.markdown('### Thank you for participating in the Chai Taste Poll!')
st.markdown('> Your feedback helps us brew better chai! ☕')