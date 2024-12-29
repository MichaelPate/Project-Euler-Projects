import math

def isTriangleNum(tn):
    # if tn = (1/2) * n * (n + 1) does an integer solution for n exist?
    # n = (1/2) * ( sqrt(8*tn + 1) - 1)

    n = (1/2) * ( math.sqrt(8*tn + 1) - 1)

    if n % 1.0 == 0:
        return True
    else:
        return False

# For each character assign a value where A=1, B=2, etc.
# Then sum up these values and return
# ASCII - 64 to get letter value
def getWordValue(word):
    val = 0
    for letter in word:
        val += (ord(letter) - 64)
    return val

def main():
    wordsList = []
    count = 0

    with open("0042_words.txt", 'r') as file:
        lines = file.readlines()
    
    for word in lines[0].split(","):
        word = word.split("\"")[1]
        if isTriangleNum(getWordValue(word)):
            count += 1
    
    print(count)

if __name__ == '__main__':
    main()