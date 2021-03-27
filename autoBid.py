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
bids = [['Adam', 'Two No Trump'], ['Dan', 'Double'], ['Ann', 'Double'], ['Andrew', 'Three Club']]
# bids = [['Adam', 'Pass'], ['Dan', 'Two Club'], ['Ann', 'pass']]

hand = [[0, 1, 7, 8, 12], [13, 18, 19], [29, 30, 32], [40,42]]
      
import re, math, getEstimatedPoints, helpers
flatten = lambda t: [item for sublist in t for item in sublist]

def autoBid(incomingBids, hand, scoring, seating, spot, clientPointCountingConvention):
    global suitCounts
    global highCardPointValuesInEachSuit

    #region Initialization (Getting Values and Dicts to work with)
    isFirstBid = len(incomingBids) < 4
    partnerHasBid = len(incomingBids) >= 2
    currentContractBid = helpers.getCurrentActualBid(incomingBids)
    if suitCounts == None:
        suitCounts = helpers.getSuitCounts(hand)
    if highCardPointValuesInEachSuit == None:
        highCardPointValuesInEachSuit = helpers.getHighCardPointValuesInEachSuit(hand)
        
    biddingObjAbsolute = helpers.getBiddingObjAbsolute(incomingBids, seating)    
    biddingObjRelative = helpers.getBiddingObjRelative(biddingObjAbsolute, spot)


    biddingHistory = helpers.getBiddingHistory(incomingBids)
    seatingRelative = helpers.getSeatingRelative(seating, spot)
    estimatedPoints = getEstimatedPoints.getEstimatedPoints(biddingObjRelative, incomingBids, seatingRelative, currentContractBid)
    estimatedSuitCounts = helpers.getEstimatedSuitCounts(biddingObjRelative, incomingBids, seatingRelative)
    partnersBids = biddingObjRelative['top']
    #endregion

    partnersEstimatedPointCount = helpers.getPartnersEstimatedPointCount(partnersBids)

    #get straight up point counts
    highCardPoints = helpers.getHighCardPoints(hand, clientPointCountingConvention)
    distributionPoints = helpers.getDistributionPoints(hand, incomingBids, biddingObjRelative, seatingRelative, suitCounts)
    totalPoints = highCardPoints + distributionPoints

    #region Check whether to double and return double if true
    canDouble = getCanDouble(biddingObjRelative)
    shouldDouble = getShouldDouble(scoring, biddingObjRelative, partnersEstimatedPointCount, hand, currentContractBid)
    if shouldDouble is True:
        return 'Double'
    #endregion    

    #handle partner 1 Club

    #handle partner 2 Club
    if (isFirstBid and re.search('two club', biddingObjRelative['top'][0], re.IGNORECASE) and re.search('pass', biddingObjRelative['left'][0], re.IGNORECASE)):
        openDistributionPoints = helpers.getOpeningDistributionPoints(suitCounts)
        return helpers.getTwoClubResponse(hand, biddingObjRelative, highCardPoints + openDistributionPoints, currentContractBid)
    

    #handle weak bid: -> pass/3NT/game in their suit/your best suit if lots of points or 6+ of a suit depending on your points, cards in their suit, if you have stoppers
    #if 1 NT -> best suit

    #TODO: do you pass if partner doubles and the person before you doubles?
    result = helpers.handlePartnerDouble(hand, incomingBids, biddingObjRelative, totalPoints) 
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


