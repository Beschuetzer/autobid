'''
    Getting the estimated points of each player based on their first two bids
'''
#TODO: make sure suit count estimates from bidding is complete
import autoBid, re

PASS_FIRST_ROUND_WITH_PARTNER_OPEN_MAX = 5
PASS_FIRST_ROUND_WITH_PARTNER_OPEN_MIN = 0
IS_TEAMS_FIRST_BID_PLAYER_PASSES_FIRST_MAX = 12
IS_TEAMS_FIRST_BID_PLAYER_PASSES_FIRST_MIN = 0
PASS_FIRST_NT_SECOND_ROUND_MAX = 12
PASS_FIRST_NT_SECOND_ROUND_MIN = 6
PASS_FIRST_BID_SECOND_ROUND_MAX = 12
PASS_FIRST_BID_SECOND_ROUND_MIN = 8
PASS_FIRST_DOUBLE_SECOND_ROUND_MAX = 12
PASS_FIRST_DOUBLE_SECOND_ROUND_MIN = 8

OPENING_BID_SUIT_FIRST_ROUND_MAX = 15
OPENING_BID_SUIT_FIRST_ROUND_MIN = 13
OPENING_TWO_CLUB_FIRST_ROUND_MAX = 25
OPENING_TWO_CLUB_FIRST_ROUND_MIN = 18
OPENING_NT_FIRST_ROUND_MAX = 18
OPENING_NT_FIRST_ROUND_MIN = 16
OPENING_DOUBLE_FIRST_ROUND_MAX = 18
OPENING_DOUBLE_FIRST_ROUND_MIN = 13
OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX = 12
OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN = 10
OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MAX = 10
OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN = 7

#THESE CASES ARE AMBIGIOUS COULD BE REGULAR OPENERS OR WEAK BID
#E.G. (1 SPADE, 2 HEART, 3 CLUB)
OPENING_WEAK_TWO_AFTER_OPENERS_MAX = OPENING_BID_SUIT_FIRST_ROUND_MAX
OPENING_WEAK_TWO_AFTER_OPENERS_MIN = OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN
OPENING_WEAK_THREE_AFTER_OPENERS_MAX = OPENING_BID_SUIT_FIRST_ROUND_MAX
OPENING_WEAK_THREE_AFTER_OPENERS_MIN = OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN


RESPONDING_BID_SUIT_FIRST_ROUND_MAX = 12
RESPONDING_BID_SUIT_FIRST_ROUND_MIN = PASS_FIRST_ROUND_WITH_PARTNER_OPEN_MAX + 1
RESPONDING_DOUBLE_FIRST_ROUND_MAX = 12
RESPONDING_DOUBLE_FIRST_ROUND_MIN = 10
RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MAX = 12
RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MIN = 10
RESPONDING_NO_JUMPSHIFT_MAX = 12
RESPONDING_NO_JUMPSHIFT_MIN = 6
RESPONDING_NO_JUMPSHIFT_NT_MAX = RESPONDING_NO_JUMPSHIFT_MAX
RESPONDING_NO_JUMPSHIFT_NT_MIN = RESPONDING_NO_JUMPSHIFT_MIN


#estimatedValues houses all of the above information but in a more logically accessible way
estimatedValues = {
    "isTeamsFirstBid": {
        "playerPassesFirst": {
            "min": IS_TEAMS_FIRST_BID_PLAYER_PASSES_FIRST_MIN,
            "max": IS_TEAMS_FIRST_BID_PLAYER_PASSES_FIRST_MAX,
        },
        "playerDoublesFirst": {
            "min": None,
            "max": None,
        },
        "playerBidsSuitFirst": {
            "min": None,
            "max": None,
        },
        "playerBidsNoTrumpFirst": {
            "min": None,
            "max": None,
        },
    },    
    "isNotTeamsFirstBid": {
        "partnerPassesFirst": {
            "playerPassesFirst": {
                "min": None,
                "max": None,
            },
            "playerDoublesFirst": {
                "min": None,
                "max": None,
            },
            "playerBidsSuitFirst": {
                "min": None,
                "max": None,
            },
            "playerBidsNoTrumpFirst": {
                "min": None,
                "max": None,
            },
        },
        "partnerBidsFirst": {
            "playerPassesFirst": {
                "min": None,
                "max": None,
            },
            "playerDoublesFirst": {
                "min": None,
                "max": None,
            },
            "playerBidsSuitFirst": {
                "min": None,
                "max": None,
            },
            "playerBidsNoTrumpFirst": {
                "min": None,
                "max": None,
            },
        },
    }, 

    "special": {
        "weakTwo": {
            "min": None,
            "max": None,
        },
        "weakThree": {
            "min": None,
            "max": None,
        },
        "twoClubs": {
            "min": None,
            "max": None,
        },
    },
}

def getEstimatedPoints(biddingObjRelative, incomingBids, seatingRelative, currentContractBid):
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

    for location, bids in biddingObjRelative.items():
        #region Skipping to Next Player if no bids made
        numberOfBidsMade = len(biddingObjRelative[location])
        if numberOfBidsMade < 1:
            continue
        #endregion
        #region Setup
        username = seatingRelative[location]
        indexOfUsersFirstBid = autoBid.getIndexOfNthBid(username, incomingBids, 1)
        hasPartnerOpened = autoBid.getHasPartnerOpened(incomingBids, username)
        firstBid = biddingObjRelative[location][0]
        firstBidIsPass = re.search('pass', firstBid, re.IGNORECASE)
        isTeamsFirstBidOpportunity = len(biddingObjRelative["top"]) == 0
        isPartnersFirstBidPass = autoBid.getIsPartnersFirstBidPass(biddingObjRelative)

        isJumpShift = False
        try: 
            biddingUpToThisPoint = incomingBids[:indexOfUsersFirstBid]
            isJumpShift = autoBid.getIsJumpShift(biddingUpToThisPoint, incomingBids[indexOfUsersFirstBid][1])
        except:
            pass
        #endregion
        #region Debugging (remove when done)
        print('username = {0}'.format(username))
        print('firstBid = {0}'.format(firstBid))    
        print('hasPartnerOpened = {0}'.format(hasPartnerOpened))
        print('isJumpShift = {0}'.format(isJumpShift))
        print('isTeamsFirstBid = {0}'.format(isTeamsFirstBidOpportunity))
        #endregion
        #region Logic
        #if player has team's first turn and they pass -> a
        if isTeamsFirstBidOpportunity is True and firstBidIsPass:
            print(1)
        
        #if player has team's firt turn and they bid -> b
        elif isTeamsFirstBidOpportunity is True and not firstBidIsPass:
            print(2)

        #if player has team's second turn, parter bids, and they pass -> c
        elif isTeamsFirstBidOpportunity is False and isPartnersFirstBidPass is False and firstBidIsPass:
            print(3)
        
        #if player has team's second turn, partner bids, and they bid -> d
        elif isTeamsFirstBidOpportunity is False and isPartnersFirstBidPass is False and not firstBidIsPass:
            print(4)

        #if player has team's second turn, parter passes, and they pass -> e
        elif isTeamsFirstBidOpportunity is False and isPartnersFirstBidPass is True and firstBidIsPass:
            print(5)

        #if player has team's second turn, parter passes, and they bid -> f
        elif isTeamsFirstBidOpportunity is False and isPartnersFirstBidPass is True and not firstBidIsPass:
            print(6)
        #endregion

        #region Adam's Not Working Code
        # if re.search('pass', firstBid, re.IGNORECASE):
        #     print('pass')
        #     currentBidsForThisPlayer = biddingObjRelative[location]
        #     #TODO: remember to check whether you length of partners bidding array is 0
        #     #if it is, it is the same case as partner passes first
        #     if len(currentBidsForThisPlayer) > 1:
        #         secondBid = currentBidsForThisPlayer[1]
        #         indexOfUsersSecondBid = getIndexOfNthBid(username, incomingBids, 2)
                
        #         secondBidIsJumpShift = getIsJumpShift(incomingBids[:indexOfUsersSecondBid], secondBid)

        #         print('secondBid = {0}'.format(secondBid))
        #         print('indexOfUsersSecondBid = {0}'.format(indexOfUsersSecondBid))
        #         print('secondBidIsJumpShift = {0}'.format(secondBidIsJumpShift))

        #         if secondBidIsJumpShift:
        #             print('here')
        #             estimatedScoring[location]['min'] = RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MIN
        #             estimatedScoring[location]['max'] = RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MAX
        #         else:
        #             if re.search('trump', secondBid, re.IGNORECASE):
        #                 estimatedScoring[location]['min'] = PASS_FIRST_NT_SECOND_ROUND_MIN
        #                 estimatedScoring[location]['max'] = PASS_FIRST_NT_SECOND_ROUND_MAX
        #             elif re.search('double', secondBid, re.IGNORECASE):
        #                 estimatedScoring[location]['min'] = PASS_FIRST_DOUBLE_SECOND_ROUND_MIN
        #                 estimatedScoring[location]['max'] = PASS_FIRST_DOUBLE_SECOND_ROUND_MAX
        #             elif re.search('pass', secondBid, re.IGNORECASE):
        #                 #this is needed to handle cases when # of bids is > 1 and 1st and 2nd bids are pass
        #                 estimatedScoring[location]['min'] = PASS_FIRST_ROUND_WITH_PARTNER_PASS_MIN
        #                 estimatedScoring[location]['max'] = PASS_FIRST_ROUND_WITH_PARTNER_OPEN_MAX
        #             else:
        #                 estimatedScoring[location]['min'] = PASS_FIRST_BID_SECOND_ROUND_MIN
        #                 estimatedScoring[location]['max'] = PASS_FIRST_BID_SECOND_ROUND_MAX
        #     else:
        #         estimatedScoring[location]['min'] = PASS_FIRST_ROUND_WITH_PARTNER_PASS_MIN
        #         estimatedScoring[location]['max'] = PASS_FIRST_ROUND_WITH_PARTNER_OPEN_MAX
        # elif not hasPartnerOpened:
        #     print('opening')
        #     if re.search('trump', firstBid, re.IGNORECASE):
        #         estimatedScoring[location]['min'] = OPENING_NT_FIRST_ROUND_MIN
        #         estimatedScoring[location]['max'] = OPENING_NT_FIRST_ROUND_MAX
        #     elif re.search('double', firstBid, re.IGNORECASE):
        #         estimatedScoring[location]['min'] = OPENING_DOUBLE_FIRST_ROUND_MIN
        #         estimatedScoring[location]['max'] = OPENING_DOUBLE_FIRST_ROUND_MAX
        #     elif re.search('Two Club', firstBid, re.IGNORECASE):
        #         estimatedScoring[location]['min'] = OPENING_TWO_CLUB_FIRST_ROUND_MIN
        #         estimatedScoring[location]['max'] = OPENING_TWO_CLUB_FIRST_ROUND_MAX
        #     else:
        #         hasSomeOneOpenedBefore = getHasSomeOneOpenedBefore(indexOfUsersFirstBid, incomingBids)
        #         if re.search('Two', firstBid, re.IGNORECASE):
        #             if not hasSomeOneOpenedBefore:
        #                 estimatedScoring[location]['min'] = OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN
        #                 estimatedScoring[location]['max'] = OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX
        #             else:
        #                 if not isJumpShift:
        #                     estimatedScoring[location]['min'] = OPENING_WEAK_TWO_AFTER_OPENERS_MIN
        #                     estimatedScoring[location]['max'] = OPENING_WEAK_TWO_AFTER_OPENERS_MAX
        #                 elif isJumpShift:
        #                     estimatedScoring[location]['min'] = OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN
        #                     estimatedScoring[location]['max'] = OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX
                       
        #         elif re.search('Three', firstBid, re.IGNORECASE):
        #             if not hasSomeOneOpenedBefore:
        #                 estimatedScoring[location]['min'] = OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN
        #                 estimatedScoring[location]['max'] = OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MAX
        #             else:
        #                 if not isJumpShift:
        #                     estimatedScoring[location]['min'] = OPENING_WEAK_THREE_AFTER_OPENERS_MIN
        #                     estimatedScoring[location]['max'] = OPENING_WEAK_THREE_AFTER_OPENERS_MAX
        #                 elif isJumpShift:
        #                     estimatedScoring[location]['min'] = OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN
        #                     estimatedScoring[location]['max'] = OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MAX
                        
        #         else:
        #             estimatedScoring[location]['min'] = OPENING_BID_SUIT_FIRST_ROUND_MIN
        #             estimatedScoring[location]['max'] = OPENING_BID_SUIT_FIRST_ROUND_MAX
        # else:
            # print('responding')
            # if re.search('double', firstBid, re.IGNORECASE):
            #     estimatedScoring[location]['min'] = RESPONDING_DOUBLE_FIRST_ROUND_MIN
            #     estimatedScoring[location]['max'] = RESPONDING_DOUBLE_FIRST_ROUND_MAX            
            # else:
            #     partnersLocation = autoBid.getPartnersLocation(username, seatingRelative)
            #     partnersLastBid = incomingBids[autoBid.getIndexOfNthBid(seatingRelative[partnersLocation], incomingBids, -1)][1]

            #     print('partnersLastBid = {0}'.format(partnersLastBid))
                
            #     if isJumpShift:
            #             if re.search('trump', firstBid, re.IGNORECASE):
            #                 estimatedScoring[location]['min'] = OPENING_NT_FIRST_ROUND_MIN
            #                 estimatedScoring[location]['max'] = OPENING_NT_FIRST_ROUND_MAX
            #             else:
            #                 estimatedScoring[location]['min'] = OPENING_BID_SUIT_FIRST_ROUND_MIN
            #                 estimatedScoring[location]['max'] = OPENING_BID_SUIT_FIRST_ROUND_MAX
            #     else:
            #         if re.search('three', firstBid, re.IGNORECASE):                     
            #             estimatedScoring[location]['min'] = OPENING_WEAK_THREE_AFTER_OPENERS_MIN
            #             estimatedScoring[location]['max'] = OPENING_WEAK_THREE_AFTER_OPENERS_MAX
            #         else:
            #             if re.search('trump', firstBid, re.IGNORECASE):
            #                 estimatedScoring[location]['min'] = RESPONDING_NO_JUMPSHIFT_NT_MIN
            #                 estimatedScoring[location]['max'] = RESPONDING_NO_JUMPSHIFT_NT_MAX
            #             else: 
            #                 estimatedScoring[location]['min'] =    RESPONDING_NO_JUMPSHIFT_MIN
            #                 estimatedScoring[location]['max'] = RESPONDING_NO_JUMPSHIFT_MAX
        #endregion 

    return estimatedScoring
