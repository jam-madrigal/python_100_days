from main import question_bank
# TODO: 1. Create a QuizBrain class
# TODO: 2. initialize a question_number attribute at 0
# TODO: 3. initialize the question_list to an input
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list

# TODO: 4. Get the question from the current question number and show it to the user, prompting for an answer
brain = QuizBrain(question_bank)
q_number = brain.question_number
question = brain.q_list[q_number]

input(f'{question.text} Answer "true" or "false":\n').lower()

