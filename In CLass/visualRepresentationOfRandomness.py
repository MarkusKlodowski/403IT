import random
import matplotlib.pyplot as plt
#create a dictionary with 10 numbers with a value of zero so that can be incremented
def createDictionary(low, high):
    nums = {}
    for i in range(low,high+1):
        nums.update({i:0})
    return nums

#plot the results
def plot(_list):
    number = list(_list.keys())
    occurances = list(_list.values())

    #viualy represent the data using a bar chart
    plt.bar(range(len(_list)), occurances, tick_label=number)
    return(plt.show())

x = createDictionary(1,10)
#generate 10000 random numbers between 1 and 10 and increment the value in the dictionary
for j in range(1,10001):
    x[random.randrange(1,11)] += 1
#plot(x)
#random dice generator

def diceThrow(diceSize):
    return(random.randrange(1,diceSize+1))

def diceRoll(x):
    return(diceThrow(x) + diceThrow(x))

y = createDictionary(1,20)
for j in range(1,101):
    y[diceThrow(20)] += 1
plot(y)







