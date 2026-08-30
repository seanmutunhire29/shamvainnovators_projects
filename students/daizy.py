import streamlit as st

st.title("Shamva water schedule")

if "daizy_water" not in st.session_state:
    st.session_state.daizy_water = [
        ["Golden Heights", "26/08/2026", "06:00AM", "02:00PM", "water available"],
        ["Wadazanai", "27/08/2026", "09:00AM", "04:00PM", "water available"],
        ["Shamva Town", "28/08/2026", "10:00AM", "06:00PM", "water available"],
        ["Alpha", "29/08/2026", "11:00AM", "07:00PM", "supply may be reduced"],
    ]

water = st.session_state.daizy_water

st.table({
    "water point": [w[0] for w in water],
    "Date": [w[1] for w in water],
    "Start Time": [w[2] for w in water],
    "End Time": [w[3] for w in water],
    "notes": [w[4] for w in water],
})

st.header("Other water points")
points = ["Wadzanai high school", "Asiah office", "Wadaznai primary school", "Clinic"]

for p in points:
    st.write(".", p)
for w in water:
    st.write(".", w)

st.header("Update water schedule")

point = st.text_input("Water point")
date = st.date_input("Date")
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")
notes = st.text_input("Notes")

if st.button("Save Changes"):
    if point:
        st.session_state.daizy_water.append([
            point,
            date.strftime("%d/%m/%Y"),
            start_time.strftime("%I:%M%p"),
            end_time.strftime("%I:%M%p"),
            notes or "",
        ])
        st.success("Schedule updated!")
        st.rerun()
    else:
        st.warning("Please enter a water point")
