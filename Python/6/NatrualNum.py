import math




def main():
    sum_of_squares = 0
    for i in range(1, 101):
        sum_of_squares += math.pow(i, 2)
    print sum_of_squares

    square_of_sum = 0
    temp = 0
    for i in range(1, 101):
        temp += i
    square_of_sum = math.pow(temp, 2)
    print square_of_sum

    print square_of_sum - sum_of_squares

if __name__ == '__main__':
    main()
