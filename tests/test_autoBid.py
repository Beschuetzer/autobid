import unittest
import autoBid, helpers

def setupSelfObject(selfObject):
    selfObject.clientPointCountingConvention = 'hcp'
    selfObject.spot = 'north'
    selfObject.seating = {
        "north": 'NorthPlayer',
        "east": 'EastPlayer',
        "south": 'SouthPlayer',
        "west": "WestPlayer",
    }
    selfObject.seatingRelative = {
        "bottom": 'NorthPlayer',
        "left": 'EastPlayer',
        "top": 'SouthPlayer',
        "right": "WestPlayer",
    }
    selfObject.scoring = {
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
    return selfObject

def printSelfInfo(object):
    print("\nTear Down-----------------")
    print(f"object = {object}")
    print(f"self.hand = {object.hand}")
    print(f"self.bids = {object.bids}")
    print(f"self.spot = {object.spot}")
    print(f"self.seating = {object.seating}")
    print(f"self.scoring = {object.scoring}")
    print(f"self.actual = {object.actual}")
    print(f"self.expected = {object.expected}")
    print("---------------------------")

class takeout_double(unittest.TestCase):
    def setUp(self):
        self = setupSelfObject(self)

    def tearDown(self) -> None:
        printSelfInfo(self)

    def test_pass_two(self):
        self.biddingRelative = {
            "left": ['Pass', 'Two Spade'],
            "top": ['One Diamond', 'Three No Trump'],
            "right": ['Double', 'Double'],
            "bottom": ['Pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "T9732",
            "diamonds": "872",
            "hearts": "865",
            "spades": "35",
        }

        self.expected = 'Pass'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)
        
    def test_real_double_pass(self):
        self.biddingRelative = {
            "left": ['One No Trump'],
            "top": ['Double'],
            "right": ['Two Club'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "T9732",
            "diamonds": "872",
            "hearts": "865",
            "spades": "42",
        }

        self.expected = 'Pass'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

class opening_no_score(unittest.TestCase):
    def setUp(self):
        self = setupSelfObject(self)

    def tearDown(self) -> None:
        printSelfInfo(self)

    def test_one_club(self):
        self.biddingRelative = {
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
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
        self.biddingRelative = {
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
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
        self.biddingRelative = {
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
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

    def test_double(self):
        self.biddingRelative = {
            "top": ['Pass'],
            "right": ['One Diamond'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "Q5",
            "diamonds": "AKQJT",
            "hearts": "985",
            "spades": "K96",
        }
        

        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.expected = 'Double'
        self.assertEqual(self.actual, self.expected)

    def test_one_spade(self):
        self.biddingRelative = {
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "AKT",
            "diamonds": "975",
            "hearts": "97",
            "spades": "AK974",
        }
      
        self.expected = 'One Spade'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_weak_two(self):
        self.biddingRelative = {
            "left": ['Pass'],
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "T9",
            "diamonds": "975",
            "hearts": "AK9753",
            "spades": "96",
        }

        self.expected = 'Two Heart'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_weak_three(self):
        self.biddingRelative = {
            "left": ['Pass'],
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "A975432",
            "diamonds": "97",
            "hearts": "T9",
            "spades": "94",
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
        self.biddingRelative = {
            "top": ['One Diamond'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "AKT",
            "diamonds": "AK9",
            "hearts": "9754",
            "spades": "964",
        }

        self.expected = 'Three Club'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_same_suit(self):
        self.biddingRelative = {
            "top": ['One Diamond'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "AKQJT",
            "diamonds": "AKQJT",
            "hearts": "9",
            "spades": "96",
        }

        self.expected = 'Three Diamond'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_nt(self):
        self.biddingRelative = {
            "top": ['One Diamond'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "AKJ",
            "diamonds": "AKJ",
            "hearts": "9853",
            "spades": "Q96",
        }

        self.expected = 'Two No Trump'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_suit_1(self):
        self.biddingRelative = {
            "top": ['One Diamond'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "AKT",
            "diamonds": "964",
            "hearts": "97",
            "spades": "AK974",
        }

        self.expected = 'Three Spade'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_weak_two(self):
        self.biddingRelative = {
            "left": ['Pass'],
            "top": ['One Diamond'],
            "right": ['Pass'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "T9",
            "diamonds": "975",
            "hearts": "AK9753",
            "spades": "96",
        }

        self.expected = 'Two Heart'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_weak_three(self):
        self.biddingRelative = {
            "left": ['Pass'],
            "top": ['One Diamond'],
            "right": ['Pass'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "AJ97532",
            "diamonds": "97",
            "hearts": "96",
            "spades": "96",
        }

        self.expected = 'Three Club'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)
        
    def test_go_to_next_game_bid(self):
        self.biddingRelative = {
            "bottom": ['One No Trump'],
            "left": ['pass'],
            "top": ['Three Spade'],
            "right": ['Pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "KJ8",
            "diamonds": "AJ2",
            "hearts": "AQ",
            "spades": "A8532",
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
        self.biddingRelative = {
            "top": ['One Heart'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "AT53",
            "diamonds": "AJ98",
            "hearts": "97",
            "spades": "964"
        }

        self.expected = 'Two Diamond'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_same_suit(self):
        self.biddingRelative = {
            "top": ['One Diamond'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "AJT",
            "diamonds": "AT98",
            "hearts": "943",
            "spades": "943",
        }

        self.expected = 'Two Diamond'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_nt(self):
        self.biddingRelative = {
            "top": ['One Spade'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.handDictionary = {
            "clubs": "QT9",
            "diamonds": "QJT",
            "hearts": "Q853",
            "spades": "J9",
        }

        self.expected = 'One No Trump'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    def test_suit_1(self):
        self.handDictionary = {
            "clubs": "AT",
            "diamonds": "9642",
            "hearts": "9",
            "spades": "K9743",
        }

        self.expected = 'Two Spade'

        self.biddingRelative = {
            "top": ['One No Trump'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

class responding_without_responding_points_no_score(unittest.TestCase):
    def setUp(self):
        self = setupSelfObject(self)

    def tearDown(self) -> None:
        printSelfInfo(self)

    def test_pass_with_0_points(self):
        self.biddingRelative = {
            "top": ['One Heart'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.handDictionary = {
            "clubs": "T953",
            "diamonds":  "987",
            "hearts":  "987",
            "spades": "987",
        }

        self.expected = 'Pass'

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)
    def test_pass_with_5_points(self):
        self.biddingRelative = {
            "top": ['One Heart'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        self.handDictionary = {
            "clubs": "985",
            "diamonds": "AJ76",
            "hearts": "976",
            "spades": "976",
        }
        self.expected = 'Pass'

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

class two_clubs(unittest.TestCase):
    def setUp(self):
        self = setupSelfObject(self)

    def tearDown(self) -> None:
        printSelfInfo(self)

    def test_respond_1(self):
        self.handDictionary = {
            "clubs": "AT53",
            "diamonds": "AJ98",
            "hearts": "97",
            "spades": "964",
        }

        self.expected = 'Two Diamond'
        self.biddingRelative = {
            "top": ['One Heart'],
            "right": ['Pass'],
            "bottom": [],
            "left": [],
        }
        

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = autoBid.autoBid(self.bids, self.hand, self.scoring, self.seating, self.spot, self.clientPointCountingConvention)
        self.assertEqual(self.actual, self.expected)

    #this case caused issues in a game once
    def test_interesting_case(self):
        self.biddingRelative = {
            "right": ['One Spade', 'Two Heart'],
            "bottom": ['One No Trump'],
            "left": ['pass'],
            "top": ['Two Diamond'],
        }
        self.handDictionary = {
            "clubs": "AT53",
            "diamonds": "AJ98",
            "hearts": "97",
            "spades": "964",
        }
        self.expected = 'Not Done'

        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
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


