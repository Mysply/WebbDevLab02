import os
import streamlit as st

# --- Bluey Themed Profile ---
profile_picture = "/mount/src/webbdevlab02/WebDevLab02/Images/bluey.png"


about_me = """
I'm Bluey, a playful and curious Australian cattle pup! I love playing games, learning new things, 
and solving fun problems. I'm currently a student at Georgia Tech, pursuing a Bachelor of Science in Computer Science. 
My goal is to combine creativity with technology to build fun and interactive learning tools!
"""

# --- Contact Information ---
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

my_linkedin_url = "https://www.linkedin.com/pulse/bluey-impact-diana-kelter-1afvc/"
my_github_url = "https://github.com/bluey-tech"
my_email_address = "bluey@georgiatech.edu"

# --- Education Data ---
education_data = {
    "Degree": "Bachelor of Science in Computer Science",
    "Institution": "Georgia Institute of Technology",
    "Location": "Atlanta, GA",
    "Graduation Date": "May 2025",
    "GPA": "3.5"
}

# --- Relevant Courses ---
course_data = {
    "code": ["CS 1301", "CS 1331", "MATH 1554", "CS 2050"], 
    "names": ["Intro to CS", "Intro to OOP", "Linear Algebra", "Discrete Mathematics"], 
    "semester_taken": ["2nd", "3rd", "2nd", "2nd"],
    "skills": [
        "Learning Python with games",
        "Exploring OOP concepts in Java",
        "Mastering linear transformations",
        "Understanding discrete logic and proofs"
    ]
}

experience_data = {
    "Game Inventor": (
        [
            "- Designed over 50 unique and fun games for my friends and family",
            "- Developed a unique storytelling app to accompany game rules",
            "- Created digital versions of some popular games in Python"
        ],
        "/mount/src/webbdevlab02/WebDevLab02/Images/blueygaming.jpeg"  # ✅ Fixed path
    ),
    "Junior Coder at TechPups": (
        [
            "- Assisted in building a collaborative app for kids to learn coding",
            "- Helped organize coding workshops for young learners",
            "- Implemented fun animations in Python for educational purposes"
        ],
        "/mount/src/webbdevlab02/WebDevLab02/Images/blueycoding.jpeg"  # ✅ Fixed path
    ),
    "Family Helper": (
        [
            "- Managed small tech-related tasks at home",
            "- Designed a chore management system for siblings using Python",
            "- Learned leadership and teamwork by helping Bingo and friends"
        ],
        "/mount/src/webbdevlab02/WebDevLab02/Images/blueyhelping.jpeg"  # ✅ Fixed path
    ),
}


# --- Projects ---
projects_data = {
    "Game Maker App": "Designed a game-making app for kids, with interactive rules and colorful animations.",
    "Coding with Bluey": "Built an educational coding tool with fun mini-games for young learners."
}

# --- Technical Skills ---
programming_data = {
    "Python": 80,  # Proficiency in percentage
    "Java": 70,
    "Scratch": 90,
}
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "Scratch": "🖌️",
}

# --- Spoken Languages ---
spoken_data = {
    "English": "Fluent",
    "French": "Intermediate",
    "Spanish": "Beginner",
}
spoken_icons = {
    "English": "🇬🇧",
    "French": "🇫🇷",
    "Spanish": "🇪🇸"
}

# --- Leadership & Activities ---
leadership_data = {
    "Game Night Organizer": (
        [
            "- Organized weekly game nights for family and friends",
            "- Designed schedules and activities to ensure everyone had fun"
        ],
        "Images/blueyleader.jpeg"
    )
}

activity_data = {
    "Play Club with Bingo and Friends": [
        "- Created new games like 'Magic Asparagus' and 'Keepy Uppy'",
        "- Hosted storytelling sessions for all members"
    ]
}
