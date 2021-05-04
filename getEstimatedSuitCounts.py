import helpers, re, autoBid

class EstimateSuitCounts: 
    '''
    assumptions:

    opening in no trump means no voids and no more than 5 in any suit?
    responding NT means same thing as opening NT?

    responding to your partner's opening suit with same suit means you have at least 3 of that suit?
    responding twice in a row to your partners's opening suit means you have at least 4 of that suit?

    opening weakTwo means at least 6
    opening weakThree means at least 7

    if a player opens a suit then says the same suit again do they likely have 1-2 more of that suit than would be assumed otherwise (5-6 for minors and 6-7 for majors?)
    responding twice with the same suit means you have at least one more than the minimum required to say that suit?  if three times in a row, at least 2 more?  does it have to be right after one another?

    does a jumpshift ever definitely mean more of a suit?
    '''

    def __init__(self, biddingRelative, biddingAbsolute, seatingRelative):
        self.biddingRelative = biddingRelative
        self.biddingAbsolute = biddingAbsolute
        self.seatingRelative = seatingRelative
        self.defaultValue = 3.25
        self.suits = {
            'clubs': 'clubs',
            'diamonds': 'diamonds',
            'hearts': 'hearts',
            'spades': 'spades'
        }
        self.suitCounts = {
            "top": {
                self.suits["clubs"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
                self.suits["diamonds"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
                self.suits["hearts"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
                self.suits["spades"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
            },
            "left": {
                self.suits["clubs"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
                self.suits["diamonds"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
                self.suits["hearts"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
                self.suits["spades"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
            },
            "right": {
                self.suits["clubs"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
                self.suits["diamonds"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
                self.suits["hearts"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
                self.suits["spades"]: {
                    "min": self.defaultValue,
                    "max": self.defaultValue,
                },
            },
        }
        print(f"self = {self}")
        print(f"suitCounts = {self.suitCounts}")

    def getResult(self, num1, num2):
        return num1 * num2
       

        # #NOTE: this is the for loop from getEstimatedPoints (most of this will be deleted)
        # for location, playersBids in biddingRelative.items():
        # #region Skipping estimation if location is bottom (as that is your hand) or the player in question has made no bids
        # numberOfBidsMade = len(biddingRelative[location])
        # if numberOfBidsMade < 1 or re.search('bottom', location, re.IGNORECASE):
        #     continue
        # #endregion
        # #region Setup
        # username = seatingRelative[location]
        # partner = seatingRelative[helpers.getLocationAfterRotationsAround(location, 2)]
        # print('')
        # print('username = {0}'.format(username))

        # #Getting the currentContractBid for the user in question
        # biddingUpToUsersLastTurn = biddingAbsolute[:helpers.getIndexOfNthBid(username, biddingAbsolute, -1)]
        # currentContractBidForUser = helpers.getCurrentContractBidFromBidding(biddingUpToUsersLastTurn)
        # print('biddingUpToUsersTurn = {0}'.format(biddingUpToUsersLastTurn))
        # print('currentContractBidForUser = {0}'.format(currentContractBidForUser))

        # hasPartnerOpened = helpers.getHasPartnerOpened(biddingAbsolute, seatingRelative, username)
        # firstBid = biddingRelative[location][0]
        # secondBid = ''
        # lastBid = ''
        # if len(biddingRelative[location]) > 1:
        #     secondBid = biddingRelative[location][1]
        #     lastBid = biddingRelative[location][-1]

        # firstBidIsPass = re.search('pass', firstBid, re.IGNORECASE)
        # isTeamsFirstBidOpportunity = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, location)
        # isPartnersFirstBidPass = helpers.getIsPartnersFirstBidPass(biddingRelative, seatingRelative, username)

        # isFirstBidJumpshift = False
        # try: 
        #     isFirstBidJumpshift = helpers.getIsJumpshift(currentContractBidForUser, firstBid)

        #     #TODO: do we need to check if the user made a bid that is a jumpshift ever and then have entirely separate logic in that case?
        #     isAnyBidJumpshift = helpers.getHasPlayerJumpshifted(username, playersBids, biddingAbsolute)


        # except:
        #     pass
        
        # hasSomeoneOpenedTwoClubs, personWhoOpenedTwoClubs = helpers.getHasSomeoneOpenedTwoClubs(biddingAbsolute, biddingRelative, seatingRelative);
        # #endregion
        # #region Debugging (remove when done)
        # print('currentContractBid = {0}'.format(currentContractBidForUser))
        # # print('players = {0}'.format(biddingAbsolute[indexOfUsersFirstBid]))
        # print('biddingObjectRelative = {0}'.format(biddingRelative))
        # print('firstBid = {0}'.format(firstBid)) 

        # print('hasPartnerOpened = {0}'.format(hasPartnerOpened))
        # print('isFirstBidJumpShift = {0}'.format(isFirstBidJumpshift))
        # print('isTeamsFirstBidOpportunity = {0}'.format(isTeamsFirstBidOpportunity))

        # #endregion

        # #region Handling Partner 1NT Scenario One Bid
        # wasPlayerForcedToBid = helpers.getWasForcedToBid(username, biddingAbsolute, seatingRelative)
        # partnersLocation = helpers.getPartnersLocation(username, seatingRelative)
        # hasPartnerOpenedOneNoTrump = helpers.getHasPartnerOpenedNoTrump(location, partnersLocation, biddingRelative, biddingAbsolute, seatingRelative)
        # if hasPartnerOpenedOneNoTrump and secondBid == '':
        #     print('one trump scenario------------------')
        #     print(f"wasPlayerForcedToBid = {wasPlayerForcedToBid}")
        #     if wasPlayerForcedToBid:
        #         if firstBidIsPass:
        #             minToUse = values['partnerBidsFirst']['playerPasses']['min']
        #             maxToUse = values['partnerBidsFirst']['playerPasses']['max']
        #         else: 
        #             minToUse = values['partnerPassesFirst']['playerPasses']['min']
        #             maxToUse = values['partnerPassesFirst']['playerPasses']['max']
        #     else:
        #         minToUse, maxToUse = setInitialBounds(username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, False)
                
        #     estimatedScoring[location]['min'] = minToUse
        #     estimatedScoring[location]['max'] = maxToUse
        #     continue

        # #endregion
        # #region Handling Two Clubs Opener Scenario
        # elif hasSomeoneOpenedTwoClubs:
        #     print('someone opened two clubs')
        #     print('personWhoOpenedTwoClubs = {0}'.format(personWhoOpenedTwoClubs))
        #     print('partner = {0}'.format(partner))

        #     if partner == personWhoOpenedTwoClubs:
        #         print('partner opened')
        #         if not re.search('pass', firstBid, re.IGNORECASE):
        #             indexOfTwoClubBid = biddingAbsolute.index([partner, 'Two Club'])
        #             contractAtThisPoint = helpers.getCurrentContractBidFromBidding(biddingAbsolute[:indexOfTwoClubBid + 2])
        #             numberOfBidsAbove = helpers.getIndexDifferenceOfBids(contractAtThisPoint, firstBid)

        #             if numberOfBidsAbove == 1:
        #                 minToUse = 0
        #             else:
        #                 minToUse = (numberOfBidsAbove - 1) * 3 + 1

        #             maxToUse = numberOfBidsAbove * 3
                
        #         else: 
        #             print('first bid pass')
        #             if hasPartnerOpened:
        #                 minToUse = values['partnerBidsFirst']['playerPasses']['min']
        #                 maxToUse = values['partnerBidsFirst']['playerPasses']['max']
        #             else:
        #                 minToUse = values['isTeamsFirstBid']['playerPasses']['min']
        #                 maxToUse = values['isTeamsFirstBid']['playerPasses']['max']

        #     else:
        #         if len(biddingRelative[location]) == 1 or username == personWhoOpenedTwoClubs:
        #             print('is person who opened or length greater than 1')
        #             print(f"firstBid = {firstBid}")
        #             minToUse, maxToUse = setInitialBounds(username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, True)

        #         else:
        #             print('more than 1 bid and not user who opened')
        #             usersFirstContractBid = helpers.getUsersFirstContractBid(username, biddingAbsolute)
        #             print(f"usersFirstContractBid = {usersFirstContractBid}")
                    
        #             if re.search('pass', firstBid, re.IGNORECASE) and re.search('pass', secondBid, re.IGNORECASE):
        #                 minToUse = values['isTeamsFirstBid']['playerPasses']['min']
        #                 maxToUse = values['isTeamsFirstBid']['playerPasses']['max']
        #             else:
        #                 minToUse, maxToUse = setInitialBounds(username, location, biddingAbsolute, biddingRelative, seatingRelative, usersFirstContractBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, False)

        #     estimatedScoring[location]['min'] = minToUse
        #     estimatedScoring[location]['max'] = maxToUse
        # #endregion
        # #region Setting Initial Bounds Logic
        # elif secondBid == '':

        #     minToUse = None;
        #     maxToUse = None;

        #     if isTeamsFirstBidOpportunity and firstBidIsPass:
        #         print('one opportunity first bid pass-----------')
        #         minToUse = values['isTeamsFirstBid']['playerPasses']['min']
        #         maxToUse = values['isTeamsFirstBid']['playerPasses']['max']
                
        #     else: 
        #         print('one opportunity else-----------')
        #         minToUse, maxToUse = setInitialBounds(username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, False)

        #     estimatedScoring[location]['min'] = minToUse
        #     estimatedScoring[location]['max'] = maxToUse
        # #endregion
        # #region Two or More Bids Made
        # else:
        #     isSecondBidJumpshift = helpers.getIsJumpshift( currentContractBidForUser, secondBid)

        #     print(f"secondBid = {secondBid}")
        #     print(f"currentContractBidForUser = {currentContractBidForUser}")
        #     print(f"isSecondBidJumpshift = {isSecondBidJumpshift}")
        #     print(f"wasPlayerForcedToBid = {wasPlayerForcedToBid}")
        #     #region when the opportunities to bid is two long
        #     if len(playersBids) == 2: 
        #         #region when the first bid is pass and 2nd bid is not pass or double

        #         #nothing more can be gleamed from second bid if they were forced to bid due to takeout double
        #         if wasPlayerForcedToBid: 
        #             minToUse, maxToUse = setInitialBounds(username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, False, True, secondBid, isSecondBidJumpshift)
        #             estimatedScoring[location]['min'] = minToUse
        #             estimatedScoring[location]['max'] = maxToUse
        #             continue

        #         if hasPartnerOpened: 
        #             print('partner has opened')
        #             if firstBidIsPass:
        #                 if not re.search('pass' , secondBid, re.IGNORECASE) and not re.search('double' , secondBid, re.IGNORECASE):
        #                     print('partner open, first bid pass')
        #                     if isSecondBidJumpshift:
        #                         print('second bid is jumpshift')
        #                         estimatedScoring[location]['min'] = values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['min']
        #                         estimatedScoring[location]['max'] = values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['max']
        #                     else:
        #                         print('second bid is not jumpshift')
        #                         didPlayerHaveFirstBidOpportunity = helpers.getUsernameOfPlayerWhoHadFirstOpportunityToBid(biddingAbsolute, username, partner) == username
                                
        #                         if didPlayerHaveFirstBidOpportunity:
        #                             estimatedScoring[location]['max'] =values['isTeamsFirstBid']['playerPasses']['max']
        #                         else:
        #                             estimatedScoring[location]['max'] = values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['max']
        #                         estimatedScoring[location]['min'] = values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min']
        #                     continue
        #                 else:
        #                     print('else clause')
        #                     print(f"isPartnersFirstBidPass = {isPartnersFirstBidPass}")
        #                     if isPartnersFirstBidPass:
        #                         partnersSecondBid = None

        #                         try:
        #                             partnersSecondBid = biddingRelative[partnersLocation][1]
        #                         except:
        #                             pass

        #                         partnersSecondBidIsGameBid = helpers.getIsBidGameBid(partnersSecondBid)
        #                         print(f"partnersSecondBidIsGameBid = {partnersSecondBidIsGameBid}")

        #                         if partnersSecondBidIsGameBid:
        #                             estimatedScoring[location]['min'] = values['partnerPassesFirst']['playerPasses']['min']
        #                             estimatedScoring[location]['max'] = values['partnerPassesFirst']['playerPasses']['max']
        #                         else:
        #                             currentContractBidForPartner = helpers.getPartnersCurrentContractBidFromBidding(username, biddingAbsolute, seatingRelative)

        #                             isPartnersSecondBidJumpshift = helpers.getIsJumpshift(currentContractBidForPartner, partnersSecondBid)

        #                             print(f"partnersSecondBid = {partnersSecondBid}")
        #                             print(f"currentContractBidForPartner = {currentContractBidForPartner}")
        #                             print(f"isPartnersSecondBidJumpshift = {isPartnersSecondBidJumpshift}")

        #                             if isPartnersSecondBidJumpshift:
        #                                 estimatedScoring[location]['min'] = values['partnerPassesFirst']['playerPasses']['min']
        #                                 estimatedScoring[location]['max'] = values['partnerPassesFirst']['playerPasses']['max']
        #                             else:
        #                                 estimatedScoring[location]['min'] = values['partnerPassesFirst']['playerPasses']['min']
        #                                 estimatedScoring[location]['max'] = values['partnerBidsFirst']['playerPasses']['max']
        #                     else:
        #                         estimatedScoring[location]['min'] = values['partnerBidsFirst']['playerPasses']['min']
        #                         estimatedScoring[location]['max'] = values['partnerBidsFirst']['playerPasses']['max']
        #                     continue

        #             else:
        #                 print('first bid is not pass')
                        
        #         else:
        #             print('partner has not opened')

        #             if firstBidIsPass:
        #                 print('first bid is pass')
        #                 if not re.search('pass' , secondBid, re.IGNORECASE) and not re.search('double' , secondBid, re.IGNORECASE):
        #                     print('second bid is not pass')
        #                     if isSecondBidJumpshift:
        #                         estimatedScoring[location]['min'] = values['passFirstBidSecond']['isJumpshift']['partnerHasNotOpened']['min']
        #                         estimatedScoring[location]['max'] = values['passFirstBidSecond']['isJumpshift']['partnerHasNotOpened']['max']
        #                     else:
        #                         estimatedScoring[location]['min'] = values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min']
        #                         estimatedScoring[location]['max'] = values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['max']
        #                     continue
        #                 else:
        #                     print('second bid is pass')
        #                     didPlayerHaveFirstBidOpportunity = helpers.getUsernameOfPlayerWhoHadFirstOpportunityToBid(biddingAbsolute, username, partner) == username

        #                     print(f"didPlayerHaveFirstBidOpportunity = {didPlayerHaveFirstBidOpportunity}")
        #                     if not didPlayerHaveFirstBidOpportunity:
        #                         estimatedScoring[location]['min'] = values['partnerPassesFirst']['playerPasses']['min']
        #                         estimatedScoring[location]['max'] = values['partnerPassesFirst']['playerPasses']['max']
        #                     else:
        #                         if hasPartnerOpened:
        #                             estimatedScoring[location]['min'] = values['partnerBidsFirst']['playerPasses']['min'],
        #                             estimatedScoring[location]['max'] = values['partnerBidsFirst']['playerPasses']['max'],
        #                         else:
        #                             estimatedScoring[location]['min'] = values['isTeamsFirstBid']['playerPasses']['min']
        #                             estimatedScoring[location]['max'] = values['isTeamsFirstBid']['playerPasses']['max']
        #                     continue

        #             else:
        #                 print('first bid is not pass')
                       
        #         #endregion
        #     #endregion

        #     #region When the opportunities to bid is longer than 2
        #     else:
        #         #did they say the same suit multiple times?
        #         #did they pass first then jumpshift?
        #         pass
        #     #endregion

        #     #returning the values that are already present if no other cases hit
            
        #     minToUse, maxToUse = setInitialBounds(username, location, biddingAbsolute, biddingRelative, seatingRelative, firstBid, isFirstBidJumpshift, hasPartnerOpened, isPartnersFirstBidPass, False, wasPlayerForcedToBid, secondBid, isSecondBidJumpshift)
        #     estimatedScoring[location]['min'] = minToUse
        #     estimatedScoring[location]['max'] = maxToUse
        #     continue
        # #endregion


def getEstimatedSuitCounts(biddingRelative = None, biddingAbsolute = None, seatingRelative = None):
    '''
    inputs: ------------------------------ 
        biddingRelative: dictionary where keys are relative positions and values are lists of strings representing that user's bids (in chronological order) 
        biddingAbsolute: list of bids as a list 
        seatingRelative: dictionary where keys are relative positions and values are strings representing user's name
    returns ------------------------------:
         a dictionary representing the current "best guess" of how many of each suit a player has
    '''
    estimateSuitCounts = EstimateSuitCounts(biddingRelative, biddingAbsolute, seatingRelative)

    #TODO: figure out what methods we need to run to get correct suitCounts
    
    return estimateSuitCounts.suitCounts
