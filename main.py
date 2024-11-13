import streamlit as st

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

# Initializing score and interpretation variables for final page access
SE_score, SE_interpretation = None, None
TA_score, TA_interpretation = None, None
DE_score, DE_interpretation = None, None

# ---------------- Rosenberg Self-Esteem Scale Page ----------------
if st.session_state.page == 1:
    # Define Rosenberg Scale questions
    questions = [
        "I feel that I am a person of worth, at least on an equal plane with others.",
        "I feel that I have a number of good qualities.",
        "All in all, I am inclined to feel that I am a failure.",
        "I am able to do things as well as most other people.",
        "I feel I do not have much to be proud of.",
        "I take a positive attitude toward myself.",
        "On the whole, I am satisfied with myself.",
        "I wish I could have more respect for myself.",
        "I certainly feel useless at times.",
        "At times I think I am no good at all."
    ]

    st.title("Rosenberg Self-Esteem Scale")
    st.write("Please rate your agreement with each statement from 1 (Strongly Disagree) to 4 (Strongly Agree).")

    # Gather user input
    SE_responses = [st.slider(question, 1, 4, 2) for question in questions]

    # Calculate score
    def calculate_rosenberg_score(SE_responses):
        reverse_indices = [2, 4, 7, 8, 9]
        return sum(5 - SE_responses[i] if i in reverse_indices else SE_responses[i] for i in range(len(SE_responses)))

    # Score interpretation
    def interpret_rosenberg_score(SE_score):
        if SE_score >= 30:
            return "High self-esteem"
        elif 15 <= SE_score < 30:
            return "Average self-esteem"
        else:
            return "Low self-esteem"

    # Calculate and interpret Rosenberg score on the final page
    SE_score = calculate_rosenberg_score(SE_responses)
    SE_interpretation = interpret_rosenberg_score(SE_score)
    
    if st.button("Next"):
        next_page()

# ---------------- STAI-YB Trait Anxiety Scale Page ----------------
elif st.session_state.page == 2:
    # Define STAI-YB questions
    questions = [
        "I feel pleasant.",
        "I feel nervous and restless.",
        "I feel satisfied with myself.",
        "I wish I could be as happy as others seem to be.",
        "I feel like a failure.",
        "I feel rested.",
        "I am calm, cool, and collected.",
        "I feel that difficulties are piling up so I cannot overcome them.",
        "I worry too much over something that doesn’t really matter.",
        "I am happy.",
        "I have disturbing thoughts.",
        "I lack self-confidence.",
        "I feel secure.",
        "I make decisions easily.",
        "I feel inadequate.",
        "I am content.",
        "Some unimportant thought runs through my mind and bothers me.",
        "I take disappointments so keenly that I can’t put them out of my mind.",
        "I am a steady person.",
        "I get in a state of tension or turmoil as I think over my recent concerns and interests."
    ]

    st.title("STAI-YB Trait Anxiety Scale")
    st.write("Please rate your agreement with each statement from 1 (Almost Never) to 4 (Almost Always).")

    # Gather user input
    TA_responses = [st.slider(question, 1, 4, 2) for question in questions]

    # Calculate score
    def calculate_stai_score(TA_responses):
        reverse_indices = [0, 2, 5, 6, 9, 12, 13, 15, 18]
        return sum(5 - TA_responses[i] if i in reverse_indices else TA_responses[i] for i in range(len(TA_responses)))

    # Score interpretation
    def interpret_stai_score(TA_score):
        if TA_score >= 45:
            return "High trait anxiety"
        elif 36 <= TA_score < 45:
            return "Moderate trait anxiety"
        else:
            return "Low trait anxiety"

    # Calculate and interpret STAI score on the final page
    TA_score = calculate_stai_score(TA_responses)
    TA_interpretation = interpret_stai_score(TA_score)
    
    if st.button("Next"):
        next_page()

# ---------------- PHQ-9 Depression Scale ----------------
elif st.session_state.page == 3:
    # Define PHQ-9 questions
    questions = [
        "Little interest or pleasure in doing things.",
        "Feeling down, depressed, or hopeless.",
        "Trouble falling or staying asleep, or sleeping too much.",
        "Feeling tired or having little energy.",
        "Poor appetite or overeating.",
        "Feeling bad about yourself — or that you are a failure or have let yourself or your family down.",
        "Trouble concentrating on things, such as reading the newspaper or watching television.",
        "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual.",
        "Thoughts that you would be better off dead, or thoughts of hurting yourself in some way."
    ]

    st.title("PHQ-9 Depression Assessment")
    st.write("""
    The Patient Health Questionnaire-9 (PHQ-9) is a clinical tool used to assess the severity of depression. Please rate how often you have been bothered by each of the following problems over the past two weeks.
    - 0: Not at all
    - 1: Several days
    - 2: More than half the days
    - 3: Nearly every day
    """)

    # Gather user input
    DE_responses = [st.slider(question, 0, 3, 0) for question in questions]

    # Calculate score
    def calculate_phq9_score(DE_responses):
        return sum(DE_responses)

    # Score interpretation
    def interpret_phq9_score(DE_score):
        if DE_score >= 20:
            return "Severe depression"
        elif 15 <= DE_score < 20:
            return "Moderately severe depression"
        elif 10 <= DE_score < 15:
            return "Moderate depression"
        elif 5 <= DE_score < 10:
            return "Mild depression"
        else:
            return "Minimal or no depression"

    # Calculate and interpret PHQ-9 score on the final page
    DE_score = calculate_phq9_score(DE_responses)
    DE_interpretation = interpret_phq9_score(DE_score)
    
    if st.button("Next"):
        next_page()

# ---------------- Scores and interpretations ----------------
elif st.session_state.page == 4:
    st.title("Results Summary")
    
    st.write(f"Your Rosenberg Self-Esteem Score is: {SE_score}")
    st.write(f"Interpretation: {SE_interpretation}")
    
    st.write(f"Your STAI-YB Trait Anxiety Score is: {TA_score}")
    st.write(f"Interpretation: {TA_interpretation}")
    
    st.write(f"Your PHQ-9 Score is: {DE_score}")
    st.write(f"Interpretation: {DE_interpretation}")
