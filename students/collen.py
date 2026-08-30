import csv
import io

import streamlit as st

if "collen_reports" not in st.session_state:
    st.session_state.collen_reports = []

st.title("report")
st.write("Report students doing foul behaviour below.")

name = st.text_input("Student Name")
class_ = st.text_input("Student Class")
crime = st.text_input("Student crime")

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    if st.button("enter"):
        if name and class_ and crime:
            st.session_state.collen_reports.append([name, class_, crime])
            st.success("report submitted")
        else:
            st.warning("please fill all boxes")

st.divider()

st.header("for admin")
st.write("these people are committing crime at school")

if st.session_state.collen_reports:
    st.table({"name": [row[0] for row in st.session_state.collen_reports]})
    st.table({"class": [row[1] for row in st.session_state.collen_reports]})
    st.table({"crime": [row[2] for row in st.session_state.collen_reports]})
    out = io.StringIO()
    csv.writer(out).writerows([["name", "class", "crime"]] + st.session_state.collen_reports)
    st.download_button("download CSV", out.getvalue(), "reports.csv")
else:
    st.info("no reports yet")
