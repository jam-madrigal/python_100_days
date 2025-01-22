# TODO: 1. Create a QuizBrain class
# TODO: 2. initialize a question_number attribute at 0
# TODO: 3. initialize the question_list to an input
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.q_list)

    def check_question(self, user_answer):
        question = self.q_list[self.question_number - 1]
        answer = question.answer.lower()
        if user_answer != answer:
            return print(f'Your answer was incorrect. Your current score is {self.score}/{self.question_number}\n')
        else:
            self.score += 1
            return print(f'Your answer was correct. Your current score is {self.score}/{self.question_number}\n')

    def next_question(self):
        question = self.q_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number} {question.text} Answer "true" or "false":\n').lower()
        self.check_question(answer)



