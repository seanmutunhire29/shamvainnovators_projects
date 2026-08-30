import streamlit as st

st.title("Men's Anonymous Forum for sharing problems")

if "samaz_posts" not in st.session_state:
    st.session_state.samaz_posts = [
        {
            "id": 1,
            "issue": "Balancing a high-stress job with family.",
            "advice": ["Set a strict no-phone rule for an hour when you reach home."],
        },
        {
            "id": 2,
            "issue": "Feeling lonely in a new city.",
            "advice": ["Join a sports league."],
        },
    ]

st.subheader("Share an Issue:")
with st.form("samaz_share"):
    issue_text = st.text_input("What is on your mind?")
    submitted = st.form_submit_button("Post")
    if submitted:
        if issue_text.strip():
            new_id = len(st.session_state.samaz_posts) + 1
            st.session_state.samaz_posts.append(
                {"id": new_id, "issue": issue_text.strip(), "advice": []}
            )
            st.success("Posted.")
            st.rerun()
        else:
            st.warning("Please type an issue before posting.")

st.divider()
st.subheader("Current Posts:")

for post in st.session_state.samaz_posts:
    with st.container(border=True):
        st.markdown(f"**Issue:** {post['issue']}")
        st.write("**Advice given:**")
        if post["advice"]:
            for reply in post["advice"]:
                st.write(f"- {reply}")
        else:
            st.caption("No advice yet.")

        with st.form(f"samaz_reply_{post['id']}"):
            advice_text = st.text_input("Give advice...", key=f"samaz_advice_{post['id']}")
            replied = st.form_submit_button("Reply")
            if replied:
                if advice_text.strip():
                    post["advice"].append(advice_text.strip())
                    st.rerun()
                else:
                    st.warning("Please type some advice first.")
