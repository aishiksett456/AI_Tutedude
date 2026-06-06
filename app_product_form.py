import streamlit as st

st.title("Product Form")
categories = ["Foods","NBDC","Agarbatti","Matches", "Personal Care Products"]

pn = st.sidebar.text_input("Enter the product name: ")
cat = st.sidebar.selectbox("Select category: ", categories)
p = st.sidebar.number_input("Enter price: ")
but=st.sidebar.button("Add Product")

if but:
	st.write("Form has been submitted")
	st.write("\nProduct details submitted are:\n")
	st.write("Product Name:", pn)
	st.write("\nCategory:", cat)
	st.write("\nPrice:", p)