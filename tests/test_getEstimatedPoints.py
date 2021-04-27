import getEstimatedPoints, helpers, unittest
import testCases

class getEstimatedPoints_1_Bid_Opportunity(unittest.TestCase):
    def setUp(self) -> None:
        self.estimatedScoringBounds = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
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

    def test_set_exit_early(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['exitEarly']

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
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
        self.estimatedScoringBounds = None

    def tearDown(self) -> None:
        print('bids = {0}'.format(self.bids))
        print('estimatedScoringBounds = {0}'.format(self.estimatedScoringBounds))
        print('expected = {0}'.format(self.expected))
        print('self.actual ={0}'.format(self.actual))

    def test_update_One_Spade_first_two_NT_second(self):
        biddingRelative = {
            "right": ['One Spade', 'Two No Trump'],
            "bottom": ['pass'],
            "left": ['One No Trump'],
            "top": ['Two Spade'],
        }

        self.estimatedScoringBounds = {
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

        self.expected = {
            "left": {
                 "min": self.estimatedScoringBounds['left']['min'],
                "max": self.estimatedScoringBounds['left']['max']
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max']
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)


    def test_update_Double_First_Pass_Second(self):
        biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['One Club', 'pass'],
            "right": ['Double', 'pass'],
            "bottom": ['One Diamond'],
        }

        self.estimatedScoringBounds = {
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max']
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Double_First_Bid_Suit_Second(self):
        biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'pass'],
            "right": ['Double', 'Two Club'],
            "bottom": ['One Diamond'],
        }

        self.estimatedScoringBounds = {
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['left']['max']

            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max']
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_partner_takeout_double_forced_bid(self):
        biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'pass'],
            "right": ['Double', 'Two Club'],
            "bottom": ['pass'],
        }

        self.estimatedScoringBounds = {
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

        self.expected = {
            #NOTE: we don't know anything extra here about left because he was forced to bid due to takeout double
            "left": {
                "min": self.estimatedScoringBounds['left']['min'],
                "max": self.estimatedScoringBounds['left']['max']
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max']
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_NT_First_Pass_Second(self):
        biddingRelative = {
            "left": ['pass', 'Two Heart'],
            "top": ['One No Trump', 'pass'],
            "right": ['pass', 'pass'],
            "bottom": ['Two Diamond'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max']
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_NT_First_Bid_Suit_Second(self):
        biddingRelative = {
            "left": ['pass', 'Two Heart'],
            "top": ['One No Trump', 'Two Spade'],
            "right": ['pass', 'Three Heart'],
            "bottom": ['Two Diamond'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_NT_First_Bid_NT_Second(self):
        biddingRelative = {
            "left": ['pass', 'Two Heart'],
            "top": ['One No Trump', 'Two No Trump'],
            "right": ['Pass', 'Three Heart'],
            "bottom": ['Two Diamond'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)
    
    def test_update_pass_first_NT_second_responding(self):
        biddingRelative = {
            "left": ['Pass', 'Two No Trump'],
            "top": ['One Club', 'Pass'],
            "right": ['Pass', 'Three Heart'],
            "bottom": ['Two Diamond'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['max']
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Pass_First_Bid_Suit_Second(self):
        biddingRelative = {
            "left": ['pass', 'Two Heart'],
            "top": ['pass', 'Two Spade'],
            "right": ['Pass', 'Three Heart'],
            "bottom": ['Two Diamond'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPassesFirstOpensSecond']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_pass_first_NT_second(self):
        biddingRelative = {
            "left": ['One Heart', 'pass'],
            "top": ['pass', 'Two No Trump'],
            "right": ['Pass', 'Three Heart'],
            "bottom": ['Two Diamond'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Pass_First_Double_Second(self):
        biddingRelative = {
            "left": ['One Heart', 'pass'],
            "top": ['pass', 'Two No Trump'],
            "right": ['Pass', 'double'],
            "bottom": ['Two Diamond'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],

                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Pass_First_Pass_Second_Partner_Opens_First(self):
        biddingRelative = {
            "left": ['One Heart', 'pass'],
            "top": ['pass', 'Two No Trump'],
            "right": ['Pass', 'pass'],
            "bottom": ['Two Diamond'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Pass_First_Pass_Second_Partner_Passes_First(self):
        biddingRelative = {
            "left": ['Pass', 'pass'],
            "top": ['pass', 'Two No Trump'],
            "right": ['Pass', 'pass'],
            "bottom": ['Two Diamond'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
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

        self.expected = {
            "left": {
                "min": self.estimatedScoringBounds['left']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_WeakTwo_First_Pass_Second(self):
        biddingRelative = {
            "left": ['Pass', 'Two No Trump'],
            "top": ['Two Diamond', 'pass'],
            "right": ['Two Heart', 'pass'],
            "bottom": ['Two Spade'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_WeakTwo_First_Same_Suit_Second(self):
        biddingRelative = {
            "left": ['Pass', 'Two No Trump'],
            "top": ['Two Diamond', 'Three Diamond'],
            "right": ['Two Heart', 'pass'],
            "bottom": ['pass'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakTwo']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Weak_Three_First_Pass_Second(self):
        biddingRelative = {
            "left": ['Pass', 'Three No Trump'],
            "top": ['Three Diamond', 'pass'],
            "right": ['Three Heart', 'pass'],
            "bottom": ['Three Spade'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Weak_Three_First_Same_Suit_Second(self):
        biddingRelative = {
            "left": ['Pass', 'Three No Trump'],
            "top": ['Three Diamond', 'Four Diamond'],
            "right": ['Three Heart', 'pass'],
            "bottom": ['Three Spade'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsSuit']['isNotJumpshift']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Has_Opened_Pass_First_Jumpshift_Suit_Second(self):
        biddingRelative = {
            "left": ['Pass', 'Three Heart'],
            "top": ['One Club', 'Pass'],
            "right": ['One Heart', 'pass'],
            "bottom": ['One Spade'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['min'],
                "max": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Has_Not_Opened_Pass_First_Jumpshift_Suit_Second(self):
        biddingRelative = {
            "left": ['Pass', 'Three Heart'],
            "top": ['One Club', 'Pass'],
            "right": ['Pass', 'pass'],
            "bottom": ['One Spade'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['special']['wtf']['min'],
                "max": getEstimatedPoints.values['special']['wtf']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Has_Opened_Pass_First_Jumpshift_NT_Second(self):
        biddingRelative = {
            "left": ['Pass', 'Three No Trump'],
            "top": ['One Club', 'Pass'],
            "right": ['One No Trump', 'pass'],
            "bottom": ['One Spade'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['min'],
                "max": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasOpened']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)
    
    def test_update_Partner_Has_Not_Opened_Pass_First_Jumpshift_NT_Second(self):
        biddingRelative = {
            "left": ['Pass', 'Three No Trump'],
            "top": ['One Club', 'Pass'],
            "right": ['Pass', 'pass'],
            "bottom": ['One Spade'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasNotOpened']['min'],
                "max": getEstimatedPoints.values['passFirstBidSecond']['isJumpshift']['partnerHasNotOpened']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Player_Opens_Then_Jumpshift_Second(self):
        biddingRelative = {
            "left": ['One No Trump', 'Four Spade'],
            "top": ['pass', 'Pass'],
            "right": ['Two Spade', 'pass'],
            "bottom": ['pass'],
        }

        self.estimatedScoringBounds = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max'],
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Opens_Two_Clubs_Interference_Two_Level_One_Above_Bid_1(self):
        biddingRelative = {
            "left": ['Two Club','Two Spade'],
            "top": ['pass', 'pass'],
            "right": ['Two Diamond', 'Three No Trump'],
            "bottom": ['Two Heart'],
        }

        self.estimatedScoringBounds = {
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

        self.expected = {
            "left": {
                "min": self.estimatedScoringBounds['left']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Opens_Two_Clubs_Interference_Two_Level_One_Above_Bid_2(self):
        biddingRelative = {
            "left": ['Two Club','Three Club'],
            "top": ['Two Heart', 'pass'],
            "right": ['Two Spade', 'Three Spade'],
            "bottom": ['pass'],
        }

        self.estimatedScoringBounds = {
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

        self.expected = {
            "left": {
                "min": self.estimatedScoringBounds['left']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max'],
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
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

    def test_update_Partner_Opens_Two_Clubs_Interference_Three_Level_One_Above_Bid(self):
        biddingRelative = {
            "left": ['Two Club','Two Spade'],
            "top": ['pass', 'Three Heart'],
            "right": ['Two Diamond', 'Three No Trump'],
            "bottom": ['pass'],
        }

        self.estimatedScoringBounds = {
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

        self.expected = {
            "left": {
                "min": self.estimatedScoringBounds['left']['min'],
                "max": self.estimatedScoringBounds['left']['max'],
            },
            "top": {
                "min": getEstimatedPoints.values['special']['weakThree']['min'],
                "max": getEstimatedPoints.values['special']['weakThree']['max'],
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max'],
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)

class getEstimatedPoints_3_Or_More_Bid_Opportunities(unittest.TestCase):
  #TODO: add tests for more than two bid opportunity cases...
  #Can just rely on the TwoBidOpportunity evaluations unless there are certain behaviors like bidding the same suit every time or jumpshifts?
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
        self.estimatedScoringBounds = None

    def tearDown(self) -> None:
        print('bids = {0}'.format(self.bids))
        print('estimatedScoringBounds = {0}'.format(self.estimatedScoringBounds))
        print('expected = {0}'.format(self.expected))
        print('self.actual ={0}'.format(self.actual))

    #NOTE: the test below is not finished.  can you think of any other cases where the third bid would change our estimated points?
    def test_update_Say_Same_Suit_Three_Or_More_Time(self):
        biddingRelative = {
            "left": ['pass', 'pass', 'pass'],
            "top": ['One Club', 'Two Club', 'Three Club'],
            "right": ['Double', 'Two Heart', 'pass'],
            "bottom": ['One Diamond', 'Two Spade'],
        }

        self.estimatedScoringBounds = {
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

        self.expected = {
            "left": {
                "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
                "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max'],
            },
            "top": {
                "min": self.estimatedScoringBounds['top']['min'],
                "max": self.estimatedScoringBounds['top']['max']
            },
            "right": {
                "min": self.estimatedScoringBounds['right']['min'],
                "max": self.estimatedScoringBounds['right']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)

        self.actual =getEstimatedPoints.getEstimatedPoints(self.estimatedScoringBounds, biddingRelative, self.bids, self.seatingRelative)
        
        self.assertDictEqual(self.actual, self.expected)











