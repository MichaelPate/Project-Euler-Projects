import math

def isPentagonal(testNum):
    # our formula is Pn = n(3n-1)/2
    # n = (1/6)(sqrt(24*P+1)+1) and if thats an integer, then our number is pentagonal
    n = (1/6)*(math.sqrt(24*testNum+1)+1)

    # It can be slightly off due to floating point math
    if n % 1 < 0.0001:
        return True
    else:
        return False
    
def main():
    # generate a big list of pentagonal numbers
    # now go through all combinations and find their difference.
    # for each combination, check their 

    print(isPentagonal(46651606))
    while True:
        None
    pentagonalNumbers = []
    for i in range(100000000):
        if isPentagonal(i):
            pentagonalNumbers.append(i)

    # go through each combination
    min_D = 1000
    for num1_idx in range(len(pentagonalNumbers)):
        for num2_idx in range(len(pentagonalNumbers)):
            
            num1 = pentagonalNumbers[num1_idx]
            num2 = pentagonalNumbers[num2_idx]
            #print(f"{num1} and {num2}")

            d = abs(num1 - num2)
            if isPentagonal(d):
                if isPentagonal(num1 + num2):
                    if d < min_D:
                        min_D = d
                        print(f"num 1: [{num1_idx}]={num1}\tnum 2: [{num2_idx}]{num2}")

    print(min_D)

if __name__ == '__main__':
    main()