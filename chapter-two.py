import streamlit as st

st.title('Chai Maker App')  

if st.button("Make Chai"):
    st.success("Your chai is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai!")

tea_type = st.radio("Select your chai base:", ["Milk", "Water", "Almond Milk"])
st.write(f"You selected {tea_type} as your chai base.")

flavor = st.selectbox("Choose a flavor:", ["Ginger", "Cardamom", "Saffron", "Tulsi"])
st.write(f"You selected {flavor} as your flavor.")

sugar = st.slider("Select sugar level (in spoons):", 0, 5, 4)
st.write(f"You selected {sugar} spoons as your sugar level.")

cups = st.number_input("How many cups of chai would you like?", min_value=1, max_value=10, step=1)
st.write(f"You selected {cups} cups.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Your chai will be ready soon.")

dob = st.date_input("Select your date of birth:","today","1980-01-01","2010-12-31")
st.write(f"Your date of birth is: {dob}")