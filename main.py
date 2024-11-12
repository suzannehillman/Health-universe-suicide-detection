import streamlit as st

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

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
    responses = [st.slider(question, 1, 4, 2) for question in questions]

    # Calculate score
    def calculate_rosenberg_score(responses):
        reverse_indices = [2, 4, 7, 8, 9]
        score = sum(5 - responses[i] if i in reverse_indices else responses[i] for i in range(len(responses)))
        return score

    # Score interpretation
    def interpret_rosenberg_score(score):
        if score >= 30:
            return "High self-esteem"
        elif 15 <= score < 30:
            return "Average self-esteem"
        else:
            return "Low self-esteem"

    # Display the results and "Next" button
    if st.button("Calculate Self-Esteem Score"):
        score = calculate_rosenberg_score(responses)
        interpretation = interpret_rosenberg_score(score)
        st.write(f"Your Rosenberg Self-Esteem Score is: {score}")
        st.write(f"Interpretation: {interpretation}")
    
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
    responses = [st.slider(question, 1, 4, 2) for question in questions]

    # Calculate score
    def calculate_stai_score(responses):
        reverse_indices = [0, 2, 5, 6, 9, 12, 13, 15, 18]
        score = sum(5 - responses[i] if i in reverse_indices else responses[i] for i in range(len(responses)))
        return score

    # Score interpretation
    def interpret_stai_score(score):
        if score >= 45:
            return "High trait anxiety"
        elif 36 <= score < 45:
            return "Moderate trait anxiety"
        else:
            return "Low trait anxiety"

    # Display the results and "Next" button
    if st.button("Calculate Trait Anxiety Score"):
        score = calculate_stai_score(responses)
        interpretation = interpret_stai_score(score)
        st.write(f"Your STAI-YB Trait Anxiety Score is: {score}")
        st.write(f"Interpretation: {interpretation}")
    
    if st.button("Next"):
        next_page()

elif st.session_state.page == 2:
# Define PHQ-9 questions and scoring function
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
responses = []
for i, question in enumerate(questions):
		response = st.slider(question, 0, 3, 0)
		responses.append(response)

# Calculate score
def calculate_phq9_score(responses):
		return sum(responses)

# Score interpretation
def interpret_score(score):
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

# Display the results
if st.button("Calculate Depression Severity Score"):
	score = calculate_phq9_score(responses)
	interpretation = interpret_score(score)
	st.write(f"Your PHQ-9 Score is: {score}")
	st.write(f"Interpretation: {interpretation}")
