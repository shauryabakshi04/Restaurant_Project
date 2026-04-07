import pandas as pd
import streamlit as st

st.set_page_config(page_title="Restaurant Recommendation", layout="wide")

data = pd.read_excel("data.xlsx")

st.title("Restaurant Recommendation System")

st.sidebar.header("Filters")

min_rating = st.sidebar.slider("Minimum Rating", 3.0, 5.0, 4.5)
min_votes = st.sidebar.slider("Minimum Votes", 0, 5000, 1000)

city = st.sidebar.selectbox("Select City", data["City"].unique())

filtered = data[
    (data["Aggregate rating"] >= min_rating) &
    (data["Votes"] >= min_votes) &
    (data["City"] == city)
]

filtered = filtered.sort_values(by=["Aggregate rating", "Votes"], ascending=False)

st.write(filtered[["Restaurant Name", "Aggregate rating", "Votes"]].head(10))