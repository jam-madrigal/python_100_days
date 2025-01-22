# TODO: 1. Import the question class and question data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# TODO: 2. Create a function to loop through question data and make a question object from each
question_bank = []
def make_questions(data):
    for question in data:
        new_question = Question(question['text'], question['answer'])
        question_bank.append(new_question)
# TODO: 3. Save each question to a question bank
make_questions(question_data)

# TODO: 4. Import quiz brain class, set the question from the current question number and show it to the user, prompting for an answer
brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print(f'The quiz is over. Your final score is {brain.score}')