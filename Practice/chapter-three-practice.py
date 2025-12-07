import streamlit as st

st.title('Programming Language Poll') 
st.write('Vote for your favorite programming language!') 

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.header("C")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/C_Programming_Language.svg/1853px-C_Programming_Language.svg.png",width=100, use_container_width=False)
    vote1 = st.button("Vote for C")

with col2:
    st.header("C++")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/1067px-ISO_C%2B%2B_Logo.svg.png", width=100, use_container_width=False)
    vote2 = st.button("Vote for C++")

with col3:
    st.header("JavaScript")
    st.image("https://i0.wp.com/blog.lewagon.com/wp-content/uploads/2023/07/javascript-g065129b6c_1280.png?fit=800%2C800&ssl=1", width=100, use_container_width=False)
    vote3 = st.button("Vote for JavaScript")

with col2:
    st.header("Python")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png", width=100, use_container_width=False)
    vote4 = st.button("Vote for Python")

if vote1:
    st.success("Thanks for voting C!")

elif vote2:
    st.success("Thanks for voting C++!")

elif vote3:
    st.success("Thanks for voting JavaScript!")

elif vote4:
    st.success("Thanks for voting Python!")