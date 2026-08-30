import streamlit as st
import pandas as pd
import datetime

st.title("Drug Abuse Awereness")
st.write("anonymous reporting platform by Loveness Kazumunyu")

#save reports
if "reports" not in st.session_state:
        st.session_state.reports = []
page = st.sidebar.selectbox("menu",["report","policedashbord"])
if page == "report":
    st.header("Report Drug Sellers")
    name = st.text_input("name")
    location = st.text_input("location")
    crime = st.text_area("crime")

    if st.button("submit"):
        if name and location and crime:
            st.session_state.reports.append({
                "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%M"),
                "name": name, "location": location, "crime": crime,             })
            st.success("report submited")
        else:
            st.error("fill all fields")
else:
    st.header("police dashbord")
    if len(st.session_state.reports) == 0:
        st.info("no reports")
    else :
        df = pd.DataFrame (st.session_state.reports)
        st.dataframe(df)
        st.download_button("downlaod csv", df.to_csv(index=False), "reports.csv")
