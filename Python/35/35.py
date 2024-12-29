import csv

def prime(n): 
    for i in range(2, n): #for every value between 1 and n
        if n%i == 0: #check if i divides n
            return False #if this is true, n is not prime
    return True if n > 1 else False #values less than 2 are not prime.

def rotateLeft(n):
    return n[1:] + n[0]

# Sieve of Eratosthenes to generate primes up to n
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
    count = 0
    print("generate primes")
    
    primes = EratosPrimes(1000000)

    print("find cyclic primes")
    for n in primes:
        #print(n)
        s = str(n)
        successes = 0
        for i in range(len(s)):
            s = rotateLeft(s)
            #if prime(int(s)):
            if int(s) in primes:
                successes += 1
            else:
                break
        if successes == len(s):
            count += 1

    print(count)




if __name__ == '__main__':
    main()