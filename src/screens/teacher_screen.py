import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_teacher_auth
from src.database import teacher_exists, register_teacher, verify_teacher, get_teacher_name, save_attendance_session, get_all_students
from src.face_utils import get_all_face_encodings, compare_encoding


def teacher_screen():
    style_base_layout()
    style_teacher_auth()

    _, home_col = st.columns([4, 1])
    with home_col:
        if st.button('👤 Go back to Home', type='secondary', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    header_home()

    if 'teacher_auth_mode' not in st.session_state:
        st.session_state['teacher_auth_mode'] = 'register'
    if 'teacher_logged_in' not in st.session_state:
        st.session_state['teacher_logged_in'] = None

    if st.session_state['teacher_logged_in']:
        name = get_teacher_name(st.session_state['teacher_logged_in'])
        st.markdown(f"<h3>Welcome, {name} 👋</h3>", unsafe_allow_html=True)

        st.markdown("<h4>Upload Class Group Photo for Attendance</h4>", unsafe_allow_html=True)
        group_photo = st.file_uploader("Upload a group photo of the class", type=['jpg', 'jpeg', 'png'])
        if group_photo is not None and st.button("Start Attendance Session", type='primary'):
            encodings = get_all_face_encodings(group_photo.getvalue())
            if len(encodings) == 0:
                st.error("No faces detected in the photo. Try a clearer image.")
            else:
                save_attendance_session(encodings)
                st.success(f"Attendance session started with {len(encodings)} face(s) detected.")

                all_students = get_all_students()
                recognized_names = []
                for face_enc in encodings:
                    match = None
                    for student in all_students:
                        if compare_encoding(student['face_embedding'], face_enc):
                            match = student['name']
                            break
                    recognized_names.append(match if match else "Unknown face")

                st.markdown("**Students identified in this photo:**")
                for i, sname in enumerate(recognized_names, start=1):
                    if sname == "Unknown face":
                        st.write(f"{i}. ⚠️ {sname} (not a registered student)")
                    else:
                        st.write(f"{i}. ✅ {sname}")

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
                elif teacher_exists(username):
                    st.error('A teacher with this username already exists.')
                else:
                    register_teacher(username, name, password)
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
                if verify_teacher(username, password):
                    st.session_state['teacher_logged_in'] = username
                    st.rerun()
                else:
                    st.error('Invalid username or password.')

            if register_instead:
                st.session_state['teacher_auth_mode'] = 'register'
                st.rerun()

    footer_home()