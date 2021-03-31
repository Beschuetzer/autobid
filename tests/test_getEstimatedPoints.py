import getEstimatedPoints, unittest

class getEstimatedPointsOneBidOpportunity(unittest.TestCase):
    def setUp(self) -> None:
        self.currentEstimatedPoints = {
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
    def tearDown(self) -> None:
      print('actual = {0}'.format(self.actual))

    #region old test cases
    # def test_no_bids(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "right": [],
    #         "left": [],
    #         "bottom": [],
    #         "top": [],
    #     }
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,[], "")
    #     expected = {
    #         "top": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "right": {
    #             "min": None,
    #             "max": None,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_pass_first_no_second(self):
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "right": ['Pass'],
    #         "left": [],
    #         "bottom": [],
    #         "top": [],
    #     }
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,[], seatingRelative,'')
    #     expected = {
    #         "top": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.values['is'],
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_pass_first_nt_second(self):
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "right": ['Pass', 'One No Trump'],
    #         "left": [],
    #         "bottom": [],
    #         "top": [],
    #     }
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,[], seatingRelative,'')
    #     expected = {
    #         "top": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.PASS_FIRST_NT_SECOND_ROUND_MIN,
    #             "max": getEstimatedPoints.PASS_FIRST_NT_SECOND_ROUND_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_pass_first_double_second(self):
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "right": ['Pass', 'double'],
    #         "left": [],
    #         "bottom": [],
    #         "top": [],
    #     }
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,[], seatingRelative,'')
    #     expected = {
    #         "top": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.PASS_FIRST_DOUBLE_SECOND_ROUND_MIN,
    #             "max": getEstimatedPoints.PASS_FIRST_DOUBLE_SECOND_ROUND_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_pass_first_bid_second(self):
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "right": ['Pass', 'Two Club'],
    #         "left": [],
    #         "bottom": [],
    #         "top": [],
    #     }
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,[], seatingRelative,'')
    #     expected = {
    #         "top": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.PASS_FIRST_BID_SECOND_ROUND_MIN,
    #             "max": getEstimatedPoints.PASS_FIRST_BID_SECOND_ROUND_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_pass_first_jumpshift_second_1(self):
    #     seatingRelative = {
    #         "right": "Andrew",
    #         "bottom": "Adam",
    #         "left": "Ann",
    #         "top": "Tim",
    #     }
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "right": ['Pass', 'Two Diamond'],
    #         "bottom": ['Pass'],
    #         "left": ['One Club'],
    #         "top": ['Pass'],
    #     }
    #     bids = [['Andrew', "Pass"],['Adam', 'Pass'],['Ann', 'One Club'], ['Tim', 'Pass'], ['Andrew', "Two Diamond"]]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative,'')
    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MIN,
    #             "max": getEstimatedPoints.RESPONDING_JUMPSHIFT_PASS_FIRST_ROUND_MAX,
    #         },
    #         "bottom": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN,
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #         "top": {
    #              "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN,
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_pass_first_jumpshift_second_2(self):
    #     seatingRelative = {
    #         "right": "Andrew",
    #         "bottom": "Adam",
    #         "left": "Ann",
    #         "top": "Tim",
    #     }
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "right": ['Pass', 'Two Diamond'],
    #         "bottom": ['Pass'],
    #         "left": ['One Club'],
    #         "top": ['One Diamond'],
    #     }
    #     bids = [['Andrew', "Pass"],['Adam', 'Pass'],['Ann', 'One Club'], ['Tim', 'One Diamond'], ['Andrew', "Two Heart"]]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative,'')
    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.PASS_FIRST_BID_SECOND_ROUND_MIN,
    #             "max": getEstimatedPoints.PASS_FIRST_BID_SECOND_ROUND_MAX,
    #         },
    #         "bottom": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN,
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #         "top": {
    #              "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # #TODO: need to add cases for double second round?
    # def test_ambiguous_WeakTwo_REVISIT(self):
    #     #TODO: what is the max value in this scenario for top?
    #     #TODO: how do we adjust the max given top's next bid?
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "left": ['One No Trump'],
    #         "top": ['Two Diamond'],
    #         "right": ['Pass'],
    #         "bottom": [],
    #     }
    #     seatingRelative = {
    #         "top": "TopPlayer",
    #         "bottom": "BottomPlayer",
    #         "left": "LeftPlayer",
    #         "right": "RightPlayer",
    #     }
    #     bids = [['LeftPlayer', "One No Trump"],['TopPlayer', 'Two Diamond'],['RightPlayer', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)

    #     expected = {
    #         "left": {
    #             "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
    #             "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max']
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.values['special']['weakTwo']['min'],
    #             "max": getEstimatedPoints.values['special']['twoClubs']['max']
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
    #             "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max']
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_ambiguous_WeakTwo_Second_Same_Suit_REVISIT(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "left": ['One No Trump', 'Two No Trump'],
    #         "top": ['Two Diamond', 'Three Diamond'],
    #         "right": ['Pass', 'Pass'],
    #         "bottom": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "top": "TopPlayer",
    #         "bottom": "BottomPlayer",
    #         "left": "LeftPlayer",
    #         "right": "RightPlayer",
    #     }
    #     bids = [['LeftPlayer', "One No Trump"],['TopPlayer', 'Two Diamond'],['RightPlayer', 'Pass'], ['BottomPlayer', "Pass"], ['LeftPlayer', "Two No Trump"],['TopPlayer', 'Three Diamond'],['RightPlayer', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)

    #     expected = {
    #         "left": {
    #             "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
    #             "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max']
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.values['special']['weakTwo']['min'],
    #             "max": getEstimatedPoints.values['special']['twoClubs']['max']
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
    #             "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max']
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_ambiguous_WeakTwo_Second_Different_Suit_REVISIT(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "left": ['One No Trump', 'Two No Trump'],
    #         "top": ['Two Diamond', 'Three Club'],
    #         "right": ['Pass', 'Pass'],
    #         "bottom": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "top": "TopPlayer",
    #         "bottom": "BottomPlayer",
    #         "left": "LeftPlayer",
    #         "right": "RightPlayer",
    #     }
    #     bids = [['LeftPlayer', "One No Trump"],['TopPlayer', 'Two Diamond'],['RightPlayer', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)

    #     expected = {
    #         "left": {
    #             "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
    #             "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max']
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
    #             "max": getEstimatedPoints.values['special']['twoClubs']['max']
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
    #             "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max']
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_ambiguous_WeakTwo_Second__Pass__REVISIT(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "left": ['One No Trump', 'Pass'],
    #         "top": ['Two Diamond', 'Pass'],
    #         "right": ['Two No Trump', 'Three No Trump'],
    #         "bottom": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "top": "TopPlayer",
    #         "bottom": "BottomPlayer",
    #         "left": "LeftPlayer",
    #         "right": "RightPlayer",
    #     }
    #     bids = [['LeftPlayer', "One No Trump"],['TopPlayer', 'Two Diamond'],['RightPlayer', 'Pass'], ['BottomPlayer', "Pass"], ['LeftPlayer', "Two No Trump"],['TopPlayer', 'Pass'],['RightPlayer', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)

    #     expected = {
    #         "left": {
    #             "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['min'],
    #             "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsNoTrump']['max']
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.values['special']['weakTwo']['min'],
    #             "max": getEstimatedPoints.values['special']['weakTwo']['max']
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
    #             "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max']
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_open_Two_Club(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Club'],
    #         "right": ['Pass'],
    #         "bottom": [],
    #         "left": [],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Adam', 'Two Club'],['Ann', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "top": {
    #             "min": getEstimatedPoints.values['special']['twoClubs']['min'],
    #             "max": getEstimatedPoints.values['special']['twoClubs']['max']
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
    #             "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_open_weak_two_unambiguous_1(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Heart'],
    #         "left": [],
    #         "bottom": [],
    #         "right": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Adam', 'Two Heart'],['Ann', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN,
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_open_weak_three_unambiguous_1(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Three Club'],
    #         "left": [],
    #         "bottom": [],
    #         "right": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Adam', 'Three Club'],['Ann', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MAX
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN,
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_open_weak_two_jumpshift(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Heart'],
    #         "left": ['One Club'],
    #         "bottom": [],
    #         "right": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', "One Club"],['Adam', 'Two Heart'],['Ann', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN,
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_open_weak_three_jumpshift(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Three Club'],
    #         "left": ['One No Trump'],
    #         "bottom": [],
    #         "right": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', 'One No Trump'],['Adam', 'Three Club'],['Ann', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MAX
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MAX,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN,
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_open_weak_two_ambiguous_1(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Heart'],
    #         "left": ['One Spade'],
    #         "bottom": [],
    #         "right": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', "One Spade"],['Adam', 'Two Heart'],['Ann', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_TWO_AFTER_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_TWO_AFTER_OPENERS_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN,
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_open_weak_three_ambiguous_2(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Three Heart'],
    #         "left": ['Pass'],
    #         "bottom": [],
    #         "right": ['Three Club'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', "Pass"],['Adam', 'Three Heart'],['Ann', 'Three Club']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.OPENING_WEAK_THREE_AFTER_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_THREE_AFTER_OPENERS_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_THREE_NO_PRIOR_OPENERS_MAX,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_PASSES_MIN,
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)

    # def test_responding_no_jumpshift_suit(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Diamond'],
    #         "left": ['One No Trump'],
    #         "bottom": [],
    #         "right": ['Two Heart'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', "One No Trump"],['Adam', 'Two Diamond'],['Ann', 'Two Heart']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_MIN,
    #             "max": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MAX,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_TWO_AFTER_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_TWO_AFTER_OPENERS_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_responding_no_jumpshift_suit2(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Heart'],
    #         "left": ['One Diamond'],
    #         "bottom": [],
    #         "right": ['Three Club'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', "One Diamond"],['Adam', 'Two Heart'],['Ann', 'Three Club']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_THREE_AFTER_OPENERS_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_responding_no_jumpshift_NT(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Heart'],
    #         "left": ['One Diamond'],
    #         "bottom": [],
    #         "right": ['Two No Trump'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', "One Diamond"],['Adam', 'Two Heart'],['Ann', 'Two No Trump']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_NT_MIN,
    #             "max": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_NT_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    
    # def test_responding_jumpshift_pass(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Diamond'],
    #         "left": ['One No Trump'],
    #         "bottom": [],
    #         "right": ['Two Heart'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', "One No Trump"],['Adam', 'Two Diamond'],['Ann', 'Two Heart']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_MIN,
    #             "max": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MAX,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_TWO_AFTER_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_TWO_AFTER_OPENERS_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)

    # def test_responding_jumpshift_suit2(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Diamond'],
    #         "left": ['One No Trump'],
    #         "bottom": [],
    #         "right": ['Three Heart'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', "One No Trump"],['Adam', 'Two Diamond'],['Ann', 'Three Heart']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_NT_MAX,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_TWO_AFTER_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_TWO_AFTER_OPENERS_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_responding_jumpshift_suit(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Heart'],
    #         "left": ['One Diamond'],
    #         "bottom": [],
    #         "right": ['Three Club'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', "One Diamond"],['Adam', 'Two Heart'],['Ann', 'Three Club']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.OPENING_WEAK_THREE_AFTER_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_THREE_AFTER_OPENERS_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_responding_jumpshift_NT(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "top": ['Two Heart'],
    #         "left": ['One Diamond'],
    #         "bottom": [],
    #         "right": ['Two No Trump'],
    #     }
    #     seatingRelative = {
    #         "top": "Adam",
    #         "bottom": "Tim",
    #         "left": "Andrew",
    #         "right": "Ann",
    #     }
    #     bids = [['Andrew', "One Diamond"],['Adam', 'Two Heart'],['Ann', 'Two No Trump']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative,bids, seatingRelative)
    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_NT_MIN,
    #             "max": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_NT_MAX,
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MIN,
    #             "max": getEstimatedPoints.OPENING_WEAK_TWO_NO_PRIOR_OPENERS_MAX,
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_only_pass_partner_open(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "left": ['One Diamond', 'Three Diamond'],
    #         "top": ['Two Heart', 'Three Heart'],
    #         "right": ['Pass', 'Pass'],
    #         "bottom": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "top": "TopPlayer",
    #         "bottom": "BottomPlayer",
    #         "left": "LeftPlayer",
    #         "right": "RightPlayer",
    #     }
    #     bids = [['LeftPlayer', "One Diamond"],['TopPlayer', 'Two Heart'],['RightPlayer', 'Pass'], ['BottomPlayer', 'Pass'], ['LeftPlayer', "Three Diamond"],['TopPlayer', 'Three Heart'],['RightPlayer', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)

    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['min'],
    #             "max": getEstimatedPoints.values['partnerBidsFirst']['playerPasses']['max']
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.values['special']['weakTwo']['min'],
    #             "max": getEstimatedPoints.values['special']['weakTwo']['max']
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
    #             "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max']
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    # def test_only_pass_partner_passes_first(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "left": ['Pass', 'Three Diamond'],
    #         "top": ['One Heart', 'Three Heart'],
    #         "right": ['Pass', 'Pass'],
    #         "bottom": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "top": "TopPlayer",
    #         "bottom": "BottomPlayer",
    #         "left": "LeftPlayer",
    #         "right": "RightPlayer",
    #     }
    #     bids = [['LeftPlayer', "Pass"],['TopPlayer', 'One Heart'],['RightPlayer', 'Pass'], ['BottomPlayer', 'Pass'], ['LeftPlayer', "Three Diamond"],['TopPlayer', 'Two Heart'],['RightPlayer', 'Pass']]

    #     expected = {
    #         "right": {
    #             "min": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['min'],
    #             "max": getEstimatedPoints.values['partnerPassesFirst']['playerPasses']['max']
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
    #             "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max']
    #         },
    #         "left": {
    #             "min": getEstimatedPoints.values['passFirstBidSecond']['min'], 
    #             "max": getEstimatedPoints.values['passFirstBidSecond']['max'],
    #         },
    #     }

    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
    #     self.assertDictEqual(actual, expected)
    # def test_pass_first_when_partner_passes(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "left": ['One Diamond'],
    #         "top": ['Pass'],
    #         "right": ['Two No Trump'],
    #         "bottom": [],
    #     }
    #     seatingRelative = {
    #         "left": "LeftPlayer",
    #         "top": "TopPlayer",
    #         "right": "RightPlayer",
    #         "bottom": "BottomPlayer",
    #     }
    #     bids = [['LeftPlayer', "One Diamond"],['TopPlayer', 'Pass'],['RightPlayer', 'Two No Trump']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
    #     expected = {
    #        "left": {
    #             "min": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['min'],
    #             "max": getEstimatedPoints.values['isTeamsFirstBid']['playerBidsSuit']['max']
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
    #             "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.values['partnerBidsFirst']['playerBidsNoTrump']['isJumpshift']['min'],
    #             "max": getEstimatedPoints.values['partnerBidsFirst']['playerBidsNoTrump']['isJumpshift']['max']
    #         },
    #         "bottom": {
    #             "min": None,
    #             "max": None,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)

    # def test_pass_first_when_partner_opens(self):
    #     currentEstimatedPoints = {
    #         "left": None,
    #         "top": None,
    #         "right": None,
    #         "Bottom": None,
    #     }
    #     biddingObjRelative = {
    #         "left": ['One Diamond'],
    #         "top": ['One Heart'],
    #         "right": ['Two No Trump'],
    #         "bottom": ['Pass'],
    #     }
    #     seatingRelative = {
    #         "left": "LeftPlayer",
    #         "top": "TopPlayer",
    #         "right": "RightPlayer",
    #         "bottom": "BottomPlayer",
    #     }
    #     bids = [['LeftPlayer', "One Diamond"],['TopPlayer', 'One Heart'],['RightPlayer', 'Two No Trump'], ['BottomPlayer', 'Pass']]
    #     actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
    #     expected = {
    #        "left": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #         "top": {
    #             "min": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MIN,
    #             "max": getEstimatedPoints.IS_TEAMS_FIRST_BID_AND_PLAYER_BIDS_SUIT_MAX,
    #         },
    #         "right": {
    #             "min": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_NT_MIN,
    #             "max": getEstimatedPoints.RESPONDING_NO_JUMPSHIFT_NT_MAX,
    #         },
    #         "bottom": {
    #             "min": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MIN,
    #             "max": getEstimatedPoints.PARTNER_BIDS_FIRST_AND_PLAYER_PASSES_MAX,
    #         },
    #     }
    #     self.assertDictEqual(actual, expected)
    
    #endregion
    def test_set_exit_early(self):
        biddingObjRelative = {
            "left": ['One Diamond'],
            "top": ['Two Heart'],
            "right": ['Two No Trump'],
            "bottom": [],
        }
        bids = [['LeftPlayer', "One Diamond"],['TopPlayer', 'Two Heart'],['RightPlayer', 'Two No Trump']]
        actual = getEstimatedPoints.getEstimatedPoints(self.currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        expected = {
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
        self.actual = actual
        self.assertDictEqual(actual, expected)
    def test_set_pass(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": [],
            "right": ['pass'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_pass2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'Pass'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_NT_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['One No Trump'],
            "right": ['pass'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'One No Trump'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_TwoClub_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['Two Club'],
            "right": ['pass'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'Two Club'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['special']['twoClubs']['min'],
                "max": getEstimatedPoints.values['special']['twoClubs']['max']
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
        self.assertDictEqual(actual, expected)
    def test_set_TwoClub_2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['Two Club'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Two Club']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['twoClubs']['min'],
                "max": getEstimatedPoints.values['special']['twoClubs']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(actual, expected)
    def test_set_TwoClub_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['Two Club'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Two Club']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['twoClubs']['min'],
                "max": getEstimatedPoints.values['special']['twoClubs']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(actual, expected)
    def test_set_Double_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['Double'],
            "right": ['pass'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'Double'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_Double_2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['Double'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Double']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_Double_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['Double'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Double']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected) 
    def test_set_Regular_Bid_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['One Diamond'],
            "right": ['pass'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'One Diamond'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_Regular_Bid_2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['One Diamond'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'One Diamond']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_Rebular_Bid_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['One Spade'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'One Spade']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_WeakTwo_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['Two Diamond'],
            "right": ['pass'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'Two Diamond'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_WeakTwo_2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['Two Spade'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Two Spade']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_WeakTwo_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['Two Heart'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Two Heart']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_WeakTwo_4(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['One Club'],
            "right": ['Two Heart'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'One Club'], ['RightPlayer', 'Two Heart']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_WeakTwo_5(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['Pass'],
            "top": ['One Club'],
            "right": ['Two Spade'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'Pass'], ['TopPlayer', 'One Club'], ['RightPlayer', 'Two Spade']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_Weak_Three_Bid_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['Three Diamond'],
            "right": ['pass'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'Three Diamond'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_Weak_Three_Bid_2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['Three Diamond'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Three Diamond']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_Weak_Three_Bid_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['Three Diamond'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Three Diamond']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_set_Weak_Three_Bid_4(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['One Diamond'],
            "top": ['Three Heart'],
            "right": ['pass'],
            "bottom": [],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'One Diamond'], ['TopPlayer', 'Three Heart'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_bottom_is_dealer(self):
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": ['Four Heart'],
        }
        bids = [['LeftPlayer', 'pass'], ['TopPlayer', 'pass'], ['RightPlayer', 'Pass'], ['BottomPlayer', 'Four Heart']]
        actual = getEstimatedPoints.getEstimatedPoints(self.currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)

#TODO: These tests are just copied over from setting above section
class getEstimatedPointsTwoBidOpportunities(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
        self.actual = None
    def tearDown(self) -> None:
      print('actual = {0}'.format(self.actual))
    def test_update_1_exit_early(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['One Diamond'],
            "top": ['Two Heart'],
            "right": ['Two No Trump'],
            "bottom": ['Pass'],
        }
        bids = [['LeftPlayer', "One Diamond"],['TopPlayer', 'Two Heart'],['RightPlayer', 'Two No Trump']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_pass(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": [],
            "right": ['pass'],
            "bottom": [],
        }
        bids = [['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_pass2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'Pass'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_NT_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['One No Trump'],
            "right": ['pass'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'One No Trump'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_TwoClub_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['Two Club'],
            "right": ['pass'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'Two Club'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['special']['twoClubs']['min'],
                "max": getEstimatedPoints.values['special']['twoClubs']['max']
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
        self.assertDictEqual(actual, expected)
    def test_update_1_TwoClub_2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['Two Club'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Two Club']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
           "left": {
                "min": None,
                "max": None,
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['twoClubs']['min'],
                "max": getEstimatedPoints.values['special']['twoClubs']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(actual, expected)
    def test_update_1_TwoClub_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['Two Club'],
            "bottom": [],
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Two Club']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
           "left": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "top": {
                "min": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['min'],
                "max": getEstimatedPoints.values['isTeamsFirstBid']['playerPasses']['max']
            },
            "right": {
                "min": getEstimatedPoints.values['special']['twoClubs']['min'],
                "max": getEstimatedPoints.values['special']['twoClubs']['max']
            },
            "bottom": {
                "min": None,
                "max": None,
            },
        }
        self.assertDictEqual(actual, expected)
    def test_update_1_Double_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['Double'],
            "right": ['pass'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'Double'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_Double_2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['Double'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Double']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_Double_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['Double'],
            "bottom": [],
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Double']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected) 
    def test_update_1_Regular_Bid_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['One Diamond'],
            "right": ['pass'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'One Diamond'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_Regular_Bid_2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['One Diamond'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'One Diamond']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_Regular_Bid_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['One Spade'],
            "bottom": [],
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'One Spade']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_WeakTwo_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['Two Diamond'],
            "right": ['pass'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'Two Diamond'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_WeakTwo_2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['Two Spade'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Two Spade']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_WeakTwo_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['Two Heart'],
            "bottom": [],
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Two Heart']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_WeakTwo_4(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['One Club'],
            "right": ['Two Heart'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'One Club'], ['RightPlayer', 'Two Heart']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_WeakTwo_5(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['Pass'],
            "top": ['One Club'],
            "right": ['Two Spade'],
            "bottom": [],
        }
        bids = [['LeftPlayer', 'Pass'], ['TopPlayer', 'One Club'], ['RightPlayer', 'Two Spade']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_Weak_Three_Bid_1(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['Three Diamond'],
            "right": ['pass'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'Three Diamond'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_Weak_Three_Bid_2(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['Three Diamond'],
            "bottom": [],
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Three Diamond']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_Weak_Three_Bid_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['Three Diamond'],
            "bottom": [],
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Three Diamond']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_update_1_Weak_Three_Bid_4(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['One Diamond'],
            "top": ['Three Heart'],
            "right": ['pass'],
            "bottom": [],
        }
        bids = [['LeftPlayer', 'One Diamond'], ['TopPlayer', 'Three Heart'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, self.seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)
    def test_bottom_is_dealer(self):
        #TODO: when bottom is dealer, 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": ['Four Heart'],
        }
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'], ['TopPlayer', 'pass'], ['RightPlayer', 'Pass'], ['BottomPlayer', 'Four Heart']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        self.actual = actual
        expected = {
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
        self.assertDictEqual(actual, expected)

   
    #region updating bounds (when a player has bid more than twice?)
    #endregion
