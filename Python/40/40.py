def main():
    numString = ''
    for i in range(1000000):
        numString += str(i)
    
    product = 1
    idx = 1

    for x in range(7):
        product *= int(numString[idx])
        print(idx)
        idx = idx * 10

    print(product)

if __name__ == '__main__':
    main()