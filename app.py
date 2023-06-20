


import streamlit as st
import pickle
import pandas as pd
import nltk
import sklearn
from nltk.stem import PorterStemmer # to stem
from sklearn.feature_extraction.text import CountVectorizer

movies_dict = pickle.load(open("mdict.pickle",'rb'))
inp1 = pd.DataFrame(movies_dict)
similarity=pickle.load(open("similarity.pickle", 'rb'))

def recomendation(movie_name):
    movie_index = inp1[inp1.title==movie_name].index[0] 
    disstance= similarity[movie_index]
    movie_list =sorted(list(enumerate(disstance)), reverse=True, key=lambda x: x[1])[1:6]
    recomended_index =[]
    r=[]
    for i in movie_list:
        recomended_index.append(inp1.iloc[i[0]].title)
        r.append(inp1.iloc[i[0]].vote_average)
        df=pd.DataFrame()
        df["Recommendation"]=recomended_index
        df["Ratting"]=r
        
    return df


st.title("Movie Recommendation System")
select_m=st.selectbox("              Select The Movie            ",inp1['title'].values)

if st.button('Recommend'):
    recommen = recomendation(select_m)
    st.write(recommen)



