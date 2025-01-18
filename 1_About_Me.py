import streamlit as st
from PIL import Image


# define variables
image_page = "bookish.jpg"
image = Image.open(image_page)
image = image.rotate(-90)


st.set_page_config(
    page_title = "Bookish and Bold!",
    page_icon = "📚", 
)

st.title("Welcome to Bookish and Bold!")
st.divider()

st.write("""


By day, I’m a Computer Scientist, but by night, I transform into a full-fledged bibliophile! For me, reading is more than just a hobby—it’s one of my favorite ways to unwind, escape the hustle of daily life, and dive into endless worlds of adventure and imagination.

This year, I decided to launch Bookish and Bold as a side project to document my reading journey in 2025. One of my biggest (but pressure-free!) goals is to read 100 books.

I’ve also had friends and family frequently ask me for book recommendations, so I figured, why not make this a space where I can share my favorite reads?

"""


)

st.markdown("""

On this site, you’ll find:

- A **fun, interactive dashboard** tracking my progress. I’m excited to see it grow and evolve as the year goes on!
- In-depth **book reviews** under the "Book Reviews" tab, where I’ll share thoughts on the stories that captivate me.

But that’s not all. Beyond reading 100 books this year, I have another dream: curating a collection of 1,000 books and building my own little library someday. No rush—it’s all part of the journey.

So, feel free to explore, get inspired, and maybe even join me on this bookish adventure. Here’s to a year full of pages and possibilities!


""")
st.divider()

col1, col2, col3 = st.columns([1, 2, 3])  #  First column takes up 1 unit, second column takes up 2 units

# Display the image in the right column
with col3:
    #st.image(image, caption = "Bookish")
    
    # Custom CSS to add a border and reduce padding
    st.markdown(
    f"""
    <style>
    .stImage {{
        border: 5px solid #8E7D57;  /* Olive Green Border */
        border-radius: 10px;        /* Rounded corners */
        padding: 0;                 /* Remove any internal padding */
        margin-left: 0;             /* Remove left padding */
        margin-right: 0;            /* Remove right padding */
        display: block;             /* Ensures the image behaves like a block element */
        margin-bottom: 20px;        /* Optional: Adds space below the image */
    }}
    </style>
    """,
    unsafe_allow_html=True
)
    

# Display the image with the new style
    st.image(image, caption = "Bookish", use_container_width = True)

