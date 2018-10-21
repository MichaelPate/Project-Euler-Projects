import math

def main():
    primeNumberCount = 0
    primeNumber = 0
    workingNum = 0

    while primeNumberCount <= 10001:
         workingNum += 1

         if isPrime(workingNum):
             primeNumberCount += 1
             primeNumber = workingNum

    print primeNumber

def isPrime(inputNumber):
    for x in range (2, int(math.sqrt(inputNumber)) + 1):
        if inputNumber % x == 0:
            #It is not a prime
            return False
    return True
if __name__ == '__main__':
    main()
