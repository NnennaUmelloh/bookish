import streamlit as st
import pandas as pd

# File path for the CSV
CSV_FILE = "bookreviewsonly.csv"

# Check if the CSV exists, and if not, create it with the appropriate columns
def initialize_csv():
    try:
        df = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        # If the file doesn't exist, create a new one with the necessary columns
        df = pd.DataFrame(columns=["title","author","year published","genre", "rating", "highlights", "lowlights", "final_take", "who_should_read_this_book", "link"])
        df.to_csv(CSV_FILE, index=False)

# Initialize CSV if not already initialized
initialize_csv()

# Function to get all posts
def get_all_posts():
    df = pd.read_csv(CSV_FILE)
    return df.values.tolist()

# Function to get a post by title
def get_post_by_title(title):
    df = pd.read_csv(CSV_FILE)
    post = df[df['Title'] == title]
    return post.iloc[0].values.tolist() if not post.empty else None

# Define some HTML templates for displaying the posts
title_temp = """
<div style="background-color:#F0F4F1;padding:10px;border-radius:10px;margin:10px;border:2px solid #8E7D57;">
<h4 style="color:#4F5B62;text-align:center;">{}</h4>
<h5 style="color:#8E7D57;">Author: {}</h5>
<div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
    <h6 style="color:#4F5B62;">Year Published: {}</h6>
    <h6 style="color:#4F5B62;">Genre: {}</h6>
    <h6 style="color:#4F5B62;">Rating: {}</h6>
</div>
<br/>
<p><strong style="color:#8E7D57;">Highlights:</strong> {}</p>
<p><strong style="color:#8E7D57;">Lowlights:</strong> {}</p>
<p><strong style="color:#8E7D57;">Final Take:</strong> {}</p>
<p><strong style="color:#8E7D57;">Who Should Read This Book:</strong> {}</p>
<a href="{}" target="_blank" style="color:#D1A15F;">Link to Book</a>
<br/>
</div>
"""

post_temp = """
<div style="background-color:#F0F4F1;padding:10px;border-radius:5px;margin:10px;border:2px solid #8E7D57;">
<h4 style="color:#4F5B62;text-align:center;">{}</h4>
<h5 style="color:#8E7D57;">Author: {}</h5>
<div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
    <h6 style="color:#4F5B62;">Year Published: {}</h6>
    <h6 style="color:#4F5B62;">Genre: {}</h6>
    <h6 style="color:#4F5B62;">Rating: {}</h6>
</div>
<br/>
<p><strong style="color:#8E7D57;">Highlights:</strong> {}</p>
<p><strong style="color:#8E7D57;">Lowlights:</strong> {}</p>
<p><strong style="color:#8E7D57;">Final Take:</strong> {}</p>
<p><strong style="color:#8E7D57;">Who Should Read This Book:</strong> {}</p>
<a href="{}" target="_blank" style="color:#D1A15F;">Link to Book</a>
<br/>
</div>
"""



st.title("Book Reviews!")
    
# Get all the posts from the CSV file
posts = get_all_posts()

# Create two columns for side-by-side layout
col1, col2 = st.columns(2)

# Display each post as a card
for i, post in enumerate(posts):
    # Make sure that the post has at least 10 elements (to match placeholders)
    if len(post) >= 10:
        # Alternating posts between col1 and col2
        if i % 2 == 0:  # Even index posts go into the first column
            with col1:
                st.markdown(title_temp.format(post[0], post[1], post[2], post[3], post[4], post[5], post[6], post[7], post[8], post[9]), unsafe_allow_html=True)
        else:  # Odd index posts go into the second column
            with col2:
                st.markdown(title_temp.format(post[0], post[1], post[2], post[3], post[4], post[5], post[6], post[7], post[8], post[9]), unsafe_allow_html=True)
    else:
        st.warning("Post data is incomplete.")
