import streamlit as st
import openai
import os
from dotenv import load_dotenv
from PIL import Image

#Load my API key from.env file
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

#This is the title that shows on the browser tab
st.set_page_config(page_title="Teen Pregnancy Education Hub",page_icon="💙", layout="wide")

st.title("Teen Pregnancy Education Hub")
st.write("Support and Information for Teenagers in Zimbabwe")

#My AI rules - keep it safe and helpful
def get_answer(question):
    SYSTEM_PROMPT="""
    You are helping teenagers in Zimbabwe about teen pregnacny.
    Be kind , give facts, and keep it short.
    Always tell them to talk to a nurse, teacher ,or parent.
    Mention clinics,ZNFPC, and Childline 116 if they ask for help.
    """

    try:
        response=openai.ChatComplete.create(
            model="gpt-4o-min",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except :
        return "Sorry, I can`t  answer right now. Please try again or ask a teacher/nurse."

#I used tabs so we have 3  pages:
tab1, tab2, tab3=st.tabs(["Page 1:Problems", "Page 2:Help","Page 3:Parents"])

with tab1:
    st.header("Problems Faced By Pregnant Teenagers")
    st.image("C:/Users/User/Pictures/Screenshots/Screenshot 2026-08-28 145217.png")

    st.write("### Health Problems")
    st.write(">Getting sick easily during pregnancy")
    st.write(">Feeling stressed and worried")
    st.write(">Hormonial changes and social stress often trigger sadness")

    st.write("### School Problems")
    st.write("~Missing classes ")
    st. write("~People laughing or judging")
    st.write("~No money for baby things")

    st.write("### Solutions")
    st.write("* Go to clinic early")
    st.write("* Talk to guidance teacher")
    st.write("* Don`t give up on school")

    st.write("---")
    st.write("### Upload a Picture")
    st.write("Share a picture of hope.Please no face for safety.")
    pic=st.file_uploader("Choose file")
    if pic:
        img=Image.open(pic)
        st.image(img)
        st.write("Thank you for sharing!")

with tab2:
    st.header("Where to Get Help")
    st.image("C:/Users/User/Pictures/Screenshots/Screenshot 2026-08-28 143714.png")

    st.write("In Zimbabwe - Especially Shamva:**")
    st.write("a) Local Clinic:Free checkups and counselling")
    st.write("b) ZNFPC:They help youth with health information")
    st.write("c) School Guidance Teacher:For talking and support")
    st.write("d) Childline 116.It`s free and 24 hours")
    st.write("e)  Social Welfare:Help with grants")

    st.info("Import :Go to clinic early.It help you and the baby.")

with tab3:
    st.header("How Parents Can Help")
    st.image("C:/Users/User/Pictures/Screenshots/Screenshot 2026-08-28 144422.png")

    st.write("-Stay calm. Don`t shout or blame.")
    st.write("-Take her to clinic for checkups.")
    st.write("-Help her to stay in school")
    st.write("-Plan for the baby together")
    st.write("-Talk openly with their girl child")
    st.write("-Listen attentively to their childrren")
    st.write("-Ask ZNFPC,church leaders or nurses for help")

    st.success("Your support bring a change into our lives")

st.write("---")
#This is the AI question box - works on every page
st.subheader("Ask Me Anything")
q=st.text_input("Type your question here...e.g. where do you access services here in Shamva?")

if st.button("send"):
    if q:
        with st.spinner("Loading answer...."):
            answer=get_answer (q)
        st.write("**Answer**, ans")
    else:
        st.write("Please type your question here...")

st.write("---")
st.write("Emergency: Childline 116 /Clinic/ ZNFPC")
st.caption("Made for school project 2026")






