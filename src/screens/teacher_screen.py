import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_teacher_auth
def teacher_screen():
    style_base_layout()
    style_teacher_auth()

    _, home_col = st.columns([4, 1])
    with home_col:
        if st.button('👤 Go back to Home', type='secondary', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    header_home(text_color="#285A45")

    # ---- session state setup (temporary, no DB yet) ----
    if 'teacher_auth_mode' not in st.session_state:
        st.session_state['teacher_auth_mode'] = 'register'
    if 'teachers_db' not in st.session_state:
        st.session_state['teachers_db'] = {}  # placeholder until Supabase is wired in
    if 'teacher_logged_in' not in st.session_state:
        st.session_state['teacher_logged_in'] = None

    # ---- already logged in ----
    if st.session_state['teacher_logged_in']:
        name = st.session_state['teachers_db'][st.session_state['teacher_logged_in']]['name']
        st.markdown(f"<h3>Welcome, {name} 👋</h3>", unsafe_allow_html=True)
        footer_home()
        return

    with st.container(key="teacher_auth_card"):
        if st.session_state['teacher_auth_mode'] == 'register':
            st.markdown("<h3>Register your teacher profile</h3>", unsafe_allow_html=True)

            username = st.text_input('Enter username', placeholder='@abhishek')
            name = st.text_input('Enter name', placeholder='Abhishek Sharma')
            password = st.text_input('Enter password', placeholder='Enter your password', type='password')
            confirm_password = st.text_input('Confirm password', placeholder='Confirm your password', type='password')

            st.markdown("<hr>", unsafe_allow_html=True)

            bcol1, bcol2 = st.columns(2)
            with bcol1:
                register_clicked = st.button('👤 Register Now', type='primary', use_container_width=True)
            with bcol2:
                login_instead = st.button('👤 Login instead', type='secondary', use_container_width=True)

            if register_clicked:
                if not username or not name or not password:
                    st.error('Please fill in all fields.')
                elif password != confirm_password:
                    st.error('Passwords do not match.')
                elif username in st.session_state['teachers_db']:
                    st.error('A teacher with this username already exists.')
                else:
                    st.session_state['teachers_db'][username] = {'name': name, 'password': password}
                    st.success(f'Welcome {name}! Please log in.')
                    st.session_state['teacher_auth_mode'] = 'login'
                    st.rerun()

            if login_instead:
                st.session_state['teacher_auth_mode'] = 'login'
                st.rerun()

        else:
            st.markdown("<h3>Login using password</h3>", unsafe_allow_html=True)

            username = st.text_input('Enter username', placeholder='ananyaroy')
            password = st.text_input('Enter password', placeholder='Enter password', type='password')

            st.markdown("<hr>", unsafe_allow_html=True)

            bcol1, bcol2 = st.columns(2)
            with bcol1:
                login_clicked = st.button('👤 Login', type='secondary', use_container_width=True)
            with bcol2:
                register_instead = st.button('👤 Register Instead', type='primary', use_container_width=True)

            if login_clicked:
                record = st.session_state['teachers_db'].get(username)
                if record and record['password'] == password:
                    st.session_state['teacher_logged_in'] = username
                    st.rerun()
                else:
                    st.error('Invalid username or password.')

            if register_instead:
                st.session_state['teacher_auth_mode'] = 'register'
                st.rerun()

    footer_home()