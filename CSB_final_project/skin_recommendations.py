import streamlit as st
import pandas as pd

def show_skin_recommendations():
    st.title("Skin Type Ingredient Recommendations")
    
    # Define the ingredients for each skin type
    skin_type_ingredients = {
        "Normal Skin": ["Vitamin C", "Hyaluronic Acid", "Niacinamide", "Peptides", "Squalane", "Panthenol (Pro-Vitamin B5)"],
        "Dry Skin": ["Ceramides", "Shea Butter", "Glycerin", "Hyaluronic Acid", "Lactic Acid", "Urea"],
        "Oily Skin": ["Salicylic Acid", "Tea Tree Oil", "Clay", "Witch Hazel", "Niacinamide", "Retinol"],
        "Combination Skin": ["Niacinamide", "Jojoba Oil", "Green Tea Extract", "Aloe Vera", "Hyaluronic Acid", "Chamomile"],
        "Sensitive Skin": ["Aloe Vera", "Colloidal Oatmeal", "Chamomile", "Centella Asiatica", "Licorice Root Extract", "Allantoin"],
    }

    # Convert the dictionary to a DataFrame for better display
    ingredients_df = pd.DataFrame.from_dict(
        skin_type_ingredients, orient='index', 
        columns=["Ingredient 1", "Ingredient 2", "Ingredient 3", "Ingredient 4", "Ingredient 5", "Ingredient 6"]
    )
    ingredients_df.index.name = "Skin Type"

    # Display the table
    st.write("Below are the recommended ingredients for each skin type:")
    st.table(ingredients_df)
