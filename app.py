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

from PIL import Image

def main():
    # Set page configuration
    st.set_page_config(
        page_title="MediCore Chatbot",
        page_icon="😊",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Load background image (optional)
    # background_img = Image.open("background.jpg")
    # st.image(background_img, use_column_width=True)

    # Header
    st.title("MediCore")
    st.subheader("Hi, I am Medi. Your empathetic mental health companion")

    # Feeling buttons
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("Feeling Anxious")
    with col2:
        st.button("Feeling Depressed")
    with col3:
        st.button("Feeling Stressed")
    with col4:
        st.button("Trouble Sleeping")

    # Chat history
    st.text_area("Chat History", height=200)

    # User input
    user_input = st.text_input("Type your message")

    # Footer
    st.markdown("---")
    st.text("Created by the Innovative Sparks. This chatbot does not replace human interaction. Seek help from nearby facilities.")

    # Custom CSS (optional)
    st.markdown('<style>body {background-color: #f0f0f0;}</style>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()



