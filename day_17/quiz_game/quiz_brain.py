# TODO: 1. Create a QuizBrain class
# TODO: 2. initialize a question_number attribute at 0
# TODO: 3. initialize the question_list to an input
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list

    def still_has_questions(self):
        if self.question_number == len(self.q_list):
            return False
        else:
            return True

    def next_question(self):
        question = self.q_list[self.question_number]
        self.question_number += 1
        input(f'Q.{self.question_number} {question.text} Answer "true" or "false":\n').lower()



