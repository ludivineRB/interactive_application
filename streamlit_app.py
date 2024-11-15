import streamlit as st 
pg = st.navigation([st.Page('Accueil.py'), st.Page('app2_without_form.py'), st.Page('Quizz.py')])
pg.run()