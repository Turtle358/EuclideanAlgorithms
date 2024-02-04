import time


def eucledianGcd(a, b):
    
    r = a % b
    while r != 0:
        r = a % b
        a,b = b,r
        if r == 0:
            return a


def primeFactorisation(n):
    factors = []
    i = 2
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > i:
        factors.append(n)
    return factors


def primeFactorGCD(a, b):
    factorsA = primeFactorisation(a)
    factorsB = primeFactorisation(b)

    commonFactors = set(factorsA) & set(factorsB)

    if len(commonFactors) == 0:
        return 1
    else:
        result = 1
        for factor in commonFactors:
            result *= factor
    return result


if __name__ == '__main__':
    number1 = int(input('Enter first number: '))
    number2 = int(input('Enter second number: '))
    timenow = time.time()
    euclidian = eucledianGcd(number1, number2)
    print(f'euclidean result: {euclidian} time taken: {time.time() - timenow}')
    timenow2 = time.time()
    gcd = primeFactorGCD(number1, number2)
    print(f'primeFactor result: {gcd} time taken: {time.time() - timenow2}')
