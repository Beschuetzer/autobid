#add case where pass then 3 level response means 1 more than min?

import helpers
import getEstimatedSuitCounts
import unittest, testCases

def getObject(biddingRelative = None):
  seatingRelative = {
    "top": "TopPlayer",
    "bottom": "BottomPlayer",
    "left": "LeftPlayer",
    "right": "RightPlayer",
  }
  biddingAbsolute = helpers.getBiddingAbsoluteFromBiddingObjAndSeatingRelative(biddingRelative, seatingRelative)
  obj = getEstimatedSuitCounts.EstimateSuitCounts(biddingRelative, biddingAbsolute, seatingRelative)
  return obj

class TestingResultMethod(unittest.TestCase):
  def tearDown(self) -> None:
    print('')
    print('biddingRelative ={0}'.format   (self.biddingRelative))
    print('actual ={0}'.format   (self.actual))
    print('expected = {0}'.format(self.expected))
    print('')

  def test_1(self):
    self.biddingRelative = testCases.biddingRelatives['oneBidOpportunity']['notForcedOneNoTrumpResponse']
    self.obj = getObject(self.biddingRelative)

    self.expected = 10
    self.actual = getEstimatedSuitCounts.EstimateSuitCounts(self.biddingRelative, self.obj.biddingAbsolute, self.obj.seatingRelative).getResult(5, 2)
    self.assertEqual(self.expected, self.actual)
