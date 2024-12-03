import streamlit as st
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from scipy.spatial.distance import cdist

def show_recommender():
    st.title("Find the Right Skin Care for You")
    
    st.write("We are very excited to help you choose the right product for your skin! 🙇‍♂️")
    
    # Load the data
    skincare = pd.read_csv("./data/cosmetics.csv")

    # Choose a product category
    category = st.selectbox(label='Select a product category', options=skincare['Label'].unique())
    category_subset = skincare[skincare['Label'] == category]

    # Choose a brand
    brand = st.selectbox(label='Select a brand', options=sorted(category_subset['Brand'].unique()))
    category_brand_subset = category_subset[category_subset['Brand'] == brand]

    # Choose product
    product = st.selectbox(label='Select the product', options=sorted(category_brand_subset['Name'].unique()))

    # Recommendation logic (copied from your original code)
    def oh_encoder(tokens):
        x = np.zeros(N)
        for ingredient in tokens:
            idx = ingredient_idx[ingredient]
            x[idx] = 1
        return x

    def closest_point(point, points):
        return points[cdist([point], points).argmin()]

    if product:
        category_subset = category_subset.reset_index(drop=True)
        ingredient_idx = {}
        corpus = []
        idx = 0

        for i in range(len(category_subset)):    
            ingredients = category_subset['Ingredients'][i]
            tokens = ingredients.lower().split(', ')
            corpus.append(tokens)
            for ingredient in tokens:
                if ingredient not in ingredient_idx:
                    ingredient_idx[ingredient] = idx
                    idx += 1

        M = len(category_subset)
        N = len(ingredient_idx)
        A = np.zeros((M, N))

        for i, tokens in enumerate(corpus):
            A[i, :] = oh_encoder(tokens)

        model_run = st.button('Find similar products!')

        if model_run:
            st.write('Here are the top 10 similar products:')
            
            model = TSNE(n_components=2, learning_rate=150, random_state=42)
            tsne_features = model.fit_transform(A)
            category_subset['X'] = tsne_features[:, 0]
            category_subset['Y'] = tsne_features[:, 1]

            target = category_subset[category_subset['Name'] == product]
            target_x = target['X'].values[0]
            target_y = target['Y'].values[0]

            skincare1 = pd.DataFrame()
            skincare1['point'] = [(x, y) for x, y in zip(category_subset['X'], category_subset['Y'])]

            category_subset['distance'] = [
                cdist(np.array([[target_x, target_y]]), np.array([p]), metric='euclidean') 
                for p in skincare1['point']
            ]

            top_matches = category_subset.sort_values(by=['distance']).reset_index(drop=True)
            top_matches = top_matches.iloc[1:]  # Exclude the selected product
            st.dataframe(top_matches.head(10))
