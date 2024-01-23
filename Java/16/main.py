def main():
    sum = pow(2, 1000)
    print(sum)
    n =sum
    s = 0
    while n:
        s += n % 10
        n //= 10

    print(s)

if __name__=='__main__':
    main()