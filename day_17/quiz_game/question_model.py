# TODO: 1. Create a question class that has a constructor with two attributes: question and answer
class Question:
    def __init__(self, question, answer):
        print('Creating question...')
        self.question = question
        self.answer = answer

q1 = Question('butt?', 'yes')

print(q1.question, q1.answer)