import streamlit as st
from db import init_db, get_notes, add_note, delete_note

# เรียก init เพื่อสร้างตาราง
init_db()

st.title("📝 Simple Note App")

# ----- เพิ่มโน้ต -----
with st.form("note_form"):
    new_note = st.text_area("✍️ Write your note")
    submitted = st.form_submit_button("➕ Add note")
    if submitted and new_note.strip() != "":
        add_note(new_note.strip())
        st.success("Add note success!")
        st.rerun()

# ----- แสดงโน้ตทั้งหมด -----
st.subheader("📋 All notes ")
notes = get_notes()
if not notes:
    st.info("No notes yet")
else:
    for note_id, content in notes:
        st.write(f"🗒️ {content}")
        if st.button("❌ Delete", key=f"delete_{note_id}"):
            delete_note(note_id)
            st.success("Delete note success!")
            st.rerun()
