import streamlit as st

st.title("Student Attendance")

if "nokutenda_students" not in st.session_state:
    st.session_state.nokutenda_students = [
        {"Name": "Tapihwa Moyo", "Absent": 2, "Present": 18},
        {"Name": "Nokutenda Munda", "Absent": 7, "Present": 13},
        {"Name": "Purity Ben", "Absent": 1, "Present": 19},
        {"Name": "Brian Ncube", "Absent": 1, "Present": 19},
    ]

students = st.session_state.nokutenda_students

st.header("Attendance Report")

for s in students:
    total = s["Present"] + s["Absent"]
    s["%"] = round((s["Present"] / total) * 100, 1) if total > 0 else 0
    s["Status"] = "Good" if s["%"] >= 85 else "Frequently Absent"

st.table(students)

st.markdown("---")
st.header("Daily Attendance")
date = st.date_input("Date")

present_today = []
for s in students:
    if st.checkbox(s["Name"], key=f"nokutenda_{s['Name']}"):
        present_today.append(s["Name"])

if st.button("Save Attendance"):
    for s in students:
        if s["Name"] in present_today:
            s["Present"] += 1
        else:
            s["Absent"] += 1

        total = s["Present"] + s["Absent"]
        s["%"] = round((s["Present"] / total) * 100, 1) if total > 0 else 0
        s["Status"] = "Good" if s["%"] >= 85 else "Frequently Absent"

    st.success("Attendance Successful")
    st.table(students)
