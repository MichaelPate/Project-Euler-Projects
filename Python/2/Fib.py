#Find every even fibo number under 4 million

total = 0
current = 1
last = 0
temp = 0

while current <= 4000000:
    temp = current
    current = last + current
    last = temp

    if current % 2 == 0:
        total += current

    print "Current: ", current, "\n"
print "Sum: ", total, "\n"
