import streamlit as st

# 1. Dictionary: Storing disease profiles and threshold configurations
DISEASE_PROFILES = {
    "Diabetes": {
        "symptoms": [
            "Frequent urination",
            "Excessive thirst",
            "Unexplained weight loss",
            "Blurry vision",
        ],
        "risk_multiplier": 1.2,
    },
    "Hypertension (High Blood Pressure)": {
        "symptoms": [
            "Severe headaches",
            "Chest pain",
            "Difficulty breathing",
            "Dizziness",
        ],
        "risk_multiplier": 1.1,
    },
    "Chronic Kidney Disease": {
        "symptoms": [
            "Fatigue",
            "Swollen ankles/feet",
            "Changes in urination frequency",
            "Foamy urine",
        ],
        "risk_multiplier": 1.3,
    },
}

# 2. Dictionary: Disease monitoring guidelines
MONITORING_GUIDELINES = {
    "Diabetes": [
        "Check fasting blood glucose levels daily using a glucometer.",
        "Schedule an HbA1c blood test every 3 to 6 months.",
        "Inspect your feet daily for cuts, blisters, or redness.",
        "Track daily carbohydrate intake and maintain physical activity.",
    ],
    "Hypertension (High Blood Pressure)": [
        "Measure your blood pressure at home twice daily (morning and evening).",
        "Keep a daily log of blood pressure numbers to show your doctor.",
        "Monitor your daily sodium (salt) consumption.",
        "Schedule regular eye and kidney assessments to screen for pressure damage.",
    ],
    "Chronic Kidney Disease": [
        "Track daily water and fluid intake as recommended by your specialist.",
        "Get regular blood tests to check your eGFR and serum creatinine levels.",
        "Perform routine urine tests to monitor protein-to-creatinine ratios.",
        "Weigh yourself daily to look for sudden fluid retention or swelling.",
    ],
}

# Dictionary: Pairings of precise medical questions and their direct answers
HEALTH_KNOWLEDGE_BASE = {
    "Select a question...": "Please choose a question from the menu above to see the answer here.",
    "What is the main difference between Type 1 and Type 2 diabetes?": "Type 1 diabetes is an autoimmune condition where the body stops producing insulin. Type 2 diabetes is primarily linked to lifestyle factors where the body becomes resistant to the insulin it produces.",
    "Why is high blood pressure called a silent killer?": "Hypertension often has no visible symptoms for years, meaning a person can experience cardiovascular damage without realizing they have the condition.",
    "How does high blood pressure affect kidney function?": "High blood pressure forces blood through your vessels with extra pressure. Over time, this stretches and scars the delicate filtering vessels inside your kidneys.",
    "What lifestyle changes help manage chronic kidney disease?": "Managing blood sugar levels, keeping blood pressure stable, reducing salt intake, and adjusting your diet to limit processed proteins can slow the progression of kidney disease.",
}

# App header styling
st.title("AfyaBot: Chronic Disease Assessment")
st.write(
    "Welcome to AfyaBot. Please answer the questions below for a preliminary health screening."
)
st.divider()

# User Input Section
st.sidebar.header("User Demographics")
age = st.sidebar.number_input("Enter your Age:", min_value=1, max_value=120, value=30)
family_history = st.sidebar.checkbox("Family history of chronic diseases?")

st.subheader("Symptom Checklist")
st.write("Select all symptoms you are currently experiencing:")

# Loop & Dictionary: Dynamically generating checkboxes for symptoms
selected_symptoms = []
for disease, info in DISEASE_PROFILES.items():
    st.markdown(f"**{disease} Indicators:**")
    for symptom in info["symptoms"]:
        if st.checkbox(symptom, key=f"{disease}_{symptom}"):
            selected_symptoms.append(symptom)

# Variable to track which diseases crossed the warning or high-risk thresholds
diseases_to_monitor = []

# Diagnostic Trigger Button
if st.button("Analyze Health Profile"):
    st.divider()
    st.subheader("Diagnostic Results")

    high_risk_detected = False

    # Loop: Check each disease to calculate specific risk scores
    for disease, info in DISEASE_PROFILES.items():
        match_count = 0

        # Loop: Check how many selected symptoms match the current disease profile
        for symptom in info["symptoms"]:
            if symptom in selected_symptoms:
                match_count += 1

        # Mathematical Operations: Calculate percentage-based risk score
        total_symptoms = len(info["symptoms"])
        base_score = (match_count / total_symptoms) * 100

        # Apply multiplier based on family history risk factors
        if family_history:
            final_score = base_score * info["risk_multiplier"]
        else:
            final_score = base_score

        # Cap the score at 100% maximum using pure Python's min()
        final_score = min(final_score, 100.0)

        # Conditionals: Evaluate the calculated risk category
        if final_score >= 70:
            st.error(
                f"High Risk for {disease} ({final_score:.1f}% Match score)."
            )
            high_risk_detected = True
            diseases_to_monitor.append(disease)
        elif 30 <= final_score < 70:
            st.warning(
                f"Moderate Risk for {disease} ({final_score:.1f}% Match score)."
            )
            diseases_to_monitor.append(disease)
        else:
            st.success(
                f"Low Risk for {disease} ({final_score:.1f}% Match score)."
            )

    # General screening conditional output
    if high_risk_detected:
        st.error(
            "AfyaBot Recommendation: Your risk profile is elevated. Please consult a qualified medical professional immediately."
        )
    elif len(selected_symptoms) == 0:
        st.info("No symptoms selected. You maintain a healthy baseline.")
    else:
        st.info(
            "AfyaBot Recommendation: Keep monitoring your symptoms and maintain routine health checkups."
        )

    # Store findings in session state so the monitoring section updates immediately
    st.session_state["diseases_to_monitor"] = diseases_to_monitor

st.divider()

# New Section: How to Monitor the Disease
st.subheader("Disease Monitoring Guide")
st.write(
    "Select a condition below to find out how to track and monitor it effectively over time:"
)

# Allow manual selection, but pre-focus if analysis flagged a specific condition
available_monitoring_keys = list(MONITORING_GUIDELINES.keys())
selected_monitor_disease = st.selectbox(
    "Choose a condition to monitor:", available_monitoring_keys
)

# Fetch guidelines from dictionary using selected disease key
st.write(f"**Recommended monitoring actions for {selected_monitor_disease}:**")
guidelines = MONITORING_GUIDELINES[selected_monitor_disease]

# Loop: Output individual checklist items for disease tracking
for index, step in enumerate(guidelines):
    st.checkbox(step, key=f"monitor_{selected_monitor_disease}_{index}")

st.divider()

# Section: Paired Q&A Portal
st.subheader("AfyaBot Knowledge Base")
st.write("Select a question below to instantly view its corresponding medical answer:")

selected_question = st.selectbox(
    "Choose a question:", list(HEALTH_KNOWLEDGE_BASE.keys())
)

st.markdown("**Answer:**")
if selected_question == "Select a question...":
    st.info(HEALTH_KNOWLEDGE_BASE[selected_question])
else:
    st.success(HEALTH_KNOWLEDGE_BASE[selected_question])

st.divider()

# Disclaimer notice
st.caption(
    "Disclaimer: AfyaBot is an AI-powered screening tool meant for educational purposes only. It does not replace professional medical advice, diagnosis, or treatment."
)
