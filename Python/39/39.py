import math

def main():

    maxSolutions = 0
    pForMaxSolutions = 0

    # Generate a perimeter
    for p in range(1001):
        if p % 10 == 0:
            print(p)

        solutions = 0


        a = 0
        b = 0
        c = 0

        
        # a + b + c = p
        # a^2 + b^2 = c^2

        # a = p - (b + c)
        # b = p - (a + c)
        # c = p - (a + b)

        for a in range(int(p)):
            for b in range(int(p)):
                # c = p - (a + b)
                # a^2 + b^2 = c^2
                c = math.sqrt(((a*a) + (b*b)))
                if a + b + c == p and c % 1.0 == 0 and b > a and a > 0 and b > 0 and c > 0:
                    #print(f"a:{a}, b:{b}, c:{c}, p:{p}")
                    solutions += 1



        # (p - (b + c))^2 + (p - (a + c))^2 = (p - (a + b))^2 





        # find solutions to a^2 + b^2 = c^2 where a+b+c=p
        #for a in range(int(p/3)):
        #    for b in range(int(p/2)):

                #c = 1
                #while a + b + c <= p:
                #    if (a*a) + (b*b) == (c*c):
                #        solutions += 1
                #    c += 1


                #for c in range(int(p/2)):
                #    if (a*a) + (b*b) == (c*c) and a + b + c == p:
                #        solutions += 1
        
        #print(f"P {p} had {solutions} solutions")
        if solutions > maxSolutions:
            maxSolutions = solutions
            pForMaxSolutions = p
            print("   " + str(pForMaxSolutions) + "  sols " + str(solutions))
    
    print(pForMaxSolutions)

if __name__ == '__main__':
    main()