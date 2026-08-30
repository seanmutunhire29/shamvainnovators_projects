import streamlit as st

if "dk_chat_step" not in st.session_state:
    st.session_state.dk_chat_step = "ask_name"
if "dk_messages" not in st.session_state:
    st.session_state.dk_messages = [
        {"role": "assistant", "content": "Hello! Welcome. What is your name?"}
    ]
if "dk_patient_name" not in st.session_state:
    st.session_state.dk_patient_name = "Unknown Patient"
if "dk_symptom" not in st.session_state:
    st.session_state.dk_symptom = "Not specified"
if "dk_symptom_duration" not in st.session_state:
    st.session_state.dk_symptom_duration = "Not specified"
if "dk_summary" not in st.session_state:
    st.session_state.dk_summary = ""

page = st.sidebar.selectbox("Navigate Pages", ["Patient Chat", "Doctor Dashboard"])

if page == "Patient Chat":
    st.title("Patient Assistant")

    for msg in st.session_state.dk_messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Type your message here...")
    if user_input:
        st.session_state.dk_messages.append({"role": "user", "content": user_input})

        if st.session_state.dk_chat_step == "ask_name":
            st.session_state.dk_patient_name = user_input
            st.session_state.dk_chat_step = "ask_symptom"
            bot_reply = f"Thank you, {user_input}. What problems or symptoms are you facing today?"
        elif st.session_state.dk_chat_step == "ask_symptom":
            st.session_state.dk_symptom = user_input
            st.session_state.dk_chat_step = "ask_duration"
            bot_reply = "How long have you been experiencing these symptoms?"
        elif st.session_state.dk_chat_step == "ask_duration":
            st.session_state.dk_symptom_duration = user_input
            st.session_state.dk_chat_step = "complete"
            st.session_state.dk_summary = (
                f"Patient: {st.session_state.dk_patient_name}\n"
                f"Symptoms: {st.session_state.dk_symptom}\n"
                f"Duration: {st.session_state.dk_symptom_duration}"
            )
            bot_reply = "Thank you. I have recorded your details and a doctor will be with you shortly."
        else:
            bot_reply = "Your request is already processing. Thank you for your patience!"

        st.session_state.dk_messages.append({"role": "assistant", "content": bot_reply})
        st.rerun()

    st.info(
        f"**Patient Name:** {st.session_state.dk_patient_name}\n\n"
        f"**Duration:** {st.session_state.dk_symptom_duration}"
    )

else:
    st.title("Doctor's Portal")
    st.subheader("Patient Conversation Summary")
    if st.session_state.dk_summary:
        st.info(st.session_state.dk_summary)
    else:
        st.info("No conversation data available")

    st.subheader("Full Chat Transcript")
    for msg in st.session_state.dk_messages:
        st.text(f"{msg['role'].upper()}: {msg['content']}")
