import re, autoBid, math

def getSeatingRelative(seating, spot):
    directions = ['north','east','south','west']
    return {
        "left": seating[directions[(directions.index(spot) + 1) % 4]],
        "top": seating[directions[(directions.index(spot) + 2) % 4]],
        "right": seating[directions[(directions.index(spot) + 3) % 4]],
        "bottom": seating[directions[(directions.index(spot) + 0) % 4]],
    }
   
def getEstimatedSuitCounts(biddingObjRelative, allBids, seatingRelative):
    '''
    inputs: 
        biddingObjRelative: dictionary where keys are relative positions and values are lists of strings representing that user's bids (in chronological order) 
        allBids: list of bids as a list 
        seatingRelative: dictionary where keys are relative positions and values are strings representing user's name
    returns: a dictionary representing the current "best guess" of how many of each suit a player has
    '''
    defaultValue = -1
    suitCounts = {
        "top": {
            "clubs": defaultValue,
            "diamonds": defaultValue,
            "hearts": defaultValue,
            "spades": defaultValue,
        },
        "bottom": {
            "clubs": defaultValue,
            "diamonds": defaultValue,
            "hearts": defaultValue,
            "spades": defaultValue,
        },
        "left": {
            "clubs": defaultValue,
            "diamonds": defaultValue,
            "hearts": defaultValue,
            "spades": defaultValue,
        },
        "right": {
            "clubs": defaultValue,
            "diamonds": defaultValue,
            "hearts": defaultValue,
            "spades": defaultValue,
        },
    }

    '''assumptions:
    if a player says the same suit twice they likely have 1-2 more of that suit that would be assumed otherwise (5-6 for minors and 6-7 for majors?)

    opening in no trump means no voids

    responding to opening points in the same suit means you have at least 3 of that suit?

    responding with a major means you have at least 5
    '''

    return suitCounts



def getIsPartnersFirstBidPass(biddingObjRelative):
    partnersBidding = biddingObjRelative["top"] 
    if len(partnersBidding) > 0:
        return partnersBidding[0] == 'pass'
    else:
        return False

def getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids):
    #returns whether someone has opened before the users first bid
    bidsUpToUsersFirstBid = allBids
    if indexOfUsersFirstBid != None:
        bidsUpToUsersFirstBid = allBids[:indexOfUsersFirstBid]

    for bid in bidsUpToUsersFirstBid:
        if not re.search('pass', bid[1], re.IGNORECASE) and not re.search('double', bid[1], re.IGNORECASE):
            return True
    return False

def getPartnersLocation(username, seatingRelative):
    '''
    returns location of the partner for username using seatingRelative
    '''
    locationToUse = None
    for location, usernameInDict in seatingRelative.items():
        if usernameInDict == username:
            locationToUse = location
            break;

    if locationToUse == None:
        return None

    locations = ['left','top','right','bottom']
    indexOfUsersLocation = locations.index(locationToUse)
    print('indexOfUsersLocation = {0}'.format(indexOfUsersLocation))
    return locations[(indexOfUsersLocation + 2) % 4]

def getIndexOfNthBid(username, allBids, nthBid):
    #inputs:
        #username - string
        #allBids - 2D array
        #nthBid - an integer greater than or equal to 1 (1 = first bid) or less than or equal to -1 (-1 = last bid, -2 = 2nd to last bid...)
    #this returns the nthBid that username made
    i = 0
    matchCount = 0

    if nthBid < 0:
        allBids = allBids[::-1]
        for bid in allBids:
            if bid[0] == username:
                matchCount += 1
                nthBidToMatch = len(allBids) - i -1
                if matchCount == -nthBid:
                    return nthBidToMatch
            i += 1 
    else:
        for bid in allBids:
            if bid[0] == username:
                matchCount += 1
                if matchCount == nthBid:
                    return i
            i += 1 
    
    return None

def getHasPlayerJumpshifted(username, playersBids, allBids):
    #inputs:
        #username as string
        #playersBids as a list of strings
        #allbids is a list of lists representing bids (bidder, bid)
    #returns true if the player with username has made a jumpshift bid ever otherwise false
    for i in range(0, len(playersBids)): 
        bid = playersBids[i]
        indexOfUsersBid = getIndexOfNthBid(username, allBids, i + 1)
        biddingUpToThisPoint = allBids[:indexOfUsersBid]
        contractBidAtThisPoint = getCurrentContractBid(biddingUpToThisPoint)
        isAnyBidJumpShift = getIsJumpshift(contractBidAtThisPoint, bid)

        print('bids = {0}'.format(playersBids))
        print('indexOfUsersBid = {0}'.format(indexOfUsersBid))
        print('biddingUpToThisPoint = {0}'.format(biddingUpToThisPoint))
        print('contractBidAtThisPoint = {0}'.format(contractBidAtThisPoint))

        i += 1
        if isAnyBidJumpShift is True:
            return True
    return False

def getIsJumpshift(currentContractBid, usersBid):
    #inputs:
        #currentActualBid and usersBid = string representing bid
    #returns True/False whether usersBid is a jumpshift of currentActualBid
    if not currentContractBid or currentContractBid == '' or re.search('pass', usersBid, re.IGNORECASE) or re.search('double', usersBid, re.IGNORECASE):
        return False
    
    if isinstance(currentContractBid, list) and len(currentContractBid) > 1:
        currentContractBid = currentContractBid[1]
    
    indexOfCurrentActualBid = autoBid.contracts.index(currentContractBid)
    indexOfUsersBid = autoBid.contracts.index(usersBid)

    return abs(indexOfCurrentActualBid - indexOfUsersBid) > 5    

def getHasPartnerOpened(allBids, username):
    #returns true or false depending on whether the player is responding to his/her partner (partner didn't say pass 1st time)
    indexOfUsersFirstBid = getIndexOfNthBid(username, allBids, 1)

    if indexOfUsersFirstBid is None:
        return None

    biddingUpToUsersFirstBid = allBids[:indexOfUsersFirstBid]
    if len(biddingUpToUsersFirstBid) <= 1:
        return False
        
    if len(biddingUpToUsersFirstBid) >=2 and not re.search('pass', biddingUpToUsersFirstBid[-2][1], re.IGNORECASE):
        return True

    return False

def getBiddingHistory(allBids):
    #returns a list of strings representing the order in which the bids occured (same as incoming bids but is a 1D array of just bids rather than bids and bidder names)
    biddingHistory = []
    for bid in allBids:
        biddingHistory.append(bid[1])

    return biddingHistory

def getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid):
    currentIndex = autoBid.contracts.index(currentActualBid[1])

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
            return autoBid.contracts[currentIndex + 1]

        wholeNumber = int(math.ceil(totalOpeningPoints / 3));
        return autoBid.contracts[currentIndex + wholeNumber]
    #endregion
    #region second response
    elif len(biddingObjRelative['top']) == 2:

        suit = getStrongestSuit(hand, biddingObjRelative)
        for i in range(1, 6):
            if re.search(suit, autoBid.contracts[currentIndex + i], re.IGNORECASE):
                return autoBid.contracts[currentIndex + i]

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

        return autoBid.contracts[currentIndex + indexAddition]
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

        return autoBid.contracts[currentIndex + indexAddition]
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

def getBiddingObjAbsolute(allBids, seating):
#     #input: all bids made
#     #return: a dictionary where the keys are cardinal directions (North South East West) and the values are arrays representing that persons bidding (['One Spade', 'Two Diamonds'])
    biddingObjAbsolute = {
        "north": [],
        "south": [],
        "east": [],
        "west": [],
    }
    for bid in allBids:
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

def getCurrentContractBid(allBids):
    #input: all bids up to now
    #return: the last bid made that is not double or pass
    print('allBids = {0}'.format(allBids))
    for bid in reversed(allBids):
        if len(bid) <= 0:
            return None
        if re.search('pass', bid[1], re.IGNORECASE) is None and re.search('double', bid[1], re.IGNORECASE) is None:
            return bid

def handlePartnerDouble(hand, allBids, biddingObjRelative, totalPoints):
    #responding to takeout dbl if applicable otherwise passing if less than 6 points total and is first bid
    if len(biddingObjRelative['top']) == 1 and re.search('Double', biddingObjRelative['top'][0], re.IGNORECASE): 
        mustBid = re.search('pass', allBids[-1][1], re.IGNORECASE)
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

def getDistributionPoints(hand, allBids, biddingObjRelative, seatingRelative, suitCounts):
    if hand == None:
        return -1    

    #otherwise use responding total
    distributionPoints = -1;
    hasPartnerOpened = getHasPartnerOpened(allBids, seatingRelative['bottom'])
    
    getShouldCalculateRespondingPoints(allBids)
    print('hasPartnerOpened = {0}'.format(hasPartnerOpened))

    if hasPartnerOpened:
        partnersMentionedSuits = getPartnersMentionedSuits(biddingObjRelative['top'])
        distributionPoints = getRespondingDistributionPoints(suitCounts, partnersMentionedSuits)
    else:
        distributionPoints = getOpeningDistributionPoints(suitCounts)

    return distributionPoints

def getPartnersMentionedSuits(partnersBids):
    #incoming list of bids 
    #return a list of suits that partner has bid

    pass

def getShouldCalculateRespondingPoints(allBids):
    #determine whether or not to calculate opening distribution or responding distribution

    #if partner bids 1 Clubs, 2 Clubs or 1NT return false

    #otherwise 
    pass

def getRespondingDistributionPoints(suitCounts, partnersMentionedSuits):

    return -1

def getOpeningDistributionPoints(suitCounts):
    #input: suitCounts as a dictionary where keys are suit names and values are ints representing how many of that suit
    #return: int representing total distribution points in all 4 suits
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
#endregion

def getLocationAfterRotationsAround(location, numberOfRotations):
    #inputs:
        #location = a string representing relative locations: ('right', 'left',...)
        #numberOfRotations = an int representing the number of clock-wise rotations
    #returns a string representing relative locations: ('right', 'left',...)
    #example location = 'right' and numberOfRotations = 1 => 'bottom'
    #example location = 'right' and numberOfRotations = -1 => 'top'
    locations = ['top', 'right', 'bottom', 'left']
    indexOfLocation = locations.index(location)
    return locations[(indexOfLocation + numberOfRotations) % 4]

def getCurrentContractBidFromBidding(bidding):
    #inputs:
        #bidding as list of all bids to consider
    #returns the currentContractBid on the bidding
    for bid in reversed(bidding):
        if not re.search('pass', bid[1], re.IGNORECASE) and not re.search('double', bid[1], re.IGNORECASE):
            return bid[1]

def getIsBidGameBid(bid):
    #input bid as a string
    #return true if bid is 3NT or greater than 4 Hearts, None if error otherwise false
    try:
        if re.match('three no trump', bid, re.IGNORECASE):
            return True
    
        indexOfBid = autoBid.contracts.index(bid)
        indexOfThreeHearts = autoBid.contracts.index('Four Heart')
        if indexOfBid >= indexOfThreeHearts:
            return True
    except:
        return None

    return False
