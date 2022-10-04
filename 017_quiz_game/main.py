from question_model import Question
from data import question_data1, question_data2
from quiz_brain import QuizBrain
import random

#database = random.choice(question_data2, question_data1)
database = question_data2

question_bank = []

for question in database:
    q = Question(question["question"], question["correct_answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.length}")