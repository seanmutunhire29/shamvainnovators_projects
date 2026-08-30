import streamlit as st

st.title("Shamva Innovators")
st.write(
    "Summer program student projects. Open any project below, or use the sidebar to switch."
)

PROJECTS = [
    {
        "name": "Christine",
        "title": "Student Resource Platform",
        "page": "students/christine.py",
    },
    {
        "name": "Crispen",
        "title": "Science quiz game",
        "page": "students/crispen.py",
    },
    {
        "name": "Daizy",
        "title": "Shamva water schedule",
        "page": "students/daizy.py",
    },
    {
        "name": "Delma Kaduya",
        "title": "Patient assistant",
        "page": "students/delma_kaduya.py",
    },
    {
        "name": "Delma Mandeya",
        "title": "Teen pregnancy education hub",
        "page": "students/delma_mandeya.py",
    },
    {
        "name": "Elisiya",
        "title": "AfyaBot chronic disease assessment",
        "page": "students/elisiya.py",
    },
    {
        "name": "Kush",
        "title": "Mentors information",
        "page": "students/kush.py",
    },
    {
        "name": "Nokutenda",
        "title": "Student attendance",
        "page": "students/nokutenda.py",
    },
    {
        "name": "Nokutenda Kuzanga",
        "title": "Waste awareness",
        "page": "students/nokutenda_kuzanga.py",
    },
    {
        "name": "Collen",
        "title": "School report system",
        "page": "students/collen.py",
    },
    {
        "name": "Loveness",
        "title": "Drug abuse awareness",
        "page": "students/loveness.py",
    },
    {
        "name": "Samaz",
        "title": "Men's anonymous forum",
        "page": "students/samaz.py",
    },
]

for i in range(0, len(PROJECTS), 2):
    cols = st.columns(2)
    for col, project in zip(cols, PROJECTS[i : i + 2]):
        with col:
            with st.container(border=True):
                st.subheader(project["name"])
                st.caption(project["title"])
                st.page_link(project["page"], label="Open project")
