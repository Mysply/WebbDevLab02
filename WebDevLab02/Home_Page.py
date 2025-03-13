import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Home - Bluey's Portfolio", page_icon="🐶", layout="wide")

# --- SIDEBAR NAVIGATION ---
from streamlit_extras.switch_page_button import switch_page

st.sidebar.title("🔗 Navigate")
if st.sidebar.button("🏠 Home"):
    switch_page("Home_Page")
if st.sidebar.button("📊 Data Exploration"):
    switch_page("PhaseII")


# --- HEADER ---
st.title("🏡 Welcome to Bluey's Portfolio!")
st.write("This web app showcases my journey, experience, and projects at Georgia Tech. Explore my portfolio and data page!")

# --- COURSE INFO ---
st.header("📖 Course Information")
st.write("**Full Name:** Bluey the Cattle Pup")
st.write("**Course:** CS 1301 - Introduction to Computing")

# --- PAGE DESCRIPTIONS ---
st.header("🌟 Explore My Pages")
st.write("**📂 Portfolio Page:** Displays my background, education, experience, and projects.")
st.write("**📊 Data Page:** A dynamic page with interactive data visualizations and user input.")
