import streamlit as st 


def style_background_home():
    st.markdown("""
    <style>
            .stApp{
            background:#5865F2 !important;
            }

            
            .stApp div[data-testid="stColumn"] {
            display: flex;
            justify-content: center;
            }


            .stApp div[data-testid="stColumn"] > div {
            background-color: #E0E3FF !important;
            width: 50% !important;
            min-height: 100px !important;
            max-height: 370px !important;
            padding: 1.2rem !important;
            border-radius: 3.5rem !important;
            box-sizing: border-box !important;
            overflow: hidden !important;
            }
    </style>

    """,unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
    <style>
            .stApp{
            background:#EOE3FF !important;
            }
    </style>

    """,unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
    
    /* Hide top bar of streamlit */
        #MainMenu,footer,header{
        visibility: hidden;
        }


        .block-container{
        padding-top:1.5rem !important;
        }



        h1{
            font-family:'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height:1.1 !important;
            margin_bottom:0rem !important;      
        }

        h2{
            font-family:'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height:1.1 !important;
            margin_bottom:0rem !important;
        
        }
        h3,h4,p{
        font-family:'Outfit',sans-serif;
        }

        button{
            border-radius: 1.5rem !important;
            background:#5865F2 !important;
            color: white !important ;
            padding : 10px 20px !important;
            border: none !important;
            transition:transform 0.25s ease-in-out !important;
            }
        button[kind="secondary"]{
            border-radius: 1.5rem !important;
            background:#EB459E !important;
            color: white !important ;
            padding : 10px 20px !important;
            border: none !important;
            transition:transform 0.25s ease-in-out !important;
            } 
        button[kind="tertiary"]{
            border-radius: 1.5rem !important;
            background: black !important;
            color: white !important ;
            padding : 10px 20px !important;
            border:none !important;
            transition:transform 0.25s ease-in-out !important;
            } 
        button:hover {
            transform: scale(1.05) !important;
        }
    </style>

    """,unsafe_allow_html=True)
def style_teacher_auth():
    st.markdown("""
    <style>
            .stApp{
            background:#20233A !important;
            }

            .st-key-teacher_auth_card {
            background-color: #F3F1FC !important;
            width: 55% !important;
            margin: 2rem auto !important;
            padding: 2.5rem 3rem !important;
            border-radius: 3.5rem !important;
            box-sizing: border-box !important;
            }

            .st-key-teacher_auth_card h3 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2.4rem !important;
            font-weight: 800 !important;
            text-align: left !important;
            color: #111111 !important;
            margin-bottom: 1.8rem !important;
            }

            .st-key-teacher_auth_card label p {
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            color: #111111 !important;
            }

            .st-key-teacher_auth_card div[data-testid="stTextInput"] input {
            background-color: #FFFFFF !important;
            color: #111111 !important;
            border: 1.5px solid #B8DEB8 !important;
            border-radius: 0.9rem !important;
            padding: 0.75rem 1rem !important;
            font-size: 0.95rem !important;
            }

            .st-key-teacher_auth_card hr {
            border: none !important;
            border-top: 1.5px solid #D6D3F0 !important;
            margin: 1.5rem 0 !important;
            }
    </style>

    """,unsafe_allow_html=True)