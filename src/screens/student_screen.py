import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_teacher_auth
from src.face_utils import get_face_encoding, compare_encoding
from src.database import register_student, get_all_students, get_latest_attendance_session, mark_attendance

def student_screen():
    style_base_layout()
    style_teacher_auth()

    _, home_col = st.columns([4, 1])
    with home_col:
        if st.button('👤 Go back to Home', type='secondary', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    header_home()

    if 'student_auth_mode' not in st.session_state:
        st.session_state['student_auth_mode'] = 'register'
    if 'student_logged_in' not in st.session_state:
        st.session_state['student_logged_in'] = None

    if st.session_state['student_logged_in']:
        st.markdown(f"<h3>Welcome, {st.session_state['student_logged_in']} 👋</h3>", unsafe_allow_html=True)

        st.markdown("<h4>Mark Today's Attendance</h4>", unsafe_allow_html=True)
        selfie = st.camera_input("Take a selfie to mark attendance")
        if selfie is not None and st.button("Mark Attendance", type='primary'):
            my_encoding = get_face_encoding(selfie.getvalue())
            if my_encoding is None:
                st.error("No face detected. Try again.")
            else:
                session = get_latest_attendance_session()
                present = False
                if session:
                    for group_enc in session['group_encodings']:
                        if compare_encoding(group_enc, my_encoding):
                            present = True
                            break

                mark_attendance(st.session_state['student_id'], present)

                if present:
                    st.success("You were found in the class photo — marked PRESENT ✅")
                else:
                    st.error("You were not found in the class photo — marked ABSENT ❌")

        footer_home()
        return

    with st.container(key="teacher_auth_card"):
        if st.session_state['student_auth_mode'] == 'register':
            st.markdown("<h3>Register your face profile</h3>", unsafe_allow_html=True)

            name = st.text_input('Enter name', placeholder='Ananya Roy')
            photo = st.camera_input('Position your face in the center')

            st.markdown("<hr>", unsafe_allow_html=True)

            bcol1, bcol2 = st.columns(2)
            with bcol1:
                register_clicked = st.button('👤 Register Now', type='primary', use_container_width=True)
            with bcol2:
                login_instead = st.button('👤 Login instead', type='secondary', use_container_width=True)

            if register_clicked:
                if not name:
                    st.error('Please enter your name.')
                elif photo is None:
                    st.error('Please take a photo.')
                else:
                    encoding = get_face_encoding(photo.getvalue())
                    if encoding is None:
                        st.error('No face detected. Try better lighting or move closer.')
                    else:
                        register_student(name, encoding)
                        st.success(f'Welcome {name}! Your face profile has been saved.')
                        st.session_state['student_auth_mode'] = 'login'
                        st.rerun()

            if login_instead:
                st.session_state['student_auth_mode'] = 'login'
                st.rerun()

        else:
            st.markdown("<h3>Login with Face ID</h3>", unsafe_allow_html=True)

            photo = st.camera_input('Position your face in the center')

            st.markdown("<hr>", unsafe_allow_html=True)

            bcol1, bcol2 = st.columns(2)
            with bcol1:
                login_clicked = st.button('👤 Login', type='secondary', use_container_width=True)
            with bcol2:
                register_instead = st.button('👤 Register Instead', type='primary', use_container_width=True)

            if login_clicked:
                if photo is None:
                    st.error('Please take a photo.')
                else:
                    live_encoding = get_face_encoding(photo.getvalue())
                    if live_encoding is None:
                        st.error('No face detected. Try again.')
                    else:
                        students = get_all_students()
                        matched_name = None
                        matched_id = None
                        for student in students:
                            if compare_encoding(student['face_embedding'], live_encoding):
                                matched_name = student['name']
                                matched_id = student['student_id']
                                break

                        if matched_name:
                            st.session_state['student_logged_in'] = matched_name
                            st.session_state['student_id'] = matched_id
                            st.rerun()
                        else:
                            st.error('Face not recognized. Please register first.')

            if register_instead:
                st.session_state['student_auth_mode'] = 'register'
                st.rerun()

    footer_home()