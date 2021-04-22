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

class Opening_No_Score(unittest.TestCase):
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

    def test_One_Club(self):
        self.bids = [
            ['SouthPlayer', 'pass'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,11,8],
            "diamonds": [12,11,7],
            "hearts": [7,5,3,2],
            "spades": [7,4,2]
        }

        self.expected = 'One Club'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)
    def test_Two_Club(self):
        self.bids = [
            ['SouthPlayer', 'pass'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,11,10,9,8],
            "diamonds": [12,11,10,9,8],
            "hearts": [7],
            "spades": [7,4]
        }

        self.expected = 'Two Club'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_One_NT(self):
        self.bids = [
            ['SouthPlayer', 'pass'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,11,9],
            "diamonds": [12,11,8],
            "hearts": [7,6,3,1],
            "spades": [10,7,4,]
        }

        self.expected = 'One No Trump'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_Double(self):
        self.bids = [
            ['SouthPlayer', 'pass'],
            ['WestPlayer', 'One Diamond'],
        ]
        self.handDictionary = {
            "clubs": [10, 3],
            "diamonds": [12,11,10,9,8],
            "hearts": [7,6,3],
            "spades": [11,7,4]
        }

        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.expected = 'Double'
        self.assertEqual(self.actual, self.expected)

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


