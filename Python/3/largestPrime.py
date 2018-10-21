#Find the largest prime factor of 600851475143.
import math

factors = []
primeFactors = []

def main():
    number = 600851475143

    getFactors(number)

    print "Prime Factors: ", primeFactors
    primeFactors.reverse()
    print "Largest Prime Factor: ", primeFactors[0]

def getFactors(inputNumber):
    for i in range (2, int(math.sqrt(inputNumber)) + 1):
        print i
        if inputNumber % i == 0:
            factors.append(i)
            if isPrime(i):
                primeFactors.append(i)

def isPrime(inputNumber):
    for x in range (2, int(math.sqrt(inputNumber)) + 1):
        print x
        if inputNumber % x == 0:
            #It is not a prime
            return False
    return True


if __name__ == "__main__":
    main()
