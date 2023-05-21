from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain
question_bank=[]
for q in question_data:
    question_bank.append(QuestionModel(q["text"],q["answer"]))

brain = QuizBrain(question_bank)
# print(brain.still_have_questions())
while brain.still_have_questions():
    brain.next_question()

print(f"You have {brain.correct_answers} correct answers for {len(brain.questions_list)}")