def main():
    currentResult = 0
    biggestPalin = 0

    for i in range (100, 999):
        for x in range (100, 999):
            currentResult = i * x
            #print "Equation: ", i, " x ", x

            if reversal(currentResult):
                #print "Palendrome: ", currentResult

                if currentResult > biggestPalin:
                    biggestPalin = currentResult

    print "Biggest Palendrome: ", biggestPalin

def reversal(num):
    return str(num) == str(num)[::-1]

if __name__ == '__main__':
    main()
