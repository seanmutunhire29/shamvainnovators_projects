import streamlit as st
st.title("Welcome to Mentors information page")
st.header("This page is for mentors")
st.subheader("Please enter your full details below")
st.text_input("Enter your name:")
st.text_input("Enter your age:")
st.text_input("Enter your occupation:")
st.text_input("Enter your location")
st.text_input("Enter your conatct/email:")
st.file_uploader("Upload your picture")
st.button("Enter")

st.write("These are the mentors available now ,reach out to them and get help")
#DATA FOR THE MENTORS
mentors =[
    {"name:""Mr Manyika",
     "picture:",
     "help:" "G & C"
     "location:" "Shamva"
     "work hours:" "08:00am -16:00pm"
     "contact:" "0773149654"
    },
 {"name:""Mr Mutinhure",
     "picture:",
  "help:" "Finding Scholarships",
  "Location:""Harare",
  "work hours:""14:00am -16:00pm"
  "contact""0712333444"
  },
 {"name:""Mr Chabata",
 "picture:",
  "help:""Bible Study Teacher",
  "location:""Bindura",
 "work hours:""09:00am -16:00pm",
"contact""0773846483"
,}
 ]

















