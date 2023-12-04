import streamlit as st
import streamlit.components.v1 as components


# [theme]
# base="dark"
# backgroundColor="#100543"

st.title("Thing I'll never use")
st.write("---")

st.sidebar.title("**Select a Page**")
yup = st.sidebar.radio("", ["**Homepage**", 2023, 2024])

if type(yup) == str:
    
    summit_style = " style=\'height: 350px;width: auto;border: 5px solid #fcb904;border-radius: 100px;margin-bottom: 50px;margin-top: 20px;\' "
    st.markdown ("<img src='https://miro.medium.com/v2/resize:fit:1144/1*QjOkG7i-wkqI2-lnJf7B_g.gif'  " + summit_style +  " />", unsafe_allow_html=True)
    
    
    expander = st.expander("**Everyday Use Functions**")
    
    function_list = [ '<a style="text-decoration: none;" href="https://gatech.instructure.com/">Canvas</a>',
                     '<a style="text-decoration: none;" href="https://portal.lawn.gatech.edu/devices">Ps4 Wifi Reset</a>',
                     '<a style="text-decoration: none;" href="https://portal.lawn.gatech.edu/devices">Notability</a>',
                     '<a style="text-decoration: none;" href="https://outlook.office.com/mail/deleteditems">Outlook</a>']
    
    for function in function_list:
        expander.markdown(function,unsafe_allow_html=True)
        
else:
    
    if yup == 2023:
        st.write("I'm Lazy, Goodluck")
    
