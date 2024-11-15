import streamlit as st 
from os import listdir
from os.path import isfile, join
import json_functions as js
#st.text('Choose your theme?')
#récupère l'ensemble des thèmes créés précédemment
themes = [f.split(".json")[0] for f in listdir('theme') if isfile(join('theme', f))]
option = st.selectbox('Choisis un thème!',(themes))
st.title(f'Jouons dans le thème {option}!')

quizz=js.load_json(option)

def initialize_session_state():
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'player_score' not in st.session_state:
            st.session_state.player_score = 0

def update_score(player_choice, correct_answer):
        position=quizz[ind]['answers'].index(player_choice)
        if (position+1) == correct_answer:
            st.session_state.player_score += 1

initialize_session_state()

def calculate_score(player_choice):
        correct_answer = quizz[st.session_state.current_question]['answer_index']
        update_score(player_choice, correct_answer)
        st.session_state.current_question += 1

ind = st.session_state.current_question
current_question = quizz[ind]
st.markdown(
                f"""
                <div style="border: 1px solid black; padding: 10px; border-radius: 5px; font-size: 20px;">
                    {quizz[ind]['question']}
                </div>
                """,
                unsafe_allow_html=True
            )

player_choice = st.selectbox("Select your answer:",
                                 options=current_question["answers"],
                                 key=f"question_{ind}") 
if st.button("Submit", key=f"submit_{ind}"):
        calculate_score(player_choice)
       
        if st.session_state.current_question < len(quizz):
            st.rerun()
        
        if st.session_state.current_question >= len(quizz):
            st.success("Quiz Finished!")
            st.write(f"Your Score: {st.session_state.player_score}")
            initialize_session_state()

#Rajouter score :x/nbde questions
#Rajouter un bouton start qui commence le game 
#Remettre en français
#Remettre des st.radio à la place du menu déroulant chiant
