#Purpose: make best bid taking into account cards in hand, previous bids, possibly score
'''
Inputs:
    incomingBids: 2D array
    hand: 2D array with four items (1st = clubs, 2nd = diamonds, 3rd = hearts, 4th = spades) containing integers from 0-51
        First index is name of bidder
        Second index is string representing the name of the bid i.e. 1 No Trump
        Is in chronological order
    scoring: a dictionary representing the current scoring
    seating: a dictionary with cardinal directions as keys and strings as keys
    spot: string representing seating position
    clientPointCountingConvention: string representing how client counts HCP points
Returns: "best" bid for current situation in the form of a string
'''

#Examples of inputs
clientPointCountingConvention = 'hcp'
spot = 'north'
seating = {
    "north": 'Adam',
    "east": 'Dan',
    "south": 'Ann',
    "west": "Andrew",
}
scoring = {
    "northSouth": {
        "aboveTheLine": 0,
        "belowTheLine": 0,
        "totalBelowTheLineScore": 0,
        "isVulnerable": False,
        "vulnerableTransitionIndex": None,
    },
    "eastWest": {
        "aboveTheLine": 0, 
        "belowTheLine": 0,
        "totalBelowTheLineScore": 0,
        "isVulnerable": False,
        "vulnerableTransitionIndex": None,
    },
}
bids = [['Adam', 'Two No Trump'], ['Dan', 'Double'], ['Ann', 'Double'], ['Andrew', '3 club']]
hand = [[0, 1, 5, 7, 8], [13, 18, 19], [29, 30, 32], [40, 42]]

from logging import exception
import re
from tests.test_main import Takeout_Double
flatten = lambda t: [item for sublist in t for item in sublist]

def autoBid(incomingBids, hand, scoring, seating, spot, clientPointCountingConvention):
    #region Initialization (Getting Values and Dicts to work with)
    isFirstBid = len(incomingBids) < 4
    partnerHasBid = len(incomingBids) >= 2
    currentActualBid = getCurrentActualBid(incomingBids)
    # theyBids = getTheyBids(incomingBids)

    biddingObjAbsolute = getBiddingObjAbsolute(incomingBids, seating)
    #biddingObjRelative is a dictionary where relative locations are keys and the values are that person's bids (top: [...], left: [...], ...)
    biddingObjRelative = getBiddingObjRelative(biddingObjAbsolute, spot)
    partnersBids = biddingObjRelative['top']
    #endregion



    partnersEstimatedPointCount = getPartnersEstimatedPointCount(partnersBids)
    print('partnersBids = {0}'.format(partnersBids))

    #region Check whether to double and return double if true
    canDouble = getCanDouble(incomingBids, partnersEstimatedPointCount)
    shouldDouble = getShouldDouble(canDouble, scoring)
    if shouldDouble is True:
        return 'Double'
    #endregion

    #get straight up point counts
    highCardPoints = getHighCardPoints(hand, clientPointCountingConvention)
    distributionPoints = getDistributionPoints(hand)
    totalPoints = highCardPoints + distributionPoints
    print('totalPoints = {0}'.format(totalPoints))

    #TODO: do you pass if partner doubles and the person before you doubles?
    result = handlePartnerDouble(hand, incomingBids, biddingObjRelative, totalPoints) 
    if result is not None:
        return result

    #pass if less than 6 points and first bid
    if (totalPoints < 6 and isFirstBid):
        return 'Pass'


    #TODO: have different behavior depending on whether set to reliable or agressive?


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

    outgoingBid = 'Recommended Bid Goes here'
    return outgoingBid

def getSpotAfterNRotations(spot, numberOfRotations):
    #input: 
    #   spot - string representing user's cardinal position
    #   numberOfRotations - how many time to go clockwise until the desired position 
    #return - string representing cardinal location n number of rotations from spot 
    if numberOfRotations < 0:
        raise TypeError('Invalid numberOfRotations')
    if numberOfRotations == 0:
        return spot

    spots = ['north', 'east', 'south', 'west']
    currentSpotIndex = spots.index(spot)
    return spots[(currentSpotIndex + numberOfRotations) % 4]

def getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor):
    #input -
    #   usersSpot = string representing cardinal direction
    #   spotToGetLocationFor = cardinal direction of spot to get
    #return: the location (left, right, top, or bottom) of spotToGetLocationFor in relation to the usersSpot
    spots = ['north', 'west', 'south', 'east']
    locations = ['bottom', 'left', 'top', 'right']
    usersSpotIndex = spots.index(usersSpot)
    spotToGetIndex = spots.index(spotToGetLocationFor)
    difference = usersSpotIndex - spotToGetIndex
    if difference < 0:
        difference += 4
    return locations[difference]

def getBiddingObjRelative(biddingObjAbsolute, spot):
    #input: 
    #   biddingObjAbsolute - dictionary of bids for each cardinal position
    #   spot - string representing user's cardinal position
    #return: dictionary with keys repsenting relative position to user (top, left, right, bottom (bottom being own bids))
    biddingObjRelative = {}
    for key, value in biddingObjAbsolute.items():
        biddingObjRelative[getRelativeLocationFromSpot(spot, key)] = value
    return biddingObjRelative

def getBiddingObjAbsolute(incomingBids, seating):
#     #input: all bids made
#     #return: a dictionary where the keys are cardinal directions (North South East West) and the values are arrays representing that persons bidding (['One Spade', 'Two Diamonds'])
    biddingObjAbsolute = {
        "north": [],
        "south": [],
        "east": [],
        "west": [],
    }
    for bid in incomingBids:
        direction = ''
        for key, value in seating.items():
            if bid[0] == value:
                direction = key
                break
        biddingObjAbsolute[direction].append(bid[1])
    return biddingObjAbsolute

def getStrongestSuit(hand, biddingObjRelative):
    #input: hand as 2D array 
    #return: 'clubs'/'diamonds'/'hearts'/'spades'/'no trump' depending on which one is the 'strongest' and which suits have already been mentioned

    #check already mentioned suits
    mentioned = {
        "clubs": False,
        "diamonds": False,
        "hearts": False,
        "spades": False,
        "nt": False,
    }

    for location, bids in biddingObjRelative.items():
        for bid in bids:
            if (re.search('club', bid[1], re.IGNORECASE)):
                mentioned.clubs = True
            elif (re.search('diamond', bid[1], re.IGNORECASE)):
                mentioned.diamond = True
            elif (re.search('heart', bid[1], re.IGNORECASE)):
                mentioned.heart = True
            elif (re.search('spade', bid[1], re.IGNORECASE)):
                mentioned.spade = True
            elif (re.search('trump', bid[1], re.IGNORECASE)):
                mentioned.nt = True

    #return strongest of unmentioned suits
    for suit, hasBeenMentioned in mentioned.items():
        if (hasBeenMentioned == False)
        fdfd
    pass

def getPartnersEstimatedPointCount(partnersBids):
    #input: partnersBids in chronological order (1st index is most first bid they made)
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


#TODO: is this needed?
def getTheyBids(incomingBids):
    #input: all bids
    #returns: the bids that are not made by you or partner
    theyBids = []
    for index, bid in enumerate(reversed(incomingBids)):
        if index % 2 == 0:
            theyBids.insert(0, bid)

    print('theyBids = {0}'.format(theyBids))
    return theyBids

def getCurrentActualBid(incomingBids):
    #input: all bids up to now
    #return: the last bid made that is not double or pass
    for bid in reversed(incomingBids):
        if re.search('pass', bid[1], re.IGNORECASE) is None and re.search('double', bid[1], re.IGNORECASE) is None:
            return bid

def handlePartnerDouble(hand, incomingBids, biddingObjRelative, totalPoints):
    #responding to takeout dbl if applicable otherwise passing if less than 6 points total and is first bid
    if len(biddingObjRelative['top']) == 1 and re.search('Double', biddingObjRelative['top'][0], re.IGNORECASE): 
        mustBid = re.search('pass', incomingBids[-1][1], re.IGNORECASE)
        if totalPoints < 6 and mustBid is None:
            return 'Pass'
        else:
            return getStrongestSuit(hand, biddingObjRelative)
    else:
        #TODO: have to figure out when to trust partner's actual double bid and when to make a bid (e.g. you have a really nice suit with 18+ points?) or just always pass if partner doubles and it's not a takeout double?
        return 'Pass'
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

print(autoBid(bids, hand, scoring, seating, spot, 'hcp'))
