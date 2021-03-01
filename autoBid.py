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
PASS_FIRST_ROUND_MAX = 5
PASS_FIRST_ROUND_MIN = 0
PASS_FIRST_NT_SECOND_ROUND_MAX = 8
PASS_FIRST_NT_SECOND_ROUND_MIN = 12
PASS_FIRST_BID_SECOND_ROUND_MAX = 8
PASS_FIRST_BID_SECOND_ROUND_MIN = 12
PASS_FIRST_DOUBLE_SECOND_ROUND_MAX = 8
PASS_FIRST_DOUBLE_SECOND_ROUND_MIN = 12

BID_SUIT_FIRST_ROUND_MAX = 15
BID_SUIT_FIRST_ROUND_MIN = PASS_FIRST_ROUND_MAX + 1
TWO_CLUB_FIRST_ROUND_MAX = 25
TWO_CLUB_FIRST_ROUND_MIN = 18
NT_FIRST_ROUND_MIN = 16
NT_FIRST_ROUND_MAX = 18
DOUBLE_FIRST_ROUND_MIN = 13
DOUBLE_FIRST_ROUND_MAX = 18


suitCounts = None
highCardPointValuesInEachSuit = None
suits = {
    "clubs": 'club',
    "diamonds": 'diamond',
    "hearts": 'heart',
    "spades": 'spade',
    "noTrump": 'trump',
}
contracts = [
  "One Club",
  "One Diamond",
  "One Heart",
  "One Spade",
  "One No Trump",
  "Two Club",
  "Two Diamond",
  "Two Heart",
  "Two Spade",
  "Two No Trump",
  "Three Club",
  "Three Diamond",
  "Three Heart",
  "Three Spade",
  "Three No Trump",
  "Four Club",
  "Four Diamond",
  "Four Heart",
  "Four Spade",
  "Four No Trump",
  "Five Club",
  "Five Diamond",
  "Five Heart",
  "Five Spade",
  "Five No Trump",
  "Six Club",
  "Six Diamond",
  "Six Heart",
  "Six Spade",
  "Six No Trump",
  "Seven Club",
  "Seven Diamond",
  "Seven Heart",
  "Seven Spade",
  "Seven No Trump",
];

#Examples of inputs
clientPointCountingConvention = 'hcp'
spot = 'west'
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
# bids = [['Adam', 'Pass'], ['Dan', 'Two Club'], ['Ann', 'pass']]

hand = [[0, 1, 7, 8, 12], [13, 18, 19], [29, 30, 32], [40,42]]

      
import re, math
flatten = lambda t: [item for sublist in t for item in sublist]

def autoBid(incomingBids, hand, scoring, seating, spot, clientPointCountingConvention):
    global suitCounts
    global highCardPointValuesInEachSuit

    #region Initialization (Getting Values and Dicts to work with)
    isFirstBid = len(incomingBids) < 4
    partnerHasBid = len(incomingBids) >= 2
    currentActualBid = getCurrentActualBid(incomingBids)
    if suitCounts == None:
        suitCounts = getSuitCounts(hand)
    if highCardPointValuesInEachSuit == None:
        highCardPointValuesInEachSuit = getHighCardPointValuesInEachSuit(hand)
        
    biddingObjAbsolute = getBiddingObjAbsolute(incomingBids, seating)    
    biddingObjRelative = getBiddingObjRelative(biddingObjAbsolute, spot)
    biddingHistory = getBiddingHistory(incomingBids)
    estimatedPoints = getEstimatedPoints(biddingObjRelative, incomingBids)
    partnersBids = biddingObjRelative['top']
    #endregion

    partnersEstimatedPointCount = getPartnersEstimatedPointCount(partnersBids)

    #get straight up point counts
    highCardPoints = getHighCardPoints(hand, clientPointCountingConvention)
    distributionPoints = getDistributionPoints(hand, incomingBids, biddingObjRelative, suitCounts)
    totalPoints = highCardPoints + distributionPoints

    #region Check whether to double and return double if true
    canDouble = getCanDouble(biddingObjRelative)
    shouldDouble = getShouldDouble(scoring, biddingObjRelative, partnersEstimatedPointCount, hand, currentActualBid)
    if shouldDouble is True:
        return 'Double'
    #endregion    

    #handle partner 1 Club

    #handle partner 2 Club
    if (isFirstBid and re.search('two club', biddingObjRelative['top'][0], re.IGNORECASE) and re.search('pass', biddingObjRelative['left'][0], re.IGNORECASE)):
        openDistributionPoints = getOpeningDistributionPoints(suitCounts)
        return partnerTwoClubResponse(hand, biddingObjRelative, highCardPoints + openDistributionPoints, currentActualBid)
    

    #handle weak bid: -> pass/3NT/game in their suit/your best suit if lots of points or 6+ of a suit depending on your points, cards in their suit, if you have stoppers
    #if 1 NT -> best suit

    #TODO: do you pass if partner doubles and the person before you doubles?
    result = handlePartnerDouble(hand, incomingBids, biddingObjRelative, totalPoints) 
    if result is not None:
        return result

    #pass if less than 13 points and first bid
    if (totalPoints < 13 and isFirstBid):
        return 'Pass'

    #pass if less than 6 points and partner bid


#logic for opening (first bid)
#your partner passed or hasn't had a turn
#do you have at least opening points or weak bid? If not, pass
#if > opening points < 20 points -> 1 NT
#2 Clubs is accounted for above
#if opening points (calculate before looking for 6+ of a suit) and less than 15 points -> if other team has bid, double, if not bid best suit
#if > 7 points < opening points and > 6 of suit -> bid 3 of suit
#if > 9 points < opening points and 6 of suit -> bid 2 of suit


#logic for responding
#TODO: if your partner takes it to game, pass (partner trust?)
#your partner opened
#special situations accounted for above (takeout double, 1/2 Clubs, 1 NT and weak bids)
#if < 6 points pass
#if > 5 points and < 10* points (high card? total?) plus 3 of partner's suit
#   -> bid up 1 in partner's suit
#   if 2 of partner's suit and biddable suit
#   -> bid that suit, if no biddable suit, bid up 1 in partner's suit
#   if < 2 of partner's suit and no biddable suit -> pass
#if > 9 points and < 13 points (high card? total?) and biddable suit -> bid that suit, if no biddable suit bid NT
#if >12 points jump shift bid to best suit or NT


#logic for continuation of bidding (communication of second suits, determining game, competing with opponents)





#Scoring considerations:
#do you have at least 10 points and opposing team is vulnerable and has at least 50 points, bid as if you have opening
#if > opening points < 20 points -> 1 NT (unless have openers in major or minor and bid in that suit results in game)
#if > 7 points < opening points and > 6 of suit -> bid 3 of suit (unless point count and previous bidding = win, i.e. 3 passes and 70-80 partial depending on suit?)
#if >9 points < opening points and 6 of suit -> bid 2 of suit (unless clubs, unless point count and previous bidding = win, i.e. 3 passes and 70-80 partial depending on suit?)



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

def getEstimatedPoints(biddingObjRelative, biddingHistory):
    #return an obj that has the min and max estimated scores for each relative location ('top'/'bottom'/etc)
    estimatedScoring = {
        "top": {
            "min": None,
            "max": None,
        },
        "bottom": {
            "min": None,
            "max": None,
        },
        "left": {
            "min": None,
            "max": None,
        },
        "right": {
            "min": None,
            "max": None,
        },
    }

    #right now this doesn't differentiate between responding and opening bids

    for location, bids in biddingObjRelative.items():
        numberOfBidsMade = len(biddingObjRelative[location])
        if numberOfBidsMade < 1:
            continue

        isRespondingToPartner = getIsRespondingToPartner(biddingObjRelative, biddingHistory)
        firstBid = biddingObjRelative[location][0]

        if re.search('pass', firstBid, re.IGNORECASE):
            if len(biddingObjRelative[location]) > 1:
                secondBid = biddingObjRelative[location][1]
                if re.search('trump', secondBid, re.IGNORECASE):
                    estimatedScoring[location]['min'] = PASS_FIRST_NT_SECOND_ROUND_MIN
                    estimatedScoring[location]['max'] = PASS_FIRST_NT_SECOND_ROUND_MAX
                elif re.search('double', secondBid, re.IGNORECASE):
                    estimatedScoring[location]['min'] = PASS_FIRST_DOUBLE_SECOND_ROUND_MIN
                    estimatedScoring[location]['max'] = PASS_FIRST_DOUBLE_SECOND_ROUND_MAX
                elif re.search('pass', secondBid, re.IGNORECASE):
                    #this is needed to handle cases when # of bids is > 1 and 1st and 2nd bids are pass
                    estimatedScoring[location]['min'] = PASS_FIRST_ROUND_MIN
                    estimatedScoring[location]['max'] = PASS_FIRST_ROUND_MAX
                else:
                    estimatedScoring[location]['min'] = PASS_FIRST_BID_SECOND_ROUND_MIN
                    estimatedScoring[location]['max'] = PASS_FIRST_BID_SECOND_ROUND_MAX
            else:
                estimatedScoring[location]['min'] = PASS_FIRST_ROUND_MIN
                estimatedScoring[location]['max'] = PASS_FIRST_ROUND_MAX
        elif re.search('trump', firstBid, re.IGNORECASE):
            estimatedScoring[location]['min'] = NT_FIRST_ROUND_MIN
            estimatedScoring[location]['max'] = NT_FIRST_ROUND_MAX
        elif re.search('double', firstBid, re.IGNORECASE):
            estimatedScoring[location]['min'] = DOUBLE_FIRST_ROUND_MIN
            estimatedScoring[location]['max'] = DOUBLE_FIRST_ROUND_MAX
        elif re.search('Two Club', firstBid, re.IGNORECASE):
            estimatedScoring[location]['min'] = TWO_CLUB_FIRST_ROUND_MIN
            estimatedScoring[location]['max'] = TWO_CLUB_FIRST_ROUND_MAX
        else:
            estimatedScoring[location]['min'] = BID_SUIT_FIRST_ROUND_MIN
            estimatedScoring[location]['max'] = BID_SUIT_FIRST_ROUND_MAX

    print('estimatedScoring = {0}'.format(estimatedScoring))
    return estimatedScoring

def getIsRespondingToPartner(biddingObjRelative, biddingHistory):
    #returns true or false depending on whether th
    pass

def getBiddingHistory(incomingBids):
    #returns a list of strings representing the order in which the bids occured (same as incoming bids but is a 1D array of just bids rather than bids and bidder names)
    biddingHistory = []
    for bid in incomingBids:
        biddingHistory.append(bid[1])

    return biddingHistory

def partnerTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid):
    currentIndex = contracts.index(currentActualBid[1])

    #return early if left bids first
    if not re.search('pass', biddingObjRelative['left'][0], re.IGNORECASE) and not re.search('double', biddingObjRelative['left'][0], re.IGNORECASE):
        return 'Pass'

    #region first response
    bestSuitIsNoTrump = None 
    if len(biddingObjRelative['top']) > 2:
        bestSuitIsNoTrump = re.search('trump', biddingObjRelative['top'][1], re.IGNORECASE)
    print('bestSuitIsNoTrump = {0}'.format(bestSuitIsNoTrump))

    if re.search('two club', biddingObjRelative['top'][-1], re.IGNORECASE):
        if totalOpeningPoints == 0:
            return contracts[currentIndex + 1]

        wholeNumber = int(math.ceil(totalOpeningPoints / 3));
        return contracts[currentIndex + wholeNumber]
    #endregion
    #region second response
    elif len(biddingObjRelative['top']) == 2:

        suit = getStrongestSuit(hand, biddingObjRelative)
        for i in range(1, 6):
            if re.search(suit, contracts[currentIndex + i], re.IGNORECASE):
                return contracts[currentIndex + i]

    #endregion
    #region handle slam Aces
    elif not bestSuitIsNoTrump and re.search('trump', biddingObjRelative['top'][-1], re.IGNORECASE):
        aceCount = 0
        for suit in hand:
            for cardAsNumber in suit:
                if cardAsNumber % 13 == 12:
                    aceCount += 1

        isAllOrNone = aceCount == 0 or aceCount == 4
        indexAddition = 0
        if isAllOrNone:
            indexAddition = 1
        else:
            indexAddition = aceCount + 1

        return contracts[currentIndex + indexAddition]
    #endregion
    #region handle slam Kings
    #if their second bid's suit is the same as their 4th bid's suit then assume wants to stop otherwise assume asking for kings
    elif getSuitFromBid(biddingObjRelative['top'][1]) != getSuitFromBid(biddingObjRelative['top'][3]):
        kingCount = 0
        for suit in hand:
            for cardAsNumber in suit:
                if cardAsNumber % 13 == 11:
                    kingCount += 1

        print('kingCount = {0}'.format(kingCount))
        isAllOrNone = kingCount == 0 or kingCount == 4
        indexAddition = 0
        if isAllOrNone:
            indexAddition = 1
        else:
            indexAddition = kingCount + 1

        return contracts[currentIndex + indexAddition]
    #endregion
    #handle stopping prematurely?
    #if opponent enter crazy bid, how to handle?

    #handle second response

    return 'Pass'

def getSuitFromBid(bid):
    split = bid.split()
    if split and len(split) > 1:
        return bid.split()[1]
    
    return None

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

def getStrongestSuit(hand, biddingObjRelative, isResponding=False):
    #input: hand as 2D array 
    #return: 'club'/'diamond'/'heart'/'spade'/'no trump' depending on which one is the 'strongest' and which suits have already been mentioned

    suitsMentionedByOpponents = getSuitsMentionedByOpponents(biddingObjRelative)

    #global vars to use: 'suitCounts' and 'highCardPointValuesInEachSuit'

    #region if you are getting strongest suit for opening 
    if isResponding:       
        
        pass
    #endregion
    #region getting responding strongest
    else:
        pass

    pass

def getSuitsMentionedByOpponents(biddingObjRelative):
    #check already mentioned suits
    mentioned = {
        "clubs": False,
        "diamonds": False,
        "hearts": False,
        "spades": False,
        "noTrump": False,
    }

    handsToCheck = ['left', 'right']

    for handToCheck in handsToCheck:
        for bid in biddingObjRelative[handToCheck]:
            for key,suit in suits.items():
                if (re.search(suit, bid, re.IGNORECASE)):
                    mentioned[key] = True
               
    return mentioned

def getPartnersEstimatedPointCount(partnersBids):
    #input: partnersBids in chronological order (1st index is most first bid they made)
    #return: a list where the first index represents the lowest point count possible and the 2nd index the highest?
    pass

def getCanDouble(biddingObjRelative):
    #inputs: if opposing team bid
    # outputs: whether or not you can double
    # if opposing team hasn't bid, can't double   
    if len(biddingObjRelative['left']) == 0 and len(biddingObjRelative['right']) == 0:
        return False

    return True
    
def getShouldDouble(scoring, biddingObjRelative, partnersEstimatedPointCount, hand, currentActualBid):
    #inputs: 
    #   scoring - an obj/dictionary representing the scores
    #   biddingObjRelative - all prior bids

    #returns: true or false representing whether it is better to double than to bid higher

    #figure out a range of how many tricks partners could win based on estimated point count
    #evaluate if unsuccessful double results in game for opponents
    #how to evaluate a void/singleton in the contract suit?

    #estimate a range of how many tricks you could win (best case and worst case)

    #if your estimated trick count + partners is >= tricks needed to set return true else false
    
    #consider total score and current game's below the line score to determine whether doubling is better than bidding something else 
    return False

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

def getHighCardPointValuesInEachSuit(hand):
    global highCardPointValuesInEachSuit
    highCardPointValuesInEachSuit = {
        "clubs": 0,
        "diamonds": 0,
        "hearts": 0,
        "spades": 0,
    }

    for suit in hand:
        suitName = ''
        for cardAsNumber in suit:
            if len(suit) > 0:
                suitName = getSuitNameFromCardAsNumber(cardAsNumber)
            if cardAsNumber >=9 and cardAsNumber <=12:
                highCardPointValuesInEachSuit[suitName] += 1

    return highCardPointValuesInEachSuit

def getSuitCounts(hand):
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
    return suitCounts

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

def getDistributionPoints(hand, incomingBids, biddingObjRelative, suitCounts):
    try:
        if hand == None:
            return -1    

        #otherwise use responding total
        distributionPoints = -1;
        shouldCalculateRespondingPoints = getShouldCalculateRespondingPoints(incomingBids)


        if shouldCalculateRespondingPoints:
            partnersMentionedSuits = getPartnersMentionedSuits(biddingObjRelative['top'])
            distributionPoints = getRespondingDistributionPoints(suitCounts, partnersMentionedSuits)
        else:
            distributionPoints = getOpeningDistributionPoints(suitCounts)

        return distributionPoints

    except:
        print(-2)

def getPartnersMentionedSuits(partnersBids):
    #incoming list of bids 
    #return a list of suits that partner has bid

    pass

def getShouldCalculateRespondingPoints(incomingBids):
    #determine whether or not to calculate opening distribution or responding distribution

    #if partner bids 1 Clubs, 2 Clubs or 1NT return false

    #otherwise 
    pass

def getRespondingDistributionPoints(incomingBids):

    pass

def getOpeningDistributionPoints(suitCounts):
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
