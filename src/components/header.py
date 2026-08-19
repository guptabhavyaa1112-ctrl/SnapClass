import streamlit as st

def header_home(text_color="#E0E3FF"):
    logo_url = "https://snapclass-landing-page-theta.vercel.app/static/img/logo.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="{logo_url}" style="height:100px;" />
            <h1 style="text-align: center; color:{text_color} !important;">SNAP<br>CLASS</h1>
        </div>
    """, unsafe_allow_html=True)