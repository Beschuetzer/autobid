import helpers, unittest, testCases

class getSuitFromCardAsNumber(unittest.TestCase):
    def test_clubLow(self):
        self.assertEqual(helpers.getSuitNameFromCardAsNumber(0), 'clubs')
    def test_clubHigh(self):
        self.assertEqual(helpers.getSuitNameFromCardAsNumber(12), 'clubs')
    def test_diamondLow(self):
        self.assertEqual(helpers.getSuitNameFromCardAsNumber(13), 'diamonds')
    def test_diamondHigh(self):
        self.assertEqual(helpers.getSuitNameFromCardAsNumber(25), 'diamonds')
    def test_heartLow(self):
        self.assertEqual(helpers.getSuitNameFromCardAsNumber(26), 'hearts')
    def test_heartHigh(self):
        self.assertEqual(helpers.getSuitNameFromCardAsNumber(38), 'hearts')
    def test_spadeLow(self):
        self.assertEqual(helpers.getSuitNameFromCardAsNumber(39), 'spades')
    def test_spadeHigh(self):
        self.assertEqual(helpers.getSuitNameFromCardAsNumber(51), 'spades')
class getHighCardPoints(unittest.TestCase):
    def test_Normal_None(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 0)

    def test_Normal_onlyTens(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 0)

    def test_Normal_onlyJacks(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 4)
    
    def test_Normal_onlyQueens(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 8)

    def test_Normal_onlyKings(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 12)

    def test_Normal_onlyAces(self):
        clubs = [i for i in range(0, 13) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 16)

    def test_Normal_All(self):
        clubs = [i for i in range(0, 13)]
        diamonds = [i for i in range(13, 26)]
        hearts = [i for i in range(26, 39)]
        spades = [i for i in range(39, 52)]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 40)

    def test_Normal_OneOfEach(self):
        clubs = [i for i in range(0, 13) if i%13==12]
        diamonds = [i for i in range(13, 26) if i%13==11]
        hearts = [i for i in range(26, 39) if i%13==10]
        spades = [i for i in range(39, 52) if i%13==9]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 4)

    def test_Normal_AllButOneOfEach(self):
        clubs = [i for i in range(0, 13) if i%13 != 11]
        diamonds = [i for i in range(13, 26) if i%13 != 10]
        hearts = [i for i in range(26, 39) if i%13 != 9]
        spades = [i for i in range(39, 52) if i%13 != 12]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 30)

    



    def test_Alternative_None(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 0)

    def test_Alternative_onlyTens(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 1)

    def test_Alternative_onlyJacks(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 3)
    
    def test_Alternative_onlyQueens(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 6)

    def test_Alternative_onlyKings(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 12)

    def test_Alternative_onlyAces(self):
        clubs = [i for i in range(0, 13) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 18)

    def test_Alternative_All(self):
        clubs = [i for i in range(0, 13)]
        diamonds = [i for i in range(13, 26)]
        hearts = [i for i in range(26, 39)]
        spades = [i for i in range(39, 52)]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 40)

    def test_Alternative_OneOfEach(self):
        clubs = [i for i in range(0, 13) if i%13==12]
        diamonds = [i for i in range(13, 26) if i%13==11]
        hearts = [i for i in range(26, 39) if i%13==10]
        spades = [i for i in range(39, 52) if i%13==9]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 4.5)

    def test_Alternative_AllButOneOfEach(self):
        clubs = [i for i in range(0, 13) if i%13 != 11]
        diamonds = [i for i in range(13, 26) if i%13 != 10]
        hearts = [i for i in range(26, 39) if i%13 != 9]
        spades = [i for i in range(39, 52) if i%13 != 12]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(helpers.getHighCardPoints(hand, convention), 30.25)

    def test_Error_NoHand(self):
        convention = 'hcp'
        self.assertEqual(helpers.getHighCardPoints(None, convention), -1)

    def test_Error_NoConvention(self):
        convention = 'hcp'
        self.assertEqual(helpers.getHighCardPoints([1,2,3], None), -1)
class tallyUpTotal(unittest.TestCase):
    def test_AllOneSuit(self):
        suitCounts = {
            "clubs": 13,
            "diamonds":  0,
            "hearts":  0,
            "spades": 0,
        }
        self.assertEqual(helpers.getOpeningDistributionPoints(suitCounts), 18)
    
    def test_None(self):
        suitCounts = {
            "clubs": 4,
            "diamonds":  3,
            "hearts":  3,
            "spades": 3,
        }
        self.assertEqual(helpers.getOpeningDistributionPoints(suitCounts), 0)
    
    def test_Singleton(self):
        suitCounts = {
            "clubs": 4,
            "diamonds":  4,
            "hearts":  4,
            "spades": 1,
        }
        self.assertEqual(helpers.getOpeningDistributionPoints(suitCounts), 2)
    
    def test_Doubleton(self):
        suitCounts = {
            "clubs": 4,
            "diamonds":  4,
            "hearts":  3,
            "spades": 2,
        }
        self.assertEqual(helpers.getOpeningDistributionPoints(suitCounts), 1)
    
    def test_FiveOfOne(self):
        suitCounts = {
            "clubs": 5,
            "diamonds":  4,
            "hearts":  3,
            "spades": 3,
        }
        self.assertEqual(helpers.getOpeningDistributionPoints(suitCounts), 1)
    
    def test_Void(self):
        suitCounts = {
            "clubs": 4,
            "diamonds":  0,
            "hearts":  4,
            "spades": 4,
        }
        self.assertEqual(helpers.getOpeningDistributionPoints(suitCounts), 3)
class getOpeningDistributionPoints(unittest.TestCase):
    def setUp(self):
        self.seatingRelative = {
            "top": "topPlayer",
            "bottom": "bottomPlayer",
            "left": "leftPlayer",
            "right": "rightPlayer",
        }
    def tearDown(self):
        print(f"self.biddingAbsolute = {self.biddingAbsolute}")
        print(f"self.biddingRelative = {self.biddingRelative}")
        print(f"self.hand = {self.hand}")
        print(f"self.suitCounts = {self.suitCounts}")
        print(f"self.expected = {self.expected}")
        print(f"self.actual = {self.actual}")
    
    def test_opening_13_of_one_Suit(self):
        self.suitCounts = {
            "clubs": 13,
            "diamonds": 0,
            "hearts": 0,
            "spades": 0,
        }
        self.expected = {
            "clubs": 40,
            "diamonds": 0,
            "hearts": 0,
            "spades": 0,
        }
        self.actual = helpers.getOpeningDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

    def test_opening_12_of_one_Suit(self):
        self.suitCounts = {
            "clubs": 12,
            "diamonds": 1,
            "hearts": 0,
            "spades": 0,
        }
        self.expected = {
            "clubs": 36,
            "diamonds": 3,
            "hearts": 0,
            "spades": 0,
        }
        self.actual = helpers.getOpeningDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

    def test_opening_11_of_one_Suit(self):
        self.suitCounts = {
            "clubs": 12,
            "diamonds": 2,
            "hearts": 0,
            "spades": 0,
        }
        self.expected = {
            "clubs": 32,
            "diamonds": 3,
            "hearts": 0,
            "spades": 0,
        }
        self.actual = helpers.getOpeningDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

    def test_opening_10_of_one_Suit(self):
        self.suitCounts = {
            "clubs": 10,
            "diamonds": 3,
            "hearts": 0,
            "spades": 0,
        }
        self.expected = {
            "clubs": 28,
            "diamonds": 3,
            "hearts": 0,
            "spades": 0,
        }
        self.actual = helpers.getOpeningDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)
    def test_Opening_None(self):
        self.suitCounts = {
            "clubs": 4,
            "diamonds": 3,
            "hearts": 4,
            "spades": 3,
        }
        self.expected = {
            "clubs": 0,
            "diamonds": 0,
            "hearts": 0,
            "spades": 0,
        }
        self.actual = helpers.getOpeningDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

    def test_Opening_Void(self):
        self.suitCounts = {
            "clubs": 0,
            "diamonds": 4,
            "hearts": 4,
            "spades": 5,
        }
        self.expected = {
            "clubs": 0,
            "diamonds": 3,
            "hearts": 3,
            "spades": 4,
        }
        self.actual = helpers.getOpeningDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

    def test_Opening_Singleton(self):
        self.suitCounts = {
            "clubs": 4,
            "diamonds": 1,
            "hearts": 3,
            "spades": 5,
        }
        self.expected = {
            "clubs": 2,
            "diamonds": 0,
            "hearts": 2,
            "spades": 3,
        }
        self.actual = helpers.getOpeningDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

    def test_Opening_Doubleton(self):
        self.suitCounts = {
            "clubs": 4,
            "diamonds": 2,
            "hearts": 3,
            "spades": 4,
        }
        self.expected = {
            "clubs": 1,
            "diamonds": 0,
            "hearts": 1,
            "spades": 1,
        }
        self.actual = helpers.getOpeningDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)
        
    def test_Opening_All_Three(self):
        self.suitCounts = {
            "clubs": 0,
            "diamonds": 1,
            "hearts": 2,
            "spades": 10,
        }
        self.expected = {
            "clubs": 1,
            "diamonds": 0,
            "hearts": 1,
            "spades": 28,
        }
        self.actual = helpers.getOpeningDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

class getRespondingDistributionPoints(unittest.TestCase):
    def setUp(self):
        self.seatingRelative = {
            "top": "topPlayer",
            "bottom": "bottomPlayer",
            "left": "leftPlayer",
            "right": "rightPlayer",
        }
    def tearDown(self):
        print(f"self.biddingAbsolute = {self.biddingAbsolute}")
        print(f"self.biddingRelative = {self.biddingRelative}")
        print(f"self.hand = {self.hand}")
        print(f"self.suitCounts = {self.suitCounts}")
        print(f"self.expected = {self.expected}")
        print(f"self.actual = {self.actual}")

    def test_Responding_Only_Use_Void_No_Singleton_Multiple_Diamonds(self):
        clubs = [i for i in range(0, 13)]
        diamonds = []
        hearts = []
        spades = []
        self.hand = [clubs, diamonds, hearts, spades]
        self.biddingAbsolute = []
        self.suitCounts = {
            "clubs": 4,
            "diamonds": 8,
            "hearts": 1,
            "spades": 0,
        }
        self.expected = {
            "clubs": 8,
            "diamonds": 20,
            "hearts": 3,
            "spades": 0,
        }
        self.actual = helpers.getRespondingDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

    def test_Responding_Only_Use_Void_No_Singleton_Multiple_heart(self):
        clubs = [i for i in range(0, 13)]
        diamonds = []
        hearts = []
        spades = []
        self.hand = [clubs, diamonds, hearts, spades]
        self.biddingAbsolute = []
        self.suitCounts = {
            "clubs": 3,
            "diamonds": 7,
            "hearts": 3,
            "spades": 0,
        }
        self.expected = {
            "clubs": 3,
            "diamonds": 15,
            "hearts": 3,
            "spades": 0,
        }
        self.actual = helpers.getRespondingDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

    def test_Responding_AllOneSuit_Partners_Suit(self):
        clubs = [i for i in range(0, 13)]
        diamonds = []
        hearts = []
        spades = []
        self.hand = [clubs, diamonds, hearts, spades]
        self.biddingRelative = {
            "left": ['Pass'],
            "top": ['One Heart'],
            "right": ['Pass'],
            "bottom": [],
        }
        self.biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
       
        self.suitCounts = {
            "clubs": 1,
            "diamonds": 2,
            "hearts": 8,
            "spades": 3,
        }
        self.expected = {
            "clubs": 1,
            "diamonds": 2,
            "hearts": 13,
            "spades": 3,
        }

        self.actual = helpers.getRespondingDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

    def test_Responding_AllOneSuit_Partners_Suit_Not(self):
        clubs = [i for i in range(0, 13)]
        diamonds = []
        hearts = []
        spades = []
        self.hand = [clubs, diamonds, hearts, spades]
        self.biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
       
        self.suitCounts = {
            "clubs": 1,
            "diamonds": 2,
            "hearts": 7,
            "spades": 3,
        }
        self.expected = {
            "clubs": 1,
            "diamonds": 2,
            "hearts": 9,
            "spades": 3,
        }
        self.actual = helpers.getRespondingDistributionPoints(self.suitCounts);
        self.assertEqual(self.actual, self.expected)

    def test_Responding_None(self):
        clubLength = 4
        diamondLength = 3
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]

        self.hand = [clubs, diamonds, hearts, spades]
        
        self.suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }
        self.expected = {
            "clubs": 0,
            "diamonds": 0,
            "hearts": 0,
            "spades": 0,
        }

        self.biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getRespondingDistributionPoints(self.suitCounts);
        self.assertEqual(self.expected, self.actual)
   
    def test_Responding_FiveLong_Partners_Suit_With_Doubleton(self):
        clubLength = 4
        diamondLength = 5
        heartLength = 2
        spadeLength = 4

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        
        self.hand = [clubs, diamonds, hearts, spades]
        self.biddingRelative = {
            "left": ['Pass'],
            "top": ['One Diamond'],
            "right": ['Pass'],
            "bottom": [],
        }
        self.suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }
        self.expected = 3
        self.biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getRespondingDistributionPoints(self.suitCounts);
        self.assertEqual(self.expected, self.actual)

    def test_Responding_FiveLong_Partners_Suit_With_Void(self):
        clubLength = 4
        diamondLength = 5
        heartLength = 0
        spadeLength = 4

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        
        self.hand = [clubs, diamonds, hearts, spades]
        self.biddingRelative = {
            "left": ['Pass'],
            "top": ['One Diamond'],
            "right": ['Pass'],
            "bottom": [],
        }
        self.suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }
        self.expected = 9
        self.biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getRespondingDistributionPoints(self.suitCounts);
        self.assertEqual(self.expected, self.actual)
    
    def test_Responding_FiveLong_Partners_Suit_With_Singleton(self):
        clubLength = 4
        diamondLength = 5
        heartLength = 1
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        
        self.hand = [clubs, diamonds, hearts, spades]
        self.biddingRelative = {
            "left": ['Pass'],
            "top": ['One Diamond'],
            "right": ['Pass'],
            "bottom": [],
        }
        self.suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }
        self.expected = 6
        self.biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getRespondingDistributionPoints(self.suitCounts);
        self.assertEqual(self.expected, self.actual)

    def test_Responding_FiveLong_Partners_Suit_Not(self):
        clubLength = 5
        diamondLength = 3
        heartLength = 3
        spadeLength = 2

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        
        self.hand = [clubs, diamonds, hearts, spades]
        self.biddingRelative = {
            "left": ['Pass'],
            "top": ['One Heart'],
            "right": ['Pass'],
            "bottom": [],
        }
        self.suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }
        self.expected = {
            "clubs": 2,
            "diamonds": 1,
            "hearts": 1,
            "spades": -1,
        }
        self.biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getRespondingDistributionPoints(self.suitCounts);
        self.assertEqual(self.expected, self.actual)
    
class getCurrentActualBid(unittest.TestCase):
    def test_Normal(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        expected = helpers.getCurrentContractBid(bids)
        actual = ['Ann', '3 Club']
        self.assertListEqual(expected, actual)
    
    def test_LowerCase(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', '2 No Trump'], ['Tim', 'double'], ['Ann', 'pass'], ['Andrew', 'pass']]
        expected = helpers.getCurrentContractBid(bids)
        actual = ['Adam', '2 No Trump']
        self.assertListEqual(expected, actual)

    def test_UpperCase(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', '2 NO TRUMP'], ['Tim', 'DOUBLE'], ['Ann', 'PASS'], ['Andrew', 'PASS']]
        expected = helpers.getCurrentContractBid(bids)
        actual = ['Adam', '2 NO TRUMP']
        self.assertListEqual(expected, actual)

    def test_Empty(self):
        bids = []
        expected = helpers.getCurrentContractBid(bids)
        actual = None
        self.assertEqual(expected, actual)
class getBiddingObjAbsolute(unittest.TestCase):
    def test_empty(self):
        bids = []
        seating = {
            "north": "Adam",
            "east": "Tim",
            "south": "Ann",
            "west": "Andrew",
        }
        expected = {
            "north": [],
            "east": [],
            "south": [],
            "west": [],
        }
        actual = helpers.getBiddingObjAbsolute([], seating)
        self.assertDictEqual(expected, actual)
    def test_One(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass']]
        seating = {
            "north": "Adam",
            "east": "Tim",
            "south": "Ann",
            "west": "Andrew",
        }
        expected = {
            "north": ['2 No Trump'],
            "east": ['Double'],
            "south": ['3 Club'],
            "west": ['Pass'],
        }
        actual = helpers.getBiddingObjAbsolute(bids, seating)
        self.assertDictEqual(expected, actual)
    def test_Two(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        seating = {
            "north": "Adam",
            "east": "Tim",
            "south": "Ann",
            "west": "Andrew",
        }
        expected = {
            "north": ['2 No Trump', 'Double'],
            "east": ['Double'],
            "south": ['3 Club'],
            "west": ['Pass'],
        }
        actual = helpers.getBiddingObjAbsolute(bids, seating)
        self.assertDictEqual(expected, actual)
    def test_Three(self):
        bids = [['Adam', 'Pass'], ['Tim', 'Double'], ['Ann', 'Pass'], ['Andrew', '1 Diamond'], ['Adam', 'Double'],  ['Tim', '1 Heart'], ['Ann', '1 Spade'], ['Andrew', '2 Diamond']]
        seating = {
            "north": "Adam",
            "east": "Tim",
            "south": "Ann",
            "west": "Andrew",
        }
        expected = {
            "north": ['Pass', 'Double'],
            "east": ['Double', '1 Heart'],
            "south": ['Pass', '1 Spade'],
            "west": ['1 Diamond', '2 Diamond'],
        }
        actual = helpers.getBiddingObjAbsolute(bids, seating)
        self.assertDictEqual(expected, actual)
class getSpotAfterNRotations(unittest.TestCase):
    def test_negative(self):
        spot = 'north'
        numberOfRotations = -1
        with self.assertRaises(TypeError) as cm:
            helpers.getSpotAfterNRotations(spot, numberOfRotations)

    def test_none(self):
        spot = 'north'
        numberOfRotations = 0
        actual = helpers.getSpotAfterNRotations(spot, numberOfRotations)
        expected = 'north'
        self.assertEqual(actual, expected)
    def test_oneRotation(self):
        spot = 'north'
        numberOfRotations = 1
        actual = helpers.getSpotAfterNRotations(spot, numberOfRotations)
        expected = 'east'
        self.assertEqual(actual, expected)
    def test_twoRotations(self):
        spot = 'east'
        numberOfRotations = 2
        actual = helpers.getSpotAfterNRotations(spot, numberOfRotations)
        expected = 'west'
        self.assertEqual(actual, expected)
    def test_threeRotations(self):
        spot = 'south'
        numberOfRotations = 3
        actual = helpers.getSpotAfterNRotations(spot, numberOfRotations)
        expected = 'east'
        self.assertEqual(actual, expected)
    def test_fourRotations(self):
        spot = 'west'
        numberOfRotations = 4
        actual = helpers.getSpotAfterNRotations(spot, numberOfRotations)
        expected = 'west'
        self.assertEqual(actual, expected)
    def test_sevenRotations(self):
        spot = 'west'
        numberOfRotations = 7
        actual = helpers.getSpotAfterNRotations(spot, numberOfRotations)
        expected = 'south'
        self.assertEqual(actual, expected)
    def test_elevenRotations(self):
        spot = 'east'
        numberOfRotations = 11
        actual = helpers.getSpotAfterNRotations(spot, numberOfRotations)
        expected = 'north'
        self.assertEqual(actual, expected)
    def test_twelveRotations(self):
        spot = 'south'
        numberOfRotations = 12
        actual = helpers.getSpotAfterNRotations(spot, numberOfRotations)
        expected = 'south'
        self.assertEqual(actual, expected)
    def test_thirteenRotations(self):
        spot = 'north'
        numberOfRotations = 13
        actual = helpers.getSpotAfterNRotations(spot, numberOfRotations)
        expected = 'east'
        self.assertEqual(actual, expected)
class getRelativeLocationFromSpot(unittest.TestCase):
    def test_self(self):
        usersSpot = 'east'
        spotToGetLocationFor = 'east'
        actual = helpers.getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor)
        expected = 'bottom'
        self.assertEqual(expected, actual)
    def test_one(self):
        usersSpot = 'east'
        spotToGetLocationFor = 'south'
        actual = helpers.getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor)
        expected = 'left'
        self.assertEqual(expected, actual)
    def test_two(self):
        usersSpot = 'east'
        spotToGetLocationFor = 'west'
        actual = helpers.getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor)
        expected = 'top'
        self.assertEqual(expected, actual)
    def test_three(self):
        usersSpot = 'east'
        spotToGetLocationFor = 'north'
        actual = helpers.getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor)
        expected = 'right'
        self.assertEqual(expected, actual)
    def test_negative_one(self):
        usersSpot = 'south'
        spotToGetLocationFor = 'east'
        actual = helpers.getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor)
        expected = 'right'
        self.assertEqual(expected, actual)
    def test_negative_two(self):
        usersSpot = 'west'
        spotToGetLocationFor = 'east'
        actual = helpers.getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor)
        expected = 'top'
        self.assertEqual(expected, actual)
    def test_negative_three(self):
        usersSpot = 'north'
        spotToGetLocationFor = 'east'
        actual = helpers.getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor)
        expected = 'left'
        self.assertEqual(expected, actual)
    def test_negative_four(self):
        usersSpot = 'west'
        spotToGetLocationFor = 'south'
        actual = helpers.getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor)
        expected = 'right'
        self.assertEqual(expected, actual)
    def test_negative_five(self):
        usersSpot = 'north'
        spotToGetLocationFor = 'west'
        actual = helpers.getRelativeLocationFromSpot(usersSpot, spotToGetLocationFor)
        expected = 'right'
        self.assertEqual(expected, actual)
class getBiddingObjRelative(unittest.TestCase):
    def test_north(self):
        spot = 'north'
        biddingObjAbsolute = {
            "north": ['Pass', 'Double'],
            "east": ['Double', '1 Heart'],
            "south": ['Pass', '1 Spade'],
            "west": ['1 Diamond', '2 Diamond'],
        }
        expected = {
            "bottom": ['Pass', 'Double'],
            "left": ['Double', '1 Heart'],
            "top": ['Pass', '1 Spade'],
            "right": ['1 Diamond', '2 Diamond'],
        }
        actual = helpers.getBiddingObjRelative(biddingObjAbsolute, spot)
        self.assertDictEqual(expected, actual)
    def test_south(self):
        spot = 'south'
        biddingObjAbsolute = {
            "north": ['Pass', 'Double'],
            "east": ['Double', '1 Heart'],
            "south": ['Pass', '1 Spade'],
            "west": ['1 Diamond', '2 Diamond'],
        }
        expected = {
            "top": ['Pass', 'Double'],
            "right": ['Double', '1 Heart'],
            "bottom": ['Pass', '1 Spade'],
            "left": ['1 Diamond', '2 Diamond'],
        }
        actual = helpers.getBiddingObjRelative(biddingObjAbsolute, spot)
        self.assertDictEqual(expected, actual)
    def test_east(self):
        spot = 'east'
        biddingObjAbsolute = {
            "north": ['Pass', 'Double'],
            "east": ['Double', '1 Heart'],
            "south": ['Pass', '1 Spade'],
            "west": ['1 Diamond', '2 Diamond'],
        }
        expected = {
            "right": ['Pass', 'Double'],
            "bottom": ['Double', '1 Heart'],
            "left": ['Pass', '1 Spade'],
            "top": ['1 Diamond', '2 Diamond'],
        }
        actual = helpers.getBiddingObjRelative(biddingObjAbsolute, spot)
        self.assertDictEqual(expected, actual)
    def test_west(self):
        spot = 'west'
        biddingObjAbsolute = {
            "north": ['Pass', 'Double'],
            "east": ['Double', '1 Heart'],
            "south": ['Pass', '1 Spade'],
            "west": ['1 Diamond', '2 Diamond'],
        }
        expected = {
            "left": ['Pass', 'Double'],
            "top": ['Double', '1 Heart'],
            "right": ['Pass', '1 Spade'],
            "bottom": ['1 Diamond', '2 Diamond'],
        }
        actual = helpers.getBiddingObjRelative(biddingObjAbsolute, spot)
        self.assertDictEqual(expected, actual)
    def test_empty(self):
        spot = 'west'
        biddingObjAbsolute = {
            "north": [],
            "east": [],
            "south": [],
            "west": [],
        }
        expected = {
            "left": [],
            "top": [],
            "right": [],
            "bottom": [],
        }
        actual = helpers.getBiddingObjRelative(biddingObjAbsolute, spot)
        self.assertDictEqual(expected, actual)
class getSuitCounts(unittest.TestCase):
    def test_empty(self):
        hand = []
        actual = helpers.getSuitCountsFromHand(hand)
        expected = {
            "clubs": 0,
            "diamonds":  0,
            "hearts":  0,
            "spades": 0,
        }
        self.assertEqual(actual, expected)
    def test_one(self):
        hand = [[0, 1, 5, 7, 8], [13, 18, 19], [29, 30, 32], [40, 42]]
        actual = helpers.getSuitCountsFromHand(hand)
        expected = {
            "clubs": 5,
            "diamonds":  3,
            "hearts":  3,
            "spades": 2,
        }
        self.assertEqual(actual, expected)
    def test_two(self):
        hand = [[0, 1, 5, 7, 8,9,10], [13, 19], [29], [40, 42,51]]
        actual = helpers.getSuitCountsFromHand(hand)
        expected = {
            "clubs": 7,
            "diamonds":  2,
            "hearts":  1,
            "spades": 3,
        }
        self.assertEqual(actual, expected)
    def test_three(self):
        hand = [[0, 1, 2,3], [13,15,17,18, 19], [29,31,33,34], []]
        actual = helpers.getSuitCountsFromHand(hand)
        expected = {
            "clubs": 4,
            "diamonds":  5,
            "hearts":  4,
            "spades": 0,
        }
        self.assertEqual(actual, expected)
    def test_four(self):
        hand = [[0, 1, 2,3,4,5,6,7,8,9,10,11,12], [],[], []]
        actual = helpers.getSuitCountsFromHand(hand)
        expected = {
            "clubs": 13,
            "diamonds":  0,
            "hearts":  0,
            "spades": 0,
        }
        self.assertEqual(actual, expected)

#TODO: FINISH partnerTwoClubResponse
class partnerTwoClubResponse(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
    
    def test_intervention(self):
        biddingRelative = {
            "top": ['Two Club'],
            "left": ['One Diamond'],
        }
        totalOpeningPoints = 0
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingRelative, self.seatingRelative, totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Pass'
        self.assertEqual(actual, expected)
    def test_initial_zero(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 0
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingRelative, self.seatingRelative, totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Two Diamond'
        self.assertEqual(actual, expected)
    def test_initial_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 3
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingRelative, self.seatingRelative, totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Two Diamond'
        self.assertEqual(actual, expected)
    def test_initial_6(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 6
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingRelative, self.seatingRelative, totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Two Heart'
        self.assertEqual(actual, expected)
    def test_initial_9(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 9
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingRelative, self.seatingRelative, totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Two Spade'
        self.assertEqual(actual, expected)
    def test_initial_12(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 12
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingRelative, self.seatingRelative, totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Two No Trump'
        self.assertEqual(actual, expected)
    def test_initial_15(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "left": ['Pass'],
            "top": ['Two Club'],
        }
        totalOpeningPoints = 15
        currentActualBid = ['Adam', biddingRelative['top'][0]]
        actual = helpers.getTwoClubResponse([], biddingRelative, self.seatingRelative, totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Three Club'
        self.assertEqual(actual, expected)
    def test_ask_for_aces_one(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23, 24], [29, 30, 32], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Five Diamond'
        self.assertEqual(actual, expected)
    def test_ask_for_aces_two(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23,25], [29, 30, 32], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Five Heart'
        self.assertEqual(actual, expected)
    def test_ask_for_aces_three(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23,25], [29, 30, 38], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Five Spade'
        self.assertEqual(actual, expected)
    def test_ask_for_aces_four(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23,25], [29, 30, 38], [40,51]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Five Club'
        self.assertEqual(actual, expected)
    def test_ask_for_aces_none(self):
        hand = [[0, 1, 7, 8,11], [13, 18, 23,24], [29, 30, 37], [40,50]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Five Club'
        self.assertEqual(actual, expected)


    def test_ask_for_kings_pass(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23, 24], [29, 30, 32], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump', 'Five Diamond'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five Club']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Pass'
        self.assertEqual(actual, expected)
    def test_ask_for_kings_pass_NT(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23, 24], [29, 30, 32], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three No Trump', 'Four No Trump', 'Five No Trump'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Pass'
        self.assertEqual(actual, expected)
    def test_ask_for_kings_one(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23, 24], [29, 30, 32], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Club', 'Four No Trump', 'Five Diamond'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five Diamond']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Five Spade'
        self.assertEqual(actual, expected)
    def test_ask_for_kings_two(self):
        hand = [[0, 1, 7, 8,11], [13, 18, 23, 24], [29, 30, 32], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Club', 'Four No Trump', 'Five Heart'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five Heart']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Six Club'
        self.assertEqual(actual, expected)
    def test_ask_for_kings_three(self):
        hand = [[0, 1, 7, 8,11], [13, 18, 23, 24], [29, 30, 32], [40,50]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Club', 'Four No Trump', 'Five Spade'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five Spade']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Six Heart'
        self.assertEqual(actual, expected)
    def test_ask_for_kings_four(self):
        hand = [[0, 1, 7, 8,11], [13, 18, 23, 24], [29, 30, 37], [40,50]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Club', 'Four No Trump', 'Five No Trump'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Six Club'
        self.assertEqual(actual, expected)
    def test_ask_for_kings_none(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23,25], [29, 30, 38], [40,51]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "top": ['Two Club', 'Three Club', 'Four No Trump', 'Four Diamond'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four Diamond']
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Four Heart'
        self.assertEqual(actual, expected)

    def test_best_suit_same_as_first(self):
        handDictionary = {
            "clubs": "AKQJ",
            "diamonds": "AJ82",
            "hearts": "865",
            "spades": "32",
        }
        hand = helpers.getHandFromHandDictionary(handDictionary)
        
        biddingRelative = {
            "left": ['Pass', 'Pass'],
            "top": ['Two Club', 'Three Diamond'],
            "right": ['Pass', 'Pass'],
            "bottom": ['Three Club'],
        }
        totalOpeningPoints = 15
        currentActualBid = ['Adam', biddingRelative['top'][1]]
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Four Club'
        self.assertEqual(actual, expected)

    def test_best_suit_same_level(self):
        handDictionary = {
            "clubs": "32",
            "diamonds": "AKJ",
            "hearts": "83",
            "spades": "QJ8532",
        }
        hand = helpers.getHandFromHandDictionary(handDictionary)
        
        biddingRelative = {
            "left": ['Pass', 'Pass'],
            "top": ['Two Club', 'Three Diamond'],
            "right": ['Pass', 'Pass'],
            "bottom": ['Three Club'],
        }
        totalOpeningPoints = 14
        currentActualBid = ['Adam', biddingRelative['top'][1]]
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Three Spade'
        self.assertEqual(actual, expected)

    def test_best_suit_next_level(self):
        handDictionary = {
            "clubs": "32",
            "diamonds": "QJ8532",
            "hearts": "83",
            "spades": "543",
        }
        hand = helpers.getHandFromHandDictionary(handDictionary)
        
        biddingRelative = {
            "left": ['Pass', 'Pass'],
            "top": ['Two Club', 'Three Diamond'],
            "right": ['Pass', 'Pass'],
            "bottom": ['Two Spade'],
        }
        totalOpeningPoints = 7
        currentActualBid = ['Adam', biddingRelative['top'][1]]
        actual = helpers.getTwoClubResponse(hand, biddingRelative, self.seatingRelative,  totalOpeningPoints, currentActualBid, 'hcp')
        expected = 'Four Diamond'
        self.assertEqual(actual, expected)

class getSuitFromBid(unittest.TestCase):
    def test_empty(self):
        actual = helpers.getSuitFromBid('')
        expected = None
        self.assertEqual(actual, expected)
    def test_NT(self):
        actual = helpers.getSuitFromBid('Five No Trump')
        expected = 'No'
        self.assertEqual(actual, expected)
    def test_club(self):
        actual = helpers.getSuitFromBid('Two Club')
        expected = 'Club'
        self.assertEqual(actual, expected)
    def test_Diamond(self):
        actual = helpers.getSuitFromBid('Two Diamond')
        expected = 'Diamond'
        self.assertEqual(actual, expected)
    def test_Heart(self):
        actual = helpers.getSuitFromBid('Two Heart')
        expected = 'Heart'
        self.assertEqual(actual, expected)
    def test_Spade(self):
        actual = helpers.getSuitFromBid('Two Spade')
        expected = 'Spade'
        self.assertEqual(actual, expected)
class getStrongestSuit(unittest.TestCase):
    def tearDown(self):
        print(f"self.hand = {self.hand}")

    def test_HCP_over_length(self):
        handDictionary = {
            "clubs": "AKQJ",
            "diamonds": "53",
            "hearts": "65432",
            "spades": "53",
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'club'
        self.assertEqual(self.actual, self.expected)

    def test_crap_1(self):
        handDictionary = {
            "clubs": "6543",
            "diamonds": "T32",
            "hearts": "654",
            "spades": "532",
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['double'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'club'
        self.assertEqual(self.actual, self.expected)

    def test_crap_2(self):
        handDictionary = {
            "clubs": "6543",
            "diamonds": "AK2",
            "hearts": "654",
            "spades": "532",
        }
        
        biddingRelative = {
            "left": ['One Heart'],
            "top": ['double'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'diamond'
        self.assertEqual(self.actual, self.expected)

    def test_crap_3(self):
        handDictionary = {
            "clubs": "6543",
            "diamonds": "AKQ",
            "hearts": "654",
            "spades": "532",
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['double'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'diamond'
        self.assertEqual(self.actual, self.expected)

    def test_crap_4(self):
        handDictionary = {
            "clubs": "65432",
            "diamonds": "AKQ",
            "hearts": "65",
            "spades": "532",
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['double'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'diamond'
        self.assertEqual(self.actual, self.expected)

    def test_crap_5(self):
        handDictionary = {
            "clubs": "65432",
            "diamonds": "AK",
            "hearts": "654",
            "spades": "532",
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['double'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'club'
        self.assertEqual(self.actual, self.expected)

    def test_crap_6(self):
        handDictionary = {
            "clubs": "65432",
            "diamonds": "J543",
            "hearts": "543",
            "spades": "2",
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['double'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'club'
        self.assertEqual(self.actual, self.expected)

    def test_no_mentionable_suit_but_higher_than_threshold_points(self):
        handDictionary = {
            "clubs": "52",
            "diamonds": "432",
            "hearts": "6543",
            "spades": "A653",
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['Double'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'spade'
        self.assertEqual(self.actual, self.expected)

    def test_no_mentionable_suit_but_less_than_or_equal_to_threshold_points(self):
        handDictionary = {
            "clubs": "52",
            "diamonds": "432",
            "hearts": "6543",
            "spades": "Q653",
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['Double'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'no trump'
        self.assertEqual(self.actual, self.expected)

    def test_Diamond_better(self):
        handDictionary = {
            "clubs": "AT932",
            "diamonds": "AQJ2",
            "hearts": "965",
            "spades": "53",
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'diamond'
        self.assertEqual(self.actual, self.expected)

    def test_opponents_mentioned_my_best_suit(self):
        handDictionary = {
            "clubs": "T932",
            "diamonds": "AKQ72",
            "hearts": "965",
            "spades": "53",
        }
        
        biddingRelative = {
            "left": ['One Diamond'],
            "top": ['Double'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'club'
        self.assertEqual(self.actual, self.expected)
    
    def test_same_score_but_one_is_major(self):
        handDictionary = {
            "clubs": "932",
            "diamonds": "A72",
            "hearts": "T9865",
            "spades": "53"
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'heart'
        self.assertEqual(self.actual, self.expected)

    def test_same_score_but_both_major(self):
        handDictionary = {
            "clubs": "932",
            "diamonds": "32",
            "hearts": "T9865",
            "spades": "A72"
        }
        
        biddingRelative = {
            "left": ['Pass'],
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": [],
        }

        self.hand = helpers.getHandFromHandDictionary(handDictionary)
        self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
        self.expected = 'heart'
        self.assertEqual(self.actual, self.expected)
    


    # def test_respond_same_suit_1(self):
    #     handDictionary = {
    #         "clubs": [0, 1, 7, 8, 12],
    #         "diamonds": [0, 5, 10, 11],
    #         "hearts": [3, 4, 6],
    #         "spades": [1,3]
    #     }
        
    #     biddingRelative = {
    #         "left": ['Pass'],
    #         "top": ['One Club'],
    #         "right": ['Pass'],
    #         "bottom": [],
    #     }

    #     self.hand = helpers.getHandFromHandDictionary(handDictionary)
    #     self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
    #     self.expected = 'club'
    #     self.assertEqual(self.actual, self.expected)
    # def test_respond_other_suit_1(self):
    #     handDictionary = {
    #         "clubs": [0, 1, 7, 8, 11],
    #         "diamonds": [0, 5, 10, 11],
    #         "hearts": [3, 4, 6],
    #         "spades": [1,3]
    #     }
        
    #     biddingRelative = {
    #         "left": ['Pass'],
    #         "top": ['One Club'],
    #         "right": ['Pass'],
    #         "bottom": [],
    #     }

    #     self.hand = helpers.getHandFromHandDictionary(handDictionary)
    #     self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
    #     self.expected = 'diamond'
    #     self.assertEqual(self.actual, self.expected)
    # def test_respond_length(self):
    #     handDictionary = {
    #         "clubs": [0, 1, 7],
    #         "diamonds": [0, 5, 12],
    #         "hearts": [3,4,6,7,8],
    #         "spades": [1,3]
    #     }
        
    #     biddingRelative = {
    #         "left": ['Pass'],
    #         "top": ['One Club'],
    #         "right": ['Pass'],
    #         "bottom": [],
    #     }

    #     self.hand = helpers.getHandFromHandDictionary(handDictionary)
    #     self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
    #     self.expected = 'heart'
    #     self.assertEqual(self.actual, self.expected)
    # def test_respond_points_over_length(self):
    #     handDictionary = {
    #         "clubs": [0, 1, 7],
    #         "diamonds": [0],
    #         "hearts": [3,4,6,7,8],
    #         "spades": [9,10,11,12]
    #     }
        
    #     biddingRelative = {
    #         "left": ['Pass'],
    #         "top": ['One Club'],
    #         "right": ['Pass'],
    #         "bottom": [],
    #     }

    #     self.hand = helpers.getHandFromHandDictionary(handDictionary)
    #     self.actual = helpers.getStrongestSuit(self.hand, biddingRelative, 'hcp')
    #     self.expected = 'spade'
    #     self.assertEqual(self.actual, self.expected)

class getSuitsMentionedByOpponents(unittest.TestCase):
    def test_five(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "right": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Two Heart', 'Three Spade'],
            "bottom": ['Pass', 'Pass'],
            "top": ['Pass', 'Pass'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingRelative)
        expected = {
            "clubs": True,
            "diamonds": True,
            "hearts": True,
            "spades": True,
            "noTrump": True,
        }
        self.assertDictEqual(actual, expected)
    def test_four(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "right": ['Pass', 'Three Diamond', 'Four No Trump'],
            "left": ['Two Heart', 'Three Spade'],
            "bottom": ['Two Club', 'Pass'],
            "top": ['Pass', 'Three Club'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingRelative)
        expected = {
            "clubs": False,
            "diamonds": True,
            "hearts": True,
            "spades": True,
            "noTrump": True,
        }
        self.assertDictEqual(actual, expected)
    def test_three(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "right": ['Pass', 'Three Diamond', 'Pass'],
            "left": ['Two Heart', 'Three Spade'],
            "bottom": ['Two Club', 'Pass'],
            "top": ['Three No Trump', 'Three Club'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingRelative)
        expected = {
            "clubs": False,
            "diamonds": True,
            "hearts": True,
            "spades": True,
            "noTrump": False,
        }
        self.assertDictEqual(actual, expected)
    def test_two(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "right": ['Pass', 'Three Diamond', 'Double'],
            "left": ['Double', 'Three Spade'],
            "bottom": ['Two Club', 'Pass'],
            "top": ['Three No Trump', 'Three Club'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingRelative)
        expected = {
            "clubs": False,
            "diamonds": True,
            "hearts": False,
            "spades": True,
            "noTrump": False,
        }
        self.assertDictEqual(actual, expected)
    def test_one(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "right": ['Pass', 'Three Club', 'Pass'],
            "left": ['Double', 'Four Club'],
            "bottom": ['Two Club', 'Pass'],
            "top": ['Three No Trump', 'Three Club'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingRelative)
        expected = {
            "clubs": True,
            "diamonds": False,
            "hearts": False,
            "spades": False,
            "noTrump": False,
        }
        self.assertDictEqual(actual, expected)
    def test_none(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "right": ['Pass', 'Double', 'Pass'],
            "left": ['Double', 'Pass'],
            "bottom": ['Two Club', 'Three Diamond'],
            "top": ['Three No Trump', 'Three Club'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingRelative)
        expected = {
            "clubs": False,
            "diamonds": False,
            "hearts": False,
            "spades": False,
            "noTrump": False,
        }
        self.assertDictEqual(actual, expected)
class getBiddingHistory(unittest.TestCase):
    def test_none(self):
        bids = []
        actual = helpers.getBiddingHistory(bids)
        expected = []
        self.assertListEqual(expected, actual)
    def test_Bids(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        actual = helpers.getBiddingHistory(bids)
        expected = ['2 No Trump', 'Double', '3 Club', 'Pass', 'Double']
        self.assertListEqual(expected, actual)
class getIsTeamsFirstBidOpportunity(unittest.TestCase):
    def test_top(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        actual = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, 'top')
        expected = True
        self.assertEqual(actual, expected)
    def test_bottom(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        actual = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, 'bottom')
        expected = False
        self.assertEqual(actual, expected)
    def test_right(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        actual = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, 'right')
        expected = False
        self.assertEqual(actual, expected)
    def test_left(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        actual = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, 'left')
        expected = True
        self.assertEqual(actual, expected)
    def test_left_2(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['pass', 'two diamond'],
            "right": ['pass', 'pass'],
            "bottom": ['two club'],
        }
        actual = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, 'left')
        expected = False
        self.assertEqual(actual, expected)
    def test_top_2(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['pass', 'two diamond'],
            "right": ['pass', 'pass'],
            "bottom": ['two club'],
        }
        actual = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, 'top')
        expected = False
        self.assertEqual(actual, expected)
    def test_bottom_2(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['pass', 'two diamond'],
            "right": ['pass', 'pass'],
            "bottom": ['two club'],
        }
        actual = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, 'bottom')
        expected = False
        self.assertEqual(actual, expected)
    def test_right_2(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['pass', 'two diamond'],
            "right": ['pass', 'pass'],
            "bottom": ['two club'],
        }
        actual = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, 'right')
        expected = False
        self.assertEqual(actual, expected)
    def test_right_3(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        actual = helpers.getIsTeamsFirstBidOpportunity(biddingRelative, 'right')
        expected = True
        self.assertEqual(actual, expected)
class getIsBidGameBid(unittest.TestCase):
    def test_empty(self):
        bid = ''
        actual = helpers.getIsBidGameBid(bid)
        expected = None
        self.assertEqual(actual, expected)
    def test_none(self):
        bid = None
        actual = helpers.getIsBidGameBid(bid)
        expected = None
        self.assertEqual(actual, expected)
    def test_lower(self):
        bid = 'Four Diamond'
        actual = helpers.getIsBidGameBid(bid)
        expected = False
        self.assertEqual(actual, expected)
    def test_3NT(self):
        bid = 'Three No Trump'
        actual = helpers.getIsBidGameBid(bid)
        expected = True
        self.assertEqual(actual, expected)
    def test_Four_Hearts(self):
        bid = 'Four Heart'
        actual = helpers.getIsBidGameBid(bid)
        expected = True
        self.assertEqual(actual, expected)
    def test_higher(self):
        bid = 'Four Spade'
        actual = helpers.getIsBidGameBid(bid)
        expected = True
        self.assertEqual(actual, expected)
class getHasPartnerOpened(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
    def tearDown(self) -> None:
        print('')
        print('bids = {0}'.format(self.bids))
        print('expected = {0}'.format(self.expected))
        print('self.actual ={0}'.format(self.actual))
        print('')

    def test_incorrect_name(self):
        self.biddingRelative = {
            "left": ['pass', 'double'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'Anns')
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_false(self):
        self.biddingRelative = {
            "left": ['pass', 'double'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'RightPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_false_2(self):
        self.biddingRelative = {
            "left": ['double', 'double'],
            "top": ['pass', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'BottomPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_false_3(self):
        self.biddingRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['Two Club'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'LeftPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_true_4(self):
        self.biddingRelative = {
            "left": ['pass', 'Two Diamond'],
            "top": ['pass', 'pass'],
            "right": ['Two Club', 'Two Heart'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'LeftPlayer')
        self.expected = True
        self.assertEqual(self.expected, self.actual)  
    def test_false_4(self):
        self.biddingRelative = {
            "left": ['Two Club'],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'LeftPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_false_5(self):
        self.biddingRelative = {
            "left": ['Two Club'],
            "top": ['pass'],
            "right": ['Two Diamond'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'LeftPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_true_3(self):
        self.biddingRelative = {
            "left": ['Two Club'],
            "top": ['pass'],
            "right": ['Two Diamond'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'RightPlayer')
        self.expected = True
        self.assertEqual(self.expected, self.actual)   
    def test_true(self):
        self.biddingRelative = {
            "left": ['Two No Trump', 'double'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['three diamond'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'RightPlayer')
        self.expected = True
        self.assertEqual(self.expected, self.actual) 
    def test_length_1(self):
        self.biddingRelative = {
            "left": [],
            "top": [],
            "right": ['pass'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'TopPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_length_0(self):
        self.biddingRelative = {
            "left": [],
            "top": [],
            "right": [],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'TopPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_length_3(self):
        self.biddingRelative = {
            "left": ['Two No Trump'],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'TopPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_true_2(self):
        self.biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['pass', 'One Spade'],
            "right": ['One Club', 'pass'],
            "bottom": ['One Diamond'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'BottomPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_2nd_bid_open(self):
        self.biddingRelative = {
            "left": ['pass', 'Two No Trump'],
            "top": ['One Club', 'pass'],
            "right": ['Pass', 'Three Heart'],
            "bottom": ['Two Diamond'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'RightPlayer')
        self.expected = True
        self.assertEqual(self.expected, self.actual) 
    def test_not_opened_2_opportunities_1(self):
        self.biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['One Club', 'pass'],
            "right": ['Double', 'pass'],
            "bottom": ['One Diamond'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'TopPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_not_opened_2_opportunities_2(self):
        self.biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['One Club', 'pass'],
            "right": ['pass', 'double'],
            "bottom": ['One Diamond'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'LeftPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_not_opened_2_opportunities_3(self):
        self.biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'pass'],
            "right": ['pass', 'double'],
            "bottom": ['One Diamond'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'LeftPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_not_opened_3_opportunities_1(self):
        self.biddingRelative = {
            "left": ['pass', 'One Heart', 'pass'],
            "top": ['One Club', 'pass', 'pass'],
            "right": ['pass', 'double', 'Two Heart'],
            "bottom": ['One Diamond','pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'LeftPlayer')
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_not_opened_3_opportunities_2(self):
        self.biddingRelative = {
            "left": ['pass', 'pass', 'One Heart'],
            "top": ['One Club', 'pass', 'pass'],
            "right": ['pass', 'double', 'Two Heart'],
            "bottom": ['One Diamond','pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'RightPlayer')
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    def test_not_opened_4_opportunities_1(self):
        self.biddingRelative = {
            "left": ['pass', 'pass', 'pass', 'Two Club'],
            "top": ['One Club', 'pass', 'pass', 'Three Diamond'],
            "right": ['pass', 'pass', 'double', 'pass'],
            "bottom": ['pass','pass', 'double', 'One Club'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'LeftPlayer')
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    
    def test_true_5(self):
        self.biddingRelative =  {
            "left": ['One No Trump', 'Four Spade'],
            "top": ['pass', 'Pass'],
            "right": ['Two Spade', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpened(self.bids, self.seatingRelative, 'RightPlayer')
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    
   

class getHasPartnerOpenedNoTrump(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
    def tearDown(self) -> None:
        print('')
        print('biddingRelative = {0}'.format(self.biddingRelative))
        print('expected = {0}'.format(self.expected))
        print('self.actual ={0}'.format(self.actual))
        print('')

    def test_False_1(self):
        self.partnersLocation = "right"
        self.location = "left"
        self.biddingRelative = {
            "left": ['pass'],
            "top": ['pass'],
            "right": ['One No Trump'],
            "bottom": [],
        }
        self.biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpenedNoTrump(self.location, self.partnersLocation, self.biddingRelative, self.biddingAbsolute, self.seatingRelative)
        self.expected = False
        self.assertEqual(self.actual, self.expected)
    def test_True_1(self):
        self.partnersLocation = "right"
        self.location = "left"
        self.biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['pass', 'pass'],
            "right": ['One No Trump', 'One Spade'],
            "bottom": ['pass'],
        }
        self.biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpenedNoTrump(self.location, self.partnersLocation, self.biddingRelative, self.biddingAbsolute, self.seatingRelative)
        self.expected = True
        self.assertEqual(self.actual, self.expected)
    def test_True_2(self):
        self.partnersLocation = "left"
        self.location = "right"
        self.biddingRelative = {
            "left": ['One No Trump'],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        self.biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasPartnerOpenedNoTrump(self.location, self.partnersLocation, self.biddingRelative, self.biddingAbsolute, self.seatingRelative)
        self.expected = True
        self.assertEqual(self.actual, self.expected)
class getIndexOfNthBid(unittest.TestCase):
    def test_invalid(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        actual = helpers.getIndexOfNthBid('Tim', bids, 2)
        expected = None
        self.assertEqual(expected, actual) 
    def test_valid_0(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double']]
        actual = helpers.getIndexOfNthBid('Adam', bids, 1)
        expected = 0
        self.assertEqual(expected, actual) 
    def test_valid_1(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        actual = helpers.getIndexOfNthBid('Tim', bids, 1)
        expected = 1
        self.assertEqual(expected, actual) 
    def test_valid_2(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        actual = helpers.getIndexOfNthBid('Adam', bids, 2)
        expected = 4
        self.assertEqual(expected, actual) 
    def test_valid_3(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass']]
        actual = helpers.getIndexOfNthBid('Andrew', bids, 2)
        expected = 7
        self.assertEqual(expected, actual) 
    def test_incorrectUsername(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass']]
        actual = helpers.getIndexOfNthBid('andrew', bids, 2)
        expected = None
        self.assertEqual(expected, actual) 
    def test_no_bids(self):
        bids = []
        actual = helpers.getIndexOfNthBid('Adam', bids, 2)
        expected = None
        self.assertEqual(expected, actual) 
    def test_valid_negative_1(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        actual = helpers.getIndexOfNthBid('Tim', bids, -1)
        expected = 1
        self.assertEqual(expected, actual) 
    def test_valid_negative_2(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double'], ['Tim', '2 No Trump'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        actual = helpers.getIndexOfNthBid('Tim', bids, -1)
        expected = 5
        self.assertEqual(expected, actual) 
    def test_valid_negative_3(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double'], ['Tim', '2 No Trump'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double'], ['Tim', '2 No Trump'], ['Ann', '3 Club'], ['Andrew', 'Pass']]
        actual = helpers.getIndexOfNthBid('Tim', bids, -1)
        expected = 9
        self.assertEqual(expected, actual) 
class getSeatingRelative(unittest.TestCase):
    def test_valid_north(self):
        spot = 'north'
        seating = {
            "north": 'Adam',
            "east": 'Dan',
            "south": 'Ann',
            "west": "Andrew",
        }
        actual = helpers.getSeatingRelative(seating, spot)
        expected = {
            "bottom": 'Adam',
            "left": 'Dan',
            "top": 'Ann',
            "right": "Andrew",
        }
        self.assertDictEqual(expected, actual) 
    def test_valid_east(self):
        spot = 'east'
        seating = {
            "north": 'Adam',
            "east": 'Dan',
            "south": 'Ann',
            "west": "Andrew",
        }
        actual = helpers.getSeatingRelative(seating, spot)
        expected = {
            "bottom": 'Dan',
            "left": 'Ann',
            "top": 'Andrew',
            "right": "Adam",
        }
        self.assertDictEqual(expected, actual) 
    def test_valid_south(self):
        spot = 'south'
        seating = {
            "north": 'Adam',
            "east": 'Dan',
            "south": 'Ann',
            "west": "Andrew",
        }
        actual = helpers.getSeatingRelative(seating, spot)
        expected = {
            "bottom": 'Ann',
            "left": 'Andrew',
            "top": 'Adam',
            "right": "Dan",
        }
        self.assertDictEqual(expected, actual) 
    def test_valid_west(self):
        spot = 'west'
        seating = {
            "north": 'Adam',
            "east": 'Dan',
            "south": 'Ann',
            "west": "Andrew",
        }
        actual = helpers.getSeatingRelative(seating, spot)
        expected = {
            "bottom": 'Andrew',
            "left": 'Adam',
            "top": 'Dan',
            "right": "Ann",
        }
        self.assertDictEqual(expected, actual) 
class getIsJumpShift(unittest.TestCase):
    def test_pass(self):
        currentContractBid = 'Two Club';
        usersBid = 'Pass'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)

    def test_pass_2(self):
        currentContractBid = 'Pass';
        usersBid = 'Two Club'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_double(self):
        currentContractBid = 'Two Club';
        usersBid = 'Double'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_noActualBid(self):
        currentContractBid = "";
        usersBid = 'Three Club';
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_False_1(self):
        currentContractBid = 'Two Club';
        usersBid = 'Three Club'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_False_2(self):
        currentContractBid = 'Two Club';
        usersBid = 'Two Diamond'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_False_3(self):
        currentContractBid = 'One Spade';
        usersBid = 'One No Trump'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_True_1(self):
        currentContractBid = 'One Club';
        usersBid = 'Three Club'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = True
        self.assertEqual(actual, expected)
    def test_True_2(self):
        currentContractBid = 'One No Trump';
        usersBid = 'Three Club'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = True
        self.assertEqual(actual, expected)
    def test_True_3(self):
        currentContractBid = 'Three Spade';
        usersBid = 'Five No Trump'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = True
        self.assertEqual(actual, expected)
    def test_currentContractBidIsString(self):
        currentContractBid = 'Three Spade'
        usersBid = 'Five No Trump'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = True
        self.assertEqual(actual, expected)
class getHasPlayerJumpShifted(unittest.TestCase):
    def test_True_1(self):
        username = 'You'
        biddingAbsolute = [['Tim', 'Pass'],['Tom', 'Pass'],['James', 'One Club'],['You', 'Pass'],['Tim', 'One Diamond'],['Tom', 'Pass'],['James', 'Pass'],['You', 'Two Heart'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass']]
        playersBids = ['Pass','Two Heart']
        actual = helpers.getHasPlayerJumpshifted(username, playersBids, biddingAbsolute)
        expected = True
        self.assertEqual(actual, expected)
    def test_True_2(self):
        username = 'You'
        biddingAbsolute = [['Tim', 'Pass'],['Tom', 'Pass'],['James', 'One Club'],['You', 'Pass'],['Tim', 'One Diamond'],['Tom', 'Pass'],['James', 'Pass'],['You', 'One Heart'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass'], ['You', 'Three Club'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass']]
        playersBids = ['Pass', 'One Heart', 'Three Club']
        actual = helpers.getHasPlayerJumpshifted(username, playersBids, biddingAbsolute)
        expected = True
        self.assertEqual(actual, expected)
    def test_False_1(self):
        username = 'You'
        biddingAbsolute = [['Tim', 'Pass'],['Tom', 'Pass'],['James', 'One Club'],['You', 'Pass'],['Tim', 'One Diamond'],['Tom', 'Pass'],['James', 'Pass'],['You', 'Two Heart'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass']]
        playersBids = ['Pass','One Heart']
        actual = helpers.getHasPlayerJumpshifted(username, playersBids, biddingAbsolute)
        expected = False
        self.assertEqual(actual, expected)
    def test_False_2(self):
        username = 'You'
        biddingAbsolute = [['Tim', 'Pass'],['Tom', 'Pass'],['James', 'One Club'],['You', 'Pass'],['Tim', 'One Diamond'],['Tom', 'Pass'],['James', 'Pass'],['You', 'One Heart'],['Tim', 'Two Spade'],['Tom', 'Pass'],['James', 'Pass'], ['You', 'Three Club'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass']]
        playersBids = ['Pass', 'One Heart', 'Three Club']
        actual = helpers.getHasPlayerJumpshifted(username, playersBids, biddingAbsolute)
        expected = False
        self.assertEqual(actual, expected)
class getHasSomeOneOpenedBefore(unittest.TestCase):
    def test_empty(self):
        indexOfUsersFirstBid = None
        biddingAbsolute = []
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute)
        expected = False
        self.assertEqual(actual, expected)
    def test_not_yet_bid_false_1(self):
        indexOfUsersFirstBid = None
        biddingAbsolute = [['Adam', 'Pass']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute)
        expected = False
        self.assertEqual(actual, expected)
    def test_not_yet_bid_false_2(self):
        indexOfUsersFirstBid = None
        biddingAbsolute = [['Adam', 'Pass'], ['Tim', 'Double']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute)
        expected = False
        self.assertEqual(actual, expected)
    def test_not_yet_bid_true_1(self):
        indexOfUsersFirstBid = None
        biddingAbsolute = [['Adam', 'Pass'], ['Tim', 'Two Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute)
        expected = True
        self.assertEqual(actual, expected)
    def test_not_yet_bid_true_2(self):
        indexOfUsersFirstBid = None
        biddingAbsolute = [['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute)
        expected = True
        self.assertEqual(actual, expected)

    def test_has_bid_false_1(self):
        indexOfUsersFirstBid = 2
        biddingAbsolute = [['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club'],['Andrew','Pass'],['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute)
        expected = False
        self.assertEqual(actual, expected)
    def test_has_bid_false_2(self):
        indexOfUsersFirstBid = 0
        biddingAbsolute = [['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Pass'],['Andrew','One Heart'],['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute)
        expected = False
        self.assertEqual(actual, expected)
    def test_has_bid_true_1(self):
        indexOfUsersFirstBid = 3
        biddingAbsolute = [['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club'],['Andrew','Pass'],['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute)
        expected = True
        self.assertEqual(actual, expected)
    def test_has_bid_true_2(self):
        indexOfUsersFirstBid = 4
        biddingAbsolute = [['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Pass'],['Andrew','One Heart'],['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, biddingAbsolute)
        expected = True
        self.assertEqual(actual, expected)
class getPartnersLocation(unittest.TestCase):
    def test_empty(self):
        username = ''
        seatingRelative = {
            "top": "Adam",
            "bottom": "Tim",
            "left": "Andrew",
            "right": "Ann",
        }
        actual = helpers.getPartnersLocation(username, seatingRelative)
        expected = None
        self.assertEqual(actual, expected)
    def test_incorrectCase(self):
        username = 'AdAm'
        seatingRelative = {
            "top": "Adam",
            "bottom": "Tim",
            "left": "Andrew",
            "right": "Ann",
        }
        actual = helpers.getPartnersLocation(username, seatingRelative)
        expected = None
        self.assertEqual(actual, expected)
    def test_top(self):
        username = 'Tim'
        seatingRelative = {
            "top": "Adam",
            "bottom": "Tim",
            "left": "Andrew",
            "right": "Ann",
        }
        actual = helpers.getPartnersLocation(username, seatingRelative)
        expected = 'top'
        self.assertEqual(actual, expected)
    def test_bottom(self):
        username = 'Adam'
        seatingRelative = {
            "top": "Adam",
            "bottom": "Tim",
            "left": "Andrew",
            "right": "Ann",
        }
        actual = helpers.getPartnersLocation(username, seatingRelative)
        expected = 'bottom'
        self.assertEqual(actual, expected)
    def test_left(self):
        username = 'Andrew'
        seatingRelative = {
            "left": "Adam",
            "bottom": "Tim",
            "right": "Andrew",
            "top": "Ann",
        }
        actual = helpers.getPartnersLocation(username, seatingRelative)
        expected = 'left'
        self.assertEqual(actual, expected)
    def test_right(self):
        username = 'Andrew'
        seatingRelative = {
            "top": "Adam",
            "bottom": "Tim",
            "left": "Andrew",
            "right": "Ann",
        }
        actual = helpers.getPartnersLocation(username, seatingRelative)
        expected = 'right'
        self.assertEqual(actual, expected)
class getPlayerHasOnlyPassed(unittest.TestCase):
    def test_empty(self):
        bids = []
        actual = helpers.getPlayerHasOnlyPassed(bids)
        expected = True
        self.assertEqual(actual, expected)
    def test_only_pass_one(self):
        bids = ['Pass']
        actual = helpers.getPlayerHasOnlyPassed(bids)
        expected = True
        self.assertEqual(actual, expected)
    def test_only_pass_multiple(self):
        bids = ['Pass', 'pass', 'Pass']
        actual = helpers.getPlayerHasOnlyPassed(bids)
        expected = True
        self.assertEqual(actual, expected)
    def test_bid_one(self):
        bids = ['Two Club']
        actual = helpers.getPlayerHasOnlyPassed(bids)
        expected = False
        self.assertEqual(actual, expected)
    def test_bid_multiple(self):
        bids = ['Pass', 'Three Diamond', 'Pass']
        actual = helpers.getPlayerHasOnlyPassed(bids)
        expected = False
        self.assertEqual(actual, expected)
class getLocationAfterRotationsAround(unittest.TestCase):
    def test_top(self):
        location = 'top'
        numberOfRotations = 1
        actual = helpers.getLocationAfterRotationsAround(location, numberOfRotations)
        expected = 'right'
        self.assertEqual(actual, expected)
    def test_top_1(self):
        location = 'top'
        numberOfRotations = 5
        actual = helpers.getLocationAfterRotationsAround(location, numberOfRotations)
        expected = 'right'
        self.assertEqual(actual, expected)
    def test_top_2(self):
        location = 'top'
        numberOfRotations = 9
        actual = helpers.getLocationAfterRotationsAround(location, numberOfRotations)
        expected = 'right'
        self.assertEqual(actual, expected)
    def test_right(self):
        location = 'right'
        numberOfRotations = 3
        actual = helpers.getLocationAfterRotationsAround(location, numberOfRotations)
        expected = 'top'
        self.assertEqual(actual, expected)
    def test_negative_1(self):
        location = 'right'
        numberOfRotations = -1
        actual = helpers.getLocationAfterRotationsAround(location, numberOfRotations)
        expected = 'top'
        self.assertEqual(actual, expected)
    def test_negative_2(self):
        location = 'top'
        numberOfRotations = -2
        actual = helpers.getLocationAfterRotationsAround(location, numberOfRotations)
        expected = 'bottom'
        self.assertEqual(actual, expected)
    def test_negative_3(self):
        location = 'top'
        numberOfRotations = -3
        actual = helpers.getLocationAfterRotationsAround(location, numberOfRotations)
        expected = 'right'
        self.assertEqual(actual, expected)
class getHasSomeoneOpenedTwoClubs(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
        self.actual = None
        self.expected = None
        self.bids = None

    def tearDown(self) -> None:
        print('actual ={0}'.format(self.actual))
        print('expected = {0}'.format(self.expected))
        print('bids = {0}'.format(self.bids))


    def test_empty(self):
        biddingRelative = {
            "left": [],
            "top": [],
            "right": [],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasSomeoneOpenedTwoClubs(self.bids, biddingRelative, self.seatingRelative)
        self.expected = (False, None)
        self.assertTupleEqual(self.actual, self.expected)

    def test_overcall(self):
        biddingRelative = {
            "left": ['One Diamond'],
            "top": ['Two Club'],
            "right": ['Pass'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasSomeoneOpenedTwoClubs(self.bids, biddingRelative, self.seatingRelative)
        self.expected = (False, None)
        self.assertTupleEqual(self.actual, self.expected)

    def test_overcall_multiple(self):
        biddingRelative = {
            "left": ['Pass', 'Two Club', 'pass'],
            "top": ['One Diamond', 'Pass', 'Pass'],
            "right": ['One No Trump', 'Three Club', 'Four Club'],
            "bottom": ['Pass', 'Pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasSomeoneOpenedTwoClubs(self.bids, biddingRelative, self.seatingRelative)
        self.expected = (False, None)
        self.assertTupleEqual(self.actual, self.expected)

    def test_is_actual_two_club_first_bidder_one_opportunity(self):
        biddingRelative = {
            "left": [],
            "top": ['Pass'],
            "right": ['Two Club'],
            "bottom": [],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasSomeoneOpenedTwoClubs(self.bids, biddingRelative, self.seatingRelative)
        self.expected = (True, "RightPlayer")
        self.assertTupleEqual(self.actual, self.expected)
    def test_is_actual_two_club_fourth_bidder_one_opportunity(self):
        biddingRelative = {
            "left": ['Two Club'],
            "top": ['Pass', 'Pass'],
            "right": ['Pass', 'Three Club'],
            "bottom": ['Pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasSomeoneOpenedTwoClubs(self.bids, biddingRelative, self.seatingRelative)
        self.expected = (True, "LeftPlayer")
        self.assertTupleEqual(self.actual, self.expected)

    def test_is_actual_two_club_fourth_bidder_multiple_opportunities(self):
        biddingRelative = {
            "left": ['Two Club', 'Three Spade'],
            "top": ['Pass', 'Pass', 'Pass'],
            "right": ['Pass', 'Three Club', 'Four Club'],
            "bottom": ['Pass', 'Pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasSomeoneOpenedTwoClubs(self.bids, biddingRelative, self.seatingRelative)
        self.expected = (True, "LeftPlayer")
        self.assertTupleEqual(self.actual, self.expected)
    
    def test_is_actual_two_club_second_bidder_one_opportunity(self):
        biddingRelative = {
            "left": ['Two Club'],
            "top": ['Pass'],
            "right": ['Pass'],
            "bottom": ['Pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasSomeoneOpenedTwoClubs(self.bids, biddingRelative, self.seatingRelative)
        self.expected = (True, "LeftPlayer")
        self.assertTupleEqual(self.actual, self.expected)

    def test_is_actual_two_club_second_bidder_multiple_opportunities(self):
        biddingRelative = {
            "left": ['Two Club', 'Three Spade'],
            "top": ['Pass', 'Pass', 'Pass'],
            "right": ['Pass', 'Three Club', 'Four Club'],
            "bottom": ['Pass', 'Pass', 'Pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasSomeoneOpenedTwoClubs(self.bids, biddingRelative, self.seatingRelative)
        self.expected = (True, "LeftPlayer")
        self.assertTupleEqual(self.actual, self.expected)

class getIndexDifferenceOfBids(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaises(TypeError) as context:
            helpers.getIndexDifferenceOfBids('Two Diamonds', 'Two Club')
     
    def test_invalid_2(self):
        with self.assertRaises(TypeError) as context:
            helpers.getIndexDifferenceOfBids('', '')

    def test_pass(self):
        actual = helpers.getIndexDifferenceOfBids('Pass', 'Two Club')
        expected = 0
        self.assertEqual(actual, expected)

    def test_pass(self):
        actual = helpers.getIndexDifferenceOfBids('Double', 'Two Club')
        expected = 0
        self.assertEqual(actual, expected)

    def test_valid_1(self):
        actual = helpers.getIndexDifferenceOfBids('Two Diamond', 'Two Club')
        expected = 1
        self.assertEqual(actual, expected)
    def test_valid_2(self):
        actual = helpers.getIndexDifferenceOfBids('Two Diamond', 'Two Spade')
        expected = 2
        self.assertEqual(actual, expected)

    def test_valid_3(self):
        actual = helpers.getIndexDifferenceOfBids('Two Diamond', 'Three Diamond')
        expected = 5
        self.assertEqual(actual, expected)

    def test_valid_4(self):
        actual = helpers.getIndexDifferenceOfBids('Four No Trump', 'Six No Trump')
        expected = 10
        self.assertEqual(actual, expected)

class getHighCardPointValuesInEachSuit(unittest.TestCase):
    def test_none(self):
        hand = [
            [0,1,3,4],
            [13,14,16],
            [27,28,29],
            [40,41,42],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'hcp')
        expected = {
            "clubs": 0,
            "diamonds": 0,
            "hearts": 0,
            "spades": 0,
         }
        self.assertEqual(actual, expected)
    def test_HCP_Ace(self):
        hand = [
            [0,1,3,4,12],
            [13,14,16],
            [27,28,29],
            [40,41,42],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'hcp')
        expected = {
            "clubs": 4,
            "diamonds": 0,
            "hearts": 0,
            "spades": 0,
         }
        self.assertEqual(actual, expected)
    def test_HCP_King(self):
        hand = [
            [0,1,3,4],
            [13,14,24],
            [27,28,29],
            [40,41,42],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'hcp')
        expected = {
            "clubs": 0,
            "diamonds": 3,
            "hearts": 0,
            "spades": 0,
         }
        self.assertEqual(actual, expected)
    def test_HCP_Queen(self):
        hand = [
            [0,1,3,4],
            [13,14,16],
            [27,28,36],
            [40,41,42],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'hcp')
        expected = {
            "clubs": 0,
            "diamonds": 0,
            "hearts": 2,
            "spades": 0,
         }
        self.assertEqual(actual, expected)
    def test_HCP_jack(self):
        hand = [
            [0,1,3,4],
            [13,14,16],
            [27,28,29],
            [40,41,48],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'hcp')
        expected = {
            "clubs": 0,
            "diamonds": 0,
            "hearts": 0,
            "spades": 1,
         }
        self.assertEqual(actual, expected)
    def test_HCP_All(self):
        hand = [
            [12,11,10,9],
            [25,24,23,22],
            [38,37,36,35],
            [51,50,49,48],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'hcp')
        expected = {
            "clubs": 10,
            "diamonds": 10,
            "hearts": 10,
            "spades": 10,
         }
        self.assertEqual(actual, expected)
    def test_Alternative_Ace(self):
        hand = [
            [0,1,3,4,12],
            [13,14,16],
            [27,28,29],
            [40,41,42],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'Alternative')
        expected = {
            "clubs": 4.5,
            "diamonds": 0,
            "hearts": 0,
            "spades": 0,
         }
        self.assertEqual(actual, expected)
    def test_Alternative_King(self):
        hand = [
            [0,1,3,4],
            [13,14,24],
            [27,28,29],
            [40,41,42],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'Alternative')
        expected = {
            "clubs": 0,
            "diamonds": 3,
            "hearts": 0,
            "spades": 0,
         }
        self.assertEqual(actual, expected)
    def test_Alternative_Queen(self):
        hand = [
            [0,1,3,4],
            [13,14,16],
            [27,28,36],
            [40,41,42],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'Alternative')
        expected = {
            "clubs": 0,
            "diamonds": 0,
            "hearts": 1.5,
            "spades": 0,
         }
        self.assertEqual(actual, expected)
    def test_Alternative_jack(self):
        hand = [
            [0,1,3,4],
            [13,14,16],
            [27,28,29],
            [40,41,48],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'Alternative')
        expected = {
            "clubs": 0,
            "diamonds": 0,
            "hearts": 0,
            "spades": .75,
         }
        self.assertEqual(actual, expected)
    def test_Alternative_ten(self):
        hand = [
            [0,1,3,4],
            [13,14],
            [27,28,29],
            [40,41,42, 47],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'Alternative')
        expected = {
            "clubs": 0,
            "diamonds": 0,
            "hearts": 0,
            "spades": .25,
         }
        self.assertEqual(actual, expected)
    def test_Alternative_All(self):
        hand = [
            [12,11,10,9,8],
            [25,24,23,22,21],
            [38,37,36,35,34],
            [51,50,49,48,47],
         ]
        actual = helpers.getHighCardPointValuesInEachSuit(hand, 'Alternative')
        expected = {
            "clubs": 10,
            "diamonds": 10,
            "hearts": 10,
            "spades": 10,
         }
        self.assertEqual(actual, expected)

class getWasPlayerForcedToBidAnNthLevelBid(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
    
    def tearDown(self) -> None:
        print(f"self.bids = {self.bids}")
    
    def test_error(self):
        self.biddingRelative = {
            "left": ['One No Trump'],
            "top": ['Two Diamond'],
            "right": ['Two Heart'],
            "bottom": [],
        }
        self.username = "RightPlayer"
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)

        with self.assertRaises(Exception) as context:
            self.actual = helpers.getWasPlayersNthBidAJumpshift(self.username, self.bids, 2)

    def test_False_1(self):
        self.biddingRelative = {
            "left": ['One No Trump'],
            "top": ['Two Diamond'],
            "right": ['Two Heart'],
            "bottom": [],
        }
        self.username = "TopPlayer"
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getWasPlayersNthBidAJumpshift(self.username, self.bids, 1)
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_false_2(self):
        self.biddingRelative = {
            "left": ['One No Trump', 'Four Club'],
            "top": ['Three Diamond', 'Four Diamond'],
            "right": ['Three Heart', 'pass'],
            "bottom": ['Three Spade'],
        }
        self.username = "TopPlayer"
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getWasPlayersNthBidAJumpshift(self.username, self.bids, 2)
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_true_1(self):
        self.biddingRelative = {
            "left": ['One No Trump'],
            "top": ['Three Diamond'],
            "right": ['Three Heart'],
            "bottom": [],
        }
        self.username = "TopPlayer"
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getWasPlayersNthBidAJumpshift(self.username, self.bids, 1)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    def test_true_2(self):
        self.biddingRelative = {
            "left": ['One No Trump', 'Four Club'],
            "top": ['Three Diamond', 'Five Diamond'],
            "right": ['Three Heart', 'pass'],
            "bottom": ['Three Spade'],
        }
        self.username = "TopPlayer"
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getWasPlayersNthBidAJumpshift(self.username, self.bids, 2)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
class getWasFirstOpeningBidANthLevelBid(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
    
    def tearDown(self) -> None:
        print(f"self.bids = {self.bids}")
    
    def test_false_1(self):
        self.biddingRelative = {
            "left": ['One Club'],
            "top": ['Two Heart'],
            "right": ['Two Spade'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getWasFirstOpeningBidANthLevelBid(self.bids, 2)
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_false_2(self):
        self.biddingRelative = {
            "left": ['One No Trump', 'Two No Trump'],
            "top": ['pass', 'pass'],
            "right": ['Two Spade', 'Three Spade'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getWasFirstOpeningBidANthLevelBid(self.bids, 2)
        self.expected = False
        self.assertEqual(self.expected, self.actual)

    def test_true_1(self):
        self.biddingRelative = {
            "left": ['pass'],
            "top": ['Two Club'],
            "right": ['Two Spade'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getWasFirstOpeningBidANthLevelBid(self.bids, 2)
        self.expected = "TopPlayer"
        self.assertEqual(self.expected, self.actual) 

    def test_true_2(self):
        self.biddingRelative = {
            "left": ['pass'],
            "top": ['Two Heart'],
            "right": ['Two Spade'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getWasFirstOpeningBidANthLevelBid(self.bids, 2)
        self.expected = "TopPlayer"
        self.assertEqual(self.expected, self.actual)
    def test_true_3(self):
        self.biddingRelative = {
            "left": ['pass', 'Two No Trump'],
            "top": ['pass', 'pass'],
            "right": ['Two Spade', 'Three Spade'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getWasFirstOpeningBidANthLevelBid(self.bids, 2)
        self.expected = "RightPlayer"
        self.assertEqual(self.expected, self.actual)
    def test_none(self):
        self.biddingRelative = {
            "left": ['pass', 'Two No Trump'],
            "top": ['pass', 'pass'],
            "right": ['Two Spade', 'Three Spade'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getWasFirstOpeningBidANthLevelBid(self.bids, 8)
        self.expected = None
        self.assertEqual(self.expected, self.actual)

class getPartnersCurrentContractBidFromBidding(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
    def test_empty(self):
        self.username = 'LeftPlayer'
        self.biddingRelative = {
            "left": [],
            "top": [],
            "right": [],
            "bottom": [],
        }
        self.username = 'LeftPlayer'
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getPartnersCurrentContractBidFromBidding(self.username, self.bids, self.seatingRelative)
        self.expected = None
        self.assertEqual(self.expected, self.actual)
    def test_1(self):
        self.biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'Pass'],
            "right": ['Double', 'Two Club'],
            "bottom": ['pass'],
        }
        self.username = 'LeftPlayer'
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getPartnersCurrentContractBidFromBidding(self.username, self.bids, self.seatingRelative)
        self.expected = "One Heart"
        self.assertEqual(self.expected, self.actual)
    def test_2(self):
        self.biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'One Spade'],
            "right": ['Double', 'Two Club'],
            "bottom": ['pass'],
        }
        self.username = 'LeftPlayer'
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getPartnersCurrentContractBidFromBidding(self.username, self.bids, self.seatingRelative)
        self.expected = "One Spade"
        self.assertEqual(self.expected, self.actual)
    def test_3(self):
        self.biddingRelative = {
            "left": ['pass'],
            "top": ['One Club'],
            "right": ['Double'],
            "bottom": [],
        }
        self.username = 'RightPlayer'
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getPartnersCurrentContractBidFromBidding(self.username, self.bids, self.seatingRelative)
        self.expected = None
        self.assertEqual(self.expected, self.actual)
    def test_4(self):
        self.biddingRelative = {
            "left": ['pass'],
            "top": ['One Club'],
            "right": ['Double'],
            "bottom": [],
        }
        self.username = 'LeftPlayer'
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getPartnersCurrentContractBidFromBidding(self.username, self.bids, self.seatingRelative)
        self.expected = 'One Club'
        self.assertEqual(self.expected, self.actual)
    def test_4(self):
        self.biddingRelative = {
            "left": ['pass'],
            "top": ['One Club'],
            "right": ['Double'],
            "bottom": [],
        }
        self.username = 'LeftPlayer'
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getPartnersCurrentContractBidFromBidding(self.username, self.bids, self.seatingRelative)
        self.expected = 'One Club'
        self.assertEqual(self.expected, self.actual)
    def test_5(self):
        self.username = 'TopPlayer'
        self.biddingRelative = {
            "left": ['pass'],
            "top": ['One Club'],
            "right": ['Double'],
            "bottom": [],
        }
        self.username = 'BottomPlayer'
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getPartnersCurrentContractBidFromBidding(self.username, self.bids, self.seatingRelative)
        self.expected = None
        self.assertEqual(self.expected, self.actual)
class getIsPartnersFirstBidPass(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }

    def test_false_1(self):
        self.username = 'LeftPlayer'
        self.biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'pass'],
            "right": ['Double', 'Two Club'],
            "bottom": ['pass'],
        }
        self.actual = helpers.getIsPartnersFirstBidPass(self.biddingRelative, self.seatingRelative, self.username)
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_false_2(self):
        self.username = 'LeftPlayer'
        self.biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'pass'],
            "right": ['One Club', 'Two Club'],
            "bottom": ['pass'],
        }
        self.actual = helpers.getIsPartnersFirstBidPass(self.biddingRelative, self.seatingRelative, self.username)
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_true_1(self):
        self.username = 'RightPlayer'
        self.biddingRelative = {
            "left": ['Pass', 'One Heart'],
            "top": ['One Club', 'pass'],
            "right": ['One Club', 'Two Club'],
            "bottom": ['pass'],
        }
        self.actual = helpers.getIsPartnersFirstBidPass(self.biddingRelative, self.seatingRelative, self.username)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    def test_true_2(self):
        self.username = 'TopPlayer'
        self.biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'pass'],
            "right": ['One Club', 'Two Club'],
            "bottom": ['pass'],
        }
        self.actual = helpers.getIsPartnersFirstBidPass(self.biddingRelative, self.seatingRelative, self.username)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    
class getNextBidInSuit(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(Exception) as context:
            actual = helpers.getNextBidInSuit('Thonfdh', 'One Club')
    def test_same_level(self):
        actual = helpers.getNextBidInSuit('diamonds', 'One Club')
        expected = 'One Diamond'
        self.assertEqual(actual, expected)
    def test_same_level2(self):
        actual = helpers.getNextBidInSuit('hearts', 'One Club')
        expected = 'One Heart'
        self.assertEqual(actual, expected)
    def test_same_level3(self):
        actual = helpers.getNextBidInSuit('Spades', 'One Club')
        expected = 'One Spade'
        self.assertEqual(actual, expected)
    def test_same_level4(self):
        actual = helpers.getNextBidInSuit('No Trump', 'One Club')
        expected = 'One No Trump'
        self.assertEqual(actual, expected)
    def test_next_level_club(self):
        actual = helpers.getNextBidInSuit('Clubs', 'Two Club')
        expected = 'Three Club'
        self.assertEqual(actual, expected)
    def test_next_level_club2(self):
        actual = helpers.getNextBidInSuit('Clubs', 'Two Diamond')
        expected = 'Three Club'
        self.assertEqual(actual, expected)
    def test_next_level_club3(self):
        actual = helpers.getNextBidInSuit('Clubs', 'Two Heart')
        expected = 'Three Club'
        self.assertEqual(actual, expected)
    def test_next_level_club4(self):
        actual = helpers.getNextBidInSuit('Clubs', 'Two Spade')
        expected = 'Three Club'
        self.assertEqual(actual, expected)
    def test_next_level_club5(self):
        actual = helpers.getNextBidInSuit('Clubs', 'Two No Trump')
        expected = 'Three Club'
        self.assertEqual(actual, expected)
    def test_next_level_diamond(self):
        actual = helpers.getNextBidInSuit('Clubs', 'Two Diamond')
        expected = 'Three Club'
        self.assertEqual(actual, expected)
    def test_next_level_heart(self):
        actual = helpers.getNextBidInSuit('Clubs', 'Two Heart')
        expected = 'Three Club'
        self.assertEqual(actual, expected)
    def test_next_level_spade(self):
        actual = helpers.getNextBidInSuit('Clubs', 'Two Spade')
        expected = 'Three Club'
        self.assertEqual(actual, expected)
    def test_next_level_trump(self):
        actual = helpers.getNextBidInSuit('Clubs', 'Three No Trump')
        expected = 'Four Club'
        self.assertEqual(actual, expected)
class getUsernamesPartner(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
    def test_none(self):
        username = ""
        actual = helpers.getUsernamesPartner(username, self.seatingRelative)
        expected = "Error in getUsernamesPartner"
        self.assertEqual(actual, expected)
    def test_typo(self):
        username = "dfdfd"
        actual = helpers.getUsernamesPartner(username, self.seatingRelative)
        expected = "Error in getUsernamesPartner"
        self.assertEqual(actual, expected)
    def test_top(self):
        username = "TopPlayer"
        actual = helpers.getUsernamesPartner(username, self.seatingRelative)
        expected = "BottomPlayer"
        self.assertEqual(actual, expected)
    def test_bottom(self):
        username = "BottomPlayer"
        actual = helpers.getUsernamesPartner(username, self.seatingRelative)
        expected = "TopPlayer"
        self.assertEqual(actual, expected)
    def test_left(self):
        username = "LeftPlayer"
        actual = helpers.getUsernamesPartner(username, self.seatingRelative)
        expected = "RightPlayer"
        self.assertEqual(actual, expected)
    def test_right(self):
        username = "RightPlayer"
        actual = helpers.getUsernamesPartner(username, self.seatingRelative)
        expected = "LeftPlayer"
        self.assertEqual(actual, expected)
class getWasForcedToBid(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
    def test_wasForced_Double(self):
        biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'pass'],
            "right": ['Double', 'Two Club'],
            "bottom": ['pass'],
        }
        username = "LeftPlayer"
        biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        actual = helpers.getWasForcedToBid(username, biddingAbsolute, self.seatingRelative)
        expected = True
        self.assertEqual(expected, actual)
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['forcedOneNoTrumpResponse']
    def test_wasForced_1NT(self):
        biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['forcedOneNoTrumpResponse']
        username = "RightPlayer"
        biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        actual = helpers.getWasForcedToBid(username, biddingAbsolute, self.seatingRelative)
        expected = True
        self.assertEqual(expected, actual)
   
    def test_wasNOTForced(self):
        biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'pass'],
            "right": ['Double', 'Two Club'],
            "bottom": ['One Diamond'],
        }
        username = "LeftPlayer"
        biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        actual = helpers.getWasForcedToBid(username, biddingAbsolute, self.seatingRelative)
        expected = False
        self.assertEqual(expected, actual)
    def test_error(self):
        biddingRelative = {
            "left": ['pass', 'One Heart'],
            "top": ['One Club', 'pass'],
            "right": ['Double', 'Two Club'],
            "bottom": ['One Diamond'],
        }
        username = "efstPlayer"
        biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        actual = helpers.getWasForcedToBid(username, biddingAbsolute, self.seatingRelative)
        expected = 'Error in getWasForcedToBid'
        self.assertEqual(expected, actual)
class getUsersFirstContractBid(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }

    def test_none(self):
        self.username = ""
        self.biddingRelative = {
            "left": ['pass', 'double'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getUsersFirstContractBid(self.username, self.bids)
        self.expected = None
        self.assertEqual(self.expected, self.actual) 
    def test_1(self):
        self.username = "TopPlayer"
        self.biddingRelative = {
            "left": ['One club', 'double'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getUsersFirstContractBid(self.username, self.bids)
        self.expected = 'double'
        self.assertEqual(self.expected, self.actual) 
    def test_2(self):
        self.username = "RightPlayer"
        self.biddingRelative = {
            "left": ['pass', 'double'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getUsersFirstContractBid(self.username, self.bids)
        self.expected = 'three club'
        self.assertEqual(self.expected, self.actual) 
    def test_3(self):
        self.username = "LeftPlayer"
        self.biddingRelative = {
            "left": ['pass', 'Three Heart'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getUsersFirstContractBid(self.username, self.bids)
        self.expected = 'Three Heart'
        self.assertEqual(self.expected, self.actual) 
    def test_4(self):
        self.username = "LeftPlayer"
        self.biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getUsersFirstContractBid(self.username, self.bids)
        self.expected = 'pass'
        self.assertEqual(self.expected, self.actual) 
class getIsBidAContractBid(unittest.TestCase):
    def test_true_1(self):
        self.bid = 'One Club'
        self.actual = helpers.getIsBidAContractBid(self.bid)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    def test_true_2(self):
        self.bid = 'Seven Heart'
        self.actual = helpers.getIsBidAContractBid(self.bid)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    def test_false_1(self):
        self.bid = 'pass'
        self.actual = helpers.getIsBidAContractBid(self.bid)
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_false_2(self):
        self.bid = 'double'
        self.actual = helpers.getIsBidAContractBid(self.bid)
        self.expected = False
        self.assertEqual(self.expected, self.actual)

class getIsUsernamesFirstContractBidTheFirstContractBid(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
    
    def test_false_1(self):
        self.username = "LeftPlayer"
        self.biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getIsUsernamesFirstContractBidTheFirstContractBid(self.username, self.bids)
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_false_2(self):
        self.username = "LeftPlayer"
        self.biddingRelative = {
            "left": ['double', 'pass'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getIsUsernamesFirstContractBidTheFirstContractBid(self.username, self.bids)
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_false_3(self):
        self.username = "RightPlayer"
        self.biddingRelative = {
            "left": ['One No Trump', 'pass'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getIsUsernamesFirstContractBidTheFirstContractBid(self.username, self.bids)
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_true_1(self):
        self.username = "LeftPlayer"
        self.location ="left"
        self.biddingRelative = {
            "left": ['One Diamond', 'pass'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getIsUsernamesFirstContractBidTheFirstContractBid(self.username, self.bids)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    def test_true_2(self):
        self.username = "RightPlayer"
        self.location = "right"
        self.biddingRelative = {
            "left": ['pass', 'pass'],
            "top": ['double', 'pass'],
            "right": ['three club', 'pass'],
            "bottom": ['pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getIsUsernamesFirstContractBidTheFirstContractBid(self.username, self.bids)
        self.expected = True
        self.assertEqual(self.expected, self.actual)

class getUsernamesOpponents(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
        }

    def test_error(self):
        self.location = "rights"
        self.actual = helpers.getUsernamesOpponents(self.location, self.seatingRelative)
        self.expected = []
        self.assertListEqual(self.expected, self.actual) 
    def test_1(self):
        self.location = "right"
        self.actual = helpers.getUsernamesOpponents(self.location, self.seatingRelative)
        self.expected = ["BottomPlayer", "TopPlayer"]
        self.assertListEqual(self.expected, self.actual) 
    def test_2(self):
        self.location = "bottom"
        self.actual = helpers.getUsernamesOpponents(self.location, self.seatingRelative)
        self.expected = ["LeftPlayer", "RightPlayer"]
        self.assertListEqual(self.expected, self.actual) 
    def test_3(self):
        self.location = "left"
        self.actual = helpers.getUsernamesOpponents(self.location, self.seatingRelative)
        self.expected = ["TopPlayer", "BottomPlayer"]
        self.assertListEqual(self.expected, self.actual) 
    def test_4(self):
        self.location = "right"
        self.actual = helpers.getUsernamesOpponents(self.location, self.seatingRelative)
        self.expected = ["BottomPlayer", "TopPlayer"]
        self.assertListEqual(self.expected, self.actual) 
class getHasOtherTeamMentionedSameSuit(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
    def tearDown(self) -> None:
        print(f"self.actual = {self.actual}")
        print(f"self.expected = {self.expected}")
        print(f"self.bids = {self.bids}")

    def test_true_1(self):
        self.location = "right"
        self.bid = "Two Heart"
        self.biddingRelative = {
            "bottom": ['One Heart'],
            "left": ['pass'],
            "top": ['One No Trump'],
            "right": ['Two Heart'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasOtherTeamMentionedSameSuit(self.location, self.bid, self.bids, self.seatingRelative)
        self.expected = True
        self.assertEqual(self.expected, self.actual) 
    def test_true_2(self):
        self.location = "right"
        self.bid = "Two Heart"
        self.biddingRelative = {
            "bottom": ['One Heart', 'Two Spade'],
            "left": ['pass', 'pass'],
            "top": ['One No Trump', 'pass'],
            "right": ['Two Heart', 'pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasOtherTeamMentionedSameSuit(self.location, self.bid, self.bids, self.seatingRelative)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    #NOTE: this case could return true if we weren't stipulating that the opponents bids must be before the bid in question
    def test_false_4(self):
        self.location = "right"
        self.bid = "Two Heart"
        self.biddingRelative = {
            "bottom": ['pass', 'Two Heart'],
            "left": ['pass', 'pass'],
            "top": ['pass', 'pass'],
            "right": ['One Heart', 'pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasOtherTeamMentionedSameSuit(self.location, self.bid, self.bids, self.seatingRelative)
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_false_1(self):
        self.location = "bottom"
        self.bid = "One Heart"
        self.biddingRelative = {
            "bottom": ['One Heart'],
            "left": ['pass'],
            "top": ['One No Trump'],
            "right": ['Two Heart'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasOtherTeamMentionedSameSuit(self.location, self.bid, self.bids, self.seatingRelative)
        self.expected = False
        self.assertEqual(self.expected, self.actual) 
    def test_false_2(self):
        self.location = "top"
        self.bid = "One Heart"
        self.biddingRelative = {
            "bottom": ['pass', 'Two Spade'],
            "left": ['pass', 'pass'],
            "top": ['One Heart', 'pass'],
            "right": ['Two Heart', 'pass'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasOtherTeamMentionedSameSuit(self.location, self.bid, self.bids, self.seatingRelative)
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_false_3(self):
        self.location = "top"
        self.bid = "Two Club"
        self.biddingRelative = {
            "right": ['One Spade', 'Two Diamond'],
            "bottom": ['One No Trump'],
            "left": ['pass'],
            "top": ['Two Club'],
        }
        self.bids = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        self.actual = helpers.getHasOtherTeamMentionedSameSuit(self.location, self.bid, self.bids, self.seatingRelative)
        self.expected = False
        self.assertEqual(self.expected, self.actual)

class getUsernameOfPlayerWhoHadFirstOpportunityToBid(unittest.TestCase):
    def tearDown(self) -> None:
        print(f"self.actual = {self.actual}")
        print(f"self.expected = {self.expected}")

    def test_1(self):
        username = "TopPlayer"
        usernamesPartner = 'BottomPlayer'
        biddingAbsolute = [
            ["TopPlayer", 'Pass'],
            ["RightPlayer", 'Pass'],
            ["BottomPlayer", 'Pass'],
        ]
        self.actual = helpers.getUsernameOfPlayerWhoHadFirstOpportunityToBid(biddingAbsolute, usernamesPartner, username);
        self.expected = username
        self.assertEqual(self.actual, self.expected)
    def test_2(self):
        username = "BottomPlayer"
        usernamesPartner = 'TopPlayer'
        biddingAbsolute = [
            ["BottomPlayer", 'Pass'],
            ["LeftPlayer", 'Pass'],
            ["TopPlayer", 'Pass'],
        ]
        self.actual = helpers.getUsernameOfPlayerWhoHadFirstOpportunityToBid(biddingAbsolute, usernamesPartner, username);
        self.expected = username
        self.assertEqual(self.actual, self.expected)
    def test_none(self):
        username = "BottomPlayer"
        usernamesPartner = 'TopPlayer'
        biddingAbsolute = [
        ]
        self.actual = helpers.getUsernameOfPlayerWhoHadFirstOpportunityToBid(biddingAbsolute, usernamesPartner, username);
        self.expected = None
        self.assertEqual(self.actual, self.expected)
class getBiddableSuits(unittest.TestCase):
    def tearDown(self) -> None:
        print(f"self.actual = {self.actual}")
        print(f"self.expected = {self.expected}")
 
    def test_1(self):
        self.handDictionary = {
            "clubs": "T932",
            "diamonds": "AKQ72",
            "hearts": "965",
            "spades": "53",
        }
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = helpers.getBiddableSuits(self.hand)
        self.expected = ['clubs', 'diamonds']
        self.assertListEqual(self.expected, self.actual)
    def test_2(self):
        self.handDictionary = {
            "clubs": "T9432",
            "diamonds": "AKQ72",
            "hearts": "96543",
            "spades": "76532",
        }
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = helpers.getBiddableSuits(self.hand)
        self.expected = ['clubs', 'diamonds', 'hearts', 'spades']
        self.assertListEqual(self.expected, self.actual)
    def test_none(self):
        self.handDictionary = {
            "clubs": "T93",
            "diamonds": "AKQ",
            "hearts": "9654",
            "spades": "533",
        }
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = helpers.getBiddableSuits(self.hand)
        self.expected = []
        self.assertListEqual(self.expected, self.actual)
class getWeightedSuitScore(unittest.TestCase):
    def tearDown(self) -> None:
        print(f"self.actual = {self.actual}")
        print(f"self.expected = {self.expected}")
 
    def test_1(self):
        self.handDictionary = {
            "clubs": "T932",
            "diamonds": "AKQ72",
            "hearts": "965",
            "spades": "53",
        }
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = helpers.getWeightedSuitScore(self.hand, 'hcp')
        self.expected = {
            "clubs": 2,
            "diamonds": 13,
            "hearts": 0,
            "spades": 0,
        }
        self.assertDictEqual(self.expected, self.actual)
    
    def test_2(self):
        self.handDictionary = {
            "clubs": "65432",
            "diamonds": "J543",
            "hearts": "543",
            "spades": "2",
        }
        
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = helpers.getWeightedSuitScore(self.hand, 'hcp')
        self.expected = {
            "clubs": 4,
            "diamonds": 3,
            "hearts": 0,
            "spades": 0,
        }
        self.assertDictEqual(self.expected, self.actual)
   
    def test_3(self):
        self.handDictionary = {
            "clubs": "AKQJ52",
            "diamonds": "AKQJT98",
            "hearts": "",
            "spades": "",
        }
        
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        self.actual = helpers.getWeightedSuitScore(self.hand, 'hcp')
        self.expected = {
            "clubs": 16,
            "diamonds": 18,
            "hearts": 0,
            "spades": 0,
        }
        self.assertDictEqual(self.expected, self.actual)

class getShouldReturnNoTrump(unittest.TestCase):
    def tearDown(self) -> None:
        print(f"self.actual = {self.actual}")
        print(f"self.expected = {self.expected}")
 
    def test_no_biddable(self):
        self.weightedSuitScores = {
            "clubs": 4,
            "diamonds": 4,
            "hearts": 4,
            "spades": 4,
        }
        self.biddableSuits = []
        self.actual = helpers.getShouldReturnNoTrump(self.weightedSuitScores, self.biddableSuits)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    def test_not_close_enough(self):
        self.weightedSuitScores = {
            "clubs": 4,
            "diamonds": 7,
            "hearts": 4,
            "spades": 4,
        }
        self.biddableSuits = []
        self.actual = helpers.getShouldReturnNoTrump(self.weightedSuitScores, self.biddableSuits)
        self.expected = False
        self.assertEqual(self.expected, self.actual)
    def test_just_right(self):
        self.weightedSuitScores = {
            "clubs": 4,
            "diamonds": 6,
            "hearts": 4,
            "spades": 4,
        }
        self.biddableSuits = []
        self.actual = helpers.getShouldReturnNoTrump(self.weightedSuitScores, self.biddableSuits)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    def test_just_right_1(self):
        self.weightedSuitScores = {
            "clubs": 0,
            "diamonds": 0,
            "hearts": 2,
            "spades": 0,
        }
        self.biddableSuits = []
        self.actual = helpers.getShouldReturnNoTrump(self.weightedSuitScores, self.biddableSuits)
        self.expected = True
        self.assertEqual(self.expected, self.actual)
    def test_biddable_suit(self):
        self.weightedSuitScores = {
            "clubs": 0,
            "diamonds": 0,
            "hearts": 2,
            "spades": 0,
        }
        self.biddableSuits = ['clubs']
        self.actual = helpers.getShouldReturnNoTrump(self.weightedSuitScores, self.biddableSuits)
        self.expected = False
        self.assertEqual(self.expected, self.actual)
class getLengthOfSuitFromHand(unittest.TestCase):
    def setUp(self) -> None:
        self.actual = None
        self.expected = None
        self.hand = None
    def tearDown(self) -> None:
        print(f"self.actual = {self.actual}")
        print(f"self.expected = {self.expected}")
        print(f"self.hand = {self.hand}")

    def test_error(self):
        self.handDictionary = {
            "clubs": "AK52",
            "diamonds": "A98",
            "hearts": "345",
            "spades": "539",
        }
        self.suitName = 'clubss'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)
        with self.assertRaises(Exception) as context:
            self.actual = helpers.getLengthOfSuitFromHand(self.hand, self.suitName)

    def test_1(self):
        self.handDictionary = {
            "clubs": "AK52",
            "diamonds": "A98",
            "hearts": "3",
            "spades": "T9876",
        }
        self.suitName = 'clubs'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)

        self.actual = helpers.getLengthOfSuitFromHand(self.hand, self.suitName)
        self.expected = 4
        self.assertEqual(self.expected, self.actual) 

    def test_2(self):
        self.handDictionary = {
            "clubs": "AK52",
            "diamonds": "A98",
            "hearts": "3",
            "spades": "T9876",
        }
        self.suitName = 'Diamonds'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)

        self.actual = helpers.getLengthOfSuitFromHand(self.hand, self.suitName)
        self.expected = 3
        self.assertEqual(self.expected, self.actual) 

    def test_3(self):
        self.handDictionary = {
            "clubs": "AK52",
            "diamonds": "A98",
            "hearts": "3",
            "spades": "T9876",
        }
        self.suitName = 'HEARTS'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)

        self.actual = helpers.getLengthOfSuitFromHand(self.hand, self.suitName)
        self.expected = 1
        self.assertEqual(self.expected, self.actual) 

    def test_4(self):
        self.handDictionary = {
            "clubs": "AK52",
            "diamonds": "A98",
            "hearts": "3",
            "spades": "T9876",
        }
        self.suitName = 'spades'
        self.hand = helpers.getHandFromHandDictionary(self.handDictionary)

        self.actual = helpers.getLengthOfSuitFromHand(self.hand, self.suitName)
        self.expected = 5
        self.assertEqual(self.expected, self.actual) 
#region Testing Test Case Helpers
class getDealerLocation(unittest.TestCase):
    def test_empty_dict(self):
        biddingRelative = {
            "left": [],
            "top": [],
            "right": [],
            "bottom": [],
        }
        estimated = None
        actual = helpers.getDealerLocation(biddingRelative)
        self.assertEqual(actual, estimated)
    def test_none(self):
        biddingRelative = None
        estimated = None
        actual = helpers.getDealerLocation(biddingRelative)
        self.assertEqual(actual, estimated)
    def test_left(self):
        biddingRelative = {
            "left": ['One Diamond'],
            "top": ['Three Heart'],
            "right": ['pass'],
            "bottom": [],
        }
        estimated = 'left'
        actual = helpers.getDealerLocation(biddingRelative)
        self.assertEqual(actual, estimated)
    def test_top(self):
        biddingRelative = {
            "left": ['One Diamond'],
            "top": ['pass', 'Four Heart'],
            "right": ['pass', 'pass'],
            "bottom": ['pass'],
        }
        estimated = 'top'
        actual = helpers.getDealerLocation(biddingRelative)
        self.assertEqual(actual, estimated)
    def test_right(self):
        biddingRelative = {
            "left": [],
            "top": [],
            "right": ['pass'],
            "bottom": [],
        }
        estimated = 'right'
        actual = helpers.getDealerLocation(biddingRelative)
        self.assertEqual(actual, estimated)
    def test_bottom(self):
        biddingRelative = {
            "left": ['p'],
            "top": ['p'],
            "right": ['pass'],
            "bottom": ['pass'],
        }
        estimated = 'bottom'
        actual = helpers.getDealerLocation(biddingRelative)
        self.assertEqual(actual, estimated)
    def test_two(self):
        biddingRelative = {
            "left": ['Pass','Two Club'],
            "top": ['Three Heart'],
            "right": ['pass'],
            "bottom": ['pass'],
        }
        estimated = 'left'
        actual = helpers.getDealerLocation(biddingRelative)
        self.assertEqual(actual, estimated)
    def test_three(self):
        biddingRelative = {
            "left": ['Pass','Two Club'],
            "top": ['Three Heart', 'T'],
            "right": ['pass', 'p'],
            "bottom": ['pass', 'p', 'p'],
        }
        estimated = 'bottom'
        actual = helpers.getDealerLocation(biddingRelative)
        self.assertEqual(actual, estimated)
    def test_four(self):
        biddingRelative = {
            "left": ['Pass','Two Club', 'p'],
            "top": ['Three Heart', 'T', 'p', 'p'],
            "right": ['pass', 'p', 'p'],
            "bottom": ['pass', 'p', 'p'],
        }
        estimated = 'top'
        actual = helpers.getDealerLocation(biddingRelative)
        self.assertEqual(actual, estimated)

class getBiddingAbsoluteFromBiddingObjAndSeatingRelative(unittest.TestCase):
    def setUp(self) -> None:
        self.seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
    def test_none(self):
        biddingRelative = None
        expected = []
        actual = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.assertEqual(actual, expected)
        
    def test_empty(self):
        biddingRelative = {
            "left": [],
            "top": [],
            "right": [],
            "bottom": [],
        }
        
        expected = []
        actual = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        self.assertEqual(actual, expected)
    def test_bottom_dealer(self):
        biddingRelative = {
            "left": ['One Diamond'],
            "top": ['Three Heart'],
            "right": ['pass'],
            "bottom": ['pass'],
        }
        expected = [[self.seatingRelative['bottom'], 'pass'], [self.seatingRelative['left'], 'One Diamond'], [self.seatingRelative['top'], 'Three Heart'], [self.seatingRelative['right'], 'pass']]

        actual = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        print('actual = {0}'.format(actual))
        print('expected = {0}'.format(expected))
        self.actual = actual
        self.assertListEqual(actual, expected)
    def test_left_dealer(self):
        biddingRelative = {
            "left": ['One Diamond', 'Two Diamond'],
            "top": ['Three Heart'],
            "right": ['pass'],
            "bottom": ['pass'],
        }
        expected = [[self.seatingRelative['left'], 'One Diamond'], [self.seatingRelative['top'], 'Three Heart'], [self.seatingRelative['right'], 'pass'], [self.seatingRelative['bottom'], 'pass'], [self.seatingRelative['left'], 'Two Diamond']]

        actual = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        print('actual = {0}'.format(actual))
        print('expected = {0}'.format(expected))
        self.actual = actual
        self.assertListEqual(actual, expected)
    def test_top_dealer(self):
        biddingRelative = {
            "left": ['One Diamond'],
            "top": ['pass', 'Four Heart'],
            "right": ['pass', 'pass'],
            "bottom": ['pass'],
        }
        expected = [[self.seatingRelative['top'], 'pass'], [self.seatingRelative['right'], 'pass'], [self.seatingRelative['bottom'], 'pass'], [self.seatingRelative['left'], 'One Diamond'], [self.seatingRelative['top'], 'Four Heart'], [self.seatingRelative['right'], 'pass']]

        actual = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        print('actual = {0}'.format(actual))
        print('expected = {0}'.format(expected))
        self.actual = actual
        self.assertListEqual(actual, expected)
    def test_right_dealer(self):
        biddingRelative = {
            "left": ['One Diamond', 'Two Diamond'],
            "top": ['Three Heart', 'Four Heart'],
            "right": ['pass', 'pass', 'pass'],
            "bottom": ['pass', 'pass'],
        }
        expected = [[self.seatingRelative['right'], 'pass'], [self.seatingRelative['bottom'], 'pass'], [self.seatingRelative['left'], 'One Diamond'], [self.seatingRelative['top'], 'Three Heart'], [self.seatingRelative['right'], 'pass'], [self.seatingRelative['bottom'], 'pass'], [self.seatingRelative['left'], 'Two Diamond'], [self.seatingRelative['top'], 'Four Heart'], [self.seatingRelative['right'], 'pass']]

        actual = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, self.seatingRelative)
        print('actual = {0}'.format(actual))
        print('expected = {0}'.format(expected))
        self.actual = actual
        self.assertListEqual(actual, expected)
    def test_2(self):
        self.biddingRelative = {
            "right": ['One Spade', 'Two Heart'],
            "bottom": ['One No Trump'],
            "left": ['pass'],
            "top": ['Two Diamond'],
        }

        self.expected = [
            [self.seatingRelative['right'], 'One Spade'],
            [self.seatingRelative['bottom'], 'One No Trump'],
            [self.seatingRelative['left'], 'pass'],
            [self.seatingRelative['top'], 'Two Diamond'],
            [self.seatingRelative['right'], 'Two Heart'],
        ]

        self.actual = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(self.biddingRelative, self.seatingRelative)
        print('actual = {0}'.format(self.actual))
        print('expected = {0}'.format(self.expected))
        self.assertListEqual(self.actual, self.expected)
class getHandFromHandDictionary(unittest.TestCase):
    def test_1(self):
        hand = {
            "clubs": "AKQ",
            "diamonds": "AKQ",
            "hearts": "AKQ",
            "spades": "AKQ",
        }
        expected = [
            [12,11,10],
            [25,24,23],
            [38,37,36],
            [51,50,49],
        ]
        actual = helpers.getHandFromHandDictionary(hand)
        self.assertListEqual(actual, expected)
    def test_all(self):
        hand = {
            "clubs": "AKQJT98765432",
            "diamonds": "AKQJT98765432",
            "hearts": "AKQJT98765432",
            "spades": "AKQJT98765432",
        }
        expected = [
            [12,11,10,9,8,7,6,5,4,3,2,1,0],
            [25,24,23,22,21,20,19,18,17,16,15,14,13],
            [38,37,36,35,34,33,32,31,30,29,28,27,26],
            [51,50,49,48,47,46,45,44,43,42,41,40,39],
        ]
        actual = helpers.getHandFromHandDictionary(hand)
        self.assertListEqual(actual, expected)
    def test_none(self):
        hand = {
            "clubs": "",
            "diamonds":"",
            "hearts":"",
            "spades":"",
        }
        expected = [
            [],
            [],
            [],
            [],
        ]
        actual = helpers.getHandFromHandDictionary(hand)
        self.assertListEqual(actual, expected)
#endregion











