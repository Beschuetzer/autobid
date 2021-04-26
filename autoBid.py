#Purpose: make best bid that the humans we play with can understand, taking into account cards in hand, previous bids, and eventually score

import re, math, getEstimatedPoints, getEstimatedSuitCounts, helpers

#region Globals

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
estimatedScoringBounds = {
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
flatten = lambda t: [item for sublist in t for item in sublist]
#endregion

#region Examples of inputs
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

bids = [['Adam', 'Two No Trump'], ['Dan', 'Double'], ['Ann', 'Double'], ['Andrew', 'Three Club']]
# bids = [['Adam', 'Pass'], ['Dan', 'Two Club'], ['Ann', 'pass']]
hand = [[0, 1, 7, 8, 12], [13, 18, 19], [29, 30, 32], [40,42]]
#endregion

def autoBid(biddingAbsolute, hand, scoring, seatingInput, spot, clientPointCountingConvention):
    '''
    inputs: ------------------------------------------------------------------------
        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])

        hand = 2D array where the first index represents clubs, the second diamonds, the third hearts, and the fourth spades (e.g. [ [11,10, 8], [24,22,20,17,15], [], [51,50,49,48,47])

         scoring = an obj/dictionary representing the scores (e.g. 
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

        seating: a dictionary with cardinal directions as keys and strings as keys (e.g. { "north": "Adam", "south": "Tim", ... })
        spot: string representing cardinal seating position (e.g. 'north', 'south', 'east', or 'west')
        clientPointCountingConvention: string representing how client counts HCP points (e.g. 'Alternative' or 'HCP' )
    returns -------------------------------------------------------------------------: 
        "best" bid for current situation in the form of a string (e.g. 'One Club', 'Two No Trump', 'Pass', etc... )
    '''
    #region Initialization (Getting Values and Dicts to work with)
    seating['north'] = seatingInput['north']
    seating['south'] = seatingInput['south']
    seating['east'] = seatingInput['east']
    seating['west'] = seatingInput['west']
    
    isFirstBid = len(biddingAbsolute) < 4
    partnerHasBid = len(biddingAbsolute) >= 2
    currentContractBid = helpers.getCurrentContractBid(biddingAbsolute)
    analyzingPlayerSuitCounts = helpers.getSuitCountsFromHand(hand)
    highCardPointValuesInEachSuit = helpers.getHighCardPointValuesInEachSuit(hand, clientPointCountingConvention)
        
    biddingObjAbsolute = helpers.getBiddingObjAbsolute(biddingAbsolute, seating)    
    biddingRelative = helpers.getBiddingObjRelative(biddingObjAbsolute, spot)


    biddingHistory = helpers.getBiddingHistory(biddingAbsolute)
    seatingRelative = helpers.getSeatingRelative(seating, spot)
    estimatedPoints = getEstimatedPoints.getEstimatedPoints(estimatedScoringBounds, biddingRelative, biddingAbsolute, seatingRelative)
    estimatedSuitCounts = getEstimatedSuitCounts.getEstimatedSuitCounts(biddingRelative, biddingAbsolute, seatingRelative)
    partnersBids = biddingRelative['top']

    print(estimatedPoints)
    #endregion

    #region get hand points
    highCardPoints = helpers.getHighCardPoints(hand, clientPointCountingConvention)
    distributionPoints = helpers.getDistributionPoints(hand, biddingAbsolute, biddingRelative, seatingRelative, analyzingPlayerSuitCounts)
    totalPoints = highCardPoints + distributionPoints
    #endregion

    #region Check whether to double and return double if true
    canDouble = helpers.getCanDouble(biddingRelative)
    shouldDouble = helpers.getShouldDouble(scoring, biddingRelative, estimatedPoints, hand, currentContractBid)
    if shouldDouble is True:
        return 'Double'
    #endregion    

    #region handle partner opens 1 Club
        #TODO:
    #endregion

    #region decide whether to open 2 clubs
        #todo:
    #endregion

    #region handle responding when analyzing player opened 2 clubs
        #todo:
    #endregion

    #handle partner opens 2 Club
    if (re.search('two club', biddingRelative['top'][0], re.IGNORECASE) and re.search('pass', biddingRelative['left'][0], re.IGNORECASE)):
        openDistributionPoints = helpers.getOpeningDistributionPoints(analyzingPlayerSuitCounts)
        return helpers.getTwoClubResponse(hand, biddingRelative, seatingRelative, highCardPoints + openDistributionPoints, currentContractBid, clientPointCountingConvention)
    
    #region check if opposing team would win game and / or get a game if they made currentActualBid (assuming they made the currentActualBid)
        #TODO: 
    #endregion


    #handle weak bid: -> pass/3NT/game in their suit/your best suit if lots of points or 6+ of a suit depending on your points, cards in their suit, if you have stoppers
    #if 1 NT -> best suit

    #TODO: do you pass if partner doubles and the person before you doubles?
    result = helpers.handlePartnerDouble(hand, biddingAbsolute, biddingRelative, totalPoints, clientPointCountingConvention) 
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
#special situations accounted for above (takeout double, 1+2 Clubs, 1 NT and weak bids)
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


