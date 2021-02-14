import unittest
import autobid



class getSuitFromCardAsNumber(unittest.TestCase):
    def test_clubLow(self):
        self.assertEqual(autobid.getSuitFromCardAsNumber(0), 'club')
    def test_clubHigh(self):
        self.assertEqual(autobid.getSuitFromCardAsNumber(12), 'club')
    def test_diamondLow(self):
        self.assertEqual(autobid.getSuitFromCardAsNumber(13), 'diamond')
    def test_diamondHigh(self):
        self.assertEqual(autobid.getSuitFromCardAsNumber(25), 'diamond')
    def test_heartLow(self):
        self.assertEqual(autobid.getSuitFromCardAsNumber(26), 'heart')
    def test_heartHigh(self):
        self.assertEqual(autobid.getSuitFromCardAsNumber(38), 'heart')
    def test_spadeLow(self):
        self.assertEqual(autobid.getSuitFromCardAsNumber(39), 'spade')
    def test_spadeHigh(self):
        self.assertEqual(autobid.getSuitFromCardAsNumber(51), 'spade')

class getPartnersBids(unittest.TestCase):
    # bidsExample = [['Adam', 'Two No Trump'], ['Tim', 'Double'], ['Ann', '3 Club'], ['Andrew', 'Pass']]

    def test_noBids(self):
        expected = autobid.getPartnersBids([])
        self.assertListEqual(expected, [])
   
    def test_1Bid(self):
        bids = [['Adam', 'Two No Trump']]
        expected = autobid.getPartnersBids(bids)
        self.assertListEqual(expected, [])
    def test_2Bids(self):
        bids = [
            ['Adam', 'Two No Trump'],
            ['Tim', 'Three No Trump'],
        ]  

        expected = autobid.getPartnersBids(bids)
        self.assertListEqual(expected, ['Two No Trump'])
    def test_3Bids(self):
        bids = [
            ['Adam', 'Two No Trump'],
            ['Tim', 'Three No Trump'],
            ['Ann', 'Four No Trump'],
            ['Andrew', 'Pass'],
        ]
        expected = autobid.getPartnersBids(bids)
        self.assertListEqual(expected, ['Four No Trump'])
    def test_5Bids(self):
        bids = [
            ['Adam', 'Two No Trump'],
            ['Tim', 'Three No Trump'],
            ['Ann', 'Four No Trump'],
            ['Andrew', 'Pass'],
            ['Adam', 'Double'],
        ]
        expected = autobid.getPartnersBids(bids)
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
        expected = autobid.getPartnersBids(bids)
        self.assertListEqual(expected, ['Pass', 'Double'])
    








