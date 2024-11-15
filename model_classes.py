from pydantic import BaseModel, field_validator
import streamlit as st

class Theme(BaseModel):
    name:str
    @field_validator("name")
    def must_filled(cls, v):
        if v == '':
            raise ValueError('Vous devez rentrer un nom')
        return v

class Question(BaseModel):
    question:str
    answers:list[str]
    answer_index: int

   
    @field_validator('question')
    def not_empty(cls, v):
        if v == '':
            raise ValueError('Veuillez renseigner une question')
        return v

    @field_validator('question')
    def point_interrogation(cls, v):
        if  '?' not in v:
            raise ValueError('votre question doit contenir un ?')
        return v
            
    @field_validator('answer_index')
    def number(cls, v):
        if v<=0 or v>3:   
            raise ValueError('0<v<3')
        return v
        
            