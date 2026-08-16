import streamlit as st 
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout,style_background_home


def home_screen():
    header_home()
    style_base_layout()
    style_background_home()

    col1,col2=st.columns(2)
    with col1:
        st.markdown(
        "<h3 style='color: black; font-size: 28px; font-weight: 800; margin-bottom: 5px;'>I'm Teacher</h3>",
        unsafe_allow_html=True
        )

        st.image("https://static.vecteezy.com/system/resources/previews/053/086/931/non_2x/teacher-clipart-with-teaching-pose-illustration-free-vector.jpg",width=200)
        if st.button('Teacher Portal'):
            st.session_state['login_type']='teacher'
            st.rerun()
    with col2:
        st.markdown(
        "<h3 style='color: black; font-size: 28px; font-weight: 800; margin-bottom: 5px;'>I'm Student</h3>",
        unsafe_allow_html=True
        )

        st.image("https://static.vecteezy.com/system/resources/thumbnails/045/546/274/small/boy-wear-graduation-hat-and-holding-book-3d-free-png.png",width=120)
        if st.button('Student Portal'):
            st.session_state['login_type']='student'
            st.rerun()
    footer_home()