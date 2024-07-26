%%writefile app.py

import streamlit as st
st.titles("WELCOME")
name = st.text_input("Enter your name")
if name:
  st.write(f"Hello, {name}! Welcome to the app")
