from logging import error
import getEstimatedPoints, autoBid
import re, math

def getSeatingRelative(seating, spot):
    '''
        returns the seating in terms of relative locations (e.g. 'top', 'left', 'right', 'bottom')
    '''
    directions = ['north','east','south','west']
    return {
        "left": seating[directions[(directions.index(spot) + 1) % 4]],
        "top": seating[directions[(directions.index(spot) + 2) % 4]],
        "right": seating[directions[(directions.index(spot) + 3) % 4]],
        "bottom": seating[directions[(directions.index(spot) + 0) % 4]],
    }
   
def getIsPartnersFirstBidPass(biddingRelative):
    '''
        returns whether the players partner passed for their first bid opportunity
    '''
    partnersBidding = biddingRelative["top"] 
    if len(partnersBidding) > 0:
        return partnersBidding[0] == 'pass'
    else:
        return False

def getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute):
    '''
       returns whether a player other than the user who made the bid at indexOfUsersFirstBid made an 'opening bid'
    '''
    bidsUpToUsersFirstBid = biddingAbsolute
    if indexOfUsersFirstBid != None:
        bidsUpToUsersFirstBid = biddingAbsolute[:indexOfUsersFirstBid]

    for bid in bidsUpToUsersFirstBid:
        if not re.search('pass', bid[1], re.IGNORECASE) and not re.search('double', bid[1], re.IGNORECASE):
            return True

    return False

def getPartnersLocation(username, seatingRelative):
    '''
    returns location of username's partner (e.g. 'top', 'left', 'right', etc...)
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

def getIndexOfNthBid(username, biddingAbsolute, nthBid):
    '''
    inputs:
        username - string
        biddingAbsolute - 2D array
        nthBid - an integer greater than or equal to 1 (1 = first bid) or less than or equal to -1 (-1 = last bid, -2 = 2nd to last bid...)
    returns the index in biddingAbsolute of the nthBid that username made  
    '''
    i = 0
    matchCount = 0

    if nthBid < 0:
        biddingAbsolute = biddingAbsolute[::-1]
        for bid in biddingAbsolute:
            if bid[0] == username:
                matchCount += 1
                nthBidToMatch = len(biddingAbsolute) - i -1
                if matchCount == -nthBid:
                    return nthBidToMatch
            i += 1 
    else:
        for bid in biddingAbsolute:
            if bid[0] == username:
                matchCount += 1
                if matchCount == nthBid:
                    return i
            i += 1 
    
    return None

def getHasPlayerJumpshifted(username, playersBids, biddingAbsolute):
    '''
    inputs:
        username as string
        playersBids as a list of strings
        allbids is a list of lists representing bids (bidder, bid)
    returns true if the player with username has made a jumpshift bid ever otherwise false
    '''
    for i in range(0, len(playersBids)): 
        bid = playersBids[i]
        indexOfUsersBid = getIndexOfNthBid(username, biddingAbsolute, i + 1)
        biddingUpToThisPoint = biddingAbsolute[:indexOfUsersBid]
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
    '''
    inputs:
        currentContractBid and usersBid are strings representing a bid ('One No Trump')
    returns True if the usersBid's index is greater than the currentcontractBid's index by 5 or more (aka a 'jumpshift' of currentContractBid)
    '''
    if not currentContractBid or currentContractBid == '' or re.search('pass', usersBid, re.IGNORECASE) or re.search('double', usersBid, re.IGNORECASE):
        return False
    
    if isinstance(currentContractBid, list) and len(currentContractBid) > 1:
        currentContractBid = currentContractBid[1]
    
    indexOfCurrentActualBid = autoBid.contracts.index(currentContractBid)
    indexOfUsersBid = autoBid.contracts.index(usersBid)

    return abs(indexOfCurrentActualBid - indexOfUsersBid) > 5    

def getHasPartnerOpened(biddingAbsolute, username):
    '''
    returns true if username's partner has mentioned a bid that is a suit, no trump, or a double and false otherwise
    '''
    indexOfUsersFirstBid = getIndexOfNthBid(username, biddingAbsolute, 1)

    if indexOfUsersFirstBid is None:
        return None

    biddingUpToUsersFirstBid = biddingAbsolute[:indexOfUsersFirstBid]
    if len(biddingUpToUsersFirstBid) <= 1:
        return False
        
    if len(biddingUpToUsersFirstBid) >=2 and not re.search('pass', biddingUpToUsersFirstBid[-2][1], re.IGNORECASE):
        return True

    return False

def getBiddingHistory(biddingAbsolute):
    '''
    returns a list of strings representing the order in which the bids occured (same as incoming bids but is a 1D array of just bids rather than bids and bidder names)
    '''
    biddingHistory = []
    for bid in biddingAbsolute:
        biddingHistory.append(bid[1])

    return biddingHistory

def getTwoClubResponse(hand, biddingRelative, totalOpeningPoints, currentActualBid):
    '''
        returns the the bid to say based on the two club convention when your partner has opened two clubs
    '''
    currentIndex = autoBid.contracts.index(currentActualBid[1])

    #return early if left bids first
    if not re.search('pass', biddingRelative['left'][0], re.IGNORECASE) and not re.search('double', biddingRelative['left'][0], re.IGNORECASE):
        return 'Pass'

    #region first response
    bestSuitIsNoTrump = None 
    if len(biddingRelative['top']) > 2:
        bestSuitIsNoTrump = re.search('trump', biddingRelative['top'][1], re.IGNORECASE)
    print('bestSuitIsNoTrump = {0}'.format(bestSuitIsNoTrump))

    if re.search('two club', biddingRelative['top'][-1], re.IGNORECASE):
        if totalOpeningPoints == 0:
            return autoBid.contracts[currentIndex + 1]

        wholeNumber = int(math.ceil(totalOpeningPoints / 3));
        return autoBid.contracts[currentIndex + wholeNumber]
    #endregion
    #region second response
    elif len(biddingRelative['top']) == 2:

        suit = getStrongestSuit(hand, biddingRelative)
        for i in range(1, 6):
            if re.search(suit, autoBid.contracts[currentIndex + i], re.IGNORECASE):
                return autoBid.contracts[currentIndex + i]

    #endregion
    #region handle slam Aces
    elif not bestSuitIsNoTrump and re.search('trump', biddingRelative['top'][-1], re.IGNORECASE):
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
    elif getSuitFromBid(biddingRelative['top'][1]) != getSuitFromBid(biddingRelative['top'][3]):
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
    biddingRelative = {}
    for key, value in biddingObjAbsolute.items():
        biddingRelative[getRelativeLocationFromSpot(spot, key)] = value
    return biddingRelative

def getBiddingObjAbsolute(biddingAbsolute, seating):
#     #input: all bids made
#     #return: a dictionary where the keys are cardinal directions (North South East West) and the values are arrays representing that persons bidding (['One Spade', 'Two Diamonds'])
    biddingObjAbsolute = {
        "north": [],
        "south": [],
        "east": [],
        "west": [],
    }
    for bid in biddingAbsolute:
        direction = ''
        for key, value in seating.items():
            if bid[0] == value:
                direction = key
                break
        biddingObjAbsolute[direction].append(bid[1])
    return biddingObjAbsolute

def getStrongestSuit(hand, biddingRelative, isResponding=False):
    #input: hand as 2D array 
    #return: 'club'/'diamond'/'heart'/'spade'/'no trump' depending on which one is the 'strongest' and which suits have already been mentioned

    suitsMentionedByOpponents = getSuitsMentionedByOpponents(biddingRelative)

    #global vars to use: 'suitCounts' and 'highCardPointValuesInEachSuit'

    #region if you are getting strongest suit for opening 
    if isResponding:       
        
        pass
    #endregion
    #region getting responding strongest
    else:
        pass

    pass

def getSuitsMentionedByOpponents(biddingRelative):
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
        for bid in biddingRelative[handToCheck]:
            for key,suit in autoBid.suits.items():
                if (re.search(suit, bid, re.IGNORECASE)):
                    mentioned[key] = True
               
    return mentioned

def getPartnersEstimatedPointCount(partnersBids):
    #input: partnersBids in chronological order (1st index is most first bid they made)
    #return: a list where the first index represents the lowest point count possible and the 2nd index the highest?
    pass

def getCanDouble(biddingRelative):
    #inputs: if opposing team bid
    # outputs: whether or not you can double
    # if opposing team hasn't bid, can't double   
    if len(biddingRelative['left']) == 0 and len(biddingRelative['right']) == 0:
        return False

    return True
    
def getShouldDouble(scoring, biddingRelative, partnersEstimatedPointCount, hand, currentActualBid):
    #inputs: 
    #   scoring - an obj/dictionary representing the scores
    #   biddingRelative - all prior bids

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

def getCurrentContractBid(biddingAbsolute):
    #input: all bids up to now
    #return: the last bid made that is not double or pass
    print('biddingAbsolute = {0}'.format(biddingAbsolute))
    for bid in reversed(biddingAbsolute):
        if len(bid) <= 0:
            return None
        if re.search('pass', bid[1], re.IGNORECASE) is None and re.search('double', bid[1], re.IGNORECASE) is None:
            return bid

def handlePartnerDouble(hand, biddingAbsolute, biddingRelative, totalPoints):
    #responding to takeout dbl if applicable otherwise passing if less than 6 points total and is first bid
    if len(biddingRelative['top']) == 1 and re.search('Double', biddingRelative['top'][0], re.IGNORECASE): 
        mustBid = re.search('pass', biddingAbsolute[-1][1], re.IGNORECASE)
        if totalPoints < 6 and mustBid is None:
            return 'Pass'
        else:
            return getStrongestSuit(hand, biddingRelative)
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

def getDistributionPoints(hand, biddingAbsolute, biddingRelative, seatingRelative, suitCounts):
    if hand == None:
        return -1    

    #otherwise use responding total
    distributionPoints = -1;
    hasPartnerOpened = getHasPartnerOpened(biddingAbsolute, seatingRelative['bottom'])
    
    getShouldCalculateRespondingPoints(biddingAbsolute)
    print('hasPartnerOpened = {0}'.format(hasPartnerOpened))

    if hasPartnerOpened:
        partnersMentionedSuits = getPartnersMentionedSuits(biddingRelative['top'])
        distributionPoints = getRespondingDistributionPoints(suitCounts, partnersMentionedSuits)
    else:
        distributionPoints = getOpeningDistributionPoints(suitCounts)

    return distributionPoints

def getPartnersMentionedSuits(partnersBids):
    #incoming list of bids 
    #return a list of suits that partner has bid

    pass

def getShouldCalculateRespondingPoints(biddingAbsolute):
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
    #returns the currentContractBid on the bidding as a string
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

def getIndexDifferenceOfBids(bid1, bid2):
    #input: lowerBid as string and higherBid as string
    #output: an int representing how many bids higher the higher bid is 
    print('bid1 = {0}'.format(bid1))
    print('bid2 = {0}'.format(bid2))
    try:
        if re.search('pass', bid1, re.IGNORECASE) or re.search('double', bid1, re.IGNORECASE) or re.search('pass', bid2, re.IGNORECASE) or re.search('double', bid2, re.IGNORECASE):
            return 0
        bid1Index = autoBid.contracts.index(bid1)
        bid2Index = autoBid.contracts.index(bid2)
        return abs(bid2Index - bid1Index)
    except:
        raise TypeError('Error in getIndexDifferenceOfBids;  Probably incorrect parameter passed in.')

#region Test Case Helpers
def getBidArrayFromBiddingObjAndSeatingRelative(biddingRelative, seatingRelative):
    #note: this is written to facilitate test case writing for getEstimatedPoints
    #input biddingRelative and seatingRelative dictionaries
    #returns the bidding array e.g. [['LeftPlayer', "One Diamond"],['TopPlayer', 'Two Heart'],['RightPlayer', 'Two No Trump'], ...]
    try:
        locations = getEstimatedPoints.locations
        locationOrder = [locations['left'], locations['top'],locations['right'], locations['bottom']]

        dealer = getDealerFromBiddingObjRelative(biddingRelative)

        #get new order based on dealer
        locationOrderToUse = locationOrder
        if dealer != locations['left']:
            index = locationOrder.index(locations[dealer])
            locationOrderToUse = locationOrder[index:] + locationOrder[:index]

        #iterate through each location n times where n is the # of opportunities the dealer has had to bid and add bids in order they were made 
        bids = []

        # print('dealer = {0}'.format(dealer))    
        # print('locationOrderToUse = {0}'.format(locationOrderToUse))
        for i in range(0, len(biddingRelative[dealer])):
            
            for j in range(0, len(locationOrderToUse)):
                locationToGet = locationOrderToUse[j]
                # print('locationToGet = {0}'.format(locationToGet))

                try:
                    bidInQuestion = biddingRelative[locationToGet][i]   
                except:
                    break      

                if bidInQuestion is not None:
                    # print('bidInQuestion = {0}'.format(bidInQuestion))
                    # print('seatingRelative[locationToGet] = {0}'.format(seatingRelative[locationToGet]))
                    bids.append([seatingRelative[locationToGet], bidInQuestion])
                    # print('bids = {0}'.format(bids))
                else:
                    break
                
        if re.search('bottom', bids[-1][0], re.IGNORECASE):
            bids = bids[:-1]
        return bids

    except:
        print('error-----------')
        return []

def getDealerFromBiddingObjRelative(biddingRelative):
    try:
        currentMax = 0
        dealer = None
        locations = getEstimatedPoints.locations
        locationOrder = [locations['bottom'], locations['left'], locations['top'],locations['right']]
        for location in locationOrder:
            lengthOfLocationsBidding = len(biddingRelative[location])
            if lengthOfLocationsBidding > currentMax:

                currentMax = lengthOfLocationsBidding
                dealer = location

        return dealer
    except:
        return None
#endregion

def getHasSomeoneOpenedTwoClubs(biddingAbsolute, biddingRelative, seatingRelative):
    #input: biddingAbsolute made (is an array of arrays where first item is name of bidder and second is bid)
    #return: tuple where first item is boolean decribing whether someone has bid two clubs and the second item is the name of that person as a string
    
    #region check whether anyone bid two clubs as their first bid
    falseTuple = (False, None)
    shouldContinue = False;
    twoClubBid = None

    for location in biddingRelative: 
        if len(biddingRelative[location]) == 0:
            continue

        firstBid = biddingRelative[location][0]
        if re.search('two club', firstBid, re.IGNORECASE):
            twoClubBid = [seatingRelative[location], firstBid]
            shouldContinue = True;
            break;
    #endregion

    if shouldContinue is True:
        indexOfTwoClubBid = biddingAbsolute.index(twoClubBid)
        hasSomeoneOpenedBefore = getHasSomeOneOpenedBefore(indexOfTwoClubBid, biddingAbsolute)
        if hasSomeoneOpenedBefore is False:
            return (True, twoClubBid[0])
    return falseTuple

def getPlayerHasOnlyPassed(playerBids):
    for bid in playerBids:
        if not re.search('pass', bid, re.IGNORECASE):
            return False;

    return True
