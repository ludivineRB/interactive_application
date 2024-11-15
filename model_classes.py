from pydantic import BaseModel

class Question(BaseModel):
    question:str
    answers:list(str)
    answer_index: int