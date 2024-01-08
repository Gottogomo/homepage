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
                     '<a style="text-decoration: none;" href="https://outlook.office.com/mail/deleteditems">Outlook</a>',
                     '<a style="text-decoration: none;" href="https://share.streamlit.io/">Edit This</a>']
    
    for function in function_list:
        expander.markdown(function,unsafe_allow_html=True)
        
else:
    
    if yup == 2023:
        st.write("I'm Lazy, Goodluck Bro")

    if yup == 2024:
        with st.expander("**Classes**",True):
            class_choice = st.radio("",["ECE 2026","ECE 2020","PHYS 2212","MATH 2552"])
        st.write("---")
        # st.markdown('<a style="text-decoration: none;" href="">Name</a>',unsafe_allow_html=True)


        if (class_choice == "ECE 2026") :
            st.markdown('<a style="text-decoration: none;" href="https://gatech.instructure.com/courses/355166">ECE 2026-A Canvas</a>',unsafe_allow_html=True)
            st.markdown('<a style="text-decoration: none;" href="https://gatech.instructure.com/courses/355252">ECE 2026-L01 Canvas</a>',unsafe_allow_html=True)

        elif (class_choice == "ECE 2020") :
            st.markdown('<a style="text-decoration: none;" href="https://gatech.instructure.com/courses/359986">ECE 2020 Canvas</a>',unsafe_allow_html=True)

        elif (class_choice == "PHYS 2212") :
            st.markdown('<a style="text-decoration: none;" href="https://gatech.instructure.com/courses/362324/assignments/syllabus">PHYS 2211 Canvas</a>',unsafe_allow_html=True)
            st.markdown('<a style="text-decoration: none;" href="https://participant.turningtechnologies.com/en/join">Point Solutions</a>',unsafe_allow_html=True)
            st.markdown('<a style="text-decoration: none;" href="https://gatech.instructure.com/courses/362324/files/folder/GPS%20-%20Group%20Problem%20Solving">GPS Files</a>',unsafe_allow_html=True)
            st.markdown('<a style="text-decoration: none;" href="https://gatech.instructure.com/courses/362324/modules">Modules</a>',unsafe_allow_html=True)
            st.markdown('<a style="text-decoration: none;" href="https://edstem.org/us/courses/50353/discussion/">Ed Discussion</a>',unsafe_allow_html=True)
            st.markdown('<a style="text-decoration: none;" href="https://app.perusall.com/courses/intro-physics-ii-spring-2024/_/dashboard/assignments/Fvh4GCtWuNa2eALw5">Pre-Lecture Videos</a>',unsafe_allow_html=True)
            st.markdown('<a style="text-decoration: none;" href="https://www.glowscript.org/#/user/Daiven/folder/MyPrograms/">Glowscript</a>',unsafe_allow_html=True)
            st.markdown('<a style="text-decoration: none;" href="https://gatech.instructure.com/courses/362324/files/folder/Course%20Documents?preview=47159049">Formula Sheet</a>',unsafe_allow_html=True)



        elif (class_choice == "MATH 2552") :
            st.markdown('<a style="text-decoration: none;" href="https://gatech.instructure.com/courses/357546">MATH 2552 Canvas</a>',unsafe_allow_html=True)

    
