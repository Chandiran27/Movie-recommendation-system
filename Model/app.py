import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended=[]
    for i in movie_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended
movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title ('Movie Recommendation System')

selected_movie=st.selectbox(
    'Enter the movie you like:',
    movies['title'].values)

if st.button("Recommend"):
    recommendations= recommend(selected_movie)
    for i in recommendations:
        st.write(i)