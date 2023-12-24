import streamlit as st

st.title("All Arithmatic Functions")

st.header("Total - 12")

st.subheader("* plusaint*")
st.markdown("It is a Model-type A function which takes two operasations and add them to one-another , Ex-")
st.code("8 plusaint* 1")
st.code("The output will be - 9")

st.subheader("* plusbint*")
st.markdown("It is a Model-type B function which takes two operasations and add them to one-another and add 1 in the result , Ex-")
st.code("8 plusbint* 1")
st.code("The output will be - 10")

st.subheader("* plusafloat*")
st.markdown("It does the same as 'plusaint*' but the operasations should be a floating point number")

st.subheader("* plusbfloat*")
st.markdown("It does the same as 'plusbint*' but the operasations should be a floating point number")

st.subheader("* plusastr*")
st.markdown("It concatinates two strings \"sentences or words\". Example-")
st.code("hello plusastr* world")
st.code("Output - helloworld")

st.subheader("* subtrAint*")
st.markdown("Subtracts two operasations (It is of Model-type A). Example-")
st.code("7 subtrAint* 4")
st.code("Output - 3")

st.subheader("* subtrBint*")
st.markdown("Subtracts the bigger operasation with the smaller operasation, adds 2 in it and multiplies it by 3 (It is of Model-type B). Example-")
st.code("7 subtrBint* 4")
st.code("Output = -3")

st.subheader("* subtrBfloat*")
st.markdown("Does the same as 'subtrBint' does but the operasations must be floating point number. Example-")
st.code("2.0 subtrBfloat 1.0")
st.code("Output - 3.0")

st.subheader("* subtrAfloat*")
st.markdown("Does the same as 'subtrAint' does but the operasations must be floating point number. Example-")
st.code("2.0 subtrAfloat 1.0")
st.code("Output - 1.0")

st.subheader("* dividedsA*")
st.markdown("Divides the operasations. Example-")
st.code("6 dividedsA 3")
st.code("Output - 2.0")

st.subheader("* dividedsBU*")
st.markdown("Displays quotient and remainder together. Example-")
st.code("8 dividedsBU 2")
st.code("""
        Output -

        4.0
        0
        """)

st.subheader("* %")
st.markdown("Show the remainder")
st.code("9 % 3")
st.code("Output - 0")

st.subheader("And all other python arithmatical operations.")