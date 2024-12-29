def generatePandigitals(lowerBound, upperBound):
    pandigitals = []
    

def zeroToBoundPandigital(num, bound = 9):
    # Lets take the input number as a string, then we will go through and add each
    # character to a list, checking first to see if it exists in the list. If a given
    # char does exist, then we see it twice and therefore return false.
    # Once the whole number is checked this way, we look at the size of the list. If it contains
    # 10 elements, return true. Otherwise false

    stringNum = str(num)
    charList = []

    for char in stringNum:
        if char in charList or int(char) > bound:
            return False
        else:
            charList.append(char)
            
    if len(charList) == bound + 1:  # +1 to account for zero
        return True
    else:
        return False
    

# Sieve of Eratosthenes to generate primes up to n
# from problem 37
def EratosPrimes(n):
    is_prime = [False, False] + [True] * (n - 1)
    primes = [2]
    for j in range(4, n + 1, 2):
        is_prime[j] = False
    for i in range(3, n + 1, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

def main():
    primes = EratosPrimes(17)
    len = 3
    sum = 0

    for i in range(1000000000, 10000000000):
        #i = 1406357289

        if i % 1000000 == 0:
            print(i)

        if zeroToBoundPandigital(i):
            num = str(i)
            successes = 0
            for x in range(6):
                val = int(num[1+x : 1+x+len])
                #print(val)
                if val % primes[x] == 0:
                    # worked
                    successes += 1
            if successes == 6:
                sum += i
        #break

    print(sum)


if __name__ == '__main__':
    main()