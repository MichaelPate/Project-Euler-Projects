
# solved 5-14-2026

import csv
#import concurrent.futures

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
    print("Done.")
    print(findSums(primes))

    # Use a context manager to ensure threads are cleaned up
    #with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    # Use executor.map to run the task for each item in the list
    #    results = list(executor.map(findSums, primes))
    #    print(results)

def findSums(primes):
    # This attempted to make a list of all series of sums and tried to use a sliding window to find the maximum count, but was even slower than the other approach below
    # cumulative = [2]
    # for i, prime in enumerate(primes):
    #     if i >= 1:
    #         cumulative.append(cumulative[i-1]+prime)
    # maxSum = 0
    # maxCount = 0
    # for i, prime in enumerate(primes):
    #     if prime > 1000000:
    #         break
    #     # start at 0 and try to work up to prime
    #     # then increment the starting position
    #     start = 0
    #     maxPrime = 0
    #     cumulativeLength = len(cumulative)
    #     while start < i // 2:
    #         end = 0
    #         count = 0
    #         while end < cumulativeLength and cumulative[end] - cumulative[start] != prime:
    #             end += 1
    #         if cumulative[end-1] - cumulative[start] == prime:
    #             count = end - start
    #             if count > maxCount:
    #                 maxCount = count
    #                 maxPrime = prime
    #         start += 1
    #     print(prime)
    # return maxPrime

    # Now we need to see if we can sum primes up to this one
    maxSum = 0
    maxCount = 0
    for i, prime in enumerate(primes):
        # have an offset from index 0 that will slowly move up towards our current position (i) in primes
        offsetIdx = 0
        #print(prime)
        while offsetIdx < i // 2:
            sum = 0
            count = 0
            # from our starting window, build a sum by adding count (1) each time until a sum is made 
            while sum <= prime:
                if sum == prime:
                    # We met exactly, so break out and lets see if our streak was bigger than the max
                    break
                if sum > prime:
                    # Though if we overshoot, break out and make sure count cant be above maxCount
                    count = -1
                    break
                sum += primes[count+offsetIdx]
                count += 1

            if sum == prime:
                if count > maxCount:
                    maxCount = count
                    maxSum = sum
                    print(f"Max sum {maxSum} has {maxCount} elements.")

            offsetIdx += 1

    return maxSum

if __name__=='__main__':
    main()