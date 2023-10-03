#sum of n terms in a geometric progression
def sumOfGP(a,r,n):
    if r == 1:
        return a*n
    else:
        return a*(1-r**n)/(1-r)
    
print(sumOfGP(1,2,10))

#sum of n terms in a geometric progression using lambda
def sumOfGpLam(a,r,n):
    return (lambda a,r,n: a*(1-r**n)/(1-r))(a,r,n)

print(sumOfGpLam(1,2,10))

# Calculate the nth power of x using recursion
def nthPower(x,n):
    if n == 0:
        return 1
    else:
        return x * nthPower(x,n-1)

print(nthPower(2,6))

#sum of the n terms using recursion
def sumOfnTerms(n):
    if n == 0:
        return 0
    else:
        return n + sumOfnTerms(n-1)