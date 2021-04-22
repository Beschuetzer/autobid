import unittest
import autoBid, helpers

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

class One_Club(unittest.TestCase):
    def setUp(self):
        self.clientPointCountingConvention = 'hcp'
        self.spot = 'north'
        self.seating = {
            "north": 'NorthPlayer',
            "east": 'EastPlayer',
            "south": 'SouthPlayer',
            "west": "WestPlayer",
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

    def tearDown(self) -> None:
        print(f"self.spot = {self.spot}")
        print(f"self.seating = {self.seating}")
        print(f"self.bids = {self.bids}")
        print(f"self.scoring = {self.scoring}")

    def test_partner_opens_and_you_have_openers(self):
        self.bids = [
            ['SouthPlayer', 'One Club'],
            ['WestPlayer', 'Pass'],
        ]
        hand = [[0], [1,3,5], [38,36,35,34,33,30,27], [47, 43]]
        actual = autoBid.autoBid(self.bids, hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        expected = 'Four Heart'
        self.assertEqual(actual, expected)

class Special_Cases(unittest.TestCase):
    def setUp(self):
        self.clientPointCountingConvention = 'hcp'
        self.spot = 'north'
        self.seating = {
            "north": 'NorthPlayer',
            "east": 'EastPlayer',
            "south": 'SouthPlayer',
            "west": "WestPlayer",
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

    def tearDown(self) -> None:
        print(f"self.spot = {self.spot}")
        print(f"self.seating = {self.seating}")
        print(f"self.bids = {self.bids}")
        print(f"self.scoring = {self.scoring}")
        print(f"self.hand = {self.hand}")

    def test_two_clubs_take_out_of_no_trump(self):
        self.bids = [
            ['SouthPlayer', 'Two Club'],
            ['WestPlayer', 'Pass'],
            ['NorthPlayer', 'Two Spade'],
            ['EastPlayer', 'Pass'],
            ['SouthPlayer', 'Three Club'],
            ['WestPlayer', 'Pass'],
            ['NorthPlayer', 'Three Heart'],
            ['EastPlayer', 'Pass'],
            ['NorthPlayer', 'Three No Trump'],
            ['EastPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [0],
            "diamonds": [5,3,1],
            "hearts": [12,10,9,8,7,4,1],
            "spades": [7,4]
        }

        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.expected = 'Four Heart'
        self.assertEqual(self.actual, self.expected)

    def test_two_clubs_took_out_of_game_but_partner_did_not_pass(self):
        self.bids = [
            ['SouthPlayer', 'Two Club'],
            ['WestPlayer', 'Pass'],
            ['NorthPlayer', 'Two Spade'],
            ['EastPlayer', 'Pass'],
            ['SouthPlayer', 'Three Club'],
            ['WestPlayer', 'Pass'],
            ['NorthPlayer', 'Three Heart'],
            ['EastPlayer', 'Pass'],
            ['NorthPlayer', 'Three No Trump'],
            ['EastPlayer', 'Pass'],
            ['NorthPlayer', 'Four Heart'],
            ['EastPlayer', 'Pass'],
            ['NorthPlayer', 'Four Spade'],
            ['EastPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [0],
            "diamonds": [5,3,1],
            "hearts": [12,10,9,8,7,4,1],
            "spades": [7,4]
        }

        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.expected = 'Pass'
        self.assertEqual(self.actual, self.expected)


