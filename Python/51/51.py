
# solved 5-19-2026

import csv
from itertools import combinations

# Taken from stackoverflow question 15285534
def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    
    return True

def main():
    print("Generating Primes.")
    primes = []
    # The primes csv was generated for problem 46, reuse it here as its way way faster
    # than generating primes
    with open("51/primes1.csv", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            primes.extend(row)
    primes = [int(p.split()[0]) for p in primes]
    stringPrimes = [str(p) for p in primes]
    print("Done.")

    # Look at each prime, skipping the first few
    for stPrime in stringPrimes[1000:]:
        # For each prime, check out ways to replace its digits with 0-9
        listStPrime = list(stPrime)
        print(stPrime)
        for replaceIdxCnt in range(1, len(stPrime)):
            # if we are replacing replaceIdxCnt of digits, what combinations are there?
            index_combinations = list(combinations(range(len(listStPrime)), replaceIdxCnt))
            # Now, for each combination, we need to replace the digits from 0 - 9
            for idxCombo in index_combinations:
                tests = []
                errorCount = 0
                for digit in range(0, 10):
                    replacedStPrime = list(stPrime)
                    for idx in idxCombo:
                        replacedStPrime[idx] = str(digit)
                    # Now we have replaced all indexes with a digit, add the number to the list
                    newStPrime = ''.join(replacedStPrime)
                    
                    if isPrime2(int(newStPrime)) == False:
                        errorCount += 1
                    else:
                        newStPrime += "prime"
                    if errorCount > 2:
                        # So far more than 2 results are not prime, so this combination cant work
                        break
                    tests.append(newStPrime)
                if errorCount == 2:
                    # Found a system with 8/10 primes
                    # using "input" to skip a result. Use ctrl-c to stop the program
                    input(f"For prime {stPrime}, replace {replaceIdxCnt} digits with 0-9. IDX Combos: {index_combinations}, Results for IDX combo {idxCombo}: {tests}. Of these, 8 were prime.")

if __name__=='__main__':
    main()