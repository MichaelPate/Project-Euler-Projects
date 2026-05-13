
# solved 5-13-2026

import csv

# most code for this function comes from geeksforgeeks article
# https://www.geeksforgeeks.org/dsa/check-if-two-strings-are-permutation-of-each-other/
def isPermutation(x, y):
    # Get set of digits 
    digitsofX = sorted([int(d) for d in str(x)])
    digitsofY = sorted([int(d) for d in str(y)])
    
    return digitsofX == digitsofY

def main():
    print("Generating Primes.")
    primes = []
    # The primes csv was generated for problem 46, reuse it here as its way way faster
    # than generating primes
    with open("49\primes1.csv", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            primes.extend(row)
    primes = [int(p.split()[0]) for p in primes]

    # keep only 4 digit primes
    fourDigitPrimes = []
    for prime in primes:
        if len(str(prime)) == 4:
            fourDigitPrimes.append(prime)
    print("Done.")
    #print(fourDigitPrimes)

    perms = []
    for fdPrime1 in fourDigitPrimes:
        permsofdPrime1 = set()
        for fdPrime2 in fourDigitPrimes:
            if isPermutation(fdPrime1, fdPrime2):
                permsofdPrime1.add(fdPrime2)
                #input(f"For prime {fdPrime1} found permutation {fdPrime2}")
        perms.append(permsofdPrime1)
        #input(permsofdPrime1)
    
    for p in perms:
        if (len(p) > 2):
            # For each list, see if the permutations are equally spaced
            permList = sorted(list(p))
            #input(permList)

            idx = len(permList) - 1
            lastDiff = 0
            diffsInaRow = 0
            while idx >= 1:
                d = permList[idx] - permList[idx-1]
                if d == lastDiff:
                    diffsInaRow += 1
                    #print(f"{permList} {d} {diffsInaRow}")
                else:
                    diffsInaRow = 0
                    lastDiff = d
                if diffsInaRow == 1:
                    print(permList)
                    # Result was [2699, 2969, 6299, 9629] where diff == 3330, took 2969, 6299, 9629
                    break
                idx -= 1

if __name__ == '__main__':
    main()