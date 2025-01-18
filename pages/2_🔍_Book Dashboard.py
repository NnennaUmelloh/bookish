import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image


# data
bookreviews = pd.read_csv('bookreviews.csv')

# reading goals data
goal = 100
current_progress = 4

# Calculate percentage
progress_percentage = (current_progress / goal) * 100


# reads per month bar graph calculations

# Convert 'Date Read' to datetime
bookreviews['Date Read'] = pd.to_datetime(bookreviews['Date Read'])

# Extract month and year, then group by month to count books
bookreviews['Month'] = bookreviews['Date Read'].dt.strftime('%B')  # e.g., "2025-01"
monthly_counts = bookreviews.groupby('Month').size().reset_index(name='Reads')

month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

monthly_counts['Month'] = pd.Categorical(monthly_counts['Month'], categories=month_order, ordered=True)
monthly_counts = monthly_counts.sort_values('Month')

# rating count calculation

# Group data by Rating and count the number of books in each rating
rating_counts = bookreviews.groupby('Rating').size().reset_index(name='Count')

# year published calculations
# Group by 'Year Published' and count the number of books published each year
year_counts = bookreviews.groupby('Year Published').size().reset_index(name='Count')


st.title("Book Dashboard")

st.markdown('### Reading Goal Progress Tracker')
st.write(f"Current Progress: {current_progress}/{goal}")
st.progress(int(progress_percentage))
st.divider()

# Row A
a1, a2, a3 = st.columns((5,5,5))

with a1:
    st.markdown('### Year Published')    
    st.bar_chart(
        data=year_counts.set_index('Year Published'),
        x_label="Year Published",
        y_label="Number of Books",
        use_container_width=True
        )

with a2:
    st.markdown('### Genre Breakdown')
    plost.donut_chart(
        data  = bookreviews,
        theta ='Genre',
        color = "Genre",
        title = "Genre Breakdown",
        )
    
with a3:
    st.markdown('### Ratings Breakdown')
    st.bar_chart(
    data    = rating_counts.set_index('Rating'),
    x_label = "Rating",
    y_label = "Number of Books",
    use_container_width = True
)
st.divider()

st.markdown("### Books Read per Month")
st.bar_chart(
    data    = monthly_counts.set_index('Month'),
    x_label = "Month",
    y_label = "Reads",
    use_container_width = True
)
st.divider()