import streamlit as st

# 1. PAGE SETUP
st.set_page_config(
    page_title="Waste awareness",
    page_icon="♻️",
    layout="centered"
)

# 2. WASTE KNOWLEDGE DATABASE
WASTE_KNOWLEDGE = {
    "Recycle in Shamva": "Take plastics to city recycling at rural district council road",
    " burning trash": "No, burning release toxic Smoke. Try Composting or recycling",
    "dump": "Illegal dumping causes diseases. Report to your local council.",
    "Litter": "Put waste in bins, Do not litter. Keep your community clean.",
    "compost": "Compost food scraps and dry leaves in a pit. Turn it weekly. Ready in 6 weeks.",
    "recycle": "Reduce, Reuse, Recycle. Separate plastics, glass and paper for recycling."
}


def get_answer(question):
    # Check if user's question contains any keyword
    question = question.lower()
    for key, answer in WASTE_KNOWLEDGE.items():
        if key.lower() in question:
            return answer

    # NEW: Instead of "I don't have that answer" we always give guidance
    return "Thanks for your question! For general waste help: Reduce waste, Reuse items, and Recycle. For specific help contact your local council."


# 3. WEBSITE CONTENT
st.title("♻️ Waste Awareness Website")
st.write("Spreading awareness on waste management, recycling and clean-ups")

st.divider()

# 4. INPUT + BUTTON
user_question = st.text_input("Type your question here:")

if st.button("enter", type="primary"):
    if user_question:
        answer = get_answer(user_question)
        st.success(f"Answer: {answer}")
    else:
        st.warning("please enter a question first")

st.divider()
st.header("Goal: help people with waste management and answer questions and spread awareness")

# Show examples
st.write("Try: 'Recycle in Shamva' or 'Is burning Safe' or 'How to compost'")