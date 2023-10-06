import time
import os

timeForTest = 60
print("You have", timeForTest, "seconds to complete the test.")
time.sleep(2)
os.system('cls')
start_time = time.time()

# Define the questions and answers
questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the smallest country in the world?",
    "What is the highest mountain in the world?",
    "What is the largest ocean in the world?",
    "What is the smallest planet in our solar system?",
    "What is the largest country in the world?",
    "What is the longest river in the world?",
    "What is the hottest planet in our solar system?",
    "What is the coolest planet in our solar system?"
]

answers = [
    ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
    ["A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"],
    ["A. Monaco", "B. Vatican City", "C. San Marino", "D. Liechtenstein"],
    ["A. Mount Everest", "B. K2", "C. Kangchenjunga", "D. Lhotse"],
    ["A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. Arctic Ocean"],
    ["A. Venus", "B. Mercury", "C. Mars", "D. Pluto"],
    ["A. Russia", "B. Canada", "C. China", "D. United States"],
    ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
    ["A. Venus", "B. Mercury", "C. Mars", "D. Jupiter"],
    ["A. Neptune", "B. Uranus", "C. Pluto", "D. Saturn"]
]
answerKey = ["A", "A", "B", "A", "A", 'B', "A", "B", "A", "D"]

# Define a function to ask a question and get the answer
def askQuestion(question, answers):
    print(question)
    for answer in answers:
        print(answer)
    response = input("Enter your answer (A, B, C, or D): ")
    os.system('cls')
    return response.upper()

# Clear the screen
os.system('cls')

# Ask each question and keep track of the score
score = 0
incorrect = []
_answers = []
for i in range(len(questions)):
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time > timeForTest:
        print("You ran out of time!")
        break
    else:
        response = askQuestion(questions[i], answers[i])
        _answers.append(response)
        if response == answerKey[i]:
            score += 1
        else:
            incorrect.append(questions[i])

for i in range(len(questions)):
    print("Question", i+1, "was", questions[i], "and you answered", _answers[i], "and the correct answer was", answerKey[i], )

# Print the final score

print("You got", score, "out of", len(questions), "questions correct. \n Your incorect questions were", incorrect )