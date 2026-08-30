import csv
import datetime
import io

import streamlit as st

st.title("Drug Abuse Awereness")
st.write("anonymous reporting platform by Loveness Kazumunyu")

if "loveness_reports" not in st.session_state:
    st.session_state.loveness_reports = []

page = st.sidebar.selectbox("menu", ["report", "policedashbord"])
if page == "report":
    st.header("Report Drug Sellers")
    name = st.text_input("name")
    location = st.text_input("location")
    crime = st.text_area("crime")

    if st.button("submit"):
        if name and location and crime:
            st.session_state.loveness_reports.append({
                "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "name": name,
                "location": location,
                "crime": crime,
            })
            st.success("report submited")
        else:
            st.error("fill all fields")
else:
    st.header("police dashbord")
    if len(st.session_state.loveness_reports) == 0:
        st.info("no reports")
    else:
        st.table(st.session_state.loveness_reports)
        out = io.StringIO()
        writer = csv.DictWriter(
            out, fieldnames=["time", "name", "location", "crime"]
        )
        writer.writeheader()
        writer.writerows(st.session_state.loveness_reports)
        st.download_button("downlaod csv", out.getvalue(), "reports.csv")
