import bcrypt
import streamlit as st
from supabase import create_client

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


def teacher_exists(username: str) -> bool:
    result = supabase.table('teachers').select('username').eq('username', username).execute()
    return len(result.data) > 0


def register_teacher(username: str, name: str, password: str):
    supabase.table('teachers').insert({
        'username': username,
        'name': name,
        'password_hash': hash_password(password)
    }).execute()


def verify_teacher(username: str, password: str) -> bool:
    result = supabase.table('teachers').select('password_hash').eq('username', username).execute()
    if not result.data:
        return False
    stored_hash = result.data[0]['password_hash']
    return check_password(password, stored_hash)


def get_teacher_name(username: str) -> str:
    result = supabase.table('teachers').select('name').eq('username', username).execute()
    return result.data[0]['name'] if result.data else None


def register_student(name: str, face_encoding: list):
    supabase.table('students').insert({
        'name': name,
        'face_embedding': face_encoding
    }).execute()


def get_all_students():
    result = supabase.table('students').select('student_id, name, face_embedding').execute()
    return result.data

def save_attendance_session(group_encodings: list):
    result = supabase.table('attendance_sessions').insert({
        'group_encodings': group_encodings
    }).execute()
    return result.data[0]['session_id']


def get_latest_attendance_session():
    result = supabase.table('attendance_sessions').select('*').order('created_at', desc=True).limit(1).execute()
    return result.data[0] if result.data else None


def mark_attendance(student_id: int, is_present: bool, subject_id=None):
    supabase.table('attendance_logs').insert({
        'student_id': student_id,
        'subject_id': subject_id,
        'is_present': is_present
    }).execute()