def greatestCommonDivisor(*args):
    factors = [set(findFactors(num)) for num in args]
    common_factors = set.intersection(*factors)
    return max(common_factors)

def findFactors(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

print(greatestCommonDivisor(30, 45, 60)) 
print(greatestCommonDivisor(10, 20, 30, 40))