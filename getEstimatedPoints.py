'''
    Getting the estimated points of each player based on their first two bids
'''
#TODO: make sure suit count estimates from bidding is complete
import helpers, re

locations = {
    "bottom": 'bottom',
    "left": 'left',
    "right": 'right',
    "top": 'top',
}

PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX = 5
PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MIN = 0
PARTNER_BIDS_FIRST_AND_PLAYER_DOUBLES_MAX = 18
PARTNER_BIDS_FIRST_AND_PLAYER_DOUBLES_MIN = 13
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_MAX = 12
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_MIN = 6
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_JUMPSHIFT_MAX = -1
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_JUMPSHIFT_MIN = 13
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_NOT_JUMPSHIFT_MAX = 12
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_NOT_JUMPSHIFT_MIN = 6

PARTNER_PASSES_FIRST_AND_PLAYER_PASSES_MAX = 12
PARTNER_PASSES_FIRST_AND_PLAYER_PASSES_MIN = 0
PARTNER_PASSES_FIRST_AND_PLAYER_DOUBLES_MAX = 18
PARTNER_PASSES_FIRST_AND_PLAYER_DOUBLES_MIN = 13
PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_SUIT_MAX = 15
PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_SUIT_MIN = 13
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_JUMPSHIFT_MAX = -1
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_JUMPSHIFT_MIN = 13
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_NOT_JUMPSHIFT_MAX = 12
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_NOT_JUMPSHIFT_MIN = 6
PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_NT_MAX = 18
PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_NT_MIN = 16

IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MAX = 12
IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN = 0
IS_TEAMS_FIRST_BID_AND_PLAYER_DOUBLES_MAX = 18
IS_TEAMS_FIRST_BID_AND_PLAYER_DOUBLES_MIN = 13
IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX = 15
IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN = 13
IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MAX = 18
IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MIN = 16

SPECIAL_WEAK_TWO_MAX = 12
SPECIAL_WEAK_TWO_MIN = 9
SPECIAL_WEAK_THREE_MAX = 12
SPECIAL_WEAK_THREE_MIN = 7
SPECIAL_WEAK_TWO_CLUBS_MAX = -1
SPECIAL_WEAK_TWO_CLUBS_MIN = 18

#region Adam's logic variables
PASS_FIRST_NT_SECOND_ROUND_MAX = 12
PASS_FIRST_NT_SECOND_ROUND_MIN = 6
PASS_FIRST_BID_SECOND_ROUND_MAX = 12
PASS_FIRST_BID_SECOND_ROUND_MIN = 8
PASS_FIRST_DOUBLE_SECOND_ROUND_MAX = 12
PASS_FIRST_DOUBLE_SECOND_ROUND_MIN = 8

RESPONDING_BID_SUIT_FIRST_ROUND_MAX = 12
RESPONDING_BID_SUIT_FIRST_ROUND_MIN = PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX + 1
RESPONDING_DOUBLE_FIRST_ROUND_MAX = 12
RESPONDING_DOUBLE_FIRST_ROUND_MIN = 10
RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MAX = 12
RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MIN = 10
RESPONDING_NO_JUMPSHIFT_MAX = 12
RESPONDING_NO_JUMPSHIFT_MIN = 6
RESPONDING_NO_JUMPSHIFT_NT_MAX = RESPONDING_NO_JUMPSHIFT_MAX
RESPONDING_NO_JUMPSHIFT_NT_MIN = RESPONDING_NO_JUMPSHIFT_MIN

OPENING_TWO_CLUB_FIRST_ROUND_MAX = 25
OPENING_TWO_CLUB_FIRST_ROUND_MIN = 18

OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX = 12
OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN = 10
OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MAX = 10
OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN = 7

#THESE CASES ARE AMBIGIOUS COULD BE REGULAR OPENERS OR WEAK BID
#E.G. (1 SPADE, 2 HEART, 3 CLUB)
OPENING_WEAK_TWO_AFTER_OPENERS_MAX = IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX
OPENING_WEAK_TWO_AFTER_OPENERS_MIN = OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN
OPENING_WEAK_THREE_AFTER_OPENERS_MAX = IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX
OPENING_WEAK_THREE_AFTER_OPENERS_MIN = OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN
#endregion


#values convey all of the above information but in a more logically organized way
values = {
    #TODO: are there any cases where the point count isn't discernible from just the first two bids of each player?
    #TODO: do we need to add values for cases like 'test_only_pass_partner_passes_first' left player case?
    "passFirstBidSecond" : {
        "min": IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN - 2,
        "max": IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX - 2,
    },
    "isTeamsFirstBid": {
        "playerPasses": {
            "min": IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN,
            "max": IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MAX,
        },
        "playerDoubles": {
            "min": IS_TEAMS_FIRST_BID_AND_PLAYER_DOUBLES_MIN,
            "max": IS_TEAMS_FIRST_BID_AND_PLAYER_DOUBLES_MAX,
        },
        "playerBidsSuit": {
            "min": IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
            "max": IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
        },
        "playerBidsNoTrump": {
            "min": IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MIN,
            "max": IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MAX,
        },
    },    

    "partnerPassesFirst": {
        "playerPasses": {
            "min": PARTNER_PASSES_FIRST_AND_PLAYER_PASSES_MIN,
            "max": PARTNER_PASSES_FIRST_AND_PLAYER_PASSES_MAX,
        },
        "playerDoubles": {
            "min": PARTNER_PASSES_FIRST_AND_PLAYER_DOUBLES_MIN,
            "max": PARTNER_PASSES_FIRST_AND_PLAYER_DOUBLES_MAX,
        },
        "playerBidsSuit": {
            "min": PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_SUIT_MIN,
            "max": PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_SUIT_MAX,
        },
        "playerBidsNoTrump": {
            "min": PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_NT_MIN,
            "max": PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_NT_MAX,
        },
    },

    "partnerBidsFirst": {
        "playerPasses": {
            "min": PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MIN,
            "max": PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
        },
        "playerDoubles": {
            "min": PARTNER_BIDS_FIRST_AND_PLAYER_DOUBLES_MIN,
            "max": PARTNER_BIDS_FIRST_AND_PLAYER_DOUBLES_MAX,
        },
        "playerBidsSuit": {
            "isJumpshift": {
                "min": PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_JUMPSHIFT_MIN,
                "max": PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_JUMPSHIFT_MAX,
            },
            "isNotJumpshift": {
                "min": PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_NOT_JUMPSHIFT_MIN,
                "max": PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_NOT_JUMPSHIFT_MAX,
            }
        },
        "playerBidsNoTrump": {
            "isJumpshift": {
                "min": PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_JUMPSHIFT_MIN,
                "max": PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_JUMPSHIFT_MAX,
            },
            "isNotJumpshift": {
                "min": PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_NOT_JUMPSHIFT_MIN,
                "max": PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_NT_IS_NOT_JUMPSHIFT_MAX,
            }
        },
    },

    "special": {
        "weakTwo": {
            "min": SPECIAL_WEAK_TWO_MIN,
            "max": SPECIAL_WEAK_TWO_MAX,
        },
        "weakThree": {
            "min": SPECIAL_WEAK_THREE_MIN,
            "max": SPECIAL_WEAK_THREE_MAX,
        },
        "respondTwoClubs": {
            "oneBidAbove": {
                "min": 0,
                "max": 3,
            },
            "twoBidAbove": {
                "min": 4,
                "max": 6,
            },
            "threeBidAbove": {
                "min": 7,
                "max": 9,
            },
            "fourBidAbove": {
                "min": 10,
                "max": 12,
            },
            "fiveBidAbove": {
                "min": 13,
                "max": 15,
            },
            "sixBidAbove": {
                "min": 16,
                "max": 18,
            },
            "sevenAndMoreAbove": {
                "min": 19,
                "max": -1,
            },
        },
        "openTwoClubs": {
            "min": SPECIAL_WEAK_TWO_CLUBS_MIN,
            "max": SPECIAL_WEAK_TWO_CLUBS_MAX,
        },
    },
}



def getEstimatedPoints(estimatedScoringBounds, biddingObjRelative, allBids, seatingRelative):
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

    for location, playersBids in biddingObjRelative.items():
        #region Skipping estimation if location is bottom (as that is your hand) or the player in question has made no bids
        numberOfBidsMade = len(biddingObjRelative[location])
        if numberOfBidsMade < 1 or re.search('bottom', location, re.IGNORECASE):
            continue
        #endregion
        #region Setup
        username = seatingRelative[location]
        print('')
        print('username = {0}'.format(username))

        #Getting the currentContractBid for the user in question
        biddingUpToUsersLastTurn = allBids[:helpers.getIndexOfNthBid(username, allBids, -1)]
        currentContractBidForUser = helpers.getCurrentContractBidFromBidding(biddingUpToUsersLastTurn)
        print('biddingUpToUsersTurn = {0}'.format(biddingUpToUsersLastTurn))
        print('currentContractBidForUser = {0}'.format(currentContractBidForUser))

        indexOfUsersFirstBid = helpers.getIndexOfNthBid(username, allBids, 1)
        hasPartnerOpened = helpers.getHasPartnerOpened(allBids, username)
        firstBid = biddingObjRelative[location][0]
        secondBid = ''
        lastBid = ''
        if len(biddingObjRelative[location]) > 1:
            secondBid = biddingObjRelative[location][1]
            lastBid = biddingObjRelative[location][-1]

        firstBidIsPass = re.search('pass', firstBid, re.IGNORECASE)
        isTeamsFirstBidOpportunity = getIsTeamsFirstBidOpportunity(biddingObjRelative, location)
        isPartnersFirstBidPass = helpers.getIsPartnersFirstBidPass(biddingObjRelative)

        isFirstBidJumpshift = False
        isLastBidJumpshift = False
        try: 
            isFirstBidJumpshift = helpers.getIsJumpshift(currentContractBidForUser, firstBid)
            isLastBidJumpshift = helpers.getIsJumpshift(currentContractBidForUser, lastBid)

            #TODO: do we need to check if the user made a bid that is a jumpshift ever and then have entirely separate logic in that case?
            isAnyBidJumpshift = helpers.getHasPlayerJumpshifted(username, playersBids, allBids)


        except:
            pass
        #endregion
        #region Debugging (remove when done)
        print('currentContractBid = {0}'.format(currentContractBidForUser))
        # print('players = {0}'.format(allBids[indexOfUsersFirstBid][1]))
        print('biddingObjectRelative = {0}'.format(biddingObjRelative))
        print('firstBid = {0}'.format(firstBid))    
        print('hasPartnerOpened = {0}'.format(hasPartnerOpened))
        print('isFirstBidJumpShift = {0}'.format(isFirstBidJumpshift))
        print('isLastBidJumpShift = {0}'.format(isLastBidJumpshift))
        print('isTeamsFirstBidOpportunity = {0}'.format(isTeamsFirstBidOpportunity))

        #endregion
        #region Setting Initial Bounds Logic
        if secondBid == '':

            minToUse = None;
            maxToUse = None;

            if isTeamsFirstBidOpportunity and firstBidIsPass:
                print('one opportunity first bid pass-----------')
                minToUse = values['isTeamsFirstBid']['playerPasses']['min']
                maxToUse = values['isTeamsFirstBid']['playerPasses']['max']
                
            else: 
                print('one opportunity else-----------')
                minToUse, maxToUse = setInitialBounds(location, biddingObjRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass)

                #region TODO: 4-6 are not being hit by test cases.  Do we need them here as we only need to handle cases where there is one bid made at most for each player and the player's bid is a pass?:

                # elif isTeamsFirstBidOpportunity is True and not firstBidIsPass:
                #     print(2)
                #     minToUse, maxToUse = setInitialBounds(location, biddingObjRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass)

                # elif isTeamsFirstBidOpportunity is False and isPartnersFirstBidPass is False and firstBidIsPass:
                #     #partner = ['something', ...]
                #     #player =['pass', ...]
                #     print(3)
                #     minToUse, maxToUse = setInitialBounds(location, biddingObjRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass)
                    
                

                # elif isTeamsFirstBidOpportunity is False and isPartnersFirstBidPass is False and not firstBidIsPass:
                #     print(4)
                #     #partner = ['something', ...]
                #     #player =['One Club', ...]
                #     minToUse, maxToUse = setInitialBounds(location, biddingObjRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass)


                # elif isTeamsFirstBidOpportunity is False and isPartnersFirstBidPass is True and firstBidIsPass:
                # # TODO: write a case for this logic
                #     print(5)
                #     #partner = ['pass', ...]
                #     #player =['One Club', ...]

                # elif isTeamsFirstBidOpportunity is False and isPartnersFirstBidPass is True and not firstBidIsPass:
                #     print(6)
                #     minToUse, maxToUse = setInitialBounds(location, biddingObjRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass)

                #     # partner = ['Pass', ...]
                #     # player =['Pass', ...]
                #endregion
                
            estimatedScoring[location]['min'] = minToUse
            estimatedScoring[location]['max'] = maxToUse
        #endregion
        #region updating bounds using estimatedScoringBounds
        else:
            #region when the opportunities to bid is two long
            if len(playersBids) == 2: 
                #region when the first bid is pass and 2nd bid is not pass or double
                if firstBidIsPass:
                    if not re.search('pass' , secondBid, re.IGNORECASE) and not re.search('double' , secondBid, re.IGNORECASE):
                        print('first bid pass second not')
                        estimatedScoring[location]['min'] = 11
                        estimatedScoring[location]['max'] = 13
                        continue
                    else:
                        #update min/max if two passes in a row?
                        pass

                else:
                    #when opportunities to bid is two and first bid is not pass?

                    #when do we need to consider partners bids?
                    #pass
                    pass
                #endregion


                    #did they pass first time?

                    #did they bid a suit or nt first time?
                        #did their partner pass or bid? 

                #bid suit
                    #did you bid same suit for first bid?

                #bid nt
                    #did you bid NT for first bid?


                #bid same suit
                pass
            #endregion
            #region When the opportunities to bid is longer than 2
            else:
                #did they say the same suit multiple times?
                #did they pass first then jumpshift?
                pass
            #endregion

            #returning the values that are already present if no other cases hit
            estimatedScoring[location]['min'] = estimatedScoringBounds[location]['min']
            estimatedScoring[location]['max'] = estimatedScoringBounds[location]['max']
        #endregion
    print('')
    return estimatedScoring

def getPlayerHasOnlyPassed(playerBids):
    for bid in playerBids:
        if not re.search('pass', bid, re.IGNORECASE):
            return False;

    return True

def setInitialBounds(location, biddingObjRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass):
    locationsRightLocation = helpers.getLocationAfterRotationsAround(location, -1);
    haveOpponentsNotHadTurnOrPassed = len(biddingObjRelative[locationsRightLocation]) == 0 or re.search('Pass' , biddingObjRelative[locationsRightLocation][0], re.IGNORECASE)
    print('setInitialBounds-----------------')
    # print('biddingObjRelative["right"][0] = {0}'.format(biddingObjRelative['right'][0]))
    # print('haveOpponentsNotHadTurnOrPassed = {0}'.format(haveOpponentsNotHadTurnOrPassed))
    # print('re:'.format(re.search('Pass' , biddingObjRelative['right'][0], re.IGNORECASE)))

    if re.search('trump', firstBid, re.IGNORECASE):
        #partner = []
        #player =['One NT']
        print('trump branch')
        print('isFirstBidJumpshift = {0}'.format(isFirstBidJumpshift))
        if isFirstBidJumpshift:
            minToUse = values['partnerBidsFirst']['playerBidsNoTrump']['isJumpshift']['min']
            maxToUse = values['partnerBidsFirst']['playerBidsNoTrump']['isJumpshift']['max']
        else:
            if hasPartnerOpened:
                minToUse = values['partnerBidsFirst']['playerBidsNoTrump']['isNotJumpshift']['min']
                maxToUse = values['partnerBidsFirst']['playerBidsNoTrump']['isNotJumpshift']['max']
            else:
                minToUse = values['isTeamsFirstBid']['playerBidsNoTrump']['min']
                maxToUse = values['isTeamsFirstBid']['playerBidsNoTrump']['max']

    elif re.search('two club', firstBid, re.IGNORECASE) and haveOpponentsNotHadTurnOrPassed:
        #partner = []
        #player =['Two Club']
        print('two branch')
        maxToUse = values['special']['openTwoClubs']['max']
        minToUse = values['special']['openTwoClubs']['min']

    elif re.search('double', firstBid, re.IGNORECASE):
        #partner = []
        #player =['Double']
        print('double branch')
        minToUse = values['isTeamsFirstBid']['playerDoubles']['min']
        maxToUse = values['isTeamsFirstBid']['playerDoubles']['max']

    elif re.search('two', firstBid, re.IGNORECASE):
        #partner = []
        #player =['Two Diamond']
        print('trump branch')
        minToUse = values['special']['weakTwo']['min']
        maxToUse = values['special']['weakTwo']['max']

    elif re.search('three', firstBid, re.IGNORECASE):
        #partner = []
        #player =['Three Club']
        print('three branch')
        minToUse = values['special']['weakThree']['min']
        maxToUse = values['special']['weakThree']['max']

    elif re.search('pass', firstBid, re.IGNORECASE):
        print('pass branch')
        if hasPartnerOpened:
            minToUse = values['partnerBidsFirst']['playerPasses']['min']
            maxToUse = values['partnerBidsFirst']['playerPasses']['max']
        else: 
            minToUse = values['isTeamsFirstBid']['playerPasses']['min']
            maxToUse = values['isTeamsFirstBid']['playerPasses']['max']

    else:
        print('else branch')
        #partner = []
        #player =['One Club']
        if hasPartnerOpened:
            if isPartnersFirstBidPass:
                minToUse = values['partnerPassesFirst']['playerBidsSuit']['min']
                maxToUse = values['partnerPassesFirst']['playerBidsSuit']['max']
            else:
                if isFirstBidJumpshift:
                    minToUse = values['partnerBidsFirst']['playerBidsSuit']['isJumpshift']['min']
                    maxToUse = values['partnerBidsFirst']['playerBidsSuit']['isJumpshift']['max']
                else:
                    minToUse = values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min']
                    maxToUse = values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['max']
        else:
            minToUse = values['isTeamsFirstBid']['playerBidsSuit']['min']
            maxToUse = values['isTeamsFirstBid']['playerBidsSuit']['max']

    return [minToUse, maxToUse]

def getIsTeamsFirstBidOpportunity(biddingObjRelative, location):
    partnersLocation = ''
    
    if location == locations['top']:
        partnersLocation = locations['bottom'] 
    elif location == locations['bottom']:
        partnersLocation = locations['top']
    elif location == locations['right']:
        partnersLocation = locations['left']
    elif location == locations['left']:
        partnersLocation = locations['right']
    else:
        raise ValueError('location must be top bottom left of right')

    partnersBids = biddingObjRelative[partnersLocation]

    #this is for the test case 'test_left'
    if location == locations['left'] and len(partnersBids) == 1:
        return True

    return len(biddingObjRelative[partnersLocation]) == 0







#region Not sure 
# #partner = ['something']
# #player =['pass']
# playerBids = biddingObjRelative[location]
# playerHasOnlyPassed = getPlayerHasOnlyPassed(playerBids);

# if playerHasOnlyPassed:
#     #partner = [...]
#     #player =['pass','pass','pass','pass','pass'...]
#     minToUse = values.isTeamsFirstBid.playerPasses.min
#     maxToUse = values.isTeamsFirstBid.playerPasses.max              
# else:
#     #case partner opened:
#     if hasPartnerOpened:
#         #partner = ['One NT', ...]
#         #player =['pass','two diamonds', ...]
#         minToUse = values.partnerPassesFirst.playerPasses.min
#         maxToUse = values.partnerPassesFirst.playerPasses.max
#     else:
#         #partner = ['pass', ...]
#         #player =['pass','two diamonds', ...]
#         minToUse = values.partnerBidsFirst.playerPasses.min
#         maxToUse = values.partnerBidsFirst.playerPasses.max
#endregion
#region Adam's Not Working Code
# if re.search('pass', firstBid, re.IGNORECASE):
#     print('pass')
#     currentBidsForThisPlayer = biddingObjRelative[location]
#     #TODO: remember to check whether you length of partners bidding array is 0
#     #if it is, it is the same case as partner passes first
#     if len(currentBidsForThisPlayer) > 1:
#         secondBid = currentBidsForThisPlayer[1]
#         indexOfUsersSecondBid = getIndexOfNthBid(username, allBids, 2)
    
#         secondBidIsJumpShift = getIsJumpShift(allBids[:indexOfUsersSecondBid], secondBid)

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
#         hasSomeOneOpenedBefore = getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids)
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
#     partnersLocation = helpers.getPartnersLocation(username, seatingRelative)
#     partnersLastBid = allBids[helpers.getIndexOfNthBid(seatingRelative[partnersLocation], allBids, -1)][1]

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
