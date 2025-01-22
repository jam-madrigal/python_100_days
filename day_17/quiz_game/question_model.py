# TODO: 1. Create a question class that has a constructor with two attributes: question and answer
class Question:

    def __init__(self, text, answer):
        print('Creating question...')
        self.text = text
        self.answer = answer

q1 = Question('butt?', 'yes')

print(q1.text, q1.answer)