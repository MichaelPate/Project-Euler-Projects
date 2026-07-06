import csv
from collections import Counter
from itertools import combinations
from concurrent.futures import ProcessPoolExecutor
from functools import partial

def find_repeat(lst, x):
    counts = Counter(lst)
    repeats = [(val, count) for val, count in counts.items() if count > 1]
    singles = sum(1 for count in counts.values() if count == 1)
    
    if len(repeats) == 1 and repeats[0][1] == x and singles == len(counts) - 1:
        return repeats[0][0]
    return None

def processNumber(stPrime, primes):
    for indexesToReplace in range(1,10):
        if indexesToReplace > len(stPrime):
            continue
        listStringPrime = list(stPrime)
        index_combinations = list(combinations(range(len(listStringPrime)), indexesToReplace))
        for idxCombo in index_combinations:
            tests = []
            count = 0
            for testNum in range(0, 10):
                listStringPrime = list(stPrime)
                for idx in idxCombo:
                    listStringPrime[idx] = str(testNum)
                newStPrime = ''.join(listStringPrime)
                testNum = int(newStPrime)
                # if we found more than 2 numbers that arent prime, this combo is imposible
                #if testNum not in primes:
                #    count += 1
                #if count > 2:
                #    break
                tests.append(int(newStPrime))
            # check if 8 out of 10 of the elements in tests are prime
            #input(f"Replacing {indexesToReplace} digits of {stPrime} which gave {tests}")
            primeCount = 0
            for testPrime in tests:
                if testPrime in primes:
                    primeCount += 1
            if primeCount > 5:
                print(f"{stPrime}, after replacing {indexesToReplace} digit(s) to get {tests}, had {primeCount} primes out of {len(tests)}")
            if primeCount == 8:
                print(f"{stPrime}, after replacing {indexesToReplace} digit(s) to get {tests}, had {primeCount} primes out of {len(tests)}")
                return tests
            else:
                return []

def main():
    print("Generating Primes.")
    primes = []
    # The primes csv was generated for problem 46, reuse it here as its way way faster
    # than generating primes
    with open("51/primes1.csv", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            primes.extend(row)
    primes = [int(p.split()[0]) for p in primes]
    
    stringPrimes = [str(p) for p in primes]

    print("Starting work")
    worker = partial(processNumber, primes=primes)
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(worker, stringPrimes, chunksize=1000))

    print("Done")
    for result in results:
        if len(result) > 1:
            print(result)
    input("")

    # For each prime, for a number of repeating digits from 1 to 10, replace all iterations of the indexes with 0-9 and check if they are prime
    globalTests = []
    for stPrime in stringPrimes[5600:]:
        processNumber(stPrime, primes)
                

                


    for stPrime in stringPrimes[5650:]:
        print(stPrime)
        for testDigit in range(0, 10):
            indexes = []
            #print(f"Finding repeating {testDigit}'s in {stPrime}")
            for charIdx, charDigit in enumerate(stPrime):
                if int(charDigit) == testDigit:
                    # Find the indexes of all occurences of testDigit in stPrime
                    indexes.append(charIdx)
            
                # in stPrime, for indexes in indexes, replace with 0-9
                # len(indexes) > 1 because we need at least one repeat
                if len(indexes) > 1:
                    #print(f"There were {len(indexes)} repeats of the digit {testDigit} in {stPrime}, at indexes {indexes}")
                    count = 0
                    results = []
                    for testDigit in range(0, 10):
                        tests = []
                        #print(stPrime)
                        chars = list(stPrime)
                        #print(indexes)
                        for idx in indexes:
                            chars[idx] = str(testDigit)
                            #newStPrime = stPrime[:idx] + str(testDigit) + stPrime[idx + 1:]
                        newStPrime = ''.join(chars)
                        #print(newStPrime)
                        tests.append(int(newStPrime))
                        #print(tests)
                        
                        for test in tests:
                            if test in primes:
                                count += 1
                                #print(f"Test {test} was a prime, count is {count}")
                                results.append(test)
                        if count == 8:
                            print(results)
                            while True: None
                        elif count > 1:
                            print(f"There were {len(indexes)} repeats of the digit {testDigit} in {stPrime}, at indexes {indexes} and {count} were prime")
    #while True: None
        

    # for repeatingCount in range(1, 10):
    #     # look for repeatingCount indexes where each has the same number in it
    #     # example: 454428 returns [0, 2, 3]
    #     # look for any digitPositions that repeats repeatingCount times


    #     repeatedPrimes = []
    #     for repeatingDigit in range(0, 10):
    #         repeatedPrimes = [int(st) for st in stringPrimes if find_repeat(st, repeatingCount) == str(repeatingDigit)]
    #         print(f"primes with {repeatingCount} repeated {repeatingDigit}'s: {len(repeatedPrimes)}")

    # while True: None

    # for repeatingDigit in range(0, 10):
    #     rpCount = 0
    #     rpList = []
    #     for repeatingCount in range(0, 10):
    #         print(f"Counting primes with {repeatingCount} repeating {repeatingDigit}'s")
    #         rpList = [st for st in stringPrimes if find_repeat(st, repeatingCount) == str(repeatingDigit)]
        
        
    #     while True: None
    #     if rpCount == 8:
    #         print(sorted(rpList))

    # while True: None

    # for numOfDigitsReplaced in range(1, 13):
    #     primesWithRepeatedDigits = []
    #     arrayOfFamilies = [[] for x in range(10)]
    #     print(f"Checking primes with {numOfDigitsReplaced} repeating digits.")
    #     for primeIdx, prime in enumerate(primes[4:]):
    #         # find a group of 8 primes that each have exactly 1 copied digit (two digits are the same)
    #         # a list of all digits and a set of all digits should have len(list) = len(set) + 1
    #         digitList = [int(digit) for digit in str(prime)]
    #         digitSet = set(int(digit) for digit in digitList)

    #         if len(digitList) - numOfDigitsReplaced == len(digitSet):
    #             primesWithRepeatedDigits.append(prime)
    #             #print(f"{prime} has {numOfDigitsReplaced} repeating digits.")

    #             # what digit was duplicated?
    #             # want occurance of any digit to be >1 and the rest 1 in digitList
    #         repeatedDigit = find_repeat(digitList, numOfDigitsReplaced)
    #         if repeatedDigit != None:
    #             #print(digitList)
    #             #print(int(repeatedDigit))
    #             arrayOfFamilies[int(repeatedDigit)].append(prime)


    #     # if any family got to 8 elements, 
    #     #print(arrayOfFamilies)
    #     for list in arrayOfFamilies:
    #         if len(list) < 10:
    #             print(f"{len(list)}\t\t{sorted(list)}")
    #         #    while True: None
    #         else:
    #             print(len(list))
    #     continue
    #     while True: None
    #     for listIdx, list in enumerate(arrayOfFamilies):
    #         print(f"{listIdx} has a family size of {len(list)}")
    #         if len(list) != 8:
    #             break
    #         for item in list:
    #             if item not in primes:
    #                 break
    #         print(list)
    #         while True:
    #             None
    # #print(arrayOfFamilies)

    # while True:
    #     None





    # # 
    # for mainNumber in range(55000, 57000):
    #     numOfDigits = len(str(mainNumber))
    #     for replacePos1 in range(0, numOfDigits):
    #         for replacePos2 in range(0, numOfDigits):
    #             if replacePos1 != replacePos2:
    #                 familyCount = 0
    #                 familyNumbers = []
    #                 for replaceNum in range(1, 10):
    #                     mainNumberString = str(mainNumber)
    #                     mainNumberString = mainNumberString[:replacePos1] + str(replaceNum) + mainNumberString[replacePos1+1:]
    #                     mainNumberString = mainNumberString[:replacePos2] + str(replaceNum) + mainNumberString[replacePos2+1:]
    #                     #print(f"original number {mainNumber} becomes " + mainNumberString)
    #                     newNum = int(mainNumberString)
    #                     if newNum in primes:
    #                         familyCount += 1
    #                         familyNumbers.append(newNum)
    #                     if familyCount == 7:
    #                         print(familyNumbers)
    #                         while True:
    #                             None

if __name__=='__main__':
    main()