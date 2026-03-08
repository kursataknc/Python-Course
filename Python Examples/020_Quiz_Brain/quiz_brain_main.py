from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_in_quiz = int(input("Welcome to the Quiz Game! Press Enter to start... How many questions would you like to answer? (Max 20): "))

question_bank = []
for question in question_data:
	question_text = question["question"]
	answer = question["correct_answer"]
	new_question = Question(question_text, answer)
	question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.question_number < questions_in_quiz:
	quiz.next_question()

print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")
