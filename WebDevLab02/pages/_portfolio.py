from info import (
    profile_picture, about_me,
    linkedin_image_url, github_image_url, email_image_url,
    my_linkedin_url, my_github_url, my_email_address,
    education_data, course_data, experience_data,
    projects_data, programming_data, programming_icons,
    spoken_data, spoken_icons, leadership_data, activity_data
)

import streamlit as st

st.set_page_config(page_title="Bluey's Portfolio", page_icon="🐶", layout="wide")

# --- HEADER SECTION ---
st.title("🐶 Bluey's Portfolio")
st.image(profile_picture, width=200)  # ✅ No 'info.profile_picture'
st.write(about_me)

# --- SIDEBAR CONTACT INFO ---
st.sidebar.header("📬 Connect with Me")
st.sidebar.image(linkedin_image_url, width=50)
st.sidebar.markdown(f"[LinkedIn]({my_linkedin_url})")
st.sidebar.image(github_image_url, width=50)
st.sidebar.markdown(f"[GitHub]({my_github_url})")
st.sidebar.image(email_image_url, width=50)
st.sidebar.markdown(f"[Email](mailto:{my_email_address})")

# --- EDUCATION ---
st.header("🎓 Education")
st.write(
    f"**{education_data['Degree']}**\n"
    f"{education_data['Institution']} - {education_data['Location']}\n"
    f"Graduation: {education_data['Graduation Date']} | GPA: {education_data['GPA']}"
)

# --- EXPERIENCE ---
st.header("💼 Experience")
for role, (desc, img) in experience_data.items():
    st.subheader(role)
    st.image(img, width=200)
    for bullet in desc:
        st.write(f"- {bullet}")

# --- PROJECTS ---
st.header("🚀 Projects")

# Portfolio Description
st.subheader("🐶 Bluey's Portfolio")
st.write("This portfolio showcases Bluey's background, education, experience, and fun projects!")

# Data Page Description (REQUIRED)
st.subheader("📊 Data Exploration Page")
st.write(
    "This page allows users to explore interactive data visualizations about Bluey's activities. "
    "Users can select different categories, filter fun levels, and analyze trends dynamically."
)

# --- PROGRAMMING SKILLS ---
st.header("💻 Programming Skills")
for skill, level in programming_data.items():
    st.write(f"{programming_icons[skill]} **{skill}**: {level}% Proficiency")
    st.progress(level / 100)

# --- SPOKEN LANGUAGES ---
st.header("🗣️ Spoken Languages")
for lang, fluency in spoken_data.items():
    st.write(f"{spoken_icons[lang]} **{lang}** - {fluency}")

# --- LEADERSHIP ---
st.header("🌟 Leadership & Activities")
for role, (desc, img) in leadership_data.items():
    st.subheader(role)
    st.image(img, width=200)
    for bullet in desc:
        st.write(f"- {bullet}")

# --- NAVIGATION TO MULTI-PAGE APP ---
st.sidebar.title("🔗 Navigate")
from streamlit_extras.switch_page_button import switch_page
if st.sidebar.button("🏠 Home"):
    switch_page("Home_Page")
if st.sidebar.button("📊 Data Exploration"):
    switch_page("PhaseII")
