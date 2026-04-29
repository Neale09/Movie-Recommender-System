import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    url=('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    response=requests.get(url)
    data=response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(mov):
    mov_ind = movies[movies['title'] == mov].index[0]
    ds = sim[mov_ind]
    mov_list = sorted(list(enumerate(ds)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in mov_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
movies_list=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)

sim=pickle.load(open('sim.pkl','rb'))
st.title('Movie Recommender System')

select_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values
)

if st.button('Recommend'):
    names,posters=recommend(select_movie_name)
    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

