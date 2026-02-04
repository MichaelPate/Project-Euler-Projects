# We need to find the smallest composite number that cannot be written as the sum of a prime and twice a square

# solved 2-4-2026

import math

# Taken from stackoverflow question 15285534
def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    
    return True

# with our list of primes, we can start adding all kinds double squares and adding the sums to a set.
# after we have done that enough, we can find the smallest number thats not in the set


def main():
    # Generate primes
    primes = []
    for i in range(100000):
        isPrime = True
        for div in range(2, i - 1):
            if i % div == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)

    # generate double squares
    double_squares = []
    for i in range(1000):
        double_squares.append(2 * i * i)

    not_found = []
    for number in range(2, 40000):
        # our number must be composite and odd
        if (number % 2 != 0 and number not in primes):
            found_solution = False

            idx = 0
            # check all primes up to the number itself
            while idx < len(primes) and primes[idx] < number:
                # Try to subtract the prime
                prime = primes[idx]
                remainder = number - prime
                # With this remainder, try to find a square that will complete the number
                # If we cant find a square, then we have no solution
                if remainder in double_squares:
                    found_solution = True
                idx += 1
            
            # After checking all combinations of primes and squares, we found no solution
            # therefore we found an odd composite that cannot be written as the sume of a prime and twice a square
            if found_solution == False:
                not_found.append(number)

    # the smallest number in this list should be the output
    print(not_found)

if __name__ == '__main__':
    main()