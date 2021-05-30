import helpers, re, autoBid

suits = {
    'clubs': 'clubs',
    'diamonds': 'diamonds',
    'hearts': 'hearts',
    'spades': 'spades',
}
expectedValue = 3.25
minDefaultValue = 0

openMinorMinValue = 4
openMajorMinValue = 5
openNoTrumpMinValue = 2
openWeakTwoMinValue = 6
openWeakThreeMinValue = 7
respondingMinValue = 3

#NOTE: when takeout dbl or 2 club responding
forcedResponseMinValue = 3


class EstimateSuitCounts: 
    '''
    inputs: ------------------------------ 
        biddingRelative: dictionary where keys are relative positions and values are lists of strings representing that user's bids (in chronological order) 
        self.biddingAbsolute: list of bids as a list 
        self.seatingRelative: dictionary where keys are relative positions and values are strings representing user's name
    returns ------------------------------:
         a dictionary representing the current "best guess" of how many of each suit a player has
    
    NOTE: Are the bottom two useful for playing phase when someone can no longer follow suit in the suit that someone said two or more time?
    if a player opens a suit then says the same suit again do they likely have 1-2 more of that suit than would be assumed otherwise (5-6 for minors and 6-7 majorsminDefaultValue)
    
    responding twice with the same suit means you have at least one more than the minimum required to say that suit?  if three minDefaultValue a row, at least 2 more?  does it have to be right after one another?

    does a jumpshift ever definitely mean more of a suit?
    '''
    def __init__(self, biddingRelative, biddingAbsolute, seatingRelative):
        self.biddingRelative = biddingRelative
        self.biddingAbsolute = biddingAbsolute
        self.seatingRelative = seatingRelative
        self.suitCounts = {
            "left": {
                suits["clubs"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
                suits["diamonds"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
                suits["hearts"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
                suits["spades"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
            },
            "top": {
                suits["clubs"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
                suits["diamonds"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
                suits["hearts"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
                suits["spades"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
            },
            "right": {
                suits["clubs"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
                suits["diamonds"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
                suits["hearts"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
                suits["spades"]: {
                    "min": minDefaultValue,
                    "expected": expectedValue,
                },
            },
        }
        self.start()

    def start(self):
        for location, playersBids in self.biddingRelative.items():
        #region Skipping estimation if location is bottom (as that is your hand) or the player in question has made no bids
            self.numberOfBidsMade = len(self.biddingRelative[location])
            if self.numberOfBidsMade < 1 or re.search('bottom', location, re.IGNORECASE):
                continue
            #endregion
            #region Setup
            
            self.username = self.seatingRelative[location]
            self.partner = self.seatingRelative[helpers.getLocationAfterRotationsAround(location, 2)]
            print('')
            print('username = {0}'.format(self.username))

            #Getting the currentContractBid for the user in question
            self.biddingUpToUsersLastTurn = self.biddingAbsolute[:helpers.getIndexOfNthBid(self.username, self.biddingAbsolute, -1)]
            self.currentContractBidForUser = helpers.getCurrentContractBidFromBidding(self.biddingUpToUsersLastTurn)
            print('biddingUpToUsersTurn = {0}'.format(self.biddingUpToUsersLastTurn))
            print('currentContractBidForUser = {0}'.format(self.currentContractBidForUser))

            self.hasPartnerOpened = helpers.getHasPartnerOpened(self.biddingAbsolute, self.seatingRelative, self.username)
            self.firstBid = self.biddingRelative[location][0]
            self.secondBid = ''
            if len(self.biddingRelative[location]) > 1:
                self.secondBid = self.biddingRelative[location][1]

            self.isFirstBidMinor = helpers.getIsMinor(self.firstBid)
            self.isFirstBidMajor = helpers.getIsMajor(self.firstBid)
            self.firstBidIsPass = re.search('pass', self.firstBid, re.IGNORECASE)
            self.isTeamsFirstBidOpportunity = helpers.getIsTeamsFirstBidOpportunity(self.biddingRelative, location)
            self.isPartnersFirstBidPass = helpers.getIsPartnersFirstBidPass(self.biddingRelative, self.seatingRelative, self.username)

            self.isFirstBidJumpshift = False
            try: 
                self.isFirstBidJumpshift = helpers.getIsJumpshift(self.currentContractBidForUser, self.firstBid)

                #TODO: do we need to check if the user made a bid that is a jumpshift ever and then have entirely separate logic in that case?
                self.isAnyBidJumpshift = helpers.getHasPlayerJumpshifted(self.username, playersBids, self.biddingAbsolute)


            except:
                pass
            
            self.currentActualBidWhenUserBid = helpers.getCurrentContractBidFromBidding(self.biddingUpToUsersLastTurn)
            self.hasSomeoneOpenedTwoClubs, self.personWhoOpenedTwoClubs = helpers.getHasSomeoneOpenedTwoClubs(self.biddingAbsolute, self.biddingRelative, self.seatingRelative);
            #endregion
            #region Debugging (remove when done)
            print('currentContractBid = {0}'.format(self.currentContractBidForUser))
            # print('players = {0}'.format(biddingAbsolute[indexOfUsersFirstBid]))
            print('biddingObjectRelative = {0}'.format(self.biddingRelative))
            print('firstBid = {0}'.format(self.firstBid)) 

            print('hasPartnerOpened = {0}'.format(self.hasPartnerOpened))
            print('isFirstBidJumpShift = {0}'.format(self.isFirstBidJumpshift))
            print('isTeamsFirstBidOpportunity = {0}'.format(self.isTeamsFirstBidOpportunity))

            #endregion

            #region Handling Partner 1NT Scenario One Bid
            self.wasPlayerForcedToBid = helpers.getWasForcedToBid(self.username, self.biddingAbsolute, self.seatingRelative)
            self.partnersLocation = helpers.getPartnersLocation(self.username, self.seatingRelative)
            self.hasPartnerOpenedOneNoTrump = helpers.getHasPartnerOpenedNoTrump(location, self.partnersLocation, self.biddingRelative, self.biddingAbsolute, self.seatingRelative)

            # if self.wasPlayerForcedToBid
            # if getIsMinor(firstBid):
           
            self.suitOfBid = helpers.getSuitFromBid(self.firstBid)
            self.suitKey = self.convertSuitOfBidToKey()

            print(f"self.wasPlayerForcedToBid = {self.wasPlayerForcedToBid}")
            print(f"self.wasPlayerForcedToBid = {self.wasPlayerForcedToBid}")
            print(f"self.currentActualBid = {self.currentActualBidWhenUserBid}")

            if self.suitKey is None: continue

            if self.wasPlayerForcedToBid  :
                self.suitCounts[location][self.suitKey]['min'] = forcedResponseMinValue

            elif re.search('trump', self.firstBid, re.IGNORECASE):
                self.suitCounts[location][suits['clubs']]['min'] = openNoTrumpMinValue
                self.suitCounts[location][suits['diamonds']]['min'] = openNoTrumpMinValue
                self.suitCounts[location][suits['hearts']]['min'] = openNoTrumpMinValue
                self.suitCounts[location][suits['spades']]['min'] = openNoTrumpMinValue

            elif re.search('two', self.firstBid, re.IGNORECASE) and (self.isFirstBidJumpshift or self.currentActualBidWhenUserBid == None):
                self.suitCounts[location][self.suitKey]['min'] = openWeakTwoMinValue

            elif re.search('three', self.firstBid, re.IGNORECASE):
                self.suitCounts[location][self.suitKey]['min'] = openWeakThreeMinValue

            elif self.isFirstBidMinor :
                self.suitCounts[location][self.suitKey]['min'] = openMinorMinValue
            
            elif self.isFirstBidMajor:
                self.suitCounts[location][self.suitKey]['min'] = openMajorMinValue

            elif self.hasPartnerOpenedOneNoTrump and self.secondBid == '':
                continue

            #endregion
            #region Handling Two Clubs Opener Scenario
            elif self.hasSomeoneOpenedTwoClubs:
                pass
            #endregion
    
    def convertSuitOfBidToKey(self):
        # 'Heart' => 'hearts'
        print(f"self.suitOfBid = {self.suitOfBid}")
        try:
            return self.suitOfBid.lower() + 's'
        except:
            return None
        

    
    


