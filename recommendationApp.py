import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=4f9b67579ffe61bd16e44090ab22c55a&language=en-US".format(movie_id))
    data = response.json()
    print(data)
    if "poster_path" in data:
        return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    else:
        return "Poster not available"
    

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))


st.markdown("<h1 style='text-align: center; color: #009688;'>Movie Recommender System</h1>", unsafe_allow_html=True)

selected_movie_name = st.selectbox("Select A Movie Name",movies["title"].values)


if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("<h4 style='text-align: center; color: lightblue;'>{}</h4>".format(names[0]),unsafe_allow_html=True,)
        st.image(posters[0])

    with col2:
        st.markdown("<h4 style='text-align: center; color: red;'>{}</h4>".format(names[1]),unsafe_allow_html=True,)
        st.image(posters[1])

    with col3:
        st.markdown("<h4 style='text-align: center; color: white;'>{}</h4>".format(names[2]),unsafe_allow_html=True,)
        st.image(posters[2])

    with col4:
        st.markdown("<h4 style='text-align: center; color: blue;'>{}</h4>".format(names[3]),unsafe_allow_html=True,)
        st.image(posters[3])

    with col5:
        st.markdown("<h4 style='text-align: center; color: green;'>{}</h4>".format(names[4]),unsafe_allow_html=True,)
        st.image(posters[4])
