import streamlit as st 
import json
import parametres as p
import os
from model_classes import Question, Theme
##Là on pourrait mettre un menu déroulant
#soit on crée 
#soit on implémente une liste préexistante
chemin="./theme/"
st.title('Créer votre thème')
st.text('Ajouter des questions et des réponses')
name = st.text_input('Entrer le thème')
if st.button('create quizz'):
    with open(f'{chemin}{name}.json', "w") as file:
        pass
    st.success(f"Quiz '{name}' sauvegardé!")

#créations des questions et réponses
question = st.text_input('Entrer une question')
answer1 =st.text_input('Entrer une première réponse possible')
answer2 =st.text_input('Entrer une deuxième réponse possible')
answer3 =st.text_input('Entrer une troisième réponse possible')
answer_index=st.text_input('Entrer le numéro de la bonne réponse')
addition_button=st.button("Ajouter")
if addition_button:
    user_question=Question(
        question=question,
        answers=[answer1,answer2,answer3],
        answer_index= answer_index
    )
    p.list_of_questions.append(user_question)
#On peut ajouter la mep des questions et réponses comme Hacene à la limite

creation_quizz=st.button("Créer le quizz")
if creation_quizz:
    with open(f'{chemin}{name}.json', "w") as file:
        data =json.dump([x.model_dump() for x in p.list_of_questions],file,indent=3)
    st.success(f"Quiz '{name}' sauvegardé!")
#.model_dump() pour faire une boucle qui fait le truc à chaque élément de la liste à ajouter
