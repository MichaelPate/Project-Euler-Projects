import math, csv

def genPrimes(n):
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
    return primes

# tests if nubmer n has 4 prime factors. If so, returns the factors
def has4primeFactors(n, primes):
    # first get all the factors of n
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    primeFactors = set()
    for factor in sorted(list(factors)):
        if factor in primes:
            primeFactors.add(factor)
    if len(primeFactors) < 4:
        return False
    else:
        #print(primeFactors)
        return primeFactors
    
def main():
    # import primes from csv
    primes = []
    with open("47\primes1.csv", newline='') as f:
        reader = csv.reader(f)
        primes = list(reader)

    #primes = genPrimes(1000000)
    print("primes generated")
    numbers = []
    for i in range(1000000):
        if i % 10 == 0:
            print(i)
        if(has4primeFactors(i,primes) is not False):
            numbers.append(i)
            print(i)

            if len(numbers) > 4:
                for idx in range(len(numbers)-4):
                    first = numbers[idx]
                    if numbers[idx+1] == first + 1:
                        if numbers[idx+2] == first + 2:
                            if numbers[idx+3] == first + 3:
                                print(first)
                                while True:
                                    None


    print(numbers)
    # find pairs of consecutive numbers in i



if __name__ == '__main__':
    main()