import math

def main():
    sum = 0
    for n in range(3, 1000000):
        stringn = str(n)

        testSum = 0
        for char in stringn:
            testSum += math.factorial(int(char))
        
        if testSum == n:
            sum += n
    print(sum)

if __name__ == '__main__':
    main()