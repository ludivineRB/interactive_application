import streamlit as st 
import json
import parametres as p
import os

##Là on pourrait mettre un menu déroulant
#soit on crée 
#soit on implémente une liste préexistante
chemin="./theme/"
st.title('Create your theme')
st.text('Add your questions and answers')
name = st.text_input('Enter the theme')
if st.button('create quizz'):
    with open(f'{chemin}{name}.json', "w") as file:
        pass
    st.success(f"Quiz '{name}' saved successfully!")

#créations des questions et réponses
question = st.text_input('Enter your question')
answer1 =st.text_input('Enter a possible answer1')
answer2 =st.text_input('Enter a possible answer2')
answer3 =st.text_input('Enter a possible answer3')
answer_index=st.text_input('Enter the number of the correct answer')
addition_button=st.button("Add")
if addition_button:
    user_question={
        "question":question,
        "answers":[answer1,answer2,answer3],
        "answer_index":answer_index
    }
    p.list_of_questions.append(user_question)
    
st.text(p.list_of_questions)
creation_quizz=st.button("Submit")
if creation_quizz:
    with open(f'{chemin}{name}.json', "w") as file:
        data =json.dump(p.list_of_questions,file,indent=3)
    st.success(f"Quiz '{name}' saved successfully!")
