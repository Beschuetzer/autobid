
import getEstimatedPoints, autoBid
import re, math

unlikelyLengths = {
    "ten": 28,
    "eleven": 32,
    "twelve": 36,
    "thirteen": 40,
}
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

def getIsTeamsFirstBidOpportunity(biddingRelative, location):
    '''
    inputs:
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }
        location = a string representing relative location to analyzing player (e.g. 'top', 'left', etc... )
    returns: 
        True if the biddingRelative[location]'s partner has not had an opportunity to bid, otherwise False
    '''
    partnersLocation = ''
    
    if location == getEstimatedPoints.locations['top']:
        partnersLocation = getEstimatedPoints.locations['bottom'] 
    elif location == getEstimatedPoints.locations['bottom']:
        partnersLocation = getEstimatedPoints.locations['top']
    elif location == getEstimatedPoints.locations['right']:
        partnersLocation = getEstimatedPoints.locations['left']
    elif location == getEstimatedPoints.locations['left']:
        partnersLocation = getEstimatedPoints.locations['right']
    else:
        raise ValueError('location must be top bottom left of right')

    partnersBids = biddingRelative[partnersLocation]

    #this is for the test case 'test_left'
    if location == getEstimatedPoints.locations['left'] and len(partnersBids) == 1:
        return True

    return len(biddingRelative[partnersLocation]) == 0

def getSeatingRelative(seating, spot):
    '''
        returns ------------------------------ the seating in terms of relative locations (e.g. 'top', 'left', 'right', 'bottom')
    '''
    directions = ['north','east','south','west']
    return {
        "left": seating[directions[(directions.index(spot) + 1) % 4]],
        "top": seating[directions[(directions.index(spot) + 2) % 4]],
        "right": seating[directions[(directions.index(spot) + 3) % 4]],
        "bottom": seating[directions[(directions.index(spot) + 0) % 4]],
    }
   
def getIsPartnersFirstBidPass(biddingRelative, seatingRelative, username):
    '''
        returns ------------------------------ whether the players partner passed for their first bid opportunity
    '''
    partnersLocation = getPartnersLocation(username, seatingRelative)

    partnersBidding = biddingRelative[partnersLocation] 
    if len(partnersBidding) > 0:
        if re.search('pass', partnersBidding[0], re.IGNORECASE): return True
    return False

def getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute):
    '''
       returns ------------------------------ whether a player other than the user who made the bid at indexOfUsersFirstBid made an 'opening bid'
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
    returns ------------------------------ location of username's partner (e.g. 'top', 'left', 'right', etc...)
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
    # print('indexOfUsersLocation = {0}'.format(indexOfUsersLocation))
    return locations[(indexOfUsersLocation + 2) % 4]

def getIndexOfNthBid(username, biddingAbsolute, nthBid):
    '''
    inputs: ------------------------------
        username - string
        biddingAbsolute - 2D array
        nthBid - an integer greater than or equal to 1 (1 = first bid) or less than or equal to -1 (-1 = last bid, -2 = 2nd to last bid...)
    returns ------------------------------ the index in biddingAbsolute of the nthBid that username made  
    '''
    i = 0
    matchCount = 0

  
    if nthBid < 0:
        nthBidCounter = 0
        for i in range(-1, -(len(biddingAbsolute) + 1), -1):
            adjustedI = len(biddingAbsolute) + i
            bid = biddingAbsolute[adjustedI]
            if bid[0] == username: 
                nthBidCounter += 1
                if nthBidCounter == -nthBid: 
                    return adjustedI
        
        if len(biddingAbsolute) == 0: return 0
        else: return len(biddingAbsolute) - 1
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
    inputs: ------------------------------
        username as string
        playersBids as a list of strings
        allbids is a list of lists representing bids (bidder, bid)
    returns ------------------------------ true if the player with username has made a jumpshift bid ever otherwise false
    '''
    for i in range(0, len(playersBids)): 
        bid = playersBids[i]
        indexOfUsersBid = getIndexOfNthBid(username, biddingAbsolute, i + 1)
        biddingUpToThisPoint = biddingAbsolute[:indexOfUsersBid]
        contractBidAtThisPoint = getCurrentContractBid(biddingUpToThisPoint)
        isAnyBidJumpShift = getIsJumpshift(contractBidAtThisPoint[1], bid)

        # print('bids = {0}'.format(playersBids))
        # print('indexOfUsersBid = {0}'.format(indexOfUsersBid))
        # print('biddingUpToThisPoint = {0}'.format(biddingUpToThisPoint))
        # print('contractBidAtThisPoint = {0}'.format(contractBidAtThisPoint))

        i += 1
        if isAnyBidJumpShift is True:
            return True
    return False

def getIsJumpshift(currentContractBid, usersBid):
    '''
    inputs: ------------------------------
        currentContractBid and usersBid are strings representing a bid ('One No Trump')
    returns ------------------------------ True if the usersBid's index is greater than the currentcontractBid's index by 5 or more (aka a 'jumpshift' of currentContractBid)
    '''
    # print(f"currentContractBid = {currentContractBid}")
    # print(f"usersBid = {usersBid}")
    print(f"currentContractBid = {currentContractBid}")
    print(f"usersBid = {usersBid}")
    if not currentContractBid or currentContractBid == '' or re.search('pass', usersBid, re.IGNORECASE) or re.search('double', usersBid, re.IGNORECASE) or re.search('pass', currentContractBid, re.IGNORECASE) or re.search('double', currentContractBid, re.IGNORECASE):
        return False
    
    if isinstance(currentContractBid, list) and len(currentContractBid) > 1:
        currentContractBid = currentContractBid[1]
    
    indexOfCurrentActualBid = autoBid.contracts.index(currentContractBid)
    indexOfUsersBid = autoBid.contracts.index(usersBid)

    print(f"indexOfCurrentActualBid = {indexOfCurrentActualBid}")
    print(f"indexOfUsersBid = {indexOfUsersBid}")
    print(f"abs(indexOfCurrentActualBid - indexOfUsersBid) = {abs(indexOfCurrentActualBid - indexOfUsersBid)}")
    
    if (indexOfCurrentActualBid > indexOfUsersBid): return False
    return abs(indexOfCurrentActualBid - indexOfUsersBid) > 5    

def getIndexOfPlayersNthBid(username, biddingAbsolute, nthBid):
    '''
    inputs:
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
        username = string of the user whose partner is to be checked
        nthBid = either positive integer starting from 1 (first bid) or negative integer starting at -1 (last bid)
    returns ------------------------------ 
        an integer representing the index of username's nth bid 
    '''
    print(f"nthBid = {nthBid}")
    if nthBid > 0:
        baseValue = -1
        for i in range(len(biddingAbsolute)):
            bid = biddingAbsolute[i]
            if bid[0] == username: 
                baseValue = i
                break
        
        indexToReturn = baseValue + (4 * (nthBid - 1))
        print(f"baseValue = {baseValue}")
        print(f"indexToReturn = {indexToReturn}")
        if indexToReturn >= 0 and indexToReturn <= len(biddingAbsolute): return indexToReturn
    elif nthBid < 0:
        baseValue = -1
        startvalue = len(biddingAbsolute) -1
        while startvalue >= 0:
            print(f"startvalue = {startvalue}")
            bid = biddingAbsolute[startvalue]
            if bid[0] == username: 
                baseValue = startvalue
                break
            startvalue -= 1
        
        indexToReturn = baseValue + (4 * (nthBid + 1))
        print(f"baseValue = {baseValue}")
        print(f"indexToReturn = {indexToReturn}")
        if indexToReturn >= 0 and indexToReturn <= len(biddingAbsolute): return indexToReturn

    else: raise ValueError('Invalid nthBid.')

def getWasForcedToBid(username, biddingAbsolute, seatingRelative):
    '''
    inputs:
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
        username = string of the user whose partner is to be checked
    returns ------------------------------ 
        true if username's partner bid double as their first bid and the bid after that was pass otherwise false
    '''

    try:
        if len(biddingAbsolute) < 1: return False
        print(f"biddingAbsolute = {biddingAbsolute}")
        partnersUsername = getUsernamesPartner(username, seatingRelative) 
        indexOfPartnersFirstBid = getIndexOfNthBid(partnersUsername, biddingAbsolute, 1)
        partnersFirstBid = biddingAbsolute[indexOfPartnersFirstBid]
        
        indexOfPlayersBid = getIndexOfPlayersNthBid(username, biddingAbsolute, 1)
        if indexOfPlayersBid < indexOfPartnersFirstBid and len(biddingAbsolute) <= 4: return False

        bidAfterPartnersFirstBid = biddingAbsolute[indexOfPartnersFirstBid + 1]

        print(f"username = {username}")
        print(f"seatingRelative = {seatingRelative}")
        print(f"partnersUsername = {partnersUsername}")
        print(f"indexOfPartnersFirstBid = {indexOfPartnersFirstBid}")
        print(f"biddingAbsolute = {biddingAbsolute}")
        print(f"partnersFirstBid = {partnersFirstBid}")
        print(f"bidAfterPartnersFirstBid = {bidAfterPartnersFirstBid}")

        caseDouble = re.search('double', partnersFirstBid[1], re.IGNORECASE) and re.search('pass', bidAfterPartnersFirstBid[1], re.IGNORECASE)
        caseNoTrump = re.search('trump', partnersFirstBid[1], re.IGNORECASE) and re.search('pass', bidAfterPartnersFirstBid[1], re.IGNORECASE)
        if caseDouble or caseNoTrump: return True
        return False
    except:
        return 'Error in getWasForcedToBid'

def getUsernamesPartner(username, seatingRelative):
    '''
    inputs:
        username = string of a player
        seatingRelative = { "top": "TopPlayerName", "bottom": "BottomPlayerName", ... }
    returns:
        the name of username's partner as a string
    '''
    try:
        locations = ['top', 'right', 'bottom', 'left']
        locationToUse = None
        for location, usernameInSeating in seatingRelative.items():
            if usernameInSeating == username: 
                locationToUse = location
                break

        indexToUse = (locations.index(locationToUse) + 2) % 4
        return seatingRelative[locations[indexToUse]]
    except:
        return "Error in getUsernamesPartner"

def getHasPartnerOpened(biddingAbsolute, seatingRelative, username):
    '''
    inputs:
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
        seatingRelative = { "top": "TopPlayerName", "bottom": "BottomPlayerName", ... }
        username = string of the user whose partner is to be checked
    returns ------------------------------ 
        true if username's partner bid something other than pass before username did unless that bid was a double that wansn't their first bid

    '''
    #figure out who bid first.  if partner bid first all the bottom applied otherwise different
    try:
        usernamesPartner = getUsernamesPartner(username, seatingRelative)
        usernameWhoHadFirstOpportunityToBid = getUsernameOfPlayerWhoHadFirstOpportunityToBid(biddingAbsolute, usernamesPartner, username)
        partnerBidFirst = usernamesPartner == usernameWhoHadFirstOpportunityToBid


        userNamesFirstBidIndex = getIndexOfNthBid(username, biddingAbsolute, 1)
        usernamesFirstBid = biddingAbsolute[userNamesFirstBidIndex]

        bidsUserHasMade = 0
        bidsPartnerHasMade = 0
        for bid in biddingAbsolute:
            if bid[0] == username: bidsUserHasMade += 1
            if bid[0] == usernamesPartner: bidsPartnerHasMade += 1

        if bidsPartnerHasMade == 0: return False
        if not partnerBidFirst and re.search('pass', usernamesFirstBid[1], re.IGNORECASE) and bidsUserHasMade == 1:
            # if re.search('pass', partnerBidFirst[1], re.IGNORECASE): 
                return False
        else:
            indexOfUsersLastBid = getIndexOfNthBid(username, biddingAbsolute, -1)
            if indexOfUsersLastBid is None:
                return None

            indexOfUsersFirstNonPassBid = -1
            i = 0
            for bid in biddingAbsolute:
                if bid[0] == username:

                    if not re.search('pass', bid[1], re.IGNORECASE):
                        if re.search('double', bid[1], re.IGNORECASE) and i != 0: continue
                        indexOfUsersFirstNonPassBid = i
                        break
                i+=1

            # print(f"indexOfUsersFirstNonPassBid = {indexOfUsersFirstNonPassBid}")

            partnersNthBid = 0
            if indexOfUsersFirstNonPassBid == -1:
                for bid in biddingAbsolute:
                    if bid[0] == usernamesPartner:
                        partnersNthBid += 1
                        if not re.search('pass', bid[1], re.IGNORECASE):
                            if partnersNthBid > 1 and re.search('double', bid[1], re.IGNORECASE): continue

                            return True
                return False

            else:
                biddingUpToUsersFirstNonPassBid = biddingAbsolute[:indexOfUsersFirstNonPassBid]

                for bid in biddingUpToUsersFirstNonPassBid:
                    if bid[0] == usernamesPartner:
                        if not re.search('pass', bid[1], re.IGNORECASE):
                            return True
                return False
    except:
        return False

def getUsernameOfPlayerWhoHadFirstOpportunityToBid(biddingAbsolute, usernamesPartner, username):
    '''
    inputs:
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
        usernamesPartner = string 
        username = string
    returns: 
        returns username if username had teams first opportunity, otherwise usernamesPartner
    '''
    for bid in biddingAbsolute:
        if bid[0] == usernamesPartner: return usernamesPartner
        elif bid[0] == username: return username

    return None

def getBiddingHistory(biddingAbsolute):
    '''
    returns ------------------------------ a list of strings representing the order in which the bids occured (same as incoming bids but is a 1D array of just bids rather than bids and bidder names)
    '''
    biddingHistory = []
    for bid in biddingAbsolute:
        biddingHistory.append(bid[1])

    return biddingHistory

def getTwoClubResponse(hand, biddingRelative, seatingRelative, totalOpeningPoints, currentActualBid, clientPointCountingConvention):
    '''
        returns ------------------------------ the the bid to say based on the two club convention when your partner has opened two clubs
    '''
    currentActualBidIndex = autoBid.contracts.index(currentActualBid[1])

    #region return early if left bids first
    if not re.search('pass', biddingRelative['left'][0], re.IGNORECASE) and not re.search('double', biddingRelative['left'][0], re.IGNORECASE):
        return 'Pass'

    #region special case of taking partner out of game bid
    longestSuit = None
    longestLength = 0
    for suit in hand:
        if len(suit) > longestLength: 
            longestSuit = getSuitNameFromCardAsNumber(suit[0])
            longestLength = len(suit)

    if totalOpeningPoints >= 13 and longestLength >= 7:
        #TODO: need to finish implementing getHasTakenPartnerOutOfGameBid
        hasTakenPartnerOutOfGameBid = getHasTakenPartnerOutOfGameBid(seatingRelative['bottom'], biddingRelative, seatingRelative)
        if hasTakenPartnerOutOfGameBid: return 'Pass'
        return getNextBidInSuit(longestSuit, currentActualBid[1])
    #endregion
    #region first response
    bestSuitIsNoTrump = None 
    if len(biddingRelative['top']) > 2:
        bestSuitIsNoTrump = re.search('trump', biddingRelative['top'][1], re.IGNORECASE)
    # print('bestSuitIsNoTrump = {0}'.format(bestSuitIsNoTrump))

    if re.search('two club', biddingRelative['top'][-1], re.IGNORECASE):
        if totalOpeningPoints == 0:
            return autoBid.contracts[currentActualBidIndex + 1]

        wholeNumber = int(math.ceil(totalOpeningPoints / 3));
        return autoBid.contracts[currentActualBidIndex + wholeNumber]
    #endregion
    #region second response
    elif len(biddingRelative['top']) == 2:

        suit = getStrongestSuit(hand, biddingRelative, clientPointCountingConvention)
        for i in range(1, 6):
            if re.search(suit, autoBid.contracts[currentActualBidIndex + i], re.IGNORECASE):
                return autoBid.contracts[currentActualBidIndex + i]

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

        return autoBid.contracts[currentActualBidIndex + indexAddition]
    #endregion
    #region handle slam Kings
    #if their second bid's suit is the same as their 4th bid's suit then assume wants to stop otherwise assume asking for kings
    elif getSuitFromBid(biddingRelative['top'][1]) != getSuitFromBid(biddingRelative['top'][3]):
        kingCount = 0
        for suit in hand:
            for cardAsNumber in suit:
                if cardAsNumber % 13 == 11:
                    kingCount += 1

        isAllOrNone = kingCount == 0 or kingCount == 4
        indexAddition = 0
        if isAllOrNone:
            indexAddition = 1
        else:
            indexAddition = kingCount + 1

        return autoBid.contracts[currentActualBidIndex + indexAddition]
    #endregion
    #handle stopping prematurely?
    #if opponent enter crazy bid, how to handle?

    #handle second response
    return 'Pass'

def getNextBidInSuit(suit, currentActualBid):
    '''
    inputs: 
        suit - string representing suit (e.g. 'clubs', 'diamonds', 'hearts', 'spades', or 'no trump')
    returns:
        nextBid - string representing the next available bid in suit (e.g. 'Two Heart', 'Three Club', etc... )
    '''
    try:
        suitsOrder = ['club', 'diamond', 'heart', 'spade', 'no trump']

        #region Normalizing Suit
        if suit[-1] == 's': suit = suit[:-1]
        suit = suit.lower()
        #endregion

        #region Normalizing the currentActualBidSuit
        currentActualBidSuit = currentActualBid.split(' ')
        if len(currentActualBidSuit) == 3:
            currentActualBidSuit = (f"{currentActualBidSuit[-2]} {currentActualBidSuit[-1]}").lower()
        else:
            currentActualBidSuit = currentActualBidSuit[-1].lower()
        #endregion
        
        currentActualBidSuitsOrderIndex = suitsOrder.index(currentActualBidSuit)
        targetSuitOrdersIndex = suitsOrder.index(suit)

        #region Getting indexToUse
        indexToUse = None
        currentActualBidIndex = autoBid.contracts.index(currentActualBid)
        if targetSuitOrdersIndex <= currentActualBidSuitsOrderIndex: 
            indexToUse = currentActualBidIndex + 5 - (currentActualBidSuitsOrderIndex - targetSuitOrdersIndex)
        else:
            indexToUse = currentActualBidIndex + targetSuitOrdersIndex - currentActualBidSuitsOrderIndex 
        #endregion

        # print(f"suit = {suit}")
        # print(f"currentActualBid = {currentActualBid}")
        # print(f"currentActualBidIndex = {currentActualBidIndex}")
        # print(f"currentActualBidSuitsOrderIndex = {currentActualBidSuitsOrderIndex}")
        # print(f"targetSuitOrdersIndex = {targetSuitOrdersIndex}")

        return autoBid.contracts[indexToUse]

    except Exception as err:
        raise Exception(f"Error in getNextBidInSuit = {err}")

def getSuitFromBid(bid):
    '''
        returns ------------------------------ the suit of bid (e.g. 'Heart', 'Spade', 'No Trump' etc)
    '''
    split = bid.split()
    if split and len(split) > 1:
        return bid.split()[1]
    
    return None

def getSpotAfterNRotations(spot, numberOfRotations):
    '''
    inputs: ------------------------------ 
       spot - string representing user's cardinal position
       numberOfRotations - how many time to go clockwise until the desired position 
    returns ------------------------------:
        string representing cardinal location n number of rotations from spot (e.g. 'north', 'south', etc...) 
    '''
    if numberOfRotations < 0:
        raise TypeError('Invalid numberOfRotations')
    if numberOfRotations == 0:
        return spot

    spots = ['north', 'east', 'south', 'west']
    currentSpotIndex = spots.index(spot)
    return spots[(currentSpotIndex + numberOfRotations) % 4]

def getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor):
    '''
    inputs
       usersSpot = string representing cardinal direction ('north', 'south', etc...)
       spotToGetLocationFor = cardinal direction of spot to get ('north', 'south', etc...)
    returns ------------------------------: 
        a location ('left','right', 'top', or 'bottom') representing the relative seating location of spotToGetLocationFor in relation to the usersSpot
    '''
    spots = ['north', 'west', 'south', 'east']
    locations = ['bottom', 'left', 'top', 'right']
    usersSpotIndex = spots.index(usersSpot)
    spotToGetIndex = spots.index(spotToGetLocationFor)
    difference = usersSpotIndex - spotToGetIndex
    if difference < 0:
        difference += 4
    return locations[difference]

def getBiddingObjRelative(biddingObjAbsolute, spot):
    '''
    inputs: ------------------------------ 
        biddingObjAbsolute = dictionary of bids for each cardinal position
        spot = string representing user's cardinal position
    returns ------------------------------:
        dictionary with keys representing relative locations to the analyzing player and values representing a list of bids the player in that location has made thus far (e.g. "top": ['One Club', 'pass', ...], "left": ['pass', 'Two Heart', ...], ...)
    '''
    biddingRelative = {}
    for key, value in biddingObjAbsolute.items():
        biddingRelative[getRelativeLocationFromSpot(spot, key)] = value
    return biddingRelative

def getBiddingObjAbsolute(biddingAbsolute, seating):
    '''
    input: 
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
    returns ------------------------------: 
        a dictionary where the keys are cardinal directions ('north', 'south', 'east', or 'west') and the values are arrays representing that persons bidding ("north": ['One Spade', 'Two Diamonds', ...], "east": ['pass', 'One No Trumo', ...], ... )
    '''
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

def getBiddableSuits(hand):
    '''
    input: 
        hand = 2D array where the first index represents clubs, the second diamonds, the third hearts, and the fourth spades 
        (e.g. [ [11,10,8], [24,22,20,17,15], [], [51,50,49,48,47]
    returns:
        a list of suits that are "biddable" (e.g. ["clubs", "spades"])
    '''
    biddableSuits = []
    suitNames = ["clubs","diamonds","hearts","spades"]

    biddableSuitLengths = {
        "clubs": 4,
        "diamonds": 4,
        "hearts": 5,
        "spades": 5,
    }

    suitCounts = getSuitCountsFromHand(hand)
    for suitName in suitNames:
        if suitCounts[suitName] >= biddableSuitLengths[suitName]: biddableSuits.append(suitName)

    return biddableSuits

def getWeightedSuitScore(hand, clientPointCountingConvention):
    '''
    input: 
        hand = 2D array where the first index represents clubs, the second diamonds, the third hearts, and the fourth spades 
        (e.g. [ [11,10,8], [24,22,20,17,15], [], [51,50,49,48,47]
    returns:
        a dictionary representing the weighted score for each suit 
        (e.g. {"clubs": 10, "diamonds": 12, ... })
    '''
    #NOTE: Idea: each additional card (valueOfAdditionalLength) in a suit above three shall be counted as 2 points (this number is arbitrary and may need some adjusting between 2 - 4).  

    #NOTE: Another idea: having 4 = 2 extra, 5 = 5 extra, 6 = 9, 7 = 14 ... (each additional is worth x more points)

    valueOfAdditionalLength = 2
    weightedSuitScores = {
        "clubs": 0,
        "diamonds": 0,
        "hearts": 0,
        "spades": 0,
    }
    pointsInEachSuit = getHighCardPointValuesInEachSuit(hand, clientPointCountingConvention)
    suitCounts = getSuitCountsFromHand(hand)

    for suit, suitCount in suitCounts.items():
        if suitCount < 3: 
            weightedSuitScores[suit] = pointsInEachSuit[suit]
        else:
            weightedSuitScores[suit] = pointsInEachSuit[suit] + ((suitCount - 3) * valueOfAdditionalLength)
    print('')

    return weightedSuitScores

def getShouldReturnNoTrump(weightedSuitScores, biddableSuits):
    '''
    input: 
        weightedSuitScores =  a dictionary representing the weighted score for each suit 
        (e.g. {"clubs": 10, "diamonds": 12, ... })
    returns ------------------------------:
        return tuple of strings representing suits with highest 'point counts'
    '''
    #NEVER BID NO TRUMP UNLESS no biddable suits and the two highest suits are within differenceThreshold points, bid return no trump
    differenceThreshold = 2

    if len(biddableSuits) == 0:
        highestSuit = None
        highestSuitValue = 0
        secondHighestSuitValue = 0

        for suit, weightedValue in weightedSuitScores.items():
            if weightedValue > highestSuitValue: 
                highestSuitValue = weightedValue
                highestSuit = suit

        for suit, weightedValue in weightedSuitScores.items():
            if weightedValue > secondHighestSuitValue and suit != highestSuit: 
                secondHighestSuitValue = weightedValue
        
        if (abs(highestSuitValue - secondHighestSuitValue) <= differenceThreshold): return True
       
    return False

def getStrongestSuit(hand, biddingRelative, clientPointCountingConvention):
    
    #NOTE: This function is only called in takeout double and two club best suit response (no need to consider partner's suit as they likely want to know your 'best' suit regardless of theirs)
    '''
    input: 
        hand = 2D array where the first index represents clubs, the second diamonds, the third hearts, and the fourth spades 
        (e.g. [ [11,10, 8], [24,22,20,17,15], [], [51,50,49,48,47])
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }
    returns ------------------------------:
        'club', 'diamond', 'heart', 'spade', or 'no trump' depending on which suit is the 'strongest' (considers which suits have already been mentioned, the number of points in that suit the analyzing player has, and how long the suit it for the analyzing player
    '''

    #region Andrew's Approach
    #compare evaluated points for each suit and rank
    # suitsYouCanMention = getSuitYouCanMention(hand)

    #add suits you can mention to a list

    #if no suits you 'can' mention in list then add longest suit and any others of that length

        #if you have a singleton:
            #if more than one suit of same length when no suits you can mention, return suit with highest point count.

            #if point counts and suit lengths tie when 'no suits you can mention' scenario return highest contract index suit (spades > hearts > ...)

        #else:
            #return next no trump bid
          
    
    #compare suits against each other and form a ranking

    #return highest suit that opponents haven't mentioned
    #endregion
    thresholdToMakeANonBiddableSuitBiddable = 3
    possibleOutputs = {
        "clubs": "club", 
        "diamonds": "diamond", 
        "hearts": "heart",
        "spades": "spade", 
        "noTrump": "no trump",     
    }

    #create a variable called biddableSuits
    biddableSuits = getBiddableSuits(hand) 

    #getting weightedSuitScore for each suit
    weightedSuitScores = getWeightedSuitScore(hand, clientPointCountingConvention)

    shouldReturnNoTrump = getShouldReturnNoTrump(weightedSuitScores, biddableSuits)
    print(f"shouldReturnNoTrump = {shouldReturnNoTrump}")
    if shouldReturnNoTrump: return possibleOutputs['noTrump']
    else:
        #NOTE: we can add all suits to biddableSuits because only cases where no biddable suits present and one suit is larger than no trump response threshold hit this line
        if len(biddableSuits) == 0: biddableSuits = ['clubs', 'diamonds', 'hearts', 'spades']

        #get suits mentioned by opponents
        suitsMentionedByOpponents = getSuitsMentionedByOpponents(biddingRelative)

        print(f"biddableSuits = {biddableSuits}")
        print(f"weightedSuitScores = {weightedSuitScores}")
        print(f"suitsMentionedByOpponents = {suitsMentionedByOpponents}")

        while weightedSuitScores.items():
            strongestSuit = max(weightedSuitScores, key=weightedSuitScores.get)
            strongestSuitValue = weightedSuitScores[strongestSuit]
            del weightedSuitScores[strongestSuit]

            secondStrongestSuit = max(weightedSuitScores, 
            key=weightedSuitScores.get)
            secondStrongestSuitValue = weightedSuitScores[secondStrongestSuit]
            del weightedSuitScores[secondStrongestSuit]

            #if values for 1st and 2nd best suit are equal swap strongest and secondStrongest if necessary
            if strongestSuitValue == secondStrongestSuitValue:
                print('equal---------------------')
                #first check length of suits (grab longer if dif.)
                strongestSuitLength = getLengthOfSuitFromHand(hand, strongestSuit)
                secondStrongestSuitLength = getLengthOfSuitFromHand(hand, secondStrongestSuit)

                if strongestSuitLength == secondStrongestSuitLength:
                    #if same length grab one higher up (spade > heart > diamond > club)
                    print('grabbing higher up')
                    suits = ['clubs', 'diamonds', 'hearts', 'spades']
                    indexForStrongestSuit = suits.find(strongestSuit)
                    indexForSecondStrongestSuit = suits.find(secondStrongestSuit)

                    largerSuitIndex = indexForStrongestSuit
                    lowerSuitIndex = indexForSecondStrongestSuit
                    higherSuit = strongestSuit
                    lowerSuit = secondStrongestSuit

                    if lowerSuitIndex > largerSuitIndex:
                        lowerSuit = strongestSuit
                        higherSuit = secondStrongestSuit

                    strongestSuit = higherSuit
                    secondStrongestSuit = lowerSuit

                else:
                    print('grabbing longer suit')

                    longerSuit = strongestSuit
                    shorterSuit = secondStrongestSuit

                    if secondStrongestSuitLength > strongestSuitLength: 
                        longerSuit = secondStrongestSuit
                        shorterSuit = strongestSuit

                    strongestSuit = longerSuit
                    secondStrongestSuit = shorterSuit
                    
            #adding strongestSuit to biddableSuits if it is thresholdToMakeANonBiddableSuitBiddable points or larger than secondStrongestSuit
            if abs(strongestSuitValue - secondStrongestSuitValue) > thresholdToMakeANonBiddableSuitBiddable: biddableSuits.append(strongestSuit) 

            if strongestSuit in biddableSuits and suitsMentionedByOpponents[strongestSuit] is False:  return possibleOutputs[strongestSuit]

            if secondStrongestSuit in biddableSuits and suitsMentionedByOpponents[secondStrongestSuit] is False:  return possibleOutputs[secondStrongestSuit]
               
        return None
    
def getLengthOfSuitFromHand(hand, suitName):
    '''
    input: 
        hand = 2D array where the first index represents clubs, the second diamonds, the third hearts, and the fourth spades 
        (e.g. [ [11,10, 8], [24,22,20,17,15], [], [51,50,49,48,47])
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }
        suitName = string (e.g. 'clubs', 'diamonds', 'hearts', or 'spades')
    returns ------------------------------:
        an integer representing the length of suitName in hand
    '''
    validSuitNames = ['clubs', 'diamonds', 'hearts', 'spades']
    if suitName.lower() not in validSuitNames: raise Exception("Invalid SuitName.  Must be 'clubs', 'diamonds', 'hearts', or 'spades'")

    suitCounts = getSuitCountsFromHand(hand)
    
    for suit in validSuitNames:
        if re.search(suit, suitName, re.IGNORECASE): return suitCounts[suit]

def getSuitsMentionedByOpponents(biddingRelative):
    '''
        input:
            biddingRelative = { "top": ['pass', 'one heart', ...], ... }
        returns ------------------------------: 
            a dictionary obj representing whether that suit has been said by opponents or not (e.g. { "clubs": True, "diamonds": False, "noTrump": True, ... })
    '''


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

def getCanDouble(biddingRelative):
    '''
    inputs: ------------------------------ 
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }
    returns ------------------------------:
        True is analyzing player can double and false otherwise   
    '''
    if len(biddingRelative['left']) == 0 and len(biddingRelative['right']) == 0:
        return False

    return True
    
#NOTE: this function will likely need a whole separate file due to its complexity
def getShouldDouble(scoring, biddingRelative, estimatedPoints, hand, currentActualBid):
    '''
    inputs: ------------------------------ 
    
    scoring = an obj/dictionary representing the scores 
    (e.g. 
        {"northSouth: 
            {
                "aboveTheLine": 120, 
                "belowTheLine": 80,
                "totalBelowTheLineScore": 160,
                "isVulnerable": False,
                "vulnerableTransitionIndex": null,
            }, 
        "eastWest": {...} 
        }
    )

    biddingRelative = { "top": ['pass', 'One Heart', ...], ... }
    
    estimatedPoints = { "top": {"min": 6, "max": 12}, ... }
    
    hand = 2D array where the first index represents clubs, the second diamonds, the third hearts, and the fourth spades (e.g. [ [11,10, 8], [24,22,20,17,15], [], [51,50,49,48,47])

    currentActualBid = string representing the bid that would be played (e.g. "One Heart")

    returns ------------------------------: 
        True if analyzing player 'should' double otherwise False
    '''

    #figure out a range of how many tricks partners could win based on estimated point count
    #evaluate if unsuccessful double results in game for opponents
    #how to evaluate a void/singleton in the contract suit?

    #estimate a range of how many tricks you could win (best case and worst case)

    #if your estimated trick count + partners is >= tricks needed to set return true else false
    
    #consider total score and current game's below the line score to determine whether doubling is better than bidding something else 
    return False

def getSuitNameFromCardAsNumber(cardAsNumber):
    '''
    input: 
        cardAsNumber = integer 0 - 51
    returns:
        a suit ('clubs', 'diamonds', 'hearts' or 'spades')
    '''
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
    '''
    input: 
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
    return:
        the last bid made that is not double or pass
    '''

    for bid in reversed(biddingAbsolute):
        if len(bid) <= 0:
            return None
        if re.search('pass', bid[1], re.IGNORECASE) is None and re.search('double', bid[1], re.IGNORECASE) is None:
            return bid

    return None

def handlePartnerDouble(hand, biddingAbsolute, biddingRelative, totalPoints, clientPointCountingConvention):
    '''
        responding to takeout dbl if applicable otherwise passing if less than 6 points total and is first bid
    '''
    if len(biddingRelative['top']) == 1 and re.search('Double', biddingRelative['top'][0], re.IGNORECASE): 
        mustBid = re.search('pass', biddingAbsolute[-1][1], re.IGNORECASE)
        if totalPoints < 6 and mustBid is None:
            return 'Pass'
        else:
            return getStrongestSuit(hand, biddingRelative, clientPointCountingConvention)
    else:
        #TODO: have to figure out when to trust partner's actual double bid and when to make a bid (e.g. you have a really nice suit with 18+ points?) or just always pass if partner doubles and it's not a takeout double?
        return 'Pass'

def getHighCardPointValuesInEachSuit(hand, clientPointCountingConvention):
    '''
    inputs:
        hand = 2D array where the items are arrays representing suits      clientPointCountingConvention = string representing method used to evaluate HCPs (either 'HCP' or 'Alternative)
    returns: the high card point value of hand (e.g. { clubs: "8", 'diamonds': 3, "hearts": 0, spades: "4" })
    '''
    conventionToUse = 'hcp'
    if re.search('alternative', clientPointCountingConvention, re.IGNORECASE):
        conventionToUse = 'alternative'

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
                cardValue = cardAsNumber % 13

                if cardValue == 12:
                    highCardPointValuesInEachSuit[suitName] += highCardPointValues[conventionToUse]['ace']
                if cardValue == 11:
                    highCardPointValuesInEachSuit[suitName] += highCardPointValues[conventionToUse]['king']
                if cardValue == 10:
                    highCardPointValuesInEachSuit[suitName] += highCardPointValues[conventionToUse]['queen']
                if cardValue == 9:
                    highCardPointValuesInEachSuit[suitName] += highCardPointValues[conventionToUse]['jack']
                if cardValue == 8 and conventionToUse == 'alternative':
                    highCardPointValuesInEachSuit[suitName] += highCardPointValues[conventionToUse]['ten']

    return highCardPointValuesInEachSuit

def getSuitCountsFromHand(hand):
    '''
        returns the suit counts for hand (e.g. { "clubs": 3, "diamonds": 4, etc... })
    '''
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
    '''
    input:
        hand = 2D array where the first index represents clubs, the second diamonds, the third hearts, and the fourth spades 
        (e.g. [ [11,10, 8], [24,22,20,17,15], [], [51,50,49,48,47])
    returns ------------------------------:
        clientPointCountingConvention as a string (either 'Alternative' or 'HCP')
    '''
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
    '''
    inputs: ------------------------------------------------- 
        hand = 2D array where the first index represents clubs, the second diamonds, the third hearts, and the fourth spades 
        
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
            
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }

        seatingRelative = { "top": "TopPlayerName", "bottom": "BottomPlayerName", ... }

        suitCounts = { "clubs": 3, "diamonds": 4, etc... }
    
    returns: -------------------------------------------------
        the estimated distribution points for hand
    '''
    if hand == None:
        return -1    

    #otherwise use responding total
    distributionPoints = -1;
    hasPartnerOpened = getHasPartnerOpened(biddingAbsolute, seatingRelative, seatingRelative['bottom'])
    
    getShouldCalculateRespondingPoints(biddingAbsolute)

    distributionPoints = getRespondingDistributionPoints(suitCounts)
    currentActualBid = getCurrentContractBid(biddingAbsolute)
    if currentActualBid is None:
        distributionPoints = getOpeningDistributionPoints(suitCounts)

    return distributionPoints

def getPartnersMentionedSuits(partnersBids):
    '''
    inputs: 
        partnersBids = ['pass', 'One Club', ... ]
    returns:
        a list of suits that the analyzing partner has bid (e.g. ['clubs', 'diamonds', 'hearts', 'spades', 'noTrump'])
    '''
    pass

def getShouldCalculateRespondingPoints(biddingAbsolute):
    '''
    inputs: 
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
    returns: 
        True if analyzing player 'should' calculate responding distribution points and False if responding distribution points
    '''

    #if partner bids 1 Clubs, 2 Clubs or 1NT return false

    #otherwise 
    pass
getDistributionPoints
def getRespondingDistributionPoints(suitCounts):
    #NOTE: needs to return the dist point in each suit if that suit is the contract
    '''
    inputs-----------------------------------------------:
        suitCounts = { "clubs": 3, "diamonds": 4, etc... }
        
        partnersMentionedSuits = array of suits that the analyzing partner has bid (e.g. ['clubs', 'diamonds', 'hearts', 'spades', 'noTrump'])
    returns:-----------------------------------------------
        the estimated responding distribution points of the analyzing player
    '''
    result = {
        "clubs": 0,
        "diamonds": 0,
        "hearts": 0,
        "spades": 0,
    }
    requiredLengthToCountMultiple = 4
    print('')
    print(f"suitCounts = {suitCounts}")

    #note: if suit length is 0 return 0 for suit
    for suit, suitCount in suitCounts.items():

        if suitCount == 13: 
            result[suit] = 40
            continue
        if suitCount == 12: 
            result[suit] = 36
            continue
        if suitCount == 11: 
            result[suit] = 32
            continue
        if suitCount == 10: 
            result[suit] = 28
            continue

        if suitCount == 0: 
            result[suit] = 0
            continue
        baselineShortnessPoints = getBaselineShortnessPoints(suitCounts, suit)

        print(f"suit = {suit}")
        #get multiple if applicable (check based on above dict)
        if suitCount >= requiredLengthToCountMultiple:
            surplusCount = suitCount - 3
            multiplier = 0
            for suit2, suitCount2 in suitCounts.items():
                if suit == suit2: continue
                if suitCount2 == 0: 
                    multiplier = 3
                    break

            if multiplier == 0:
                for suit2, suitCount2 in suitCounts.items():
                    if suit == suit2: continue
                    if suitCount2 == 1: 
                        multiplier = 2
                        break

            if multiplier == 0:
                for suit2, suitCount2 in suitCounts.items():
                    if suit == suit2: continue
                    if suitCount2 == 2: 
                        multiplier = 1
                        break
            
            print('surplus')
            print(f"multiplier = {multiplier}")
            print(f"surplusCount = {surplusCount}")
            result[suit] = baselineShortnessPoints + (multiplier * surplusCount)
        else:
            print('baseline')
            result[suit] = baselineShortnessPoints
    print('')
    return result

def getNumberOfQuickTricks(hand):
    '''
    input:
        hand = [ [12,11,10], [...], [...], [51,50,49,...] ]
        suit = string representing the suit to check for quick trick in
    returns: 
        an integer representing the number of quick tricks in every suit other than the suit given
    '''

    quickTrickTotals = {
        "aceKing": 2,
        "aceQueen": 1.5,
        "aceOnly": 1,
        "kingQueen": 1,
        "kingCovered": .5,
    }

    totalQuickTricks = 0
    for i in range(len(hand)):
        suit = hand[i]
        hasAce = False
        hasKing = False
        hasQueen = False
        isCovered = len(suit) > 1
        print('')

        for j in range(len(suit)):
            cardAsNumber = suit[j]
            cardValue = cardAsNumber % 13
            print(f"cardValue = {cardValue}")
            if cardValue == 12: hasAce = True
            if cardValue == 11: hasKing = True
            if cardValue == 10: hasQueen = True

        if hasAce and hasKing: totalQuickTricks += quickTrickTotals["aceKing"]
        elif hasAce and hasQueen: totalQuickTricks += quickTrickTotals["aceQueen"]
        elif hasAce: totalQuickTricks += quickTrickTotals["aceOnly"]
        elif hasKing and hasQueen: totalQuickTricks += quickTrickTotals["kingQueen"]
        elif hasKing and isCovered: totalQuickTricks += quickTrickTotals["kingCovered"]

    return totalQuickTricks



def getOpeningDistributionPoints(suitCounts):
    #NOTE: needs to return the dist point in each suit if no contract given (only count Lenght points so length - 4 is point count for each suit)
    '''
    input:
        suitCounts = { "clubs": 3, "diamonds": 4, etc... }
    returns: 
        an integer representing total opening distribution that the analyzing player has
    '''

    #note: if length of suit is 10 or greater just return a fixed amount (to ensure that the bidding doesn't stay low)
    distributionPoints = {
        "clubs": 0,
        "diamonds": 0,
        "hearts": 0,
        "spades": 0,
    }

    requiredLengthsToCount = {
        "clubs": 4,
        "diamonds": 4,
        "hearts": 5,
        "spades": 5,
    }
    
    for suit, suitCount in suitCounts.items():
        if suitCount >= 10:
            if suitCount == 10: distributionPoints[suit] = unlikelyLengths['ten']
            if suitCount == 11: distributionPoints[suit] = unlikelyLengths['eleven']
            if suitCount == 12: distributionPoints[suit] = unlikelyLengths['twelve']
            if suitCount == 13: distributionPoints[suit] = unlikelyLengths['thirteen']
        else:
            #average case logic

            if suitCount == 0: distributionPoints[suit] = 0

            #need to have function that returns baseline void, singleton, and doubleton points (inputs are)
            if suitCount < requiredLengthsToCount[suit]: distributionPoints[suit] = 0
            else:
                baselineShortnessPoints = getBaselineShortnessPoints(suitCounts, suit)
                
                #get length points
                if suitCount > 4:
                    distributionPoints[suit] = baselineShortnessPoints + (suitCount - 4)
                else: distributionPoints[suit] = baselineShortnessPoints

    return distributionPoints    

def getBaselineShortnessPoints(suitCounts, suitToSkip):
    '''
    input:
        suitCounts = { "clubs": 3, "diamonds": 4, etc... }
        suit = string representing suit to not count shortness points for
    returns: 
        a dictionary representing how many shortness points you would have if in the suit suitToSkip given suitCounts
    '''

    points = 0
    for suit, suitCount in suitCounts.items():
        if re.search(suitToSkip, suit, re.IGNORECASE): continue

        if suitCount == 0:
            points += distributionPointValues['shortness']['void']
        elif suitCount == 1:
            points += distributionPointValues['shortness']['singleton']
        elif suitCount == 2:
            points += distributionPointValues['shortness']['doubleton']

    return points

def getLocationAfterRotationsAround(location, numberOfRotations):
    '''
    inputs: ------------------------------
        location = a string representing relative locations: ('right', 'left',...)
        numberOfRotations = an int representing the number of clock-wise rotations
    returns ------------------------------ 
        a string representing a relative location: ('right', 'left', 'top',  or 'bottom')
        example - location = 'right' and numberOfRotations = 1 => 'bottom'
        example - location = 'right' and numberOfRotations = -1 => 'top'
    '''
    locations = ['top', 'right', 'bottom', 'left']
    indexOfLocation = locations.index(location)
    return locations[(indexOfLocation + numberOfRotations) % 4]

def getCurrentContractBidFromBidding(biddingAbsolute):
    '''
    inputs: ------------------------------
        biddingAbsolute = an array of arrays representing the bids to consider (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
    returns ------------------------------
        a string representing the currentContractBid based on biddingAbsolute (e.g. 'One Club', 'Two Heart', etc... )
    '''
    for bid in reversed(biddingAbsolute):
        if not re.search('pass', bid[1], re.IGNORECASE) and not re.search('double', bid[1], re.IGNORECASE):
            return bid[1]

def getWasPlayersNthBidAJumpshift(username, biddingAbsolute, nthBid):
    '''
    inputs:
        username = string
        biddingAbsolute = an array of arrays representing the bids to consider (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
        nthBid = integer representing the 1st, 2nd, 3rd, etc. bid that the user name (e.g. 1 = 1st bid user made, 5 = 5th bid that user made)
        bidLevel = integer representing the level of bid to check for 
            (e.g. 
                1 = 'One Club', 'One Diamond', ... ; 
                2 = 'Two Club', 'Two Diamond', ... ;
                3 = 'Three Club', 'Three Diamond', ... ;
                ...
                7 (is highest)
            )
    returns:
        True if username's nthBid had to be at nthLevel due to currentContractBid up to that point, otherwise false
    '''
    indexOfNthBid = -1
    nthBidCount = 1
    for i in range(len(biddingAbsolute)):
        bid = biddingAbsolute[i]
        if bid[0] == username:
            if nthBidCount == nthBid: 
                indexOfNthBid = i
                break
            nthBidCount += 1

    if indexOfNthBid == -1: raise Exception('Invalid nthBid to getWasPlayerForcedToBidAnNthLevelBidAsTheirNthBid()')

    bidsUpToUsersNthBid = biddingAbsolute[:indexOfNthBid]
    currentContractBid = getCurrentContractBidFromBidding(bidsUpToUsersNthBid)

    return getIsJumpshift(currentContractBid, biddingAbsolute[indexOfNthBid][1])

def getWasFirstOpeningBidANthLevelBid(biddingAbsolute, bidLevel):
    '''
    inputs:
        biddingAbsolute = an array of arrays representing the bids to consider (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
        bidLevel = integer representing the level of bid to check for 
            (e.g. 
                1 = 'One Club', 'One Diamond', ... ; 
                2 = 'Two Club', 'Two Diamond', ... ;
                3 = 'Three Club', 'Three Diamond', ... ;
                ...
                7 (is highest)
            )
    returns:
        the username who made the first non-pass, non-double bid that was at bidLevel (e.g. a two level bid (One No Trump and two club included) if bidLevel == 2), false otherwise
    '''
    try:
        bidLevels = dict([
            (1, 'one'),
            (2, 'two'),
            (3, 'three'),
            (4, 'four'),
            (5, 'five'),
            (6, 'six'),
            (7, 'seven'),
        ])

        for bid in biddingAbsolute:
            if not re.search('pass', bid[1], re.IGNORECASE) and  not re.search('double', bid[1], re.IGNORECASE): 
                if re.search(bidLevels[bidLevel], bid[1], re.IGNORECASE): return bid[0]
                return False

        return False
    except:
        return None

def getUsersFirstContractBid(username, biddingAbsolute):
    '''
    inputs:
        username = string
        biddingAbsolute = an array of arrays representing the bids to consider (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
    returns:
        the first bid that a user made that is not double or pass. if user has never made a contract bid, returns first bid made
    '''
    try:
        firstBid = None
        count = 0
        for bid in biddingAbsolute:
            if bid[0] == username: 
                if count == 0: firstBid = bid[1]
                if not re.search('pass', bid[1], re.IGNORECASE) and not re.search('double', bid[1], re.IGNORECASE): return bid[1]
                count += 1

        return firstBid
    except:
        return None

def getIsUsernamesFirstContractBidTheFirstContractBid(username, biddingAbsolute):
    '''
    inputs: 
        username = string
        biddingAbsolute = an array of arrays representing the bids to consider (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
    returns
        true if the username's first contract bid is the first contract bid made, false otherwise
    '''

    for bid in biddingAbsolute:
        isContractBid = getIsBidAContractBid(bid[1])
        if isContractBid:
            if bid[0] == username:
                return True
            return False

    return False

def getIsBidAContractBid(bid):
    '''
    inputs:
        bid = a string (e.g. 'one club')
    returns 
        true if bid is not double and not pass, false otherwise
    '''
    return not re.search('double', bid, re.IGNORECASE) and not re.search('pass', bid, re.IGNORECASE)

def getPartnersCurrentContractBidFromBidding(username, biddingAbsolute, seatingRelative):
    '''
    inputs:
        biddingAbsolute = an array of arrays representing the bids to consider (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
        username = string
    returns
        the current contract bid that username's partner had when username's partner made their last bid
    '''

    usernamesPartner = getUsernamesPartner(username, seatingRelative)
    indexOfPartnersLastBid = getIndexOfNthBid(usernamesPartner, biddingAbsolute, -1)
    biddingUpToPartnersLastBid = biddingAbsolute[:indexOfPartnersLastBid]
    for bid in reversed(biddingUpToPartnersLastBid):
        if not re.search('pass', bid[1], re.IGNORECASE) and  not re.search('double', bid[1], re.IGNORECASE): return bid[1]

    return None

def getIsBidGameBid(bid):
    '''
    inputs:
        bid = a string ('One Club', "Two Heart', etc... )
    returns:
        True if bid is 3NT or greater than 4 Hearts, None if error, otherwise false
    '''
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
    '''
    inputs: 
        bid1 = a string representing a bid ('One Club', 'One Diamond', etc... )
        bid2 = a string representing a bid ('One Club', 'One Diamond', etc... )
    returns:
        an int representing how many bids higher the higher bid is (e.g. 1, 2, 3, etc... )
    '''
    try:
        if re.search('pass', bid1, re.IGNORECASE) or re.search('double', bid1, re.IGNORECASE) or re.search('pass', bid2, re.IGNORECASE) or re.search('double', bid2, re.IGNORECASE):
            return 0
        bid1Index = autoBid.contracts.index(bid1)
        bid2Index = autoBid.contracts.index(bid2)
        return abs(bid2Index - bid1Index)
    except:
        raise TypeError('Error in getIndexDifferenceOfBids;  Probably incorrect parameter passed in.')

def getHasSomeoneOpenedTwoClubs(biddingAbsolute, biddingRelative, seatingRelative):
    '''
    inputs:
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }
        seatingRelative = { "top": "TopPlayerName", "bottom": "BottomPlayerName", ... }
    returns:
        a tuple where first item is boolean decribing whether someone has bid two clubs and the second item is the name of that person as a string (e.g. [ True, 'Adam'])
    '''
    
    #region check whether anyone bid two clubs as their first bid
    falseTuple = (False, None)
    shouldContinue = False;
    twoClubBid = None

    for location, values in biddingRelative.items(): 
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
    '''
    inputs:
        playerBids = an array representing a player's bidding: ['pass', 'one heart', ...]
    returns:
        False if the player has bid anything other than 'pass' and True otherwise
    '''
    for bid in playerBids:
        if not re.search('pass', bid, re.IGNORECASE):
            return False;

    return True

def getHasOtherTeamMentionedSameSuit(location, usersBid, biddingAbsolute, seatingRelative):
    '''
    inputs:
        location = string (e.g. 'top, 'left', 'right', or 'bottom')
        usersBid = string (e.g. 'One Club', "Two Heart", etc)
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])
        seatingRelative = { "top": "TopPlayerName", "bottom": "BottomPlayerName", ... }
    returns:
        true if the other team has mentioned the same suit as bid's suit but at a lower level, false otherwise
    '''
    try:
        usernamesOpponents = getUsernamesOpponents(location, seatingRelative)
        indexOfUserBid = autoBid.contracts.index(usersBid)

        for i in range(len(biddingAbsolute)):
            bid = biddingAbsolute[i]
            if not getIsBidAContractBid(bid[1]): continue
            indexOfBid = autoBid.contracts.index(bid[1])
            print(f"indexOfBid = {indexOfBid}")
            if indexOfUserBid > indexOfBid and abs(indexOfBid - indexOfUserBid) % 5 == 0:
                if bid[0] in usernamesOpponents:
                    return True

        return False
    except:
        return False

def getUsernamesOpponents(location, seatingRelative):
    '''
    inputs:
        location = string (e.g. 'top, 'left', 'right', or 'bottom')
        seatingRelative = { "top": "TopPlayerName", "bottom": "BottomPlayerName", ... }
    returns:
        an array of location's opposing player usernames
    '''
    try:
        leftUser = seatingRelative[getLocationAfterRotationsAround(location, 1)]
        rightUser = seatingRelative[getLocationAfterRotationsAround(location, -1)]
        return [leftUser, rightUser]
    except:
        return []

def getHasTakenPartnerOutOfGameBid(username, biddingRelative, seatingRelative):
    '''
    inputs:
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }
        username = string (e.g. "Adam" or "Andrew")
    returns:
        true if analyzing player's partner has made a game lvl bid and the analyzing player made a bid after that wasn't 'pass' otherwise false
    '''
    #determine whether username has made a game lvl bid
    for bids in biddingRelative['top']:
    #if they have, return true iff analyzing player has not bid pass after
        pass
    return False

def getHasPartnerOpenedNoTrump(location, partnersLocation, biddingRelative, biddingAbsolute, seatingRelative):
    '''
    inputs:
        partnersLocation = string (e.g. 'left', 'right', 'top', or 'bottom')
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }
    returns:
        true if the first bid for the player at partnersLocation a no trump bid and that bid came before the player at partnersLocation's partner's last bid, false otherwise
    '''
    
    if len(biddingRelative[partnersLocation]) == 0: return False
    if re.search('trump', biddingRelative[partnersLocation][0], re.IGNORECASE):

        partnersOneNoTrumpBidIndex = -1
        locationsLastBidIndex = -1

        for i in range(len(biddingAbsolute)):
            bid = biddingAbsolute[i]

            if bid[0] == seatingRelative[partnersLocation] and re.search('trump', bid[1], re.IGNORECASE): partnersOneNoTrumpBidIndex = i
            if bid[0] == seatingRelative[location]: locationsLastBidIndex = i

        if partnersOneNoTrumpBidIndex < locationsLastBidIndex: return True
        return False

def getIsMinor(bid):
    try:
        indexOfBid = autoBid.contracts.index(bid)
        isClub = indexOfBid % 5 == 0
        isDiamond = indexOfBid % 5 == 1
        return isDiamond or isClub
    except:
        return None

def getIsMajor(bid):
    try:
        indexOfBid = autoBid.contracts.index(bid)
        isHeart = indexOfBid % 5 == 2
        isSpade = indexOfBid % 5 == 3
        return isHeart or isSpade
    except:
        return None

#region Test Case Helpers
def getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, seatingRelative):
    '''
    note: this is written to facilitate test case writing for getEstimatedPoints
    inputs:------------------------------
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }
        seatingRelative = { "top": "TopPlayerName", "bottom": "BottomPlayerName", ... }
    returns:------------------------------
        the bidding array e.g. [['LeftPlayer', "One Diamond"],['TopPlayer', 'Two Heart'],['RightPlayer', 'Two No Trump'], ...] based on inputs
    '''
    try:
        print(f"biddingRelative = {biddingRelative}")
        print(f"seatingRelative = {seatingRelative}")
        locations = getEstimatedPoints.locations
        locationOrder = [locations['left'], locations['top'],locations['right'], locations['bottom']]

        dealer = getDealerLocation(biddingRelative)

        #get new order based on dealer
        locationOrderToUse = locationOrder
        if dealer != locations['left']:
            index = locationOrder.index(locations[dealer])
            locationOrderToUse = locationOrder[index:] + locationOrder[:index]

        #iterate through each location n times where n is the # of opportunities the dealer has had to bid and add bids in order they were made 
        bids = []
        for i in range(0, len(biddingRelative[dealer])):
            for j in range(0, len(locationOrderToUse)):
                locationToGet = locationOrderToUse[j]
                try:
                    bidInQuestion = biddingRelative[locationToGet][i]   
                except:
                    break      

                if bidInQuestion is not None:
                    bids.append([seatingRelative[locationToGet], bidInQuestion])
                else:
                    break
                
        if re.search('bottom', bids[-1][0], re.IGNORECASE):
            bids = bids[:-1]
        return bids

    except:
        print('error-----------')
        return []

def getDealerLocation(biddingRelative):
    '''
    inputs:
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }
    returns:
        a string representing the location of the dealer (e.g. 'top', 'left', etc... )
    '''
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

def getHandFromHandDictionary(handsDictionary):
    '''
    inputs:
        handsDictionary = {"clubs": ["AQJ..."], ... , "spades": ["AQJ...", ...]}
    returns:
        hand = [ [12,11,10], [...], [...], [51,50,49,...] ]
    '''
    starts = {
        "clubs": 0,
        "diamonds": 13,
        "hearts": 26,
        "spades": 39,
    }
    charValues = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "J": 9,
        "T": 8,
        "9": 7,
        "8": 6,
        "7": 5,
        "6": 4,
        "5": 3,
        "4": 2,
        "3": 1,
        "2": 0,
    }
    hand = []
    for suitName, suitString in handsDictionary.items():
        
        newSuitArray = []
        for character in suitString:
            # print(f"character = {character}")
            newSuitArray.append(charValues[character] + starts[suitName])
        hand.append(newSuitArray)

    return hand


#endregion