import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'snapclass.db')


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            username TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    return conn


def teacher_exists(username: str) -> bool:
    conn = get_connection()
    row = conn.execute('SELECT 1 FROM teachers WHERE username = ?', (username,)).fetchone()
    conn.close()
    return row is not None


def register_teacher(username: str, name: str, password: str):
    conn = get_connection()
    conn.execute(
        'INSERT INTO teachers (username, name, password) VALUES (?, ?, ?)',
        (username, name, password)
    )
    conn.commit()
    conn.close()


def verify_teacher(username: str, password: str) -> bool:
    conn = get_connection()
    row = conn.execute(
        'SELECT 1 FROM teachers WHERE username = ? AND password = ?',
        (username, password)
    ).fetchone()
    conn.close()
    return row is not None


def get_teacher_name(username: str) -> str:
    conn = get_connection()
    row = conn.execute('SELECT name FROM teachers WHERE username = ?', (username,)).fetchone()
    conn.close()
    return row[0] if row else None