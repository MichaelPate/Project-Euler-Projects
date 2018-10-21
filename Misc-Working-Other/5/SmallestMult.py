def main():
    #Find the smallest integer that can be divided by numbers 1-20 with no remainder
    workingNum = 1
    flag = False
    valid = False

    while not flag:
        if workingNum % 1000000 == 0:
            print workingNum / 1000000

        for i in range(1, 20):
            if workingNum % i == 0:
                #It worked
                valid = True
            else:
                #It did not work
                valid = False
                break

        if valid:
            print workingNum
            flag = True
        else:
            flag = False
            workingNum += 1

if __name__ == '__main__':
    main()
