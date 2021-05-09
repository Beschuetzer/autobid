import getEstimatedPoints, helpers, unittest
import testCases

#NOTE: ESTIMATED SCORING BOUNDS ARE NOT USED IN THIS VERSION

class getEstimatedPoints_1_Bid_Opportunity(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
        self.actual = None
        self.expected = None

    def tearDown(self) -> None:
        print('')
        print('bids = {0}'.format(self.   bids))
        print('self.actual ={0}'.format   (self.actual))
        print('expected = {0}'.format(self.expected))
        print('')

    def test_set_forced_1NT(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['forcedOneNoTrumpResponse']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        
        self.assertDictEqual(self.actual, self.expected)

    def test_set_not_forced_1NT(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['notForcedOneNoTrumpResponse']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_exit_early(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['exitEarly']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsNoTrump']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerBidsNoTrump']['isNotJumpshift']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['special']['weakTwo']['max'],
            },
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max']
            },
        }
        
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_pass(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['pass']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": None,
                "max": None,
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_pass2(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['pass2']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_NT_1(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['nt1']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max']
            },
            "top": {
               "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_NT_2(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['nt2']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_NT_3(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['nt3']
                
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'] 
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
               
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsNoTrump']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_TwoClub_1(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClub1']
                
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_TwoClub_2(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClub2']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_TwoClub_3(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClub3']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_Double_1(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['double1']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerDoubles']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerDoubles']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_Double_2(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['double2']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerDoubles']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerDoubles']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_Double_3(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['double3']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerDoubles']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerDoubles']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected) 
    
    def test_set_Suit_1(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['suit1']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_Suit_2(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['suit2']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_Suit_3(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['suit3']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_WeakTwo_1(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakTwo1']
      
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['special']['weakTwo']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_WeakTwo_2(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakTwo2']
                
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['special']['weakTwo']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_WeakTwo_3(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakTwo3']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['special']['weakTwo']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_WeakTwo_4(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakTwo4']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['special']['weakTwo']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_WeakTwo_5(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakTwo5']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['special']['weakTwo']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_WeakTwo_6(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakTwo6']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['special']['weakTwo']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_Weak_Three_Bid_1(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakThree1']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['special']['weakThree']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_Weak_Three_Bid_2(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakThree2']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['special']['weakThree']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_Weak_Three_Bid_3(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakThree3']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['special']['weakThree']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_Weak_Three_Bid_4(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakThree4']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['special']['weakThree']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_set_Weak_Three_Bid_5(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['weakThree5']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['special']['weakThree']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)
    
    def test_bottom_is_dealer(self):
        #my assumption that bottom would always have one fewer bids than the others was incorrect as it will be the same if it is bottom's deal:
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['bottomIsDealer']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsNoTrump']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

    def test_bid_same_suit_as_opponent(self):
        #my assumption that bottom would always have one fewer bids than the others was incorrect as it will be the same if it is bottom's deal:
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['bidSameAsOpponent']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsNoTrump']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerBidsNoTrump']['isNotJumpshift']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)


    def test_set_Partner_Opens_Two_Clubs_Two_Diamond_Response(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClubsTwoDiamondResponse']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['oneBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['oneBidAbove']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

    def test_set_Partner_Opens_Two_Clubs_Two_Heart_Response(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClubsTwoHeartResponse']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['twoBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['twoBidAbove']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

    def test_set_Partner_Opens_Two_Clubs_Two_Spade_Response(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClubsSpadeResponse']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['threeBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['threeBidAbove']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

    def test_set_Partner_Opens_Two_Clubs_Two_NT_Response(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClubsTwoNTResponse']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['fourBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['fourBidAbove']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

    def test_set_Partner_Opens_Two_Clubs_Three_Club_Response(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClubsThreeClubResponse']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['fiveBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['fiveBidAbove']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

    def test_set_Partner_Opens_Two_Clubs_Interference_Double(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClubsInterferenceDouble']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerDoubles']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerDoubles']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['fiveBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['fiveBidAbove']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

    def test_set_Partner_Opens_Two_Clubs_Interference_Two_Level_Bid(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClubsInterferenceTwoLevelBid']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['twoBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['twoBidAbove']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

    def test_set_Partner_Opens_Two_Clubs_Interference_Three_Level_Pass_Bid(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClubsInterferenceThreeLevelPassBid']
        
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['special']['wtf']['min'],
                "max": getEstimatedPoints.values['special']['wtf']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

    def test_set_Partner_Opens_Two_Clubs_Interference_Three_Level_Two_Above_Bid(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClubsInterferenceThreeLevelTwoAboveBid']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['special']['wtf']['min'],
                "max": getEstimatedPoints.values['special']['wtf']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['threeBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['threeBidAbove']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

    def test_set_Partner_Opens_Two_Clubs_Interference_Random_Bid(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['twoClubsInterferenceRandomBid']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['special']['wtf']['min'],
                "max": getEstimatedPoints.values['special']['wtf']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(self.actual, self.expected)

class getEstimatedPoints_2_Bid_Opportunities(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
        self.bids = None
        self.actual = None
        self.expected = None

    def tearDown(self) -> None:
        print('bids = {0}'.format(self.bids))
        print('expected = {0}'.format(self.expected))
        print('self.actual ={0}'.format(self.actual))

    def test_update_not_forced_1NT_pass_second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['notForcedOneNoTrumpResponsePassSecond']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        
        self.assertDictEqual(self.actual, self.expected)
    
    def test_update_not_forced_1NT_suit_second_not_jumpshift(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['notForcedOneNoTrumpResponseBidSuitSecondNotJumpshift']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_not_forced_1NT_suit_second_jumpshift(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['notForcedOneNoTrumpResponseBidSuitSecondJumpshift']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['wtf']['min'],
                "max": getEstimatedPoints.values['special']['wtf']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_forced_1NT_pass_second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['forcedOneNoTrumpResponsePassSecond']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_forced_1NT_pass_second_partner_bids(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['forcedOneNoTrumpResponsePassSecondPartnerBids']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_forced_1NT_suit_second_not_jumpshift(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['forcedOneNoTrumpResponseBidSuitSecondNotJumpshift']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_forced_1NT_suit_second_jumpshift(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['forcedOneNoTrumpResponseBidSuitSecondJumpshift']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['wtf']['min'],
                "max": getEstimatedPoints.values['special']['wtf']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_two_club_response_check_issue(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['twoClubIssue']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_One_Spade_first_two_NT_second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['oneSpadeFirstTwoNTSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsNoTrump']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerBidsNoTrump']['isNotJumpshift']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Double_First_Pass_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['doubleFirstPassSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerDoubles']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerDoubles']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Double_First_Bid_Suit_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['doubleFirstBidSuitSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerDoubles']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerDoubles']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_partner_takeout_double_forced_bid(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['partnerTakeoutDoubleForcedBid']

        self.expected = {
            #NOTE: we don't know anything extra here about left because he was forced to bid due to takeout double
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerDoubles']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerDoubles']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_NT_First_Pass_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['ntFirstPassSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_NT_First_Bid_Suit_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['ntFirstBidSuitSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_NT_First_Bid_NT_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['ntFirstNTSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)
    
    def test_update_pass_first_NT_second_responding(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['passFirstNTSecondResponding']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Pass_First_Bid_Suit_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['passFirstBidSuitSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_pass_first_NT_second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['passFirstNTSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Pass_First_Double_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['passFirstDoubleSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Pass_First_Pass_Second_Partner_Opens_First(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['passFirstPassSecondPartnerOpensFirst']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Pass_First_Pass_Second_Partner_Passes_First(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['passFirstPassSecondPartnerPassesFirst']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_WeakTwo_First_Pass_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['weakTwoFirstPassSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['special']['weakTwo']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_WeakTwo_First_Same_Suit_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['weakTwoFirstSameSuitSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['special']['weakTwo']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Weak_Three_First_Pass_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['weakThreeFirstPassSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['special']['weakThree']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Weak_Three_First_Same_Suit_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['weakThreeFirstSameSuitSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                 "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['special']['weakThree']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Has_Opened_Pass_First_Jumpshift_Suit_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['partnerHasOpenedPassFirstJumpshiftSuitSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['min'],
                "max": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsSuit']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Has_Not_Opened_Pass_First_Jumpshift_Suit_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['partnerHasNotOpenedPassFirstJumpshiftSuitSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['wtf']['min'],
                "max": getEstimatedPoints.values['special']['wtf']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Has_Opened_Pass_First_Jumpshift_NT_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['partnerHasOpenedPassFirstJumpshiftNTSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['min'],
                "max": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerBidsNoTrump']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)
    
    def test_update_Partner_Has_Not_Opened_Pass_First_Jumpshift_NT_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['partnerHasNotOpenedPassFirstJumpshiftNTSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasNotOpened']['min'],
                "max": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasNotOpened']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Player_Opens_Then_Jumpshift_Second(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['openFirstJumpshiftPartnersRespondingSuitSecond']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Opens_Two_Clubs_Interference_Two_Level_One_Above_Bid_1(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['partnerOpensTwoClubsInterferenceTwoLevelOneAboveBid1']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['oneBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['oneBidAbove']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Opens_Two_Clubs_Interference_Two_Level_One_Above_Bid_2(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['partnerOpensTwoClubsInterferenceTwoLevelOneAboveBid2']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['oneBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['oneBidAbove']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Opens_Two_Clubs_Interference_Three_Level_One_Above_Bid(self):
        biddingRelative = testCases.biddingRelatives['twoBidOpportunities']['partnerOpensTwoClubsInterferenceThreeLevelOneAboveBid']

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['openTwoClubs']['min'],
                "max": getEstimatedPoints.values['special']['openTwoClubs']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['special']['weakThree']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['respondTwoClubs']['oneBidAbove']['min'],
                "max": getEstimatedPoints.values['special']['respondTwoClubs']['oneBidAbove']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

class getEstimatedPoints_3_Or_More_Bid_Opportunities(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
        self.bids = None
        self.actual = None
        self.expected = None

    def tearDown(self) -> None:
        print('bids = {0}'.format(self.bids))
        print('expected = {0}'.format(self.expected))
        print('self.actual ={0}'.format(self.actual))

    def test_update_Say_Same_Suit_Three_Or_More_Time(self):
        biddingRelative = {
            "left": ['pass', 'pass', 'pass'],
            "top": ['One Club', 'Two Club', 'Three Club'],
            "right": ['Double', 'Two Heart', 'pass'],
            "bottom": ['One Diamond', 'Two Spade'],
        }

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerPassesFirst']['playerDoubles']['min'],
                "max": getEstimatedPoints.values['partnerPassesFirst']['playerDoubles']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_pass_two_bid_pass(self):
        biddingRelative = {
            "right": ['Pass', 'Two Diamond', 'Pass'],
            "bottom": ['One Club', 'Two Heart'],
            "left": ['pass', 'pass'],
            "top": ['One Spade', 'Two Spade'],
        }

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints( biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)










