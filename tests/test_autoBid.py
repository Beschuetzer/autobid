import unittest
import autoBid, helpers

def setupSelfObject(self):
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
    return self

def printSelfInfo(object):
    print("\nTear Down-----------------")
    print(f"self.spot = {object.spot}")
    print(f"self.seating = {object.seating}")
    print(f"self.bids = {object.bids}")
    print(f"self.scoring = {object.scoring}")
    print(f"self.actual = {object.actual}")
    print(f"self.expected = {object.expected}")
    print(f"self.hand = {object.hand}")
    print("---------------------------")

class takeout_double(unittest.TestCase):
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

class opening_no_score(unittest.TestCase):
    def setUp(self):
        self = setupSelfObject(self)

    def tearDown(self) -> None:
        printSelfInfo(self)

    def test_one_club(self):
        self.bids = [
            ['SouthPlayer', 'Pass'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": "AKT",
            "diamonds": "AK9",
            "hearts": "9754",
            "spades": "964",
        }

        self.expected = 'One Club'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_two_club(self):
        self.bids = [
            ['SouthPlayer', 'pass'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": "AKQJT",
            "diamonds": "AKQJT",
            "hearts": "9",
            "spades": "96",
        }

        self.expected = 'Two Club'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_one_nt(self):
        self.bids = [
            ['SouthPlayer', 'pass'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": "AKJ",
            "diamonds": "AKQ",
            "hearts": "9853",
            "spades": "Q96"
        }

        self.expected = 'One No Trump'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    #TODO: all tests below here need to have handDictionary written as a string
    def test_double(self):
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

    def test_one_spade(self):
        self.bids = [
            ['SouthPlayer', 'pass'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,11,8],
            "diamonds": [7,4,2],
            "hearts": [7,5],
            "spades": [12,11,7,5,2],
        }

        self.expected = 'One Spade'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_weak_two(self):
        self.bids = [
            ['EastPlayer', 'pass'],
            ['SouthPlayer', 'pass'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [8,7],
            "diamonds": [7,5,3],
            "hearts": [12,11,7,5,3,1],
            "spades": [7,4]
        }

        self.expected = 'Two Heart'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_weak_three(self):
        self.bids = [
            ['EastPlayer', 'pass'],
            ['SouthPlayer', 'pass'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,9,7,5,3,2,1],
            "diamonds": [7,5],
            "hearts": [8,7],
            "spades": [7,4]
        }

        self.expected = 'Three Club'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)
        
class responding_with_openers_no_score(unittest.TestCase):
    def setUp(self):
        self = setupSelfObject(self)

    def tearDown(self) -> None:
        printSelfInfo(self)

    def test_one_club_(self):
        self.bids = [
            ['SouthPlayer', 'One Diamond'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,11,8],
            "diamonds": [12,11,7],
            "hearts": [7,5,3,2],
            "spades": [7,4,2]
        }

        self.expected = 'Three Club'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_same_suit(self):
        self.bids = [
            ['SouthPlayer', 'One Diamond'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,11,10,9,8],
            "diamonds": [12,11,10,9,8],
            "hearts": [7],
            "spades": [7,4]
        }

        self.expected = 'Three Diamond'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_nt(self):
        self.bids = [
            ['SouthPlayer', 'One Diamond'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,11,9],
            "diamonds": [12,11,8],
            "hearts": [7,6,3,1],
            "spades": [10,7,4,]
        }

        self.expected = 'Two No Trump'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_suit_1(self):
        self.bids = [
            ['SouthPlayer', 'One Diamond'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,11,8],
            "diamonds": [7,4,2],
            "hearts": [7,5],
            "spades": [12,11,7,5,2],
        }

        self.expected = 'Three Spade'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_weak_two(self):
        self.bids = [
            ['EastPlayer', 'pass'],
            ['SouthPlayer', 'One Diamond'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [8,7],
            "diamonds": [7,5,3],
            "hearts": [12,11,7,5,3,1],
            "spades": [7,4]
        }

        self.expected = 'Two Heart'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_weak_three(self):
        self.bids = [
            ['EastPlayer', 'pass'],
            ['SouthPlayer', 'One Diamond'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,9,7,5,3,2,1],
            "diamonds": [7,5],
            "hearts": [8,7],
            "spades": [7,4]
        }

        self.expected = 'Three Club'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)
        
    def test_go_to_next_game_bid(self):
        self.bids = [
            ['NorthPlayer', 'One No Trump'],
            ['EastPlayer', 'pass'],
            ['SouthPlayer', 'Three Spade'],
            ['WestPlayer', 'pass'],
        ]
        self.handDictionary = {
            "clubs": ["KJ8"],
            "diamonds": ["AJ2"],
            "hearts": ["AQ"],
            "spades": ["A8532"]
        }


        self.expected = 'Four Spade'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)
     
        
class responding_without_openers_no_score(unittest.TestCase):
    def setUp(self):
        self = setupSelfObject(self)

    def tearDown(self) -> None:
        printSelfInfo(self)

    def test_better_off_suit(self):
        self.bids = [
            ['SouthPlayer', 'One Heart'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,8,3,1],
            "diamonds": [12,9,7,6],
            "hearts": [7,5],
            "spades": [7,4,2]
        }

        self.expected = 'Two Diamond'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_same_suit(self):
        self.bids = [
            ['SouthPlayer', 'One Diamond'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,9,8],
            "diamonds": [12,8,7,6],
            "hearts": [7,2,1],
            "spades": [7,4,1]
        }

        self.expected = 'Two Diamond'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_nt(self):
        self.bids = [
            ['SouthPlayer', 'One Spade'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [10,8,7],
            "diamonds": [10,9,8],
            "hearts": [10,6,3,1],
            "spades": [9,7]
        }

        self.expected = 'One No Trump'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_suit_1(self):
        self.bids = [
            ['SouthPlayer', 'One No Trump'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,8],
            "diamonds": [7,4,2],
            "hearts": [7,5],
            "spades": [11,7,5,2,1],
        }

        self.expected = 'Two Spade'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

class responding_without_responding_points_no_score(unittest.TestCase):
    def setUp(self):
        self = setupSelfObject(self)

    def tearDown(self) -> None:
        printSelfInfo(self)

    def test_pass_with_0_points(self):
        self.bids = [
            ['SouthPlayer', 'One Heart'],
            ['WestPlayer', 'Pass'],
        ]

        self.handDictionary = {
            "clubs": [8,7,3,1],
            "diamonds": [7,6,5],
            "hearts": [7,5,4],
            "spades": [7,4,2]
        }

        self.expected = 'Pass'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)
    def test_pass_with_5_points(self):
        self.bids = [
            ['SouthPlayer', 'One Heart'],
            ['WestPlayer', 'Pass'],
        ]

        self.handDictionary = {
            "clubs": [7,6,3],
            "diamonds": [12,9,5,4],
            "hearts": [7,5,4],
            "spades": [7,4,2]
        }

        self.expected = 'Pass'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

class two_clubs(unittest.TestCase):
    def setUp(self):
        self = setupSelfObject(self)

    def tearDown(self) -> None:
        printSelfInfo(self)

    def test_respond_1(self):
        self.bids = [
            ['SouthPlayer', 'One Heart'],
            ['WestPlayer', 'Pass'],
        ]
        self.handDictionary = {
            "clubs": [12,8,3,1],
            "diamonds": [12,9,7,6],
            "hearts": [7,5],
            "spades": [7,4,2]
        }

        self.expected = 'Two Diamond'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

class special_cases(unittest.TestCase):
    def setUp(self):
        self = setupSelfObject(self)

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


