import streamlit as st
st.title("WELCOME")
name = st.text_input("Enter your name")
if name:
  st.write(f"Hello, {name}! Welcome to the app")

<!DOCTYPE html>
<html>
<head>
    <title>MediCore Chatbot</title>
    <link rel="stylesheet" href="styles.css">
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
    <script src="script.js"></script>
</body>
</html>

/* styles.css */
body {
    font-family: Arial, sans-serif;
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

// script.js
// Add JavaScript for chatbot functionality, button clicks, etc.



