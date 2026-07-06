# solved 6-15-2026

def convertCardToScore(card):
    if len(card) > 1:
        charCard = card[0]
    else:
        charCard = card
    if charCard.isdigit():
        return int(charCard)
    #charToInt = int(charCard)
    #if charToInt > 2 and charToInt < 11:
    #    return charToInt
    if charCard == 'T':
        return 10
    if charCard == 'J':
        return 11
    if charCard == 'Q':
        return 12
    if charCard == 'K':
        return 13
    if charCard == 'A':
        return 14
    return 0

def convertScoreToCard(intScore):
    if intScore > 2 and intScore < 10:
        return str(intScore)
    if intScore == 10:
        return 'T'
    if intScore == 11:
        return 'J'
    if intScore == 12:
        return 'Q'
    if intScore == 13:
        return 'K'
    if intScore == 14:
        return 'A'
    return ''

# hand contains 5 strings, where each string is 2 chars
# first char is the card value, second is suit
# Want to return a tuple, where one is a [score, card] and the other is the highest value card in the hand
# The score is based off combinations like one pair, flush, four of a kind, etc
# if a score is zero, that means there was no combos and only the high card matters
def handScore(hand):
    valuesList = [card[0] for card in hand.split(" ")]
    valuesScoreList = [convertCardToScore(card) for card in valuesList]
    suitesList = [card[1] for card in hand.split(" ")]

    returnScore = [0, ' ', ' ']   # rank, value of card that made the rank, highest valued card in the hand
    maxReturnScore = 0
    
    # find the highest value in the hand
    returnScore[2] = convertScoreToCard(sorted(valuesScoreList)[-1])

    # Look for pairs or multiple of a kind
    # If found return the type of pair and the card that made the pair
    twoCounts = 0
    threeCounts = 0
    for valueIdx, value in enumerate(valuesScoreList):
        count = valuesScoreList.count(value)
        #print(f"card {convertScoreToCard(value)} seen {count} times")
        #print(count)
        if count == 2:
            # two of a kind worth a score of 2
            if maxReturnScore < 2:
                returnScore[0] = 2
                returnScore[1] = convertScoreToCard(value)
                maxReturnScore = 2
            twoCounts += 1
        if count == 3:
            # three of a kind worth a score of 4
            if maxReturnScore < 4:
                returnScore[0] = 4
                returnScore[1] = convertScoreToCard(value)
                maxReturnScore = 4
            threeCounts += 1
        if count == 4:
            # four of a kind worth a score of 8
            if maxReturnScore < 8:
                returnScore[0] = 8
                returnScore[1] = convertScoreToCard(value)
                maxReturnScore = 8
    
    if twoCounts > 2:
        # we actually found a two pairs which is 3 points
        if maxReturnScore < 3:
            returnScore[0] = 3
            returnScore[1] = returnScore[2]
            maxReturnScore = 3    
    if twoCounts == 2 and threeCounts == 3:
        # we actually found a full house which is 7 points
        if maxReturnScore < 7:
            returnScore[0] = 7
            #returnScore[1] = returnScore[2]
            maxReturnScore = 7
    
    # still need straight, straight flush, and royal flush
    # check if straight
    sortedScores = sorted(valuesScoreList)
    if sortedScores[-1] - sortedScores[0] == 4 and len(set(sortedScores)) == 5:  # Difference of 4 across 5 unique cards -> straight
        # thats a straight, for 5 points
        if maxReturnScore < 5:
            returnScore[0] = 5
            returnScore[1] = returnScore[2]
            maxReturnScore = 5

    # check if a flush
    #input(set(suitesList))
    if len(set(suitesList)) == 1:
        # All same suite, so flush worth 6
        if maxReturnScore < 6:
            returnScore[0] = 6
            returnScore[1] = returnScore[2]
            maxReturnScore = 6
        
        # if all cards are consecutive then upgrade to straight flush for 9 points
        sortedScores = sorted(valuesScoreList)
        if sortedScores[-1] - sortedScores[0] == 4 and len(set(sortedScores)) == 5:
            # 5 in a row
            if maxReturnScore < 9:
                returnScore[0] = 9
                returnScore[1] = returnScore[2]
                maxReturnScore = 9
    
        # if the following cards are present, then royal flush for 10 points
        if valuesScoreList.count(10) == 1 and valuesScoreList.count(11) == 1 and \
            valuesScoreList.count(12) == 1 and valuesScoreList.count(13) == 1 and valuesScoreList.count(14) == 1:
            if maxReturnScore < 10:
                returnScore[0] = 10
                returnScore[1] = returnScore[2]
                maxReturnScore = 10          

    #print(returnScore)
    return returnScore

# takes a hand of any length and returns the n-th highest 
def highCard(hand, n):
    cardsList = [card for card in hand.split(" ")]
    #print(cardsList)
    cardScoreList = [convertCardToScore(card) for card in cardsList]

    # bubble sort on the list of cards
    idx = 0
    sorted = False
    while not sorted:
        didASwap = False
        for idx in range(0, len(cardsList)-1):
            #print(f"{cardsList[idx]}({convertCardToScore(cardsList[idx])}) compared to {cardsList[idx+1]}({convertCardToScore(cardsList[idx+1])})")
            if convertCardToScore(cardsList[idx]) > convertCardToScore(cardsList[idx+1]):
                temp = cardsList[idx+1]
                cardsList[idx+1] = cardsList[idx]
                cardsList[idx] = temp
                didASwap = True
        if didASwap == False:
            sorted = True

    # for i in range(20):
    #     for cardIdx, card in enumerate(cardsList):
    #         # compare card to all others
    #         for compIdx, compCard in enumerate(cardsList):
    #             if compIdx != cardIdx:
    #                 if convertCardToScore(card[0]) < convertCardToScore(compCard[0]):
    #                     temp = cardsList[cardIdx]
    #                     cardsList[cardIdx] = cardsList[compIdx]
    #                     cardsList[compIdx] = temp
    #print(cardsList)
    if n == 0:
        return cardsList
    else:
        return cardsList[-n]


# Takes two hands (10x 2 character items in a string), scores them, and determines a winner
def winningHand(handRow):
    hand1 = handRow[:14]
    hand2 = handRow[15:]
    
    score1 = handScore(hand1)
    score2 = handScore(hand2)

    #print(score1)
    #print(score2)

    highestCard1 = convertCardToScore(score1[2])
    highestCard2 = convertCardToScore(score2[2])
    # comboCard is the card that made the combo, like in a pair of fives, the combocard is 5

    print(f"Hand 1: {hand1} has score {score1}, Hand 2: {hand2} has score {score2}")
    #print(highestCard1)
    #print(highestCard2)

    if score1[0] > score2[0]:
        return 1
    if score2[0] > score1[0]:
        return 2
    # Both hands had the same score
    if score1[0] == score2[0]:
        if score1[0] == 0:
            # both hands bad, compare highest cards
            if highestCard1 > highestCard2:
                return 1
            if highestCard2 > highestCard1:
                return 2
            else:
                return 1
    
        # not just high card, since we havent returned yet, so lets look at the card that made the combo
        highestCard1 = convertCardToScore(score1[1])
        highestCard2 = convertCardToScore(score2[1])
        compared = 1
        while compared < 25:
            if highestCard1 > highestCard2:
                return 1
            if highestCard2 > highestCard1:
                return 2
            if highestCard1 == highestCard2:
                #somehow we need to find the next highest card
                highestCard1 = highCard(hand1, compared)
                highestCard2 = highCard(hand2, compared)
                compared += 1
        # They both had something, what is the highest card in the middle position
        #if comboCard1 > comboCard2:
        #    return 1
        #if comboCard2 > comboCard1:
        #    return 2



def main():
    #print(winningHand("5H 5C 6S 7S KD 2C 3S 8S 8D TD")) # player 2 should win (right side)
    #print(winningHand("5D 8C 9S JS AC 2C 5C 7D 8S QH")) # player 1
    #print(winningHand("2D 9C AS AH AC 3D 6D 7D TD QD")) # player 2
    # 5S 4D JS 3D 8H 6C TS 3S AD 8C
    #print(highCard("5S 4D JS 3D 8H", 3))
    #print(" ")
    #print(highCard("6C TS 3S AD 8C", 1))
    #print(winningHand("4D 6S 9H QH QC 3D 6D 7H QD QS")) # player 1
    #print(winningHand("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D")) # player 1
    

    player1Wins = 0
    handsCounted = 0
    with open("54/0054_poker.txt", newline='') as f:
        for handString in f:

            # for a given set of cards, try it one way and see if player 1 wins. 
            # If they do, flip the cards and see if player 2 wins. If they do, then player 1's win was valid
            handsCounted += 1
            handString = handString.split("\n")[0]
            winner = winningHand(handString)
            if winner == 1:
                #input(handString)
                reverseHand = handString[15:] + ' ' + handString[:14]
                #input(reverseHand)
                if winningHand(reverseHand) == 2:
                    player1Wins += 1 # we reversed the hand and then it still win (player 2) so the original player 1 win was valid
            print(f"for hand {handString}, player {winner} won")
    print(f"Player 1 won {player1Wins} hands out of {handsCounted} hands.")

if __name__=='__main__':
    main()