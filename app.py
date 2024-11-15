import streamlit as st 
import pandas as pd
import numpy as np
import time
import json
#create a title
st.title('Create your quizz')
list_of_questions =[]
name = st.text_input('Enter the name of your quiz')
if st.button('Save'):
    with open(f'{name}.json', "w") as file:
        json.dump(list_of_questions, file, indent=3)
    st.success(f"Quiz '{name}' saved successfully!")

with st.form("my_form"):
    st.write("Inside the form")
    question = st.text_input('Enter your first question')
    answer1 =st.text_input('Enter a possible answer1')
    answer2 =st.text_input('Enter a possible answer2')
    answer3 =st.text_input('Enter a possible answer3')
    answer_index=st.text_input('Enter the number of the correct answer')

    addition_button=st.form_submit_button("Add")
    if addition_button:
        user_question={
            "question":question,
            "answers":[answer1,answer2,answer3],
            "answer_index":answer_index
        }
        list_of_questions.append(user_question)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        with open(f'{name}.json', "w") as file:
            #data=json.loads(file)
            data =json.dump(user_question,file,indent=3)
            #data = json.dump(answer_index, indent=2, separators=",")
        """have_it = animal.lower() in animal_shelter
        'We have that animal!' if have_it else 'We don\'t have that animal.'"""

        # st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")


"""for l in liste_questions:
    #personnalisation de la police, taille, et encadrement
    
    #Liste des réponses
    options = [r for r in quizz[l]['answers']]

    # Utiliser st.radio pour limiter l'utilisateur à un seul choix
    choix = st.radio("", options)
    st.write(f'réponse choisie : {choix}')
    liste_reponse.append({choix})
liste_reponse=list(liste_reponse)  
    #st.text(compteur_question)
if st.button("Valider"):
    #st.write(liste_reponse)
    bonne_reponse = 0
    for li in liste_questions:
        if liste_reponse[li][0] == quizz[li]['answer_index']:
            bonne_reponse+=1
    st.write(f"{bonne_reponse} sur {len(quizz)}")"""

def initialize_session_state():
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'player_score' not in st.session_state:
            st.session_state.player_score = 0


    def update_score(player_choice, correct_answer):
        if player_choice == correct_answer:
            st.session_state.player_score += 1


    quiz_questions = [
        {
            'text': 'What type of learning uses historical data to make predictions?',
            'options': ('Supervised', 'Unsupervised', 'Reinforcement'),
            'answer': 'Supervised'
        },
        {
            'text': 'Which loss function is used in Support Vector Machines?',
            'options': ('Mean Squared Error', 'Huber Loss', 'Hinge Loss'),
            'answer': 'Hinge Loss'
        },
        {
            'text': 'Which metric measures the performance of a classification model?',
            'options': ('Accuracy', 'R-Squared', 'Mean Squared Error'),
            'answer': 'Accuracy'
        }
    ]

    st.title("Quiz Game")
    initialize_session_state()

    def calculate_score(player_choice):
        correct_answer = quiz_questions[st.session_state.current_question]['answer']
        update_score(player_choice, correct_answer)
        st.session_state.current_question += 1

    ind = st.session_state.current_question
    current_question = quiz_questions[ind]
    st.write(quiz_questions[ind]["text"])

    player_choice = st.selectbox("Select your answer:",
                                 options=current_question["options"],
                                 key=f"question_{ind}") 

    if st.button("Submit", key=f"submit_{ind}"):
        calculate_score(player_choice)
       
        if st.session_state.current_question < len(quiz_questions):
            st.experimental_rerun()
        
        if st.session_state.current_question >= len(quiz_questions):
            st.success("Quiz Finished!")
            st.write(f"Your Score: {st.session_state.player_score}")
            initialize_session_state()