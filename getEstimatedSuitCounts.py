import helpers, re, autoBid

class EstimateSuitCounts: 
    '''
    assumptions:

    opening majors = 5
    opening minors = 4
    opening in no trump means no voids and probably no singleton and no more than 7 in any suit?
    responding NT means same thing as opening NT?

    responding to your partner's opening suit with same suit means you have at least 3 of that suit?

    opening weakTwo means at least 6
    opening weakThree means at least 7

    
    NOTE: Are the bottom two useful for playing phase when someone can no longer follow suit in the suit that someone said two or more time?
    if a player opens a suit then says the same suit again do they likely have 1-2 more of that suit than would be assumed otherwise (5-6 for minors and 6-7 for majorsminDefaultValue)
    
    responding twice with the same suit means you have at least one more than the minimum required to say that suit?  if three times minDefaultValue a row, at least 2 more?  does it have to be right after one another?

    does a jumpshift ever definitely mean more of a suit?
    '''

    def __init__(self, biddingRelative, biddingAbsolute, seatingRelative):
        self.biddingRelative = biddingRelative
        self.biddingAbsolute = self.biddingAbsolute
        self.seatingRelative = self.seatingRelative
        self.expectedValue = 3.25
        self.minDefaultValue = 0
        self.suits = {
            'clubs': 'clubs',
            'diamonds': 'diamonds',
            'hearts': 'hearts',
            'spades': 'spades'
        }
        self.suitCounts = {
            "top": {
                self.suits["clubs"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
                self.suits["diamonds"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
                self.suits["hearts"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
                self.suits["spades"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
            },
            "left": {
                self.suits["clubs"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
                self.suits["diamonds"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
                self.suits["hearts"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
                self.suits["spades"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
            },
            "right": {
                self.suits["clubs"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
                self.suits["diamonds"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
                self.suits["hearts"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
                self.suits["spades"]: {
                    "min": self.minDefaultValue,
                    "expected": self.expectedValue,
                },
            },
        }
        print(f"self = {self}")
        print(f"suitCounts = {self.suitCounts}")

    def getResult(self, num1, num2):
        return num1 * num2
       

    def start(self):
        # #NOTE: this is the for loop from getEstimatedPoints (most of this will be deleted)
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
        if self.hasPartnerOpenedOneNoTrump and self.secondBid == '':
           
            continue

        #endregion
        #region Handling Two Clubs Opener Scenario
        elif self.hasSomeoneOpenedTwoClubs:
            pass
        #endregion
        #region Setting Initial Bounds Logic
        elif self.secondBid == '':
            pass
            
        #endregion
        #region Two or More Bids Made
        else:
            continue
        # #endregion


def getEstimatedSuitCounts(biddingRelative = None, self.biddingAbsolute = None, self.seatingRelative = None):
    '''
    inputs: ------------------------------ 
        biddingRelative: dictionary where keys are relative positions and values are lists of strings representing that user's bids (in chronological order) 
        self.biddingAbsolute: list of bids as a list 
        self.seatingRelative: dictionary where keys are relative positions and values are strings representing user's name
    returns ------------------------------:
         a dictionary representing the current "best guess" of how many of each suit a player has
    '''
    estimateSuitCounts = EstimateSuitCounts(biddingRelative, self.biddingAbsolute, self.seatingRelative)

    #TODO: figure out what methods we need to run to get correct suitCounts
    
    return estimateSuitCounts.suitCounts
