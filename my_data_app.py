import streamlit as st
import pandas as pd


st.markdown("<h1 style='text-align: center; color: black;'>MY DATA APP</h1>", unsafe_allow_html=True) # Pour le titre de l'application via une balise html la balise est h1

st.markdown("""
This app allows you to download scraped data on motocycles from expat-dakar 
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
""") # Pour la description de l'application


# Fonction de loading des données
def load_(dataframe, title, key) : # Creation de la fonction qui Prend en paramètre le dataframe, le titre et la clé et permet de charger les données
    st.markdown("""
    <style>
    div.stButton {text-align:center} # Pour centrer le bouton
    </style>""", unsafe_allow_html=True)

    if st.button(title,key): # Ca veut dire que si le bouton est cliqué il rentre dans le contenu
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.') # Afficher la dimension des données
        st.dataframe(dataframe) # Afficher les données

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button { 
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

          
# Charger les données 
load_(pd.read_csv('data/motos_scooters1.csv'), 'Motocycles data 1', '1') # Appel de la fonction load_ pour charger les données prend le dataframe, le titre et la clé
load_(pd.read_csv('data/motos_scooters2.csv'), 'Motocycles data 2', '2')
load_(pd.read_csv('data/motos_scooters3.csv'), 'Motocycles data 3', '3')
load_(pd.read_csv('data/motos_scooters4.csv'), 'Motocycles data 4', '4')
load_(pd.read_csv('data/motos_scooters5.csv'), 'Motocycles data 5', '5')


# Par defaut Streamlit (ou n'importe quel build app) donne la possibilite de telecharger, de rechercher, d'agrandir le dataframe
# Le background et les couleurs sont geres dans ./.streamlit/config.toml


