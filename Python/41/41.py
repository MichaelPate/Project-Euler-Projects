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

# pandigital function from problem 32
def isPandigital(num, bound = 9):
    # Lets take the input number as a string, then we will go through and add each
    # character to a list, checking first to see if it exists in the list. If a given
    # char does exist, then we see it twice and therefore return false.
    # Once the whole number is checked this way, we look at the size of the list. If it contains
    # 10 elements, return true. Otherwise false

    stringNum = str(num)
    charList = []

    for char in stringNum:
        if char in charList or char == '0' or int(char) > bound:
            return False
        else:
            charList.append(char)
            
    if len(charList) == bound:
        return True
    else:
        return False

def main():
    primes = EratosPrimes(1000000000)
    print(f"found {len(primes)} primes. Finding largest pandigital")
    
    maxPrime = 0
    idx = len(primes) - 1
    
    bound = 9
    while bound > 3:
        idx = len(primes) - 1
        while idx > 0:
            if isPandigital(primes[idx], bound):
                print(primes[idx])
                bound = 0
                break
            idx -= 1

        bound -= 1


        

if __name__ == '__main__':
    main()