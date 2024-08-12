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

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Initialize chat history
chat_history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_message = request.form['user_message']
        chat_history.append({'user': user_message})

        # Replace this with your chatbot logic to generate a response
        bot_response = "I'm still under development. Please try again later."
        chat_history.append({'bot': bot_response})

    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html>
<head>
    <title>MediCore Chatbot</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>MediCore</h1>
        <p>Hi, I am Medi. Your empathetic mental health companion</p>
    </header>
    <div class="buttons">
        <button>Feeling Anxious</button>
        <button>Feeling Depressed</button>
        <button>Feeling Stressed</button>
        <button>Trouble Sleeping</button>
    </div>
    <div class="chat-history">
        {% for message in chat_history %}
            <div class="message {{ message.type }}">
                {{ message.text }}
            </div>
        {% endfor %}
    </div>
    <form method="post">
        <input type="text" name="user_message" placeholder="Type your message">
        <button type="submit">Send</button>
    </form>
    <footer>
        Created by the Innovative Sparks. This chatbot does not replace human interaction.
        Seek help from nearby facilities.
    </footer>
</body>
</html>






