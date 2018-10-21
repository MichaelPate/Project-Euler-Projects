#List the sum of all the mutiples of 3 and 5 under 1000

sumOfMult = 0

for x in range (0, 1000):
    if x % 5 == 0:
        sumOfMult += x
    elif x %3 == 0:
        sumOfMult += x

print "Sum of all multiples of 3 and 5: ", sumOfMult
