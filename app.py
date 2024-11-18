import streamlit as st

# Set page config
st.set_page_config(page_title="Interactive Quiz Game", page_icon="🎉", layout="centered")

# Quiz questions and answers
questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"], "answer": "Blue Whale"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], "answer": "William Shakespeare"},
    {"question": "What is the boiling point of water?", "options": ["50°C", "100°C", "150°C", "200°C"], "answer": "100°C"},
    {"question": "Which country has the most population?", "options": ["India", "USA", "China", "Russia"], "answer": "China"},
    {"question": "Who painted the Mona Lisa?", "options": ["Vincent Van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"], "answer": "Leonardo da Vinci"},
    {"question": "What is the currency of Japan?", "options": ["Yuan", "Won", "Yen", "Rupee"], "answer": "Yen"},
    {"question": "Which is the smallest ocean?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Arctic"},
    {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
]

# Initialize session state
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answers = []

# Header
st.title("🎉 Welcome to the Interactive Quiz Game!")
st.markdown("**Test your knowledge and see how much you can score!**")

# Show progress bar
total_questions = len(questions)
progress = st.session_state.current_question / total_questions
st.progress(progress)

# Display the quiz
if st.session_state.current_question < total_questions:
    # Get the current question
    current = st.session_state.current_question
    q = questions[current]

    # Display the question
    st.subheader(f"**Question {current + 1} of {total_questions}**")
    st.write(f"**{q['question']}**")

    # Display options as radio buttons
    user_answer = st.radio("Choose your answer:", q["options"], key=f"q{current}")

    # Submit button
    submit_button = st.button("Submit", key=f"submit{current}")

    if submit_button:
        # Check the answer and update the score
        if user_answer == q["answer"]:
            st.session_state.score += 1

        # Save the user's answer
        st.session_state.answers.append({"question": q["question"], "user_answer": user_answer, "correct_answer": q["answer"]})

        # Update session state for the next question
        st.session_state.current_question += 1
else:
    # If the quiz is completed, display the final score
    st.header("🎉 Quiz Completed!")
    st.write(f"Your total score is: **{st.session_state.score}/{total_questions}**")

    if st.session_state.score == total_questions:
        st.balloons()
        st.success("🌟 Excellent! You nailed it!")
    elif st.session_state.score >= total_questions // 2:
        st.info("✨ Good Job! Keep practicing!")
    else:
        st.warning("👀 Better luck next time!")

    # Show answers with green for correct and red for incorrect
    st.write("### Your Answers")
    for i, answer_info in enumerate(st.session_state.answers):
        question = answer_info["question"]
        user_answer = answer_info["user_answer"]
        correct_answer = answer_info["correct_answer"]

        # Determine the color
        color = "green" if user_answer == correct_answer else "red"

        # Display the question and answers with color coding
        st.markdown(
            f"""
            **Q{i+1}: {question}**  
            - Your Answer: <span style="color:{color};">{user_answer}</span>  
            - Correct Answer: <span style="color:green;">{correct_answer}</span>
            """,
            unsafe_allow_html=True,
        )

    # Restart button
    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answers = []
