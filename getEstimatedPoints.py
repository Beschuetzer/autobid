'''
    Getting the estimated points of each player based on their first two bids
'''
#TODO: make sure suit count estimates from bidding is complete
from tests.test_helpers import getCurrentActualBid, getIsJumpShift
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
PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_SUIT_MAX = 18
PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_SUIT_MIN = 13
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_JUMPSHIFT_MAX = -1
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_JUMPSHIFT_MIN = 13
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_NOT_JUMPSHIFT_MAX = 12
PARTNER_BIDS_FIRST_AND_PLAYER_BIDS_SUIT_IS_NOT_JUMPSHIFT_MIN = 6
PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_NT_MAX = 18
PARTNER_PASSES_FIRST_AND_PLAYER_BIDS_NT_MIN = 16
IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MAX = 13
IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN = 0
IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_FIRST_OPENS_SECOND_MIN = 10
IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_FIRST_OPENS_SECOND_MAX = 13

IS_TEAMS_FIRST_BID_AND_PLAYER_DOUBLES_MAX = 18
IS_TEAMS_FIRST_BID_AND_PLAYER_DOUBLES_MIN = 13
IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX = 18
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
        "isJumpshift": {
            "partnerHasOpened": {
                "min": RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MIN,
                "max": RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MAX,
            },
            "partnerHasNotOpened": {
                "min": SPECIAL_WEAK_THREE_MIN,
                "max": SPECIAL_WEAK_TWO_CLUBS_MAX,
            }
        },
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
        "playerPassesFirstOpensSecond": {
            "min": IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_FIRST_OPENS_SECOND_MIN,
            "max": IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_FIRST_OPENS_SECOND_MAX,
        }
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
        "wtf": {
           "min": SPECIAL_WEAK_THREE_MIN,
           "max": SPECIAL_WEAK_TWO_CLUBS_MAX,
        },
    },
}

def getEstimatedPoints(estimatedScoringBounds, biddingRelative, biddingAbsolute, seatingRelative):
    '''
    inputs: ----------------------------------------------------------
        estimatedScoringBounds = {
            "top": {
                "min": 0,
                "max": 5,
            },
            ...
        }

        biddingRelative = { "top": ['pass', 'one heart', ...], ... }

        biddingAbsolute = an array of arrays representing every bid made thus far (e.g. [ ['Andrew', 'Pass], ['Adam', 'One Club'], ... ])

        seatingRelative = { "top": "TopPlayerName", "bottom": "BottomPlayerName", ... }

    returns: ----------------------------------------------------------
        an obj that has the min and max estimated scores for each relative location e.g. (
            "top": {
                "min": 0,
                "max": 5,
            },
            ...
        )
    '''
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

    for location, playersBids in biddingRelative.items():
        #region Skipping estimation if location is bottom (as that is your hand) or the player in question has made no bids
        numberOfBidsMade = len(biddingRelative[location])
        if numberOfBidsMade < 1 or re.search('bottom', location, re.IGNORECASE):
            continue
        #endregion
        #region Setup
        username = seatingRelative[location]
        partner = seatingRelative[helpers.getLocationAfterRotationsAround(location, 2)]
        print('')
        print('username = {0}'.format(username))

        #Getting the currentContractBid for the user in question
        biddingUpToUsersLastTurn = biddingAbsolute[:helpers.getIndexOfNthBid(username, biddingAbsolute, -1)]
        currentContractBidForUser = helpers.getCurrentContractBidFromBidding(biddingUpToUsersLastTurn)
        print('biddingUpToUsersTurn = {0}'.format(biddingUpToUsersLastTurn))
        print('currentContractBidForUser = {0}'.format(currentContractBidForUser))

        indexOfUsersFirstBid = helpers.getIndexOfNthBid(username, biddingAbsolute, 1)
        hasPartnerOpened = helpers.getHasPartnerOpened(biddingAbsolute, seatingRelative, username)
        firstBid = biddingRelative[location][0]
        secondBid = ''
        lastBid = ''
        if len(biddingRelative[location]) > 1:
            secondBid = biddingRelative[location][1]
            lastBid = biddingRelative[location][-1]

        firstBidIsPass = re.search('pass', firstBid, re.IGNORECASE)
        isTeamsFirstBidOpportunity = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, location)
        isPartnersFirstBidPass = helpers.getIsPartnersFirstBidPass(biddingRelative, seatingRelative, username)

        isFirstBidJumpshift = False
        isLastBidJumpshift = False
        try: 
            isFirstBidJumpshift = helpers.getIsJumpshift(currentContractBidForUser[1], firstBid)
            isLastBidJumpshift = helpers.getIsJumpshift(currentContractBidForUser[1], lastBid)

            #TODO: do we need to check if the user made a bid that is a jumpshift ever and then have entirely separate logic in that case?
            isAnyBidJumpshift = helpers.getHasPlayerJumpshifted(username, playersBids, biddingAbsolute)


        except:
            pass
        #endregion
        #region Debugging (remove when done)
        print('currentContractBid = {0}'.format(currentContractBidForUser))
        # print('players = {0}'.format(biddingAbsolute[indexOfUsersFirstBid][1]))
        print('biddingObjectRelative = {0}'.format(biddingRelative))
        print('firstBid = {0}'.format(firstBid)) 

        print('hasPartnerOpened = {0}'.format(hasPartnerOpened))
        print('isFirstBidJumpShift = {0}'.format(isFirstBidJumpshift))
        print('isLastBidJumpShift = {0}'.format(isLastBidJumpshift))
        print('isTeamsFirstBidOpportunity = {0}'.format(isTeamsFirstBidOpportunity))

        #endregion

        #region Handling Two Clubs Opener Scenario
        hasSomeoneOpenedTwoClubs, personWhoOpenedTwoClubs = helpers.getHasSomeoneOpenedTwoClubs(biddingAbsolute, biddingRelative, seatingRelative);

        if hasSomeoneOpenedTwoClubs:
            print('someone opened two clubs')
            print('personWhoOpenedTwoClubs = {0}'.format(personWhoOpenedTwoClubs))
            print('partner = {0}'.format(partner))

            if partner == personWhoOpenedTwoClubs:
                print('partner opened')
                if not re.search('pass', firstBid, re.IGNORECASE):
                    indexOfTwoClubBid = biddingAbsolute.index([partner, 'Two Club'])
                    contractAtThisPoint = helpers.getCurrentContractBidFromBidding(biddingAbsolute[:indexOfTwoClubBid + 2])
                    numberOfBidsAbove = helpers.getIndexDifferenceOfBids(contractAtThisPoint, firstBid)

                    if numberOfBidsAbove == 1:
                        minToUse = 0
                    else:
                        minToUse = (numberOfBidsAbove - 1) * 3 + 1

                    maxToUse = numberOfBidsAbove * 3
                
                else: 
                    print('first bid pass')
                    if hasPartnerOpened:
                        minToUse = values['partnerBidsFirst']['playerPasses']['min']
                        maxToUse = values['partnerBidsFirst']['playerPasses']['max']
                    else:
                        minToUse = values['isTeamsFirstBid']['playerPasses']['min']
                        maxToUse = values['isTeamsFirstBid']['playerPasses']['max']

            else:
                if len(biddingRelative[location]) == 1 or username == personWhoOpenedTwoClubs:
                    print('is person who opened or length greater than 1')
                    print(f"firstBid = {firstBid}")
                    minToUse, maxToUse = setInitialBounds(username, location, biddingAbsolute, biddingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, True)

                else:
                    print('more than 1 bid and not user who opened')
                    usersFirstContractBid = helpers.getUsersFirstContractBid(username, biddingAbsolute)
                    print(f"usersFirstContractBid = {usersFirstContractBid}")
                    
                    if re.search('pass', firstBid, re.IGNORECASE) and re.search('pass', secondBid, re.IGNORECASE):
                        minToUse = values['isTeamsFirstBid']['playerPasses']['min']
                        maxToUse = values['isTeamsFirstBid']['playerPasses']['max']
                    else:
                        minToUse, maxToUse = setInitialBounds(username, location, biddingAbsolute, biddingRelative, usersFirstContractBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, False)

            estimatedScoring[location]['min'] = minToUse
            estimatedScoring[location]['max'] = maxToUse
        #endregion
        #region Setting Initial Bounds Logic
        elif secondBid == '':

            minToUse = None;
            maxToUse = None;

            if isTeamsFirstBidOpportunity and firstBidIsPass:
                print('one opportunity first bid pass-----------')
                minToUse = values['isTeamsFirstBid']['playerPasses']['min']
                maxToUse = values['isTeamsFirstBid']['playerPasses']['max']
                
            else: 
                print('one opportunity else-----------')
                minToUse, maxToUse = setInitialBounds(username, location, biddingAbsolute, biddingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, False)

            estimatedScoring[location]['min'] = minToUse
            estimatedScoring[location]['max'] = maxToUse
        #endregion
        #region updating bounds using estimatedScoringBounds
        else:
            isSecondBidJumpshift = helpers.getIsJumpshift( currentContractBidForUser, secondBid)
            wasPlayerForcedToBid = helpers.getWasForcedToBid(username, biddingAbsolute, seatingRelative)

            print(f"secondBid = {secondBid}")
            print(f"currentContractBidForUser = {currentContractBidForUser}")
            print(f"isSecondBidJumpshift = {isSecondBidJumpshift}")
            print(f"wasPlayerForcedToBid = {wasPlayerForcedToBid}")
            #region when the opportunities to bid is two long
            if len(playersBids) == 2: 
                #region when the first bid is pass and 2nd bid is not pass or double

                #nothing more can be gleamed from second bid if they were forced to bid due to takeout double
                if wasPlayerForcedToBid: 
                    estimatedScoring[location]['min'] = estimatedScoringBounds[location]['min']
                    estimatedScoring[location]['max'] = estimatedScoringBounds[location]['max']
                    continue

                if hasPartnerOpened: 
                    print('partner has opened')
                    if firstBidIsPass:
                        if not re.search('pass' , secondBid, re.IGNORECASE) and not re.search('double' , secondBid, re.IGNORECASE):
                            print('partner open, first bid pass')
                            if isSecondBidJumpshift:
                                print('second bid is jumpshift')
                                estimatedScoring[location]['min'] = values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['min']
                                estimatedScoring[location]['max'] = values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['max']
                            else:
                                print('second bid is not jumpshift')
                                didPlayerHaveFirstBidOpportunity = helpers.getUsernameOfPlayerWhoHadFirstOpportunityToBid(biddingAbsolute, username, partner) == username
                                
                                if didPlayerHaveFirstBidOpportunity:
                                    estimatedScoring[location]['max'] =values['isTeamsFirstBid']['playerPasses']['max']
                                else:
                                    estimatedScoring[location]['max'] = values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['max']
                                estimatedScoring[location]['min'] = values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min']
                            continue
                        else:
                            print('else clause')
                            print(f"isPartnersFirstBidPass = {isPartnersFirstBidPass}")
                            if isPartnersFirstBidPass:
                                partnersLocation = helpers.getPartnersLocation(username, seatingRelative)
                                partnersSecondBid = None

                                try:
                                    partnersSecondBid = biddingRelative[partnersLocation][1]
                                except:
                                    pass

                                partnersSecondBidIsGameBid = helpers.getIsBidGameBid(partnersSecondBid)
                                print(f"partnersSecondBidIsGameBid = {partnersSecondBidIsGameBid}")

                                if partnersSecondBidIsGameBid:
                                    estimatedScoring[location]['min'] = values['partnerPassesFirst']['playerPasses']['min']
                                    estimatedScoring[location]['max'] = values['partnerPassesFirst']['playerPasses']['max']
                                else:
                                    currentContractBidForPartner = helpers.getPartnersCurrentContractBidFromBidding(username, biddingAbsolute, seatingRelative)

                                    isPartnersSecondBidJumpshift = helpers.getIsJumpshift(currentContractBidForPartner, partnersSecondBid)

                                    print(f"partnersSecondBid = {partnersSecondBid}")
                                    print(f"currentContractBidForPartner = {currentContractBidForPartner}")
                                    print(f"isPartnersSecondBidJumpshift = {isPartnersSecondBidJumpshift}")

                                    if isPartnersSecondBidJumpshift:
                                        estimatedScoring[location]['min'] = values['partnerPassesFirst']['playerPasses']['min']
                                        estimatedScoring[location]['max'] = values['partnerPassesFirst']['playerPasses']['max']
                                    else:
                                        estimatedScoring[location]['min'] = values['partnerPassesFirst']['playerPasses']['min']
                                        estimatedScoring[location]['max'] = values['partnerBidsFirst']['playerPasses']['max']
                            else:
                                estimatedScoring[location]['min'] = values['partnerBidsFirst']['playerPasses']['min']
                                estimatedScoring[location]['max'] = values['partnerBidsFirst']['playerPasses']['max']
                            continue

                    else:
                        print('first bid is not pass')
                        estimatedScoring[location]['min'] = estimatedScoringBounds[location]['min']
                        estimatedScoring[location]['max'] = estimatedScoringBounds[location]['max']
                        continue
                else:
                    print('partner has not opened')

                    if firstBidIsPass:
                        print('first bid is pass')
                        if not re.search('pass' , secondBid, re.IGNORECASE) and not re.search('double' , secondBid, re.IGNORECASE):
                            print('second bid is not pass')
                            if isSecondBidJumpshift:
                                estimatedScoring[location]['min'] = values['passFirstBidSecond']['isJumpshift']['partnerHasNotOpened']['min']
                                estimatedScoring[location]['max'] = values['passFirstBidSecond']['isJumpshift']['partnerHasNotOpened']['max']
                            else:
                                estimatedScoring[location]['min'] = values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min']
                                estimatedScoring[location]['max'] = values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['max']
                            continue
                        else:
                            print('second bid is pass')
                            didPlayerHaveFirstBidOpportunity = helpers.getUsernameOfPlayerWhoHadFirstOpportunityToBid(biddingAbsolute, username, partner) == username

                            if not didPlayerHaveFirstBidOpportunity:
                                estimatedScoring[location]['min'] = values['partnerPassesFirst']['playerPasses']['min']
                                estimatedScoring[location]['max'] = values['partnerPassesFirst']['playerPasses']['max']
                            else:
                                estimatedScoring[location]['min'] = values['isTeamsFirstBid']['playerPasses']['min']
                                estimatedScoring[location]['max'] = values['isTeamsFirstBid']['playerPasses']['max']
                            continue

                    else:
                        print('first bid is not pass')
                        estimatedScoring[location]['min'] = estimatedScoringBounds[location]['min']
                        estimatedScoring[location]['max'] = estimatedScoringBounds[location]['max']
                        continue
                #endregion
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

def setInitialBounds(username, location, biddingAbsolute, biddingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, hasOtherTeamOpenedTwoClubs = False):
    '''
    inputs--------------------------------------------------:
        location = a string representing relative locations: ('right', 'left',...)
        biddingRelative = { "top": ['pass', 'one heart', ...], ... }
        firstBid = a string representing the users first bid ('One Club', 'Pass', etc... )
        isFirstBidJumpshift = boolean
        hasPartnerOpened = boolean
        isPartnersFirstBidPass = boolean
        hasOtherTeamOpenedTwoClubs = boolean
    returns--------------------------------------------------:
        a min and max value to use e.g. [ minToUse, maxToUse ]
    '''
    IsUsernamesFirstContractBidTheFirstContractBid = helpers.getIsUsernamesFirstContractBidTheFirstContractBid(username, biddingAbsolute)

    print(f"IsUsernamesFirstContractBidTheFirstContractBid = {IsUsernamesFirstContractBidTheFirstContractBid}")
    print('setInitialBounds-----------------')
    # print('biddingRelative["right"][0] = {0}'.format(biddingRelative['right'][0]))
    # print('haveOpponentsNotHadTurnOrPassed = {0}'.format(haveOpponentsNotHadTurnOrPassed))
    # print('re:'.format(re.search('Pass' , biddingRelative['right'][0], re.IGNORECASE)))
            
    if re.search('trump', firstBid, re.IGNORECASE):
        #partner = []
        #player =['One NT']
        print('trump branch')
        print('isFirstBidJumpshift = {0}'.format(isFirstBidJumpshift))
        if hasOtherTeamOpenedTwoClubs:
            minToUse = values['special']['wtf']['min']
            maxToUse = values['special']['wtf']['max']
        elif isFirstBidJumpshift:
            minToUse = values['partnerBidsFirst']['playerBidsNoTrump']['isJumpshift']['min']
            maxToUse = values['partnerBidsFirst']['playerBidsNoTrump']['isJumpshift']['max']
        else:
            if hasPartnerOpened:
                minToUse = values['partnerBidsFirst']['playerBidsNoTrump']['isNotJumpshift']['min']
                maxToUse = values['partnerBidsFirst']['playerBidsNoTrump']['isNotJumpshift']['max']
            else:
                minToUse = values['isTeamsFirstBid']['playerBidsNoTrump']['min']
                maxToUse = values['isTeamsFirstBid']['playerBidsNoTrump']['max']

    elif re.search('two club', firstBid, re.IGNORECASE) and IsUsernamesFirstContractBidTheFirstContractBid:
        #partner = []
        #player =['Two Club']
        print('two club branch')
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
        print('two branch')
        print(f"hasOtherTeamOpenedTwoClubs = {hasOtherTeamOpenedTwoClubs}")
        if hasOtherTeamOpenedTwoClubs:
            minToUse = values['special']['weakTwo']['min']
            maxToUse = values['isTeamsFirstBid']['playerBidsSuit']['max']
        else: 
            wasFirstOpeningBidANthLevelBid = helpers.getWasFirstOpeningBidANthLevelBid(biddingAbsolute, 2)

            if wasFirstOpeningBidANthLevelBid != False and  wasFirstOpeningBidANthLevelBid != username:
                minToUse = values['special']['weakTwo']['min']
                maxToUse = values['partnerPassesFirst']['playerBidsSuit']['max']
            else:
                minToUse = values['special']['weakTwo']['min']
                maxToUse = values['special']['weakTwo']['max']

    elif re.search('three', firstBid, re.IGNORECASE):
        #partner = []
        #player =['Three Club']
        print('three branch')
        if hasOtherTeamOpenedTwoClubs:
            minToUse = values['special']['wtf']['min']
            maxToUse = values['special']['wtf']['max']
        else:
            wasFirstOpeningBidANthLevelBid = helpers.getWasFirstOpeningBidANthLevelBid(biddingAbsolute, 3)

            if wasFirstOpeningBidANthLevelBid != False and  wasFirstOpeningBidANthLevelBid != username:
                maxToUse = values['partnerPassesFirst']['playerBidsSuit']['max']
            else:
                maxToUse = values['special']['weakThree']['max']

            minToUse = values['special']['weakThree']['min']

    elif re.search('pass', firstBid, re.IGNORECASE):
        print('pass branch')
        print(f"hasPartnerOpened = {hasPartnerOpened}")
        print(f"hasOtherTeamOpenedTwoClubs = {hasOtherTeamOpenedTwoClubs}")
        if hasPartnerOpened:
            if hasOtherTeamOpenedTwoClubs:
                minToUse = values['isTeamsFirstBid']['playerPasses']['min']
                maxToUse = values['isTeamsFirstBid']['playerPasses']['max']
            else:
                minToUse = values['partnerBidsFirst']['playerPasses']['min']
                maxToUse = values['partnerBidsFirst']['playerPasses']['max']
        else: 
            minToUse = values['isTeamsFirstBid']['playerPasses']['min']
            maxToUse = values['isTeamsFirstBid']['playerPasses']['max']

    else:
        print('else branch')
        #partner = []
        #player =['One Club']
        if hasOtherTeamOpenedTwoClubs:
            minToUse = values['special']['wtf']['min']
            maxToUse = values['special']['wtf']['max']
        elif hasPartnerOpened:
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
