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
    sum = 0
    count = 0
    primes = EratosPrimes(1000000)

    for idx in range(4, len(primes)):   # start at 4 to skip primes up to 7
        prime = str(primes[idx])

        if idx % 100 == 0:
            print(f"IDX: {idx}")

        # lets try left to right
        successes = 0
        for digit_idx in range(len(prime)):
            if int(prime[digit_idx:]) in primes:
                successes += 1
            else:
                break
            #print("  " + prime[digit_idx:])
            
        for digit_idx in range(1, len(prime)):
            #print(f"{prime}   {digit_idx}    :" + prime[:digit_idx])
            if int(prime[:digit_idx]) in primes:
                successes += 1
            else:
                break

        if successes == (2 * len(prime) - 1):
            count += 1
            sum += int(prime)


    print(count)
    print(sum)


if __name__ == '__main__':
    main()