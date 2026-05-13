# Find 4 consecutive numbers that each have 4 unique prime factors

# Solved 5-13-2026

import math, csv

# Taken from stackoverflow question 15285534
def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    
    return True

def genPrimesUpToN(n):
    # Generate primes up to number n
    primes = []
    for i in range(2,n):
        isPrime = True
        for div in range(2, i - 1):
            if i % div == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        if (i % 1000 == 0):
            print(i)
    return primes

def main():
    print("Generating Primes")
    primes = []
    # The primes csv was generated for problem 46, reuse it here as its way way faster
    # than generating primes
    with open("47\primes1.csv", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            primes.extend(row)
    primes = [int(p.split()[0]) for p in primes]

    # Implement prime factorization
    print("Factorizing...")
    countOf4PrimeFactors = 0
    testNum = 643
    while testNum < 500001:
        done = False
        workingNum = testNum
        factors = []
        factorSet = set()
        while done == False:
            # Take testNum and divide it by the smallest prime, 
            # starting at the smallest prime each time, until the 
            # test quotient is 1 or we have gotten to primes that 
            # are too large (2*sqrt(testNum)).

            # Then, check to see if we had 4 unique factors (set has no duplicates)
            # If we see 4 numbers in a row that have 4 unique factors each, return the test number minus 3 (contains the result)
            for prime in primes:
                if prime > 2 * math.sqrt(testNum):
                    done = True
                    break
                testQ = workingNum / prime
                if testQ % 1.0 == 0:
                    factors.append(prime)
                    factorSet.add(prime)
                    workingNum = int(testQ)
                    break
                if testQ == 1:
                    done = True

        if(len(factorSet)) == 4:
            countOf4PrimeFactors += 1
            print(f"Number {testNum} has factors {factors}, or as a set {factorSet} with length {len(factorSet)}")
        else:
            countOf4PrimeFactors = 0
        if countOf4PrimeFactors == 4:
            print(testNum - 3)
            # We printed the result so just stop here in an infinite loop
            while True:
                None

        #print(f"Number {testNum} has factors {factors}, or as a set {factorSet} with length {len(factorSet)}")
        testNum += 1
        if (testNum % 500 == 0):
            print(f"Reached {testNum}")



    None

if __name__=='__main__':
    main()