import streamlit as st

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

# ---------------- Rosenberg Self-Esteem Scale Page ----------------
if st.session_state.page == 1:
    # initialize session state for scores and interpretations
    if 'SE_score' not in st.session_state:
        st.session_state.SE_score = ""
    if 'SE_interpretation' not in st.session_state:
        st.session_state.SE_interpretation = ""

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

    # Gather user input, but first set it to null
    responses = [st.slider(question, 1, 4, 2) for question in questions]

    # Calculate score
    def calculate_rosenberg_score(responses):
        reverse_indices = [2, 4, 7, 8, 9]
        return sum(5 - responses[i] if i in reverse_indices else responses[i] for i in range(len(responses)))

    # Score interpretation
    def interpret_rosenberg_score(score):
        if score >= 30:
            return "High self-esteem"
        elif 15 <= score < 30:
            return "Average self-esteem"
        else:
            return "Low self-esteem"

    # Calculate and interpret Rosenberg score on the final page
    st.session_state.SE_score = calculate_rosenberg_score(responses)
    st.session_state.SE_interpretation = interpret_rosenberg_score(st.session_state.SE_score)
    
    if st.button("Next"):
        next_page()

# ---------------- STAI-YB Trait Anxiety Scale Page ----------------
elif st.session_state.page == 2:
    # initialize session state for scores and interpretations
    if 'TA_score' not in st.session_state:
        st.session_state.TA_score = ""
    if 'TA_interpretation' not in st.session_state:
        st.session_state.TA_interpretation = ""

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
    responses = [st.slider(question, 1, 4, 2) for question in questions]

    # Calculate score
    def calculate_stai_score(responses):
        reverse_indices = [0, 2, 5, 6, 9, 12, 13, 15, 18]
        return sum(5 - responses[i] if i in reverse_indices else responses[i] for i in range(len(responses)))

    # Score interpretation
    def interpret_stai_score(score):
        if score >= 45:
            return "High trait anxiety"
        elif 36 <= score < 45:
            return "Moderate trait anxiety"
        else:
            return "Low trait anxiety"

    # Calculate and interpret STAI score on the final page
    st.session_state.TA_score = calculate_stai_score(responses)
    st.session_state.TA_interpretation = interpret_stai_score(st.session_state.TA_score)
    
    if st.button("Next"):
        next_page()

# ---------------- PHQ-9 Depression Scale ----------------
elif st.session_state.page == 3:
        # initialize session state for scores and interpretations
    if 'DE_score' not in st.session_state:
        st.session_state.DE_score = ""
    if 'DE_interpretation' not in st.session_state:
        st.session_state.DE_interpretation = ""

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
    responses = [st.slider(question, 0, 3, 0) for question in questions]

    # Calculate score
    def calculate_phq9_score(responses):
        return sum(responses)

    # Score interpretation
    def interpret_phq9_score(score):
        if score >= 20:
            return "Severe depression"
        elif 15 <= score < 20:
            return "Moderately severe depression"
        elif 10 <= score < 15:
            return "Moderate depression"
        elif 5 <= score < 10:
            return "Mild depression"
        else:
            return "Minimal or no depression"

    # Calculate and interpret PHQ-9 score on the final page
    st.session_state.DE_score = calculate_phq9_score(responses)
    st.session_state.DE_interpretation = interpret_phq9_score(st.session_state.DE_score)
    
    if st.button("Next"):
        next_page()

# ---------------- Scores and interpretations ----------------
elif st.session_state.page == 4:
    #grab the scores and interpretations from session state
    SE_score = st.session_state.get("SE_score", "")
    SE_interpretation = st.session_state.get("SE_interpretation", "")
    TA_score = st.session_state.get("TA_score", "")
    TA_interpretation = st.session_state.get("TA_interpretation", "")
    DE_score = st.session_state.get("DE_score", "")
    DE_interpretation = st.session_state.get("DE_interpretation", "")
    st.title("Results Summary")
    
    st.write(f"Your Rosenberg Self-Esteem Score is: {SE_score}")
    st.write(f"Interpretation: {SE_interpretation}")
    
    st.write(f"Your STAI-YB Trait Anxiety Score is: {TA_score}")
    st.write(f"Interpretation: {TA_interpretation}")
    
    st.write(f"Your PHQ-9 Score is: {DE_score}")
    st.write(f"Interpretation: {DE_interpretation}")
