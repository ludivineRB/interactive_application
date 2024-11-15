import streamlit as st
from os import listdir
from os.path import isfile, join
import json_functions as js

# Charger les thèmes disponibles
themes = [f.split(".json")[0] for f in listdir('theme') if isfile(join('theme', f))]
option = st.selectbox('Choisis un thème!', (themes))
st.title(f'Jouons dans le thème {option}!')
st.title('')

# Charger le quiz
quizz = js.load_json(option)

# Initialiser l'état de session
def initialize_session_state():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0

# Réinitialiser le quiz
def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.player_score = 0

# Mettre à jour le score
def update_score(choix, correct_answer):
    position = quizz[st.session_state.current_question]['answers'].index(choix)
    if (position + 1) == correct_answer:
        st.session_state.player_score += 1

# Calculer le score et passer à la question suivante
def calculate_score(player_choice):
    correct_answer = int(quizz[st.session_state.current_question]['answer_index'])
    update_score(player_choice, correct_answer)
    st.session_state.current_question += 1

# Initialiser l'état
initialize_session_state()

# Vérifier si le quiz est terminé
if st.session_state.current_question < len(quizz):  # Si le quiz n'est pas terminé
    compteur = st.session_state.current_question
    current_question = quizz[compteur]
    
    # Afficher la question
    st.markdown(
        f"""
        <div style="border: 1px solid black; padding: 10px; border-radius: 5px; font-size: 20px;">
            {current_question['question']}
        </div>
        """,
        unsafe_allow_html=True
    )
    choix = st.radio(
        " ",
        options=current_question["answers"],
        key=f"question_{compteur}"
    )

    st.write(f'Questions {compteur + 1}/{len(quizz)}')
    if st.button("Valider", key=f"submit_{compteur}"):
        calculate_score(choix)
        st.rerun()

else:  # Si le quiz est terminé
    st.success("Quiz terminé !")
    st.write(f"Votre score : {st.session_state.player_score}/{len(quizz)}")
    if st.button('Recommencer !'):
        reset_quiz()
        st.rerun()
