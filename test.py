import streamlit as st

# Liste des options
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Utiliser st.radio pour limiter l'utilisateur à un seul choix
choix = st.radio("Sélectionnez une option :", options)

# Afficher le choix sélectionné
st.write(f"Vous avez sélectionné : {choix}")
