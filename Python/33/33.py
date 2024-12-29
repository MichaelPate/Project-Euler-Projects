def main():
    prod = 1
    nums = []
    dens = []

    for numer in range(10, 99):
        for denom in range(10, 99):
            n = str(numer)
            d = str(denom)
            realFrac = numer / denom

            # if the n and d share a number, find it and remove it
            if n[1] == d[0]:
                # remove n[1] and the same from d
                n = n[0]
                d = d[1]
            elif n[1] == d[1]:
                n = n[0]
                d = d[0]
            elif n[0] == d[0]:
                n = n[1]
                d = d[1]
            elif n[0] == d[1]:
                n = n[1]
                d = d[0]
            
            
            if len(n) == 1 and int(d) != 0 and numer % 10 != 0 and realFrac <= 1.0:
                newFrac = int(n) / int(d)
                if newFrac == realFrac and newFrac != 1.0:
                    print(f"{numer}/{denom} = {realFrac} --> {n}/{d} = {newFrac}")
                    prod *= newFrac
                    nums.append(n)
                    dens.append(d)
                    #print(str(realFrac) + " " + str(newFrac))
            
    print(prod)

    prodN = 1
    for n in nums:
        prodN *= int(n)
    
    prodD = 1
    for d in dens:
        prodD *= int(d)
    
    print(prodN / prodD)

    # from here I 'cheated' because I submitted '100' after seeing a result of prodN / prodD = 0.01


if __name__ == '__main__':
    main()