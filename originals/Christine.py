import streamlit as st

st.title("Student Resource Platform")
st.write("Welcome! Share and find learning resources")

menu = st.sidebar.selectbox("Menu", ["Home", "Search materials", "Share materials", "Submit", "Download materials"])

material_types = ["Notes", "books", "Past exam papers", "Assignment", "Research materials"]
subjects = ["Biology", "Maths", "Chemistry", "Computer Science", "others"]

# sample materials list
st.session_state.materials = [
    {"title": "Biology notes", "subject": "Biology", "type": "Notes", "topic": "Genetics"},
    {"title": "Acids and bases", "subject": "Chemistry", "type": "Notes", "topic": "Acids and bases"},
    {"title": "Algebra", "subject": "Mathematics", "type": "notes", "topic": "Algebra"}
]

uploaded_file = st.file_uploader("Upload your notes", type=["pdf"])
if uploaded_file is not None:
    st.success("Notes uploaded successfully")

st.header("How the platform works")
st.write("User")
st.write("Home page")
st.write("Search materials")
st.write("Choose subject")
st.write("Download materials")

st.header("Books")
st.write("search materials")

if menu == "Search materials":
    st.header("Search materials")
    search = st.text_input("Enter material name")
    selected_subject = st.selectbox("Choose subject", subjects)
    if st.button("Search"):
        if search == "":
            st.warning("Please enter something to search")
        else:
            results = [m for m in st.session_state.materials
                       if search.lower() in m["title"].lower() and selected_subject.lower() in m["subject"].lower()]
            if results:
                for r in results:
                    st.write(r)
                st.success("Search successful")
            else:
                st.info("No materials found")

elif menu == "Share materials":
    st.header("Share notes or books")
    title = st.text_input("Material title")
    subject = st.selectbox("Subject", subjects)

elif menu == "Submit":
    st.header("Submit materials")
    name = st.text_input("Name")
    title = st.text_input("Material title")
    file = st.file_uploader("Upload file")
    if name == "":
        st.error("Enter your name")
    elif title == "":
        st.error("Enter material title")
    elif file is None:
        st.error("Upload a file")
    else:
        st.success("Material submitted successfully")

elif menu == "Download materials":
    st.header("Download materials")
    st.download_button("Download materials", data=b"", file_name="material.pdf")
    books_subject = st.selectbox("Book subject", subjects)
    st.subheader("Available books")

st.header("Search")
search = st.text_input("Search by subject, book title")
if search:
    for note in st.session_state.materials:
        if search.lower() in note["subject"].lower():
            st.write(note)
            st.success("Search successful")

st.header("Past papers")
past_subject = st.selectbox("Past paper subject", subjects)
st.subheader("Available past papers")

st.header("Textbook library")
text_subject = st.selectbox("Textbook subject", subjects)
st.success("Textbook uploaded successfully")

st.header("Sharing")
sharing_subjects = st.selectbox("Sharing subject", subjects)
st.success("Sharing uploaded successfully")