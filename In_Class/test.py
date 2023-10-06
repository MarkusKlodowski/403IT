#sum of n terms in a geometric progression
def sumOfGP(a,r,n):
    if r == 1:
        return a*n
    else:
        return a*(1-r**n)/(1-r)
def sumOfAP(a,d,n):
    if n == 1:
        return a
    else:
        return a + sumOfAP(a+d,d,n-1)

#sum of n terms in a geometric progression using lambda
def sumOfGpLam(a,r,n):
    return (lambda a,r,n: a*(1-r**n)/(1-r))(a,r,n)


# Calculate the nth power of x using recursion
def nthPower(x,n):
    if n == 0:
        return 1
    else:
        return x * nthPower(x,n-1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#sum of the n terms using recursion
def sumOfnTerms(n):
    if n == 0:
        return 0
    else:
        return n + sumOfnTerms(n-1)
# l1 = [2,4,3]
# l2 = [5,6,4]
# l3 = []
# for i in l1:
#     sum = l1[i-1] + l2[i-1]
#     if sum > 10:
#         sum -= 10
#         l3[i+1] += sum
#     l3.append(sum)
# print(l3)
import os
print("Which of the following operations would you like to do? \n 1. Summation of a sequence \n 2. Nth power of a number \n 3. Factorial of a number")
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
        print("Your result: ", sumOfAP(a,d,n))
    elif y == 2:
        a = int(input("Enter the first term: "))
        r = int(input("Enter the common ratio: "))
        n = int(input("Enter the number of terms: "))
        print("Your result: ",sumOfGP( a,r,n))
elif x == 2:
    print("What number would you like to raise to the nth power?")
    y = int(input("Enter the number you would like to raise: "))
    n = int(input("Enter the power: "))
    print("Your result: ", nthPower(y,n))
elif x == 3:
    print("What number would you like to find the factorial of?")
    y = int(input("Enter your number: "))
    print("Your result: ",factorial(y))
