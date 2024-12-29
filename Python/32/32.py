# Take num as an integer, return true if contains numbers 1-9 only once, otherwise false
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
    # interate over all multiplicands and multipliers.
    # get the product, and put all three into one number. 
    # check if the whole thing is pandigital.
    # if it is, check to see if the product is in the list,
    # and add it if it isnt. 
    # then at the end sum up the list of products

    prodList = []
    for i in range(1, 10000):

        for j in range(1, 10000):
            
            prod = str(i * j)
            #
            if len(prod + str(i) + str(j)) == 9:
                if is1to9Pandigital(prod + str(i) + str(j)) == True:
                    print("prod " + prod + "   " + str(i) + " " + str(j))
                    if prod not in prodList:
                        prodList.append(prod)

    
    sum = 0
    for x in prodList:
        sum += int(x)
    print(sum)


if __name__ == '__main__':
    main()