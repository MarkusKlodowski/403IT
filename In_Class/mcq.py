import time
import os

#user verification

def hash(password):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()


def verification(user, password):
    with open("in_Class/userCredentials.txt", "r") as file:
        user = user.split("@")[0]
        print(user)
        if user.split("@")[1] != "coventry.ac.uk":
            return False
        for line in file:
            if line.strip() == "":
                # Skip blank lines
                continue
            elif line.strip().startswith("Username"):
                # Check if the line is the desired question
                if user in line.strip() and hash(password) in line.strip():
                    return True
                else:
                    return False

    return True

if verification(input("Enter your username: "), input("Enter your password: ")) == True:
    print("Welcome!")
else:
    print("Incorrect username or password")
    exit()

timeForTest = 60
print("You have", timeForTest, "seconds to complete the test.")
time.sleep(4)
os.system('cls')
start_time = time.time()

question = []

def getQuestion():
    question = []
    with open("in_Class/mcqQuestions.txt", "r") as file:
        for line in file:
            if line.strip() == "":
                # Skip blank lines
                continue
            elif line.strip().startswith("What is") and line.strip().endswith("?"):
                # Check if the line is the desired question
                if line.strip().startswith("What is"): 
                    question.append(line.strip())
                    # Add the next 4 lines to the question list
                elif line.strip() == f"end of questions":
                    break
    return question

def getAnswer():
    answers = []
    with open("in_Class/mcqQuestions.txt", 'r') as file:
        for line in file:
            if line.strip() == "":
                # Skip blank lines
                continue
            elif line.strip().startswith("A."):
                #Check if the line is the desired question
                answers.append(line.strip())
                if line.strip() ==  "end of answers":
                    break
    return answers

def getAnswerKey():
    answersKey = []
    foo = False
    with open("in_Class/mcqQuestions.txt", 'r') as file:
        for line in file:
            if line.strip() == "":
                # Skip blank lines
                continue
            elif line.strip() == "end of answer key":
                foo = False
            if foo == True:
                answersKey.append(line.strip())
            elif line.strip().startswith("Answer key"):
                foo = True
    return answersKey

#Define a function to ask a question and get the answer
def askQuestion(question, answers):
    print(question)
    print(answers)
    response = input("Enter your answer (A, B, C, or D): ")
    os.system('cls')
    return response.upper()

def checkAnswer(question, response, answerKey):
    # Extract the option corresponding to the response
    option = question.split(", ")[ord(response) - ord("A")]
    # Extract the text after the option letter
    text = option[3:]
    # Check if the text is answerKey
    if text == answerKey:
        return True
    else:
        return False, text
# Clear the screen
os.system('cls')

# Ask each question and keep track of the score
score = 0
incorrect = []
_answers = []
for i in range(len(getQuestion())):
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time > timeForTest:
        print("You ran out of time!")
        break
    else:
        response = askQuestion(getQuestion()[i], getAnswer()[i])
        _answers.append(response)
    result = checkAnswer(getAnswer()[i], response, getAnswerKey()[i])
    if result == True:
        score += 1
    else:
        incorrect.append(i+1)
        

for i in range(len(getQuestion())):
    print("Question", i+1, "was", getQuestion()[i], "and you answered", _answers[i], "and the correct answer was", getAnswerKey()[i], )

# Print the final score

print("You got", score, "out of", len(getQuestion()), "questions correct. \n Your incorect questions were", incorrect )