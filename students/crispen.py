import streamlit as st

# Initialize state
if "crispen_step" not in st.session_state:
    st.session_state.crispen_step = 1
    st.session_state.crispen_level = 1
    st.session_state.crispen_score = 0
    st.session_state.crispen_name = ""
    st.session_state.crispen_age = 1
    st.session_state.crispen_sex = ""

questions = {
    1: [  # Easy
        {"q": "What is a cell?",
         "options": ["basic unit of life ", "cell membrane", "biological catalyst", "specific ph"],
         "answer": "basic unit of life "},
        {"q": "define an atom", "options": ["a good mineral", "sub unit of an element", "catalyst", "from paradise"],
         "answer": "sub unit of an element"},
        {"q": "what is momentum",
         "options": ["change in velocity", "product of mass and unit", "product of mass and velocity",
                     "magnitude of the earth"], "answer": "product of mass and velocity"}
    ],
    2: [  # Medium
        {"q": "define acceleration",
         "options": ["rate of change in velocity", "velocity at constant motion ", "sean is the best",
                     "amplitude at rest"], "answer": "rate of change in velocity"},
        {"q": "state newton third law of motion",
         "options": [" when force exerted on an object the object exert the same amount of force",
                     "constant  motion of an object", "magnitude of a vector", "amount of work done"],
         "answer": " when force exerted on an object the object exert the same amount of force"},
        {"q": "Which one is a python IDE", "options": ["java script", "SQ script", "pycham", "alien"],
         "answer": "pycham"}
    ],
    3: [  # Hard
        {"q": "What is DNA stands for  ?",
         "options": ["Deoxy-ribo nucleic acid", "doctor nicole alice", " do not act", "do not use ai"],
         "answer": "Deoxy-ribo nucleic acid"},
        {"q": "molecule of water contains what elements",
         "options": ["nitrogen", "argon and helium", "carbon and oxygen", "hydrogen and oxygen"],
         "answer": "hydrogen and oxygen"},
        {"q": "What is the boiling point of ethanol?", "options": ["78C", "100C", "150C", "12C"], "answer": "78C"}
    ]
}

# STEP 1: WELCOME
if st.session_state.crispen_step == 1:
    st.title("STEP ONE: Hello genius welcome to the real gaming mode to test your Genius")
    st.session_state.crispen_name = st.text_input(" ENTER YOUR NAME")
    st.session_state.crispen_age = st.number_input("AGE PLEASE", min_value=1, max_value=100)
    st.session_state.crispen_sex = st.selectbox("ENTER SEX GENIUS", ["", "Male", "Female", "TRANS"])

    if st.button("CLICK TO GO NEXT"):
        if st.session_state.crispen_name and st.session_state.crispen_age and st.session_state.crispen_sex:
            st.session_state.crispen_step = 2
            st.rerun()
        else:
            st.warning("details not retrieved from the user please enter your details")

# STEP 2: SUBJECT
elif st.session_state.crispen_step == 2:
    st.title("STEP 2:science subject")
    subject = st.text_input("Enter Subject")
    notes = st.text_area("Paste your notes here")

    if st.button("Start Quiz"):
        st.session_state.crispen_step = 3
        st.rerun()

# ===== STEP 3: QUIZ GAME =====
elif st.session_state.crispen_step == 3:
    st.title(f"Phase 3: Level {st.session_state.crispen_level}")
    current_qs = questions[st.session_state.crispen_level]

    for i, q in enumerate(current_qs):
        st.radio(q["q"], q["options"], key=f"crispen_q{i}")

    if st.button(f"Submit Level {st.session_state.crispen_level}"):
        for j, qq in enumerate(current_qs):
            if st.session_state[f"crispen_q{j}"] == qq["answer"]:
                st.session_state.crispen_score += 1
        if st.session_state.crispen_level < 3:
            st.session_state.crispen_level += 1
        else:
            st.session_state.crispen_step = 4
        st.rerun()

# STEP 4: RESULTS
elif st.session_state.crispen_step == 4:
    st.title("Phase 4: Results")
    st.write(f"**Name:** {st.session_state.crispen_name}")
    st.write(f"**Age:** {st.session_state.crispen_age} | **Sex:** {st.session_state.crispen_sex}")
    st.write(f"**Final Score:** {st.session_state.crispen_score} / 9")

    if st.session_state.crispen_score >= 7:
        st.success("Great job! 🟢")
    elif st.session_state.crispen_score >= 4:
        st.info("Not bad! 🟡")
    else:
        st.error("Keep practicing! 🔴")

    if st.button("Play Again"):
        st.session_state.crispen_step = 1
        st.session_state.crispen_score = 0
        st.session_state.crispen_level = 1
        st.rerun()
