import streamlit as st

# HTML Content using st.markdown
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>MediCore Chatbot</title>
    <style>
        body {
            font-family: Elegant, sans-serif;
            text-align: center;
            background-color: #f0f0f0;
        }
        header {
            background-color: #3498db;
            color: white;
            padding: 20px;
        }
        blockquote {
            font-style: italic;
            margin: 20px;
        }
        .features {
            list-style: none;
            padding: 0;
        }
        button {
            background-color: #3498db;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        footer {
            background-color: #3498db;
            color: white;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>MediCore</h1>
        <p>Hi, I'm Medi! Here to help you.</p>
    </header>
    <main>
        <blockquote cite="Lisa Olivera">
            "Just because no one else can heal or do your inner work for you doesn't mean you can, should, or need to do it alone."
        </blockquote>
        <ul class="features">
            <li>Symptom Checking</li>
            <li>24/7 Availability</li>
            <li>100% Confidentiality</li>
        </ul>
        <button>Sign Up</button>
    </main>
    <footer>
        <p>Your mental health matters!</p>
    </footer>
</body>
</html>
"""

st.markdown(html_content, unsafe_allow_html=True)


# Display motivational messages
st.markdown('<div class="centered-text">Daily Motivation 💬</div>', unsafe_allow_html=True)
st.markdown('<div class="centered-text">You are stronger than you think. Take it one step at a time.</div>', unsafe_allow_html=True)

# Title and welcome message
st.title("MediCore Chatbot 💡")
st.write("Welcome to MediCore! I’m Medi, your digital mental health companion — here to support you with empathetic conversations.")

# Sidebar for selecting symptoms
st.sidebar.subheader('Symptom Checker 🩺')
selected_symptom = st.sidebar.radio(
    "How do you feel today?",
    ('😔 Feeling Anxious', '😞 Feeling Depressed', '😓 Feeling Stressed', '🛌 Trouble Sleeping', '🤕 Physical Symptoms')
)

# Main content form for asking questions
with st.form(key='question_form'):
    question = st.text_input("How can I help you?")
    submit_button = st.form_submit_button(label='Send')

# Handle form submission
if submit_button:
    if question:
        # Get response from the chatbot based on the question and selected symptoms
        answer = get_response(selected_symptom, question)
        st.write("### Answer")
        st.write(answer)
        # Play a sound notification after getting the answer
        playsound('notification_sound.mp3')
    else:
        st.write("Please enter a question.")

# Footer with additional information
st.markdown(
    """
    <hr>
    <footer>
    <div class="centered-text">
    <p>Created by the Innovative Sparks. This chatbot does not replace human interaction. Seek help from nearby facilities.</p>
    </div>
    </footer>
    """,
    unsafe_allow_html=True
)




