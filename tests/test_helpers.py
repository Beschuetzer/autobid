import unittest
import autoBid



class getSuitFromCardAsNumber(unittest.TestCase):
    def test_clubLow(self):
        self.assertEqual(autoBid.getSuitNameFromCardAsNumber(0), 'clubs')
    def test_clubHigh(self):
        self.assertEqual(autoBid.getSuitNameFromCardAsNumber(12), 'clubs')
    def test_diamondLow(self):
        self.assertEqual(autoBid.getSuitNameFromCardAsNumber(13), 'diamonds')
    def test_diamondHigh(self):
        self.assertEqual(autoBid.getSuitNameFromCardAsNumber(25), 'diamonds')
    def test_heartLow(self):
        self.assertEqual(autoBid.getSuitNameFromCardAsNumber(26), 'hearts')
    def test_heartHigh(self):
        self.assertEqual(autoBid.getSuitNameFromCardAsNumber(38), 'hearts')
    def test_spadeLow(self):
        self.assertEqual(autoBid.getSuitNameFromCardAsNumber(39), 'spades')
    def test_spadeHigh(self):
        self.assertEqual(autoBid.getSuitNameFromCardAsNumber(51), 'spades')

class getPartnersBids(unittest.TestCase):
    # bidsExample = [['Adam', 'Two No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass']]

    def test_noBids(self):
        expected = autoBid.getPartnersBids([])
        self.assertListEqual(expected, [])
   
    def test_1Bid(self):
        bids = [['Adam', 'Two No Trump']]
        expected = autoBid.getPartnersBids(bids)
        self.assertListEqual(expected, [])
    def test_2Bids(self):
        bids = [
            ['Adam', 'Two No Trump'],
            ['Tim', 'Three No Trump'],
        ]  

        expected = autoBid.getPartnersBids(bids)
        self.assertListEqual(expected, ['Two No Trump'])
    def test_3Bids(self):
        bids = [
            ['Adam', 'Two No Trump'],
            ['Tim', 'Three No Trump'],
            ['Ann', 'Four No Trump'],
            ['Andrew', 'Pass'],
        ]
        expected = autoBid.getPartnersBids(bids)
        self.assertListEqual(expected, ['Four No Trump'])
    def test_5Bids(self):
        bids = [
            ['Adam', 'Two No Trump'],
            ['Tim', 'Three No Trump'],
            ['Ann', 'Four No Trump'],
            ['Andrew', 'Pass'],
            ['Adam', 'Double'],
        ]
        expected = autoBid.getPartnersBids(bids)
        self.assertListEqual(expected, ['Pass'])
    def test_9Bids(self):
        bids = [
            ['Adam', 'Two No Trump'],
            ['Tim', 'Three No Trump'],
            ['Ann', 'Four No Trump'],
            ['Andrew', 'Double'],
            ['Adam', 'Double'],
            ['Tim', 'Five No Trump'],
            ['Ann', 'Six Club'],
            ['Andrew', 'Pass'],
            ['Adam', 'Double']
        ]
        expected = autoBid.getPartnersBids(bids)
        self.assertListEqual(expected, ['Pass', 'Double'])
    
class getHighCardPoints(unittest.TestCase):
    def test_Normal_None(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 0)

    def test_Normal_onlyTens(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 0)

    def test_Normal_onlyJacks(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 4)
    
    def test_Normal_onlyQueens(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 8)

    def test_Normal_onlyKings(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 12)

    def test_Normal_onlyAces(self):
        clubs = [i for i in range(0, 13) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 16)

    def test_Normal_All(self):
        clubs = [i for i in range(0, 13)]
        diamonds = [i for i in range(13, 26)]
        hearts = [i for i in range(26, 39)]
        spades = [i for i in range(39, 52)]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 40)

    def test_Normal_OneOfEach(self):
        clubs = [i for i in range(0, 13) if i%13==12]
        diamonds = [i for i in range(13, 26) if i%13==11]
        hearts = [i for i in range(26, 39) if i%13==10]
        spades = [i for i in range(39, 52) if i%13==9]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 4)

    def test_Normal_AllButOneOfEach(self):
        clubs = [i for i in range(0, 13) if i%13 != 11]
        diamonds = [i for i in range(13, 26) if i%13 != 10]
        hearts = [i for i in range(26, 39) if i%13 != 9]
        spades = [i for i in range(39, 52) if i%13 != 12]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'HCP'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 30)

    



    def test_Alternative_None(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 0)

    def test_Alternative_onlyTens(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 9]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 1)

    def test_Alternative_onlyJacks(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 10 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 3)
    
    def test_Alternative_onlyQueens(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 11 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 6)

    def test_Alternative_onlyKings(self):
        clubs = [i for i in range(0, 13) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 12 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 12)

    def test_Alternative_onlyAces(self):
        clubs = [i for i in range(0, 13) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        diamonds = [i for i in range(13, 26) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hearts = [i for i in range(26, 39) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        spades = [i for i in range(39, 52) if i%13 != 11 if i%13 != 10 if i%13 != 9 if i%13 != 8]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 18)

    def test_Alternative_All(self):
        clubs = [i for i in range(0, 13)]
        diamonds = [i for i in range(13, 26)]
        hearts = [i for i in range(26, 39)]
        spades = [i for i in range(39, 52)]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 40)

    def test_Alternative_OneOfEach(self):
        clubs = [i for i in range(0, 13) if i%13==12]
        diamonds = [i for i in range(13, 26) if i%13==11]
        hearts = [i for i in range(26, 39) if i%13==10]
        spades = [i for i in range(39, 52) if i%13==9]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 4.5)

    def test_Alternative_AllButOneOfEach(self):
        clubs = [i for i in range(0, 13) if i%13 != 11]
        diamonds = [i for i in range(13, 26) if i%13 != 10]
        hearts = [i for i in range(26, 39) if i%13 != 9]
        spades = [i for i in range(39, 52) if i%13 != 12]
        hand = [clubs, diamonds, hearts, spades]
        convention = 'Alternative'
        self.assertEqual(autoBid.getHighCardPoints(hand, convention), 30.25)

    def test_Error_NoHand(self):
        convention = 'hcp'
        self.assertEqual(autoBid.getHighCardPoints(None, convention), -1)

    def test_Error_NoConvention(self):
        convention = 'hcp'
        self.assertEqual(autoBid.getHighCardPoints([1,2,3], None), -1)


class tallyUpTotal(unittest.TestCase):
    def test_AllOneSuit(self):
        suitCounts = {
            "clubs": 13,
            "diamonds":  0,
            "hearts":  0,
            "spades": 0,
        }
        self.assertEqual(autoBid.tallyUpTotal(suitCounts), 18)
    
    def test_None(self):
        suitCounts = {
            "clubs": 4,
            "diamonds":  3,
            "hearts":  3,
            "spades": 3,
        }
        self.assertEqual(autoBid.tallyUpTotal(suitCounts), 0)
    
    def test_Singleton(self):
        suitCounts = {
            "clubs": 4,
            "diamonds":  4,
            "hearts":  4,
            "spades": 1,
        }
        self.assertEqual(autoBid.tallyUpTotal(suitCounts), 2)
    
    def test_Doubleton(self):
        suitCounts = {
            "clubs": 4,
            "diamonds":  4,
            "hearts":  3,
            "spades": 2,
        }
        self.assertEqual(autoBid.tallyUpTotal(suitCounts), 1)
    
    def test_FiveOfOne(self):
        suitCounts = {
            "clubs": 5,
            "diamonds":  4,
            "hearts":  3,
            "spades": 3,
        }
        self.assertEqual(autoBid.tallyUpTotal(suitCounts), 1)
    
    def test_Void(self):
        suitCounts = {
            "clubs": 4,
            "diamonds":  0,
            "hearts":  4,
            "spades": 4,
        }
        self.assertEqual(autoBid.tallyUpTotal(suitCounts), 3)

class getDistributionPoints(unittest.TestCase):
    def test_AllOneSuit(self):
        clubs = [i for i in range(0, 13)]
        diamonds = []
        hearts = []
        spades = []
        hand = [clubs, diamonds, hearts, spades]
        self.assertEqual(autoBid.getDistributionPoints(hand), 18)
    
    def test_None(self):
        clubLength = 4
        diamondLength = 4
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        self.assertEqual(autoBid.getDistributionPoints(hand), 0)
    
    def test_Void(self):
        clubLength = 0
        diamondLength = 4
        heartLength = 4
        spadeLength = 4

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        self.assertEqual(autoBid.getDistributionPoints(hand), 3)

    def test_Singleton(self):
        clubLength = 4
        diamondLength = 1
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        self.assertEqual(autoBid.getDistributionPoints(hand), 2)

    def test_Doubleton(self):
        clubLength = 4
        diamondLength = 2
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        self.assertEqual(autoBid.getDistributionPoints(hand), 1)

    def test_FiveLong(self):
        clubLength = 5
        diamondLength = 4
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        self.assertEqual(autoBid.getDistributionPoints(hand), 1)
   
class getCurrentActualBid(unittest.TestCase):
    def test_Normal(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        expected = autoBid.getCurrentActualBid(bids)
        actual = ['Ann', '3 Club']
        self.assertListEqual(expected, actual)
    
    def test_LowerCase(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', '2 No Trump'], ['Tim', 'double'], ['Ann', 'pass'], ['Andrew', 'pass']]
        expected = autoBid.getCurrentActualBid(bids)
        actual = ['Adam', '2 No Trump']
        self.assertListEqual(expected, actual)

    def test_UpperCase(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', '2 NO TRUMP'], ['Tim', 'DOUBLE'], ['Ann', 'PASS'], ['Andrew', 'PASS']]
        expected = autoBid.getCurrentActualBid(bids)
        actual = ['Adam', '2 NO TRUMP']
        self.assertListEqual(expected, actual)

    def test_Empty(self):
        bids = []
        expected = autoBid.getCurrentActualBid(bids)
        actual = None
        self.assertEqual(expected, actual)

