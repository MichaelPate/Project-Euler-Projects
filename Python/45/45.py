# Triangle, pentagonal, and hexagonal numbers are generated with the following formulas
# Triangle: Tn = n(n + 1) / 2
# Pentagonal: Pn = n(3n-1) / 2
# Hexagonal: Hn = n(2n-1)

# See that T285 = P165 = H143 = 40755
# Find the next triangle number that is also pentagonal and hexagonal

# Solved on 2-4-2026

import math

def generateTriangleN(n):
    return int(n * (n + 1) / 2)

# This function re-used from problem 44
def isPentagonal(Pn):
    n = (1.0 / 6.0) * (math.sqrt((24.0 * Pn) + 1.0) + 1.0)
    if (n.is_integer()):
        return int(n)
    else:
        return False
    
# Very similar to isPentagonal
def isHexagonal(Hn):
    n = (1.0 / 4.0) * (math.sqrt((8.0 * Hn) + 1.0) + 1.0)
    if (n.is_integer()):
        return int(n)
    else:
        return False
    
# Just generate a triangle number (we know its triangular)
# and check to see if its also pentagonal and hexagonal
# If so print the number, up to the top of the range
# We can increase the range to find the number    
def main():
    for x in range(1, 10000000):
        triangleNum = generateTriangleN(x)
        if isPentagonal(triangleNum) and isHexagonal(triangleNum):
            print(triangleNum)

if __name__ == '__main__':

    main()
