Skincare Recommendation System
This project provides a content-based skincare recommendation system that suggests products based on ingredient similarities. It includes over 1,400 products across six categories: Moisturizer, Cleanser, Face Mask, Treatment, Eye Cream, and Sun Protection. The system uses t-SNE for ingredient visualization and is implemented as an interactive app using Streamlit.

Features
Content-based recommendation engine
Ingredient similarity visualization with t-SNE
Interactive user interface built with Streamlit
Dataset includes 1,400+ skincare products

Installation and Setup
Follow these steps to set up the project on your local device:

Prerequisites
Python 3.8 or later installed
pip package manager installed
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/Boreyvina/skincare-recommender.git
cd skincare-recommender
Step 2: Create a Virtual Environment (Optional but Recommended)
Create and activate a virtual environment to isolate dependencies:

bash
Copy code
# On Windows
python -m venv env
env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate
Step 3: Install Required Dependencies
Install all required Python libraries using the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Step 4: Run the Application
Launch the Streamlit app:

bash
Copy code
streamlit run app.py
This will open the app in your default web browser. If it doesn't open automatically, visit the URL http://localhost:8501 in your browser.

Project Structure
app.py: Main file for running the Streamlit application.
data/: Contains the skincare product dataset.
utils/: Helper functions for processing data and generating recommendations.
requirements.txt: List of required Python packages.
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements or new features.

License
This project is licensed under the MIT License.
