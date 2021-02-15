#Purpose: make best bid taking into account cards in hand, previous bids, possibly score
'''
Inputs:
    Hand: 2D array with four items (1st = clubs, 2nd = diamonds, 3rd = hearts, 4th = spades) containing integers from 0-51
    Incoming Bids: 2D array
        First index is name of bidder
        Second index is string representing the name of the bid i.e. 1 No Trump
Returns: "best" bid for current situation in the form of the original input (2D array or string)
'''
bids = [['Adam', 'Two No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass']]
hand = [0, 1, 5, 7, 11, 13, 18, 19, 29, 30, 32, 40, 51]
flatten = lambda t: [item for sublist in t for item in sublist]

def autoBid(incomingBids, hand, score):
    print(1)
    print(flatten([[1,2,3],[4,5,6]]))
    #get partners bids
    partnersBids = getPartnersBids(incomingBids)

    #add a function to check whether should double

    #don't pass when have close to openers and a partial and you are third or fourth bidder and all previous bids are passes

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



    # for cardAsNumber in hand:
    #     suit = getSuitFromCardAsNumber(somethingElse)
    #     print(sui


    outgoingBid = None
    return outgoingBid




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

def getPartnersBids(incomingBids):
    #input: all the bids made
    #return an array of bid names representing the bids your partner has made up to now.  the first index is the most recent bid and the last index is the first bid
    bids = []
    i = 1
    for bid in reversed(incomingBids):
        if i % 2 == 0 and i % 4 != 0:
            # print(bid)
            bids.append(bid[1])
        i+=1
    print(bids)
    return bids


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
            # print(len(suit))
            for j in range(len(suit)):
                # print(points)
                # print(pointCountsToUse)
                # print(suitLengthRequiredToCount)
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
            
        print(points)
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
        print(suitCounts)
        print(distributionPointValues)
        for suit in suitCounts:
            print(points)
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



# print(autoBid(bids, 2, 0))
clubLength = 4
diamondLength = 4
heartLength = 3
spadeLength = 3


clubs = [i for i in range(0, clubLength)]
diamonds = [i for i in range(13, 13 + diamondLength)]
hearts = [i for i in range(26, 26 + heartLength)]
spades = [i for i in range(39, 39 + spadeLength)]

hand = [clubs, diamonds, hearts, spades]
print(hand)
print(getDistributionPoints(hand))