import unittest
import autoBid

class Takeout_Double(unittest.TestCase):
    def setUp(self):
        self.clientPointCountingConvention = 'hcp'
        self.spot = 'north'
        self.seating = {
            "north": 'Adam',
            "east": 'Dan',
            "south": 'Ann',
            "west": "Andrew",
        }
        self.scoring = {
            "northSouth": {
                "aboveTheLine": 0,
                "belowTheLine": 0,
                "totalBelowTheLineScore": 0,
                "isVulnerable": False,
                "vulnerableTransitionIndex": None,
            },
            "eastWest": {
                "aboveTheLine": 0, 
                "belowTheLine": 0,
                "totalBelowTheLineScore": 0,
                "isVulnerable": False,
                "vulnerableTransitionIndex": None,
            },
        }
    def test_pass_two(self):
        bids = [['Adam', 'Pass'], ['Dan', 'One Diamond'], ['Ann', 'Double'], ['Andrew', 'Pass'], ['Adam', 'Two Diamond'], ['Dan', 'Three No Trump'], ['Ann', 'Double'], ['Andrew', 'Pass']]
        hand = [[0, 1, 5, 7, 8], [13, 18, 19], [29, 30, 32], [40, 42]]
        actual = autoBid.autoBid(bids, hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        #TODO: Finish expected when done with rest of autoBid()
        expected = 'Pass'
        self.assertEqual(actual, expected)
    def test_real_double_pass(self):
        bids = [['Adam', 'Two No Trump'], ['Dan', 'Double'], ['Ann', 'Double'], ['Andrew', '3 club']]
        hand = [[0, 1, 5, 7, 8], [13, 18, 19], [29, 30, 32], [40, 42]]
        actual = autoBid.autoBid(bids, hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        expected = 'Pass'
        self.assertEqual(actual, expected)


class partnerTwoClubResponse(unittest.TestCase):
    def test_initial_zero(self):
        biddingObjRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 0
        currentActualBid = 'Two Club'
        actual = autoBid.parpartnerTwoClubResponse(biddingObjRelative, totalOpeningPoints, currentActualBid)
        expected = 'Two Diamond'
        self.assertEqual(actual, expected)