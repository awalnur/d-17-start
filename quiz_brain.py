class QuizBrain:
    def __init__(self, questions_list):
        self.current_question = 0
        self.correct_answers = 0
        self.questions_list = questions_list
    def still_have_questions(self):
        return self.current_question < len(self.questions_list)
    def next_question(self):
        current_questions = self.questions_list[self.current_question]
        answr= input(f"Q.{self.current_question+1} {current_questions.question_text} (True/False)")
        self.check_answer(current_questions.question_answer, answr)
        self.current_question += 1

    def check_answer(self, question, answer):
        if question == answer.title():
            self.correct_answers += 1
            print("Correct!")
        else:
            print("Wrong!")
