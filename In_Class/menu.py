import test
import os

print("Which of the following operations would you like to do? \n 1. Summation of a sequence \n 2. Nth power of a number \n 3. Factorial of a number \n 4. Exit")
x = int(input("Enter your choice: "))
os.system('cls')
if x == 1:
    print("What type of sequence would you like to sum? \n 1. Arithmetic \n 2. Geometric")
    y = int(input("Enter your choice: "))
    os.system('cls')
    if y == 1:
        a = int(input("Enter the first term: "))
        d = int(input("Enter the common difference: "))
        n = int(input("Enter the number of terms: "))
        print("Your result: ", test.sumOfAP(a,d,n))
    elif y == 2:
        a = int(input("Enter the first term: "))
        r = int(input("Enter the common ratio: "))
        n = int(input("Enter the number of terms: "))
        print("Your result: ",test.sumOfGP( a,r,n))
elif x == 2:
    print("What number would you like to raise to the nth power?")
    y = int(input("Enter the number you would like to raise: "))
    n = int(input("Enter the power: "))
    print("Your result: ", test.nthPower(y,n))
elif x == 3:
    print("What number would you like to find the factorial of?")
    y = int(input("Enter your number: "))
    print("Your result: ",test.factorial(y))
elif x == 4:
    print("exiting")
    os.system('cls')