import streamlit as st

st.title("What are Models, Operasation?")
st.header("Models")
st.markdown("Models are the functions to perform on numbers, variables, strings, dicts etc. These have two types: \n")
st.markdown("* Model-type A\n")
st.markdown("* Model-type B\n")
st.subheader("Model-type A")
st.markdown("Model-type A are functions which performs simple things for example the code given bellow adds 5 and 1\n")
st.code("5 plusaint* 1")
st.markdown("The 'plusaint*' model is of type A")

st.subheader("Model-type B")
st.markdown("Model-type B functions add some new thing to the task performed by model-type A functions for example the code given below subtracts 5 with 7 , adds 2 and multiply it by 3")
st.code("7 subtrBint* 5")
st.markdown("The model 'subtrBint*' is of type B")

st.header("Operasation")
st.markdown("Operasation are the elements on which the model should do it's task for example the code given below divides 9 by 3 by Model-type A-")
st.code("9 dividedsA* 3")
st.markdown("Here, 9 and 3 are the operasations")