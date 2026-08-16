import streamlit as st 
def footer_home():
    logo_url="https://logos.textgiraffe.com/logos/logo-name/Bhavya-designstyle-pastel-m.png"
    st.markdown(f"""
        <div style="margin-top:1.5rem; display:flex;gap:12px; justify-content: center;items-align: center">
        <p> Created with ❤️ by </p>
        <img src='{logo_url}' style='max-height:38px'/>
        </div>
    """, unsafe_allow_html=True)