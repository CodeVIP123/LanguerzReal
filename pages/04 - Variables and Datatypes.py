import streamlit as st

st.title("Variables and Datatypes")
st.header("Variables")
st.markdown("Variables are the storage blocks in the memory. There are a certain rules to define a variable-\n")
st.markdown("* No whitespaces! Instead underscores (_)")
st.markdown("The syntax of defining a variable is-\n")
st.code("<variable_name> = <value>", "python")

st.header("Datatypes")
st.markdown("While defining a variable, you must put the type of the data to be putten. The datatypes available is-\n")
st.markdown("* int - whole numbers\n")
st.markdown("* float - floating point numbers\n")
st.markdown("* list - a list of items starting with []. Example- var list a = [one,two,three]\n")
st.markdown("* dict - a key-value pairs. Example - var dict a = \{\"key\": \"value\"\}\n")
st.markdown("* str - a literal of text\n")