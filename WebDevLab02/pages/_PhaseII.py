import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Bluey's Adventures", page_icon="📊", layout="wide")

# --- PAGE HEADER ---
st.title("📊 Bluey's Adventures & Fun Data!")
st.write("Explore interactive data visualizations about Bluey, her activities, and favorite moments!")

# --- LOAD DATA ABOUT BLUEY ---
bluey_data = {
    "category": ["Games", "Family Time", "Adventures", "School Activities", "Helping Others"],
    "subcategory": ["Keepy Uppy", "Playing with Bingo", "Camping", "Art Class", "Helping Dad"],
    "fun_level": [95, 100, 90, 85, 80]  # Rating out of 100
}
df = pd.DataFrame(bluey_data)

# --- USER INPUT (INTERACTIVE ELEMENTS) ---
st.sidebar.header("🔧 Customize View")

# Use session state to remember selected category
if "selected_category" not in st.session_state:
    st.session_state.selected_category = df["category"].unique()[0]  # Default to first

st.session_state.selected_category = st.sidebar.selectbox(
    "Select Category", df["category"].unique(),
    index=list(df["category"].unique()).index(st.session_state.selected_category)  # Maintain selection
)

fun_level_filter = st.sidebar.slider("Minimum Fun Level", min_value=0, max_value=100, value=50)  # NEW

# --- FILTER DATA BASED ON USER INPUT ---
filtered_data = df[(df["category"] == st.session_state.selected_category) & (df["fun_level"] >= fun_level_filter)]

# --- DISPLAY DATA ---
st.subheader(f"Filtered Adventures: {st.session_state.selected_category}")
st.dataframe(filtered_data)  # NEW

# --- STATIC DATA VISUALIZATION ---
st.subheader("📊 Fun Level Comparison")
fig, ax = plt.subplots()
df.groupby("category")["fun_level"].mean().plot(kind="bar", ax=ax, color="skyblue")
ax.set_ylabel("Fun Level (0-100)")
st.pyplot(fig)

# --- DYNAMIC DATA VISUALIZATION ---
st.subheader("📈 Fun Trends Over Time")
fig2, ax2 = plt.subplots()
filtered_data.plot(x="subcategory", y="fun_level", kind="line", ax=ax2, marker='o', linestyle='-', color='orange')
ax2.set_ylabel("Fun Level (0-100)")
st.pyplot(fig2)  # Dynamic visualization
