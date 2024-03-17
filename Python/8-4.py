def isPrime(p):
    for i in range(2,p//2+1):
        if p%i == 0:
            return False
    return True
def somePrime(numbers):
    for num in numbers:
        if isPrime(num):
            return True
    return False

def allPrime(numbers):
    for num in numbers:
        if not isPrime(num):
            return False

num1 = [217, 287, 143, 163, 319]
num2 = [217, 287, 143, 169, 319]
num3 = [223, 281, 227, 151, 149]
print(somePrime(num1), allPrime(num1))   # True False
print(somePrime(num2), allPrime(num2))   # False False
print(somePrime(num3), allPrime(num3))   # True True
