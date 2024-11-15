import streamlit as st 
pg = st.navigation([st.Page('Accueil.py'), st.Page('Creation_quizz.py'), st.Page('Quizz.py')])
pg.run()