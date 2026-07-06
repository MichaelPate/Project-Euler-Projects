
# solved 5-19-2026



# I am proud of myself that I one-shotted this recursive factorial function in 15 seconds flat (not a joke)
# only two mistakes were first doing + instead of *, and returning n when n>1==False instead of returning 1 (that way we handle factorial(0))
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
    
def combinations(n, r):
    if r > n:
        return -1
    return factorial(n) // (factorial(r) * factorial(n - r))

def main():
    count = 0
    for n in range(1, 101):
        for r in range(1, n):
            if combinations(n, r) > 1000000:
                count += 1
    print(count)

if __name__=='__main__':
    main()