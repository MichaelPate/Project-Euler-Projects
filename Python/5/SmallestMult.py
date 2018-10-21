def main():
    workingNum = 1
    numValid = False
    done = False

    while numValid is False:
        for i in range (1, 10):
            #If there is a remainder...
            if not workingNum % i == 0 and workingNum <= i:
                #Flag that the working number is not valid
                numValid = False
            else:
                numValid = True

        if not numValid:
            workingNum += 1

    print workingNum

if __name__ == '__main__':
    main()
