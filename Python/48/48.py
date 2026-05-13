# Find the last ten digits of the series 1^1 + 2^2 + 3^3 + 4^4 + ... + 1000^1000

# solved 5-13-2026

# naive approach, just do it and print out the last 10 digits of the result converted to a string
def main():
    sum = 0
    for i in range(1, 1000):
        sum += i**i
        #input(i**i)
    print(str(sum)[-10:])
    None

if __name__ == '__main__':
    main()