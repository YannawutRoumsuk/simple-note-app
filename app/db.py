import psycopg2

def get_connection():
    return psycopg2.connect(
        host="postgres",
        database="notesdb",
        user="postgres",
        password="postgres"
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def get_notes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, content FROM notes;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_note(content):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (content) VALUES (%s);", (content,))
    conn.commit()
    cur.close()
    conn.close()

def delete_note(note_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM notes WHERE id = %s;", (note_id,))
    conn.commit()
    cur.close()
    conn.close()
