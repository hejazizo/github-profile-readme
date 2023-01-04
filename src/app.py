import streamlit as st
from pathlib import Path
from src.github_profile import generate_profile

st.title(":zap: Github Profile Readme Generator")

# Personal Info
kwargs = {}
st.header("Personal Info")
with st.expander("Personal Info"):
    col1, col2 = st.columns(2)
    kwargs["name"] = col1.text_input("Name")
    kwargs["email"] = col2.text_input("Email")
    kwargs["phone"] = col1.text_input("Phone")
    kwargs["homepage"] = col2.text_input("Homepage")
    kwargs["location"] = col1.text_input("Location")

# Social Media
st.header("Social Media")
with st.expander("Social Media"):
    st.markdown("Enter your social media usernames (not links):")
    col1, col2 = st.columns(2)
    kwargs["github"] = col1.text_input("Github")
    kwargs["linkedin"] = col2.text_input("Linkedin")
    kwargs["twitter"] = col1.text_input("Twitter")
    kwargs["facebook"] = col2.text_input("Facebook")
    kwargs["instagram"] = col1.text_input("Instagram")
    kwargs["youtube"] = col2.text_input("Youtube")
    kwargs["medium"] = col1.text_input("Medium")

# Extensions
st.header("Extensions")
with st.expander("Extensions"):
    if st.checkbox("Show Github Stats"):
        kwargs["github_stats"] = st.text_input("Github Stats Username:")

# Select Theme
st.header("Theme")
themes = Path("src/themes").iterdir()
themes = [theme.name for theme in themes]
theme = st.selectbox("Select Theme", themes)
st.markdown(f"Selected Theme: **{theme}**")

# Generate Readme
st.header("Readme")
profile = generate_profile(theme, **kwargs)
st.text("Copy the code below and paste it in your README.md file")
st.code(profile)
