#Purpose: make best bid taking into account cards in hand, previous bids, possibly score
import helpers.getHandPoints

'''
Inputs:
    Hand: 2D array
        Integers from 0-51
    Incoming Bids: 2D array
        First index is name of bidder
        Second index is string representing the name of the bid i.e. 1 No Trump
Returns: "best" bid for current situation in the form of the original input (2D array or string)
'''
bids = [['Adam', 'Two No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass']]
hand = [0, 1, 5, 7, 11, 13, 18, 19, 29, 30, 32, 40, 51]

def autoBid(incomingBids, hand, score):
    #get partners bids
    partnersBids = getPartnersBids(incomingBids)

    #get total hand point count based on partners bids and hand
    handPoints = getHandPoints(hand, partnersBids)

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




def getSuitFromCardAsNumber(cardAsNumber):
    #input: integer 0 - 51
    #return a suit ('club', 'diamond', 'heart' or 'spade')
    if cardAsNumber >= 0 and cardAsNumber <= 12:
        return 'club'
    elif cardAsNumber >= 13 and cardAsNumber <= 25:
        return 'diamond'
    elif cardAsNumber >= 26 and cardAsNumber <= 38:
        return 'heart'
    elif cardAsNumber >= 39 and cardAsNumber <= 51:
        return 'spade'
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

def getHandPoints(hand, partnersBids):
    #input: the hand and the bids partner has made up to this point from most current to least
    #return: an integer represting the estimated value of the hand based on partner's bids

    if len(partnersBids) == 0:
        return getHandPointValue




# print(autoBid(bids, 2, 0))

