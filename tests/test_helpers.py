import unittest
from unittest.case import TestCase
import autoBid 
import helpers
import getEstimatedPoints

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
class getDistributionPoints(unittest.TestCase):
    def setUp(self):
        self.seatingRelative = {
            "top": "Adam",
            "bottom": "Tim",
            "left": "Andrew",
            "right": "Ann",
        }
    def test_Opening_AllOneSuit(self):
        clubs = [i for i in range(0, 13)]
        diamonds = []
        hearts = []
        spades = []
        hand = [clubs, diamonds, hearts, spades]
        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": 13,
            "diamonds": 0,
            "hearts": 0,
            "spades": 0,
        }

        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 18)
    def test_Opening_None(self):
        clubLength = 4
        diamondLength = 4
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }

        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 0)
    def test_Opening_Void(self):
        clubLength = 0
        diamondLength = 4
        heartLength = 4
        spadeLength = 4

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }

        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 3)
    def test_Opening_Singleton(self):
        clubLength = 4
        diamondLength = 1
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }

        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 2)
    def test_Opening_Doubleton(self):
        clubLength = 4
        diamondLength = 2
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }

        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 1)
    def test_Opening_FiveLong(self):
        clubLength = 5
        diamondLength = 4
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]

        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }
        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 1)

    def test_Responding_AllOneSuit(self):
        clubs = [i for i in range(0, 13)]
        diamonds = []
        hearts = []
        spades = []
        hand = [clubs, diamonds, hearts, spades]
        allBids = [["Adam", 'One Club'],['Tim', 'Pass']]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['One Club'],
            "bottom": [],
            "left": [],
            "right": ['Pass'],
        }
        suitCounts = {
            "clubs": 13,
            "diamonds": 0,
            "hearts": 0,
            "spades": 0,
        }

        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 'Not Done')
    def test_Responding_None(self):
        clubLength = 4
        diamondLength = 4
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }

        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 'Not Done')
    def test_Responding_Void(self):
        clubLength = 0
        diamondLength = 4
        heartLength = 4
        spadeLength = 4

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }

        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 'Not Done')
    def test_Responding_Singleton(self):
        clubLength = 4
        diamondLength = 1
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }

        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 'Not Done')
    def test_Responding_Doubleton(self):
        clubLength = 4
        diamondLength = 2
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]
        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }

        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 'Not Done')
    def test_Responding_FiveLong(self):
        clubLength = 5
        diamondLength = 4
        heartLength = 3
        spadeLength = 3

        clubs = [i for i in range(0, 0 + clubLength)]
        diamonds = [i for i in range(13, 13 + diamondLength)]
        hearts = [i for i in range(26, 26 + heartLength)]
        spades = [i for i in range(39, 39 + spadeLength)]
        hand = [clubs, diamonds, hearts, spades]

        allBids = []
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
        }
        suitCounts = {
            "clubs": clubLength,
            "diamonds": diamondLength,
            "hearts": heartLength,
            "spades": spadeLength,
        }
        self.assertEqual(helpers.getDistributionPoints(hand, allBids, biddingObjRelative, self.seatingRelative, suitCounts), 'Not Done')
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
class getRotationsAround(unittest.TestCase):
    def test_negative(self):
        spot = 'north'
        numberOfRotations = -1
        with self.assertRaises(TypeError) as context:
            helpers.getSpotAfterNRotations(spot, numberOfRotations)
            self.assertTrue('Invalid numberOfRotations' in context.exception)

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
        actual = helpers.getSuitCounts(hand)
        expected = {
            "clubs": 0,
            "diamonds":  0,
            "hearts":  0,
            "spades": 0,
        }
        self.assertEqual(actual, expected)
    def test_one(self):
        hand = [[0, 1, 5, 7, 8], [13, 18, 19], [29, 30, 32], [40, 42]]
        actual = helpers.getSuitCounts(hand)
        expected = {
            "clubs": 5,
            "diamonds":  3,
            "hearts":  3,
            "spades": 2,
        }
        self.assertEqual(actual, expected)
    def test_two(self):
        hand = [[0, 1, 5, 7, 8,9,10], [13, 19], [29], [40, 42,51]]
        actual = helpers.getSuitCounts(hand)
        expected = {
            "clubs": 7,
            "diamonds":  2,
            "hearts":  1,
            "spades": 3,
        }
        self.assertEqual(actual, expected)
    def test_three(self):
        hand = [[0, 1, 2,3], [13,15,17,18, 19], [29,31,33,34], []]
        actual = helpers.getSuitCounts(hand)
        expected = {
            "clubs": 4,
            "diamonds":  5,
            "hearts":  4,
            "spades": 0,
        }
        self.assertEqual(actual, expected)
    def test_four(self):
        hand = [[0, 1, 2,3,4,5,6,7,8,9,10,11,12], [],[], []]
        actual = helpers.getSuitCounts(hand)
        expected = {
            "clubs": 13,
            "diamonds":  0,
            "hearts":  0,
            "spades": 0,
        }
        self.assertEqual(actual, expected)
class partnerTwoClubResponse(unittest.TestCase):
    def test_intervention(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club'],
            "left": ['One Diamond'],
        }
        totalOpeningPoints = 0
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingObjRelative, totalOpeningPoints, currentActualBid)
        expected = 'Pass'
        self.assertEqual(actual, expected)
    def test_initial_zero(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 0
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingObjRelative, totalOpeningPoints, currentActualBid)
        expected = 'Two Diamond'
        self.assertEqual(actual, expected)
    def test_initial_3(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 3
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingObjRelative, totalOpeningPoints, currentActualBid)
        expected = 'Two Diamond'
        self.assertEqual(actual, expected)
    def test_initial_6(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 6
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingObjRelative, totalOpeningPoints, currentActualBid)
        expected = 'Two Heart'
        self.assertEqual(actual, expected)
    def test_initial_9(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 9
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingObjRelative, totalOpeningPoints, currentActualBid)
        expected = 'Two Spade'
        self.assertEqual(actual, expected)
    def test_initial_12(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 12
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingObjRelative, totalOpeningPoints, currentActualBid)
        expected = 'Two No Trump'
        self.assertEqual(actual, expected)
    def test_initial_15(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club'],
            "left": ['Pass'],
        }
        totalOpeningPoints = 15
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse([], biddingObjRelative, totalOpeningPoints, currentActualBid)
        expected = 'Three Club'
        self.assertEqual(actual, expected)
    def test_second_true(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23, 24], [29, 30, 32], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club', 'Three Diamond'],
            "left": ['Pass', 'Pass'],
        }
        totalOpeningPoints = 15
        currentActualBid = ['Adam', 'Two Club']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
        expected = 'Four Club'
        self.assertEqual(actual, expected)
    def test_ask_for_aces_one(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23, 24], [29, 30, 32], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three Diamond', 'Four No Trump', 'Five Diamond'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five Club']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three No Trump', 'Four No Trump', 'Five No Trump'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three Club', 'Four No Trump', 'Five Diamond'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five Diamond']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three Club', 'Four No Trump', 'Five Heart'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five Heart']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three Club', 'Four No Trump', 'Five Spade'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five Spade']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three Club', 'Four No Trump', 'Five No Trump'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Five No Trump']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
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
        biddingObjRelative = {
            "top": ['Two Club', 'Three Club', 'Four No Trump', 'Four Diamond'],
            "left": ['Pass', 'Pass', 'Pass', 'Pass'],
        }
        totalOpeningPoints = 4
        currentActualBid = ['Adam', 'Four Diamond']
        actual = helpers.getTwoClubResponse(hand, biddingObjRelative, totalOpeningPoints, currentActualBid)
        expected = 'Four Heart'
        self.assertEqual(actual, expected)
#need to finish this
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
    def test_LengthOverPointCount(self):
        hand = [[0, 1, 7, 8,12], [13, 18, 23, 24], [29, 30, 32], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club', 'Three Diamond'],
            "left": ['Pass', 'Pass'],
        }
        actual = helpers.getStrongestSuit(hand, biddingObjRelative)
        expected = 'Four Club'
        self.assertEqual(actual, expected)
    def test_length(self):
        hand = [[0, 1, 7], [13, 18, 25], [29, 30, 32,33,34], [40,42]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club', 'Three Diamond'],
            "left": ['Pass', 'Pass'],
        }
        totalOpeningPoints = 0
        currentActualBid = ['Adam', 'Three Diamond']
        actual = helpers.getStrongestSuit(hand, biddingObjRelative)
        expected = 'Three Heart'
        self.assertEqual(actual, expected)
    def test_pointCountOverLength(self):
        hand = [[0, 1, 7], [13, 18, 25], [29, 30, 32,33,34], [48,49,50,51]]
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "top": ['Two Club', 'Three Diamond'],
            "left": ['Pass', 'Pass'],
        }
        totalOpeningPoints = 0
        currentActualBid = ['Adam', 'Three Diamond']
        actual = helpers.getStrongestSuit(hand, biddingObjRelative)
        expected = 'Three Spade'
        self.assertEqual(actual, expected)
class getSuitsMentionedByOpponents(unittest.TestCase):
    def test_five(self):
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "right": ['Two Club', 'Three Diamond', 'Four No Trump'],
            "left": ['Two Heart', 'Three Spade'],
            "bottom": ['Pass', 'Pass'],
            "top": ['Pass', 'Pass'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingObjRelative)
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
        biddingObjRelative = {
            "right": ['Pass', 'Three Diamond', 'Four No Trump'],
            "left": ['Two Heart', 'Three Spade'],
            "bottom": ['Two Club', 'Pass'],
            "top": ['Pass', 'Three Club'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingObjRelative)
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
        biddingObjRelative = {
            "right": ['Pass', 'Three Diamond', 'Pass'],
            "left": ['Two Heart', 'Three Spade'],
            "bottom": ['Two Club', 'Pass'],
            "top": ['Three No Trump', 'Three Club'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingObjRelative)
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
        biddingObjRelative = {
            "right": ['Pass', 'Three Diamond', 'Double'],
            "left": ['Double', 'Three Spade'],
            "bottom": ['Two Club', 'Pass'],
            "top": ['Three No Trump', 'Three Club'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingObjRelative)
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
        biddingObjRelative = {
            "right": ['Pass', 'Three Club', 'Pass'],
            "left": ['Double', 'Four Club'],
            "bottom": ['Two Club', 'Pass'],
            "top": ['Three No Trump', 'Three Club'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingObjRelative)
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
        biddingObjRelative = {
            "right": ['Pass', 'Double', 'Pass'],
            "left": ['Double', 'Pass'],
            "bottom": ['Two Club', 'Three Diamond'],
            "top": ['Three No Trump', 'Three Club'],
        }
        actual = helpers.getSuitsMentionedByOpponents(biddingObjRelative)
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
        biddingObjRelative = {
            "left": [],
            "top": ['pass'],
            "right": ['pass'],
            "bottom": [],
        }
        actual = getEstimatedPoints.getIsTeamsFirstBidOpportunity(biddingObjRelative, 'top')
        expected = True
        self.assertEqual(actual, expected)
    def test_bottom(self): 
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
        actual = getEstimatedPoints.getIsTeamsFirstBidOpportunity(biddingObjRelative, 'bottom')
        expected = False
        self.assertEqual(actual, expected)
    def test_right(self): 
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
            "bottom": [],
        }
        actual = getEstimatedPoints.getIsTeamsFirstBidOpportunity(biddingObjRelative, 'right')
        expected = False
        self.assertEqual(actual, expected)
    def test_left(self): 
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
            "bottom": [],
        }
        actual = getEstimatedPoints.getIsTeamsFirstBidOpportunity(biddingObjRelative, 'left')
        expected = True
        self.assertEqual(actual, expected)
    def test_left_2(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass', 'pass'],
            "top": ['pass', 'two diamond'],
            "right": ['pass', 'pass'],
            "bottom": ['two club'],
        }
        actual = getEstimatedPoints.getIsTeamsFirstBidOpportunity(biddingObjRelative, 'left')
        expected = False
        self.assertEqual(actual, expected)
    def test_top_2(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass', 'pass'],
            "top": ['pass', 'two diamond'],
            "right": ['pass', 'pass'],
            "bottom": ['two club'],
        }
        actual = getEstimatedPoints.getIsTeamsFirstBidOpportunity(biddingObjRelative, 'top')
        expected = False
        self.assertEqual(actual, expected)
    def test_bottom_2(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass', 'pass'],
            "top": ['pass', 'two diamond'],
            "right": ['pass', 'pass'],
            "bottom": ['two club'],
        }
        actual = getEstimatedPoints.getIsTeamsFirstBidOpportunity(biddingObjRelative, 'bottom')
        expected = False
        self.assertEqual(actual, expected)
    def test_right_2(self): 
        currentEstimatedPoints = {
            "left": None,
            "top": None,
            "right": None,
            "Bottom": None,
        }
        biddingObjRelative = {
            "left": ['pass', 'pass'],
            "top": ['pass', 'two diamond'],
            "right": ['pass', 'pass'],
            "bottom": ['two club'],
        }
        actual = getEstimatedPoints.getIsTeamsFirstBidOpportunity(biddingObjRelative, 'right')
        expected = False
        self.assertEqual(actual, expected)
    def test_right_3(self): 
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
        actual = getEstimatedPoints.getIsTeamsFirstBidOpportunity(biddingObjRelative, 'right')
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



class getEstimatedPointsModule(unittest.TestCase):
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
    #region Setting Initial Bounds (when a player has only bid once)
    def test_set_exit_early(self):
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
            "bottom": [],
        }
        seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
        bids = [['LeftPlayer', "One Diamond"],['TopPlayer', 'Two Heart'],['RightPlayer', 'Two No Trump']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
        print('actual = {0}'.format(actual))
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
    #endregion
    #region Updating Initial Bounds (when a player has bid twice)
    #TODO: These tests are just copied over from setting intial section
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
        seatingRelative = {
            "top": "TopPlayer",
            "bottom": "BottomPlayer",
            "left": "LeftPlayer",
            "right": "RightPlayer",
        }
        bids = [['LeftPlayer', "One Diamond"],['TopPlayer', 'Two Heart'],['RightPlayer', 'Two No Trump']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'Pass'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'One No Trump'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'Two Club'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Two Club']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Two Club']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'Double'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Double']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Double']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'One Diamond'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'One Diamond']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'One Spade']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'Two Diamond'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Two Spade']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Two Heart']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'One Club'], ['RightPlayer', 'Two Heart']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'Pass'], ['TopPlayer', 'One Club'], ['RightPlayer', 'Two Spade']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'Three Diamond'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['TopPlayer', 'pass'], ['RightPlayer', 'Three Diamond']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'pass'],['TopPlayer', 'pass'], ['RightPlayer', 'Three Diamond']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
        seatingRelative = {
            "left": "LeftPlayer",
            "top": "TopPlayer",
            "right": "RightPlayer",
            "bottom": "BottomPlayer",
        }
        bids = [['LeftPlayer', 'One Diamond'], ['TopPlayer', 'Three Heart'], ['RightPlayer', 'Pass']]
        actual = getEstimatedPoints.getEstimatedPoints(currentEstimatedPoints, biddingObjRelative, bids, seatingRelative)
        print('actual = {0}'.format(actual))
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
   
    #endregion
    #region updating bounds (when a player has bid more than twice?)
    #endregion

class getHasPartnerOpened(unittest.TestCase):
    def test_incorrect_name(self):
        bids = [['Adam', 'Pass'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        expected = helpers.getHasPartnerOpened(bids, 'Anns')
        actual = None
        self.assertEqual(expected, actual) 
    def test_false(self):
        bids = [['Adam', 'Pass'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        expected = helpers.getHasPartnerOpened(bids, 'Ann')
        actual = False
        self.assertEqual(expected, actual) 
    def test_false_2(self):
        bids = [['Adam', 'Double'], ['Tim', 'Pass'], ['Ann', '3 Club'], ['Andrew', 'Pass'], ['Adam', 'Double']]
        expected = helpers.getHasPartnerOpened(bids, 'Andrew')
        actual = False
        self.assertEqual(expected, actual) 
    def test_true(self):
        bids = [['Adam', 'Two No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Three Diamond'], ['Adam', 'Double']]
        expected = helpers.getHasPartnerOpened(bids, 'Andrew')
        actual = True
        self.assertEqual(expected, actual) 
    def test_length_1(self):
        bids = [['Adam', '2 No Trump']]
        expected = helpers.getHasPartnerOpened(bids, 'Andrew')
        actual = None
        self.assertEqual(expected, actual) 
    def test_length_0(self):
        bids = []
        expected = helpers.getHasPartnerOpened(bids, 'Andrew')
        actual = None
        self.assertEqual(expected, actual) 
    def test_length_2(self):
        bids = [['Adam', '2 No Trump'],['Tim','Pass']]
        expected = helpers.getHasPartnerOpened(bids, 'Tim')
        actual = False
        self.assertEqual(expected, actual) 
    def test_true_2(self):
        bids = [['Adam', '2 No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Three Diamond'], ['Adam', 'Double'], ['Tim', 'Three Heart']]

        expected = helpers.getHasPartnerOpened(bids, 'Ann')
        actual = True
        self.assertEqual(expected, actual) 
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
        currentContractBid = ['Tim','Two Club']
        usersBid = 'Pass'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_double(self):
        currentContractBid = ['Tim','Two Club']
        usersBid = 'Double'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_noActualBid(self):
        currentContractBid = []
        usersBid = 'Three Club'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_False_1(self):
        currentContractBid = ['Tim','Two Club']
        usersBid = 'Three Club'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_False_2(self):
        currentContractBid = ['Tim','Two Club']
        usersBid = 'Two Diamond'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_False_3(self):
        currentContractBid = ['Tim','One Spade']
        usersBid = 'One No Trump'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = False
        self.assertEqual(actual, expected)
    def test_True_1(self):
        currentContractBid = ['Tim','One Club']
        usersBid = 'Three Club'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = True
        self.assertEqual(actual, expected)
    def test_True_2(self):
        currentContractBid = ['Tim','One No Trump']
        usersBid = 'Three Club'
        actual = helpers.getIsJumpshift(currentContractBid, usersBid)
        expected = True
        self.assertEqual(actual, expected)
    def test_True_3(self):
        currentContractBid = ['Tim','Three Spade']
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
        allBids = [['Tim', 'Pass'],['Tom', 'Pass'],['James', 'One Club'],['You', 'Pass'],['Tim', 'One Diamond'],['Tom', 'Pass'],['James', 'Pass'],['You', 'Two Heart'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass']]
        playersBids = ['Pass','Two Heart']
        actual = helpers.getHasPlayerJumpshifted(username, playersBids, allBids)
        expected = True
        self.assertEqual(actual, expected)
    def test_True_2(self):
        username = 'You'
        allBids = [['Tim', 'Pass'],['Tom', 'Pass'],['James', 'One Club'],['You', 'Pass'],['Tim', 'One Diamond'],['Tom', 'Pass'],['James', 'Pass'],['You', 'One Heart'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass'], ['You', 'Three Club'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass']]
        playersBids = ['Pass', 'One Heart', 'Three Club']
        actual = helpers.getHasPlayerJumpshifted(username, playersBids, allBids)
        expected = True
        self.assertEqual(actual, expected)
    def test_False_1(self):
        username = 'You'
        allBids = [['Tim', 'Pass'],['Tom', 'Pass'],['James', 'One Club'],['You', 'Pass'],['Tim', 'One Diamond'],['Tom', 'Pass'],['James', 'Pass'],['You', 'Two Heart'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass']]
        playersBids = ['Pass','One Heart']
        actual = helpers.getHasPlayerJumpshifted(username, playersBids, allBids)
        expected = False
        self.assertEqual(actual, expected)
    def test_False_2(self):
        username = 'You'
        allBids = [['Tim', 'Pass'],['Tom', 'Pass'],['James', 'One Club'],['You', 'Pass'],['Tim', 'One Diamond'],['Tom', 'Pass'],['James', 'Pass'],['You', 'One Heart'],['Tim', 'Two Spade'],['Tom', 'Pass'],['James', 'Pass'], ['You', 'Three Club'],['Tim', 'Pass'],['Tom', 'Pass'],['James', 'Pass']]
        playersBids = ['Pass', 'One Heart', 'Three Club']
        actual = helpers.getHasPlayerJumpshifted(username, playersBids, allBids)
        expected = False
        self.assertEqual(actual, expected)
class getHasSomeOneOpenedBefore(unittest.TestCase):
    def test_empty(self):
        indexOfUsersFirstBid = None
        allBids = []
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids)
        expected = False
        self.assertEqual(actual, expected)
    def test_not_yet_bid_false_1(self):
        indexOfUsersFirstBid = None
        allBids = [['Adam', 'Pass']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids)
        expected = False
        self.assertEqual(actual, expected)
    def test_not_yet_bid_false_2(self):
        indexOfUsersFirstBid = None
        allBids = [['Adam', 'Pass'], ['Tim', 'Double']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids)
        expected = False
        self.assertEqual(actual, expected)
    def test_not_yet_bid_true_1(self):
        indexOfUsersFirstBid = None
        allBids = [['Adam', 'Pass'], ['Tim', 'Two Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids)
        expected = True
        self.assertEqual(actual, expected)
    def test_not_yet_bid_true_2(self):
        indexOfUsersFirstBid = None
        allBids = [['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids)
        expected = True
        self.assertEqual(actual, expected)

    def test_has_bid_false_1(self):
        indexOfUsersFirstBid = 2
        allBids = [['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club'],['Andrew','Pass'],['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids)
        expected = False
        self.assertEqual(actual, expected)
    def test_has_bid_false_2(self):
        indexOfUsersFirstBid = 0
        allBids = [['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Pass'],['Andrew','One Heart'],['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids)
        expected = False
        self.assertEqual(actual, expected)
    def test_has_bid_true_1(self):
        indexOfUsersFirstBid = 3
        allBids = [['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club'],['Andrew','Pass'],['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids)
        expected = True
        self.assertEqual(actual, expected)
    def test_has_bid_true_2(self):
        indexOfUsersFirstBid = 4
        allBids = [['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Pass'],['Andrew','One Heart'],['Adam', 'Pass'], ['Tim', 'Pass'], ['Ann', 'Three Club']]
        actual = helpers.getHasSomeOneOpenedBefore(indexOfUsersFirstBid, allBids)
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
        actual = getEstimatedPoints.getPlayerHasOnlyPassed(bids)
        expected = True
        self.assertEqual(actual, expected)
    def test_only_pass_one(self):
        bids = ['Pass']
        actual = getEstimatedPoints.getPlayerHasOnlyPassed(bids)
        expected = True
        self.assertEqual(actual, expected)
    def test_only_pass_multiple(self):
        bids = ['Pass', 'pass', 'Pass']
        actual = getEstimatedPoints.getPlayerHasOnlyPassed(bids)
        expected = True
        self.assertEqual(actual, expected)
    def test_bid_one(self):
        bids = ['Two Club']
        actual = getEstimatedPoints.getPlayerHasOnlyPassed(bids)
        expected = False
        self.assertEqual(actual, expected)
    def test_bid_multiple(self):
        bids = ['Pass', 'Three Diamond', 'Pass']
        actual = getEstimatedPoints.getPlayerHasOnlyPassed(bids)
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
    

#region Testing Test Case Helpers
class getDealerFromBiddingObjRelative(unittest.TestCase):
    def test_empty_dict(self):
        biddingObjRelative = {
            "left": [],
            "top": [],
            "right": [],
            "bottom": [],
        }
        estimated = None
        actual = helpers.getDealerFromBiddingObjRelative(biddingObjRelative)
        self.assertEqual(actual, estimated)
    def test_none(self):
        biddingObjRelative = None
        estimated = None
        actual = helpers.getDealerFromBiddingObjRelative(biddingObjRelative)
        self.assertEqual(actual, estimated)
    def test_left(self):
        biddingObjRelative = {
            "left": ['One Diamond'],
            "top": ['Three Heart'],
            "right": ['pass'],
            "bottom": [],
        }
        estimated = 'left'
        actual = helpers.getDealerFromBiddingObjRelative(biddingObjRelative)
        self.assertEqual(actual, estimated)
    def test_top(self):
        biddingObjRelative = {
            "left": [],
            "top": ['Three Heart'],
            "right": ['pass'],
            "bottom": [],
        }
        estimated = 'top'
        actual = helpers.getDealerFromBiddingObjRelative(biddingObjRelative)
        self.assertEqual(actual, estimated)
    def test_bottom(self):
        biddingObjRelative = {
            "left": [],
            "top": [],
            "right": ['pass'],
            "bottom": [],
        }
        estimated = 'right'
        actual = helpers.getDealerFromBiddingObjRelative(biddingObjRelative)
        self.assertEqual(actual, estimated)
    def test_two_1(self):
        biddingObjRelative = {
            "left": ['Pass','Two Club'],
            "top": ['Three Heart'],
            "right": ['pass'],
            "bottom": ['pass'],
        }
        estimated = 'left'
        actual = helpers.getDealerFromBiddingObjRelative(biddingObjRelative)
        self.assertEqual(actual, estimated)
    def test_three(self):
        biddingObjRelative = {
            "left": ['Pass','Two Club'],
            "top": ['Three Heart', 'T'],
            "right": ['pass', 'p'],
            "bottom": ['pass', 'p', 'p'],
        }
        estimated = 'bottom'
        actual = helpers.getDealerFromBiddingObjRelative(biddingObjRelative)
        self.assertEqual(actual, estimated)
    def test_four(self):
        biddingObjRelative = {
            "left": ['Pass','Two Club', 'p'],
            "top": ['Three Heart', 'T', 'p', 'p'],
            "right": ['pass', 'p', 'p'],
            "bottom": ['pass', 'p', 'p'],
        }
        estimated = 'top'
        actual = helpers.getDealerFromBiddingObjRelative(biddingObjRelative)
        self.assertEqual(actual, estimated)
#endregion










