# pandigital function from problem 32
def is1to9Pandigital(num):
    # Lets take the input number as a string, then we will go through and add each
    # character to a list, checking first to see if it exists in the list. If a given
    # char does exist, then we see it twice and therefore return false.
    # Once the whole number is checked this way, we look at the size of the list. If it contains
    # 10 elements, return true. Otherwise false

    stringNum = str(num)
    charList = []

    for char in stringNum:
        if char in charList or char == '0':
            return False
        else:
            charList.append(char)
            
    if len(charList) == 9:
        return True
    else:
        return False

def main():
    # take a number and start multiplying it by 1,2,3,...,n while concatenating the products together
    # Stop once we have 9 digits worth of products
    # Then check the string, and see if its pandigital. Keep the max

    maxPandigital = 0

    for i in range(1000000):
        productString = ''
        multiple = 0
        while len(productString) < 9:
            multiple += 1
            productString += str(i * multiple)
        
        if is1to9Pandigital(productString):
            if int(productString) > maxPandigital:
                maxPandigital = int(productString)
    
    print(maxPandigital)


if __name__ == '__main__':
    main()