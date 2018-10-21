import time
import numpy as np

def main():
    #Begin time tracking
    start_time = time.time()

    #Read the file into a list
    numberFile = open("numberSource.txt", "r")
    numbers = str(numberFile.readlines())
    numbers = numbers[2:1002]
    numberList = map(int, numbers)

    #Positions for elements in the list
    beginning = 0
    end = 0
    #List to hold divisors
    divisors = []
    #Results
    product = 1
    largestProduct = 1

    for beginning in range (0, 988):
        #Get the end, this creates a range of 13 numbers each time
        end = beginning + 13

        for i in range (beginning, end):
            #All the numbers in the range need to be multiplied.
            divisors.append(numberList[i])

        #Multiply all the numbers together
        print "Divisors: ", divisors
        product = np.prod(np.array(divisors))

        #Compare the products
        if product > largestProduct:
            largestProduct = product
            print "New Largest Product: ", product
            product = 0

        #Empty the list of divisors
        divisors[:] = []
        print "List Emptied. ", divisors

    print largestProduct

    print time.time()-start_time
if __name__ == '__main__':
    main()
