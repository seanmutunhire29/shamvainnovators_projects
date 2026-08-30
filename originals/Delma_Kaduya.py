import streamlit as st
if "chat_step" not in st.session_state:
    st.session_state.chat_step = "ask name"
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! Welcome. What is your name?"}]
if "patient_name" not in st.session_state:
    st.session_state.patient_name = "Unknown Patient"
if "symptom_duration" not in st.session_state:
    st.session_state.symptom_duration = " Symptom Not specified"
if "summary" not in st.session_state:
    st.session_state.summary = ""
page = st.sidebar.selectbox("Navigate Pages",["Patient Chat", "Doctor Dashboard"])
if page == "Patient Chat":
    st.title("Patient Assistant")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
user_input = st.chat_input("Type your message here...")
if user_input:
    with st.chat_message("user"):
     st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
if st.session_state.chat_step == "ask_name":
    st.session_state.patient_name = user_input
    st.session.state.chat_step = "ask symptom"
    bot_reply =f"Thank you,{user_input}.What problems or symptoms are you facing today?"
elif st.session_state.chat_step == "ask_symptom":
    st.session_state.state_symptom = user_input
    st.session_state.chat_step = "ask duration"
    bot_reply = "How long have you been experiencing these symptoms?"
elif st.session_state.chat_step == "ask_duration":
    st.session_state.state_duration = user_input
    st.session_state.chat_step = "complete"
    bot_reply = "Thank you. I have recorded your details and a doctor will be with you shortly."
else:
    bot_reply = "Your request is already processing. Thank you for your patience!"
    with st.chat_message("assistant"):
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
if "patient_name" in st.session_state:
        st.info(
            f"**Patient Name:** {{st.session_state.patient_name}}\n"
            f"Duration:{{st.session_state.symptom_duration}}\n"
            f"Latest patient input:{{user_input}}"
        )
elif page == "Doctor Dashboard":
    st.title("Doctor's Portal")
    st.subheader("Patient Conversation Summary")
if st.session_state.summary:
    st.info(st.session_state.summary)
else:
    st.info("No conversation data available")
    st.subheader("Full Chat Transcript")
    for msg in st.session_state.messages:
        role_label = msg['role'].upper()
        content_text = msg['content']
        st.text(f"{role_label}: {content_text}")



