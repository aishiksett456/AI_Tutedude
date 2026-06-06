import streamlit as st

st.title("Simple Sales Dashboard")
st.subheader("The dashboard is related to sales")

m=["January", "February", "March", "April"]
sm=st.selectbox("Select a month from the list: ",m)
st.metric(label="Selected Month is: ", value=sm)

sales = {"January":1200,"February":1500,"March":900,"April":2000}
st.bar_chart(list(sales.values()))