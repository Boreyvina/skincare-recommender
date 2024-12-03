import streamlit as st

def show_homepage():
    st.title("Welcome to the Skincare Recommendation System! 🌟")
    
    # Add homepage content
    st.write(
        """
        This application helps you find the perfect skincare products tailored to your skin type.
        Navigate to the **Recommender** page to get started!
        """
    )

    # Optionally, add visuals or background
    st.image("./images/background.jpg", use_container_width=True)
    st.markdown("### Why Choose Us?")
    st.write("""
    - Personalized recommendations.
    - Expert-curated ingredient analysis.
    - Easy to use!
    """)

    st.write("Navigate using the sidebar to begin your journey. 😊")
