# We need to generate pentagonal numbers using the fomula Pn = n (3n - 1) / 2
# We know the first ten pentagonal numbers: 1,5,12,22,35,51,70,92,117,145

# It can be seen that P4 + P7 = 22 + 70 = 92, which equals P8, but their minDifferenceerence, 70 - 22 = 48, is not pentagonal.
# We must find the pair of pentagonal numbers whose sum and minDifferenceerence are both pentagonal, such that D = | Pk - Pj | is minimuzed.
# Return the value of minimal value of D

# Success on 2-4-2026

import math

# Returns the pentagonal number for the passed index n
def generatePentagonalN(n):
    return int(n * (3 * n - 1) / 2)

# Returns the index of the pentagonal number for the passed test number
# or False if it does not exist
def isPentagonal(Pn):
    n = (1.0 / 6.0) * (math.sqrt((24.0 * Pn) + 1.0) + 1.0)
    if (n.is_integer()):
        return int(n)
    else:
        return False

def main():
    # Lets try brute forcing it
    minDifference = 10**30
    pentagonals = []
    for x in range(1, 10000):
        pentagonals.append(generatePentagonalN(x))

    # with our list of pentagonal numbers we can iterate over it
    for pj in pentagonals:
        for pk in pentagonals:
            sum = pj + pk
            diff = int(math.fabs(pk - pj))

            # Instead of searching the list for sum and dif, use the test function
            # to find the minimum
            if isPentagonal(sum) > 0 and isPentagonal(dif) > 0 and diff < minDifference:
                minDifference = dif
    print(minDifference)

if __name__ == '__main__':
    main()