def main():
    iterations = 2000
    totalSum = 0

    print isPrime(2)

    for iterations in range(1, 20040001):

        if isPrime(iterations):
            totalSum += iterations


    print totalSum

def isPrime(inputNumber):
    import math
    for x in range (2, int(math.sqrt(inputNumber)) + 1):
        if inputNumber % x == 0:
            #It is not a prime
            return False
    return True
if __name__ == '__main__':
    main()
