from data_modl import question_data
from question_model import Question
question_bank=[]

for question in question_data:
    question_text=question[ ]
    question_answer=question[ ]
    new_question=Question(question_text , question_answer)
    question_bank.append(new_question)

print(question_bank)
i