import streamlit as st
import pandas as pd
st.title("Price Calculator")
p=st.number_input("Enter product price:")
d=st.slider("Select discount(%): ", 0, 50, 10)
b=st.button("Click here for Final Price")
if b:
	fp=p-((p*d)/100.00)
	st.write("Final Price: ",fp)
	st.write("In Tabular Format:\n")
	cdf = pd.DataFrame({"Before": [p],"After": [fp]})
	st.table(cdf)