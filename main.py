import streamlit as st

name=st.text_input("enter your name:")
father_name=st.text_input("enter your father name:")
address=st.text_area("enter your address:")
classes=st.selectbox("select your class:",[1,2,3,4,5,6,7,8,9,10])
button=st.button("submit")
if button:
    st.markdown(f"""Name: {name}
                    Father Name: {father_name}
                    Address: {address}
                    Classes: {classes}""")


