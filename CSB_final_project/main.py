import streamlit as st
from homepage import show_homepage
from recommender import show_recommender
from skin_recommendations import show_skin_recommendations

# Set page configuration
st.set_page_config(page_title="Skincare App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Homepage", "Recommender", "Skin Type Recommendations"])

# Render pages based on selection
if page == "Homepage":
    show_homepage()
elif page == "Recommender":
    show_recommender()
elif page == "Skin Type Recommendations":
    show_skin_recommendations()
