import streamlit as st
st.title("Welcome to Streamlit!")
inp=st.text_input("Enter your Name: ")
gm=st.button("Greet Me")
if gm:
	st.write("Hello,",inp,"!")