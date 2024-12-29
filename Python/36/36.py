def isPalindrome(n):
    n = str(n)
    rn = n[::-1]
    return rn == n

def main():
    sum = 0

    #print(isPalindrome(43))
    #print(isPalindrome(8558))
    #print(str(bin(45))[2:])

    for i in range(1000000):
        if isPalindrome(i):
            if isPalindrome(str(bin(i))[2:]):
                sum += i
    
    print(sum)
    

if __name__ == '__main__':
    main()