import streamlit as st

st.set_page_config(
    page_title="Shamva Innovators",
    page_icon="🎓",
    layout="centered",
)

pages = {
    "Shamva Innovators": [
        st.Page("gallery.py", title="All projects", icon="🏠", default=True),
    ],
    "Student projects": [
        st.Page("students/christine.py", title="Christine", url_path="christine"),
        st.Page("students/crispen.py", title="Crispen", url_path="crispen"),
        st.Page("students/daizy.py", title="Daizy", url_path="daizy"),
        st.Page("students/delma_kaduya.py", title="Delma Kaduya", url_path="delma-kaduya"),
        st.Page("students/delma_mandeya.py", title="Delma Mandeya", url_path="delma-mandeya"),
        st.Page("students/elisiya.py", title="Elisiya", url_path="elisiya"),
        st.Page("students/kush.py", title="Kush", url_path="kush"),
        st.Page("students/nokutenda.py", title="Nokutenda", url_path="nokutenda"),
        st.Page("students/nokutenda_kuzanga.py", title="Nokutenda Kuzanga", url_path="nokutenda-kuzanga"),
        st.Page("students/collen.py", title="Collen", url_path="collen"),
        st.Page("students/loveness.py", title="Loveness", url_path="loveness"),
        st.Page("students/samaz.py", title="Samaz", url_path="samaz"),
    ],
}

st.navigation(pages).run()
