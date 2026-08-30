import streamlit as st

st.title("Student Attendance")

# Your student data - DICTIONARY + LIST
students = [
    {"Name": "Tapihwa Moyo", "Absent": 2, "Present": 18},
    {"Name": "Nokutenda Munda", "Absent": 7, "Present": 13},
    {"Name": "Purity Ben", "Absent": 1, "Present": 19},
    {"Name": "Brian Ncube", "Absent": 1, "Present": 19}
]

st.header("Attendance Report")

# FIX 1: Calculate % and Status with a LOOP
for s in students:
    total = s["Present"] + s["Absent"]  # Total days
    s["%"] = round((s["Present"] / total) * 100, 1) if total > 0 else 0  # FIXED FORMULA
    s["Status"] = "Good" if s["%"] >= 85 else "Frequently Absent"  # Added this

st.table(students)  # Show table

st.markdown("---")
st.header("Daily Attendance")
date = st.date_input("Date")  # VARIABLE

# FIX 2: Track who is present today
present_today = []
for s in students:  # LOOP
    if st.checkbox(s["Name"], key=s["Name"]):  # If ticked
        present_today.append(s["Name"])

if st.button("Save Attendance"):
    # Update counts
    for s in students:  # LOOP
        if s["Name"] in present_today:  # Present
            s["Present"] += 1
        else:  # Absent
            s["Absent"] += 1

        # Recalculate % after update
        total = s["Present"] + s["Absent"]
        s["%"] = round((s["Present"] / total) * 100, 1) if total > 0 else 0
        s["Status"] = "Good" if s["%"] >= 85 else "Frequently Absent"

    st.success("Attendance Successful")
    st.table(students)  # Show updated table