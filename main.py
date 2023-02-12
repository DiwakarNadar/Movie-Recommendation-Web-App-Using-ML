import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movieid):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6a0c1ab3ac0e9b97b435651bf558dd28&language=en-US'.format(movieid))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


sim=pickle.load(open('sim.pkl','rb'))
def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distance = sim[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie=[]
    recommended_movie_poster=[]
    for i in movie_list:
        movieid=movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].original_title)
        recommended_movie_poster.append(fetch_poster(movieid))
    return recommended_movie,recommended_movie_poster



movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
st.title('Movie Recommender System')
selected_movie=st.selectbox('Which You are interested in?',
                    (movies['original_title'].values))
if st.button('Recommend'):
    names,poster=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])


