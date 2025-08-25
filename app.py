import streamlit as st
import pickle
import pandas as pd
songs = pickle.load(open('songs.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Song Recommendation System")
song_list = songs['song'].values
selected_song = st.selectbox("Choose a song you like:", song_list)
def recommend(song):
    index = songs[songs['song'] == song].index[0]
    distances = similarity[index]
    song_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]
    recommended_songs = [songs.iloc[i[0]].song for i in song_list]
    return recommended_songs

if st.button("Recommend"):
    recommendations = recommend(selected_song)
    st.write("You might also like:")
    for song in recommendations:
        st.write(f"- {song}")
