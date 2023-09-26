import random
import matplotlib.pyplot as plt

print("Course Moduels for cyber secuitry: \n", 7*"-", "\n Year 1\n" , 7*"-", " \n Networking \n operating system \n information secuirty \n problem solving and programing\n", 7*"-", "\n Year 2\n" , 7*"-", "\n Cryptography \n Computer Forensics \n Algorithms and Communications\n", 7*"-", "\n Year 3\n" , 7*"-", "\n Secure Programing \n IOT\n Contemporary issues in Computing \n Final Project\n" )
x = 3**2**3*4
print(x)

#in class rocket launcher example in python
p = 1
a = 0
b = 0 
c = 0 

if (a or b or c == 1):
    sum = 1

if(p and sum == 1):
    print("launch rocket")
else:
    print("dont launch rocket")

x = random.randrange(1,10)
y = random.randrange(1,10)

print(x+y, x-y, x*y, x/y, x%y, x**y)

sentence = "the boy is a bad boy"
#split the string into a list of words
sentence = sentence.split()
words = {}
for i in sentence:
    #check if the word is in the dictionary and if it is increment the value if not add it to the list
    if i in words:
        words[i] += 1
    else:
        words.update({i:1})

print(words)

word = list(words.keys())
occurances = list(words.values())

plt.bar(range(len(words)), occurances, tick_label=word)
plt.show()

