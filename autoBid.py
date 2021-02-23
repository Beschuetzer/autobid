#Purpose: make best bid taking into account cards in hand, previous bids, possibly score
'''
Inputs:
    Hand: 2D array with four items (1st = clubs, 2nd = diamonds, 3rd = hearts, 4th = spades) containing integers from 0-51
    Incoming Bids: 2D array
        First index is name of bidder
        Second index is string representing the name of the bid i.e. 1 No Trump
        Is in chronological order
Returns: "best" bid for current situation in the form of a string
'''

import re

#Examples of inputs
scoring = {
    "northSouth": {
        "totalScore": 150,   #this is the total including 'below'
        "below": 0,
    },
    "eastWest": {
        "totalScore": 350,   #this is the total including 'below'
        "below": 40,
    },
}
bids = [['Adam', 'Two No Trump'], ['Tim', 'Double'], ['Ann', 'Double'], ['Andrew', '3 club']]
hand = [[0, 1, 5, 7, 8], [13, 18, 19], [29, 30, 32], [40, 42]]
flatten = lambda t: [item for sublist in t for item in sublist]

def autoBid(incomingBids, hand, scoring, clientPointCountingConvention):
    isFirstBid = len(incomingBids) < 4
    partnerHasBid = len(incomingBids) >= 2
    currentActualBid = getCurrentActualBid(incomingBids)
    # theyBids = getTheyBids(incomingBids)
    partnersBids = getPartnersBids(incomingBids)
    partnersEstimatedPointCount = getPartnersEstimatedPointCount(partnersBids)

    #Check whether to double and return double if true
    canDouble = getCanDouble(incomingBids, partnersEstimatedPointCount)
    shouldDouble = getShouldDouble(canDouble, scoring)
    if shouldDouble is True:
        return 'Double'

    #get straight up point counts
    highCardPoints = getHighCardPoints(hand, clientPointCountingConvention)
    distributionPoints = getDistributionPoints(hand)
    totalPoints = highCardPoints + distributionPoints
    print('totalPoints = {0}'.format(totalPoints))

    # result = handleTakeoutDouble(hand, incomingBids, partnersBids, theyBids, totalPoints) 
    # if result is not True:
    #     return result

    #pass if less than 6 points and first bid
    if (totalPoints < 6 and isFirstBid):
        return 'Pass'

    #don't pass when have close to openers and a partial and you are third or fourth bidder and all previous bids are passes?

    #get total hand point count based on partners bids and hand
    
    #get all possible bids based on suit counts and hand points

    #remove bids from possible bids that meet one of the following conditions:
        #they bid your preferred suit

    #must rank highly due to convention for certain bids:
        #partner doubles
            #first round and defense passes => you must bid your 'strongest' suit
            #not first round then pass

        #if partner bids 2 clubs then respond with point count in 3 point increments, then respond again with 'strongest' suit 
        #if partner 'asks for aces'
        #if partner bids 1NT opening round must respond with 'strongest' suit
        #if partner bids 'weak bid' then decide which bid is best pass, game in partner's suit or 3NT

    #analyze they's bids

    outgoingBid = None
    return outgoingBid

def getStrongestSuit(theysBids, hand):
    #input: hand as 2D array 
    #return: 'clubs'/'diamonds'/'hearts'/'spades'/'no trump' depending on which one is the 'strongest' and which suits have already been mentioned

    #check already mentioned suits

    #return strongest of unmentioned suits

    pass

def getPartnersEstimatedPointCount(partnersBids):
    #input: partnersBids in reverse chronological order (1st index is most recent)
    #return: a list where the first index represents the lowest point count possible and the 2nd index the highest?
    pass

def getCanDouble(incomingBids, partnersEstimatedPointCount):
    #inputs: all bids made and partner's estimated point count
    #return: true or false representing whether a double bid is feasible

    #figure out a range of how many tricks partners could win based on estimated point count

    #how to evaluate a void/singleton in the contract suit?

    #estimate a range of how many tricks you could win (best case and worst case)

    #if your estimated trick count + partners is >= tricks needed to set return true else false
    pass

def getShouldDouble(canDouble, scoring):
    #inputs: 
    #   canDouble - whether double is 'possible'
    #   scoring - an obj/dictionary representing the scores
    #returns: true or false representing whether it is better to double than to bid higher

    #return if you can't double
    if canDouble is False:
        return

    #consider total score and current game's below the line score to determine whether doubling is better than bidding something else 
    pass

def getSuitNameFromCardAsNumber(cardAsNumber):
    #input: integer 0 - 51
    #return a suit ('clubs', 'diamonds', 'hearts' or 'spades')
    if cardAsNumber >= 0 and cardAsNumber <= 12:
        return 'clubs'
    elif cardAsNumber >= 13 and cardAsNumber <= 25:
        return 'diamonds'
    elif cardAsNumber >= 26 and cardAsNumber <= 38:
        return 'hearts'
    elif cardAsNumber >= 39 and cardAsNumber <= 51:
        return 'spades'
    else: 
        return None

def getTheyBids(incomingBids):
    #input: all bids
    #returns: the bids that are not made by you or partner
    theyBids = []
    for index, bid in enumerate(reversed(incomingBids)):
        if index % 2 == 0:
            theyBids.insert(0, bid)


    print('theyBids = {0}'.format(theyBids))
    return theyBids

def getPartnersBids(incomingBids):
    #input: all the bids made
    #return an array of bid names representing the bids your partner has made up to now.  the first index is the most recent bid and the last index is the first bid
    bids = []
    i = 1
    for bid in reversed(incomingBids):
        if i % 2 == 0 and i % 4 != 0:
            bids.append(bid[1])
        i+=1
    return bids

def getCurrentActualBid(incomingBids):
    #input: all bids up to now
    #return: the last bid made that is not double or pass
    for bid in reversed(incomingBids):
        if re.search('pass', bid[1], re.IGNORECASE) is None and re.search('double', bid[1], re.IGNORECASE) is None:
            return bid

def handleTakeoutDouble(hand, incomingBids, partnersBids, theyBids, totalPoints):
    #responding to takeout dbl if applicable otherwise passing if less than 6 points total and is first bid
    if len(partnersBids) == 1 and re.search('Double', partnersBids[0], re.IGNORECASE): 
        mustBid = re.search('pass', incomingBids[-1][1], re.IGNORECASE)
        if totalPoints < 6 and mustBid is None:
            return 'Pass'
        else:
            return getStrongestSuit(hand, theyBids)
    else:
        return True
#region Hand Counting Stuff
#region Initialization (Hard Coding Stuff)
highCardPointValues = {
    "hcp": {
        "ace": 4,
        "king": 3,
        "queen": 2,
        "jack": 1,
    },
    "alternative": {
        "ace": 4.5,
        "king": 3,
        "queen": 1.5,
        "jack": 0.75,
        "ten": 0.25,
    },
}
suitLengthRequiredToCount = {
    "king": 2,
    "queen": 3,
    "jack": 4,
    "ten": 5,
}
distributionPointValues = {
    "shortness": {
        "void": 3,
        "singleton": 2,
        "doubleton": 1,
    },
    "length": {
        "fiveCardSuit": 1,
        "sixCardsSuit": 2,
        "sevenCardsSuit": 3,  
    },
}
#endregion

def getHighCardPoints(hand, clientPointCountingConvention): 
    #input:
        #hand as 2d list (not flat)
        #clientPointCountingConvention as a string (either 'Alternative' or 'HCP')
    try:
        if hand == None or clientPointCountingConvention == None:
            return -1

        pointCountsToUse = highCardPointValues["hcp"]
        if clientPointCountingConvention.lower() == "alternative":
            pointCountsToUse = highCardPointValues["alternative"]

        points = 0
        for i in range(len(hand)):
            suit = hand[i]
            for j in range(len(suit)):
                cardValue = suit[j] % 13
                if cardValue == 8 and clientPointCountingConvention.lower() == 'alternative' and len(suit) >= suitLengthRequiredToCount['ten']:
                    points += pointCountsToUse['ten']
                if cardValue == 9 and len(suit) >= suitLengthRequiredToCount['jack']:
                    points += pointCountsToUse['jack']
                if cardValue == 10 and len(suit) >= suitLengthRequiredToCount['queen']:
                    points += pointCountsToUse['queen']
                if cardValue == 11 and len(suit) >= suitLengthRequiredToCount['king']:
                    points += pointCountsToUse['king']
                if cardValue == 12:
                    points += pointCountsToUse['ace']
            
        return points   
    except:
        return -2

def getDistributionPoints(hand):
    try:
        if hand == None:
            return -1

        suitCounts = {
            "clubs": 0,
            "diamonds":  0,
            "hearts":  0,
            "spades": 0,
        }

        for suit in hand:
            if len(suit) == 0:
                continue
            suitName = getSuitNameFromCardAsNumber(suit[0])
            suitCounts[suitName] = len(suit)

        return tallyUpTotal(suitCounts)
    except:
        print(-2)

def tallyUpTotal(suitCounts):
    #input: suitCounts as a dictionary where keys are suit names and values are ints representing how many of that suit
    #return: int representing total distribution points in all 4 suits
    try:
        points = 0
        for suit in suitCounts:
            if suitCounts[suit] == 0:
                points += distributionPointValues['shortness']['void']
            elif suitCounts[suit] == 1:
                points += distributionPointValues['shortness']['singleton']
            elif suitCounts[suit] == 2:
                points += distributionPointValues['shortness']['doubleton']
            elif suitCounts[suit] > 4:
                points += suitCounts[suit] - 4

        return points
    except:
        return -2       
#endregion

print(autoBid(bids, hand, scoring, 'hcp'))

# clubLength = 4
# diamondLength = 4
# heartLength = 3
# spadeLength = 3


# clubs = [i for i in range(0, clubLength)]
# diamonds = [i for i in range(13, 13 + diamondLength)]
# hearts = [i for i in range(26, 26 + heartLength)]
# spades = [i for i in range(39, 39 + spadeLength)]

# hand = [clubs, diamonds, hearts, spades]
# print(hand)
# print(getDistributionPoints(hand))