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
  def setUp(self) -> None:
    self.actual = {}
    self.expected = {}

  def tearDown(self) -> None:
    print('')
    print('biddingRelative ={0}'.format   (self.biddingRelative))
    print('')
    print('actual:--------------------')
    for location, values in self.actual.items():
      print(location)
      print(f'\t{values}')
    print('')
    print('expected:--------------------')
    for location, values in self.expected.items():
      print(location)
      print(f'\t{values}')
    print('')

  def test_default(self):
    self.biddingRelative = {
        "left": [],
        "top": [],
        "right": [],
        "bottom": [],
    }

    self.obj = getObject(self.biddingRelative)
    print(self.obj)
    self.expected = {
        "left": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
        "top": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          }, 
        },
        "right": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
           getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
    }

    self.actual = getEstimatedSuitCounts.EstimateSuitCounts(self.biddingRelative, self.obj.biddingAbsolute, self.obj.seatingRelative).suitCounts
    self.assertDictEqual(self.expected, self.actual)
  
  def test_open_minor(self):
    self.biddingRelative = {
        "left": ['One Diamond'],
        "top": ['pass'],
        "right": ['pass'],
        "bottom": [],
    }

    self.obj = getObject(self.biddingRelative)
    print(self.obj)
    self.expected = {
        "left": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.openMinorMinValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
        "top": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          }, 
        },
        "right": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
           getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
    }

    self.actual = getEstimatedSuitCounts.EstimateSuitCounts(self.biddingRelative, self.obj.biddingAbsolute, self.obj.seatingRelative).suitCounts
    self.assertDictEqual(self.expected, self.actual)

  def test_open_major(self):
    self.biddingRelative = {
        "left": ['One Spade'],
        "top": ['pass'],
        "right": ['pass'],
        "bottom": [],
    }

    self.obj = getObject(self.biddingRelative)
    print(self.obj)
    self.expected = {
        "left": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.openMajorMinValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
        "top": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          }, 
        },
        "right": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
           getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
    }

    self.actual = getEstimatedSuitCounts.EstimateSuitCounts(self.biddingRelative, self.obj.biddingAbsolute, self.obj.seatingRelative).suitCounts
    self.assertDictEqual(self.expected, self.actual)

  def test_open_NT(self):
    self.biddingRelative = {
        "left": ['One No Trump'],
        "top": ['pass'],
        "right": ['pass'],
        "bottom": [],
    }

    self.obj = getObject(self.biddingRelative)
    print(self.obj)
    self.expected = {
        "left": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.openNoTrumpMinValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.openNoTrumpMinValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.openNoTrumpMinValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.openNoTrumpMinValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
        "top": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          }, 
        },
        "right": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
           getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
    }

    self.actual = getEstimatedSuitCounts.EstimateSuitCounts(self.biddingRelative, self.obj.biddingAbsolute, self.obj.seatingRelative).suitCounts
    self.assertDictEqual(self.expected, self.actual)

def test_open_weakTwo(self):
    self.biddingRelative = {
        "left": ['Two Spade'],
        "top": ['pass'],
        "right": ['pass'],
        "bottom": [],
    }

    self.obj = getObject(self.biddingRelative)
    print(self.obj)
    self.expected = {
        "left": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.openWeakTwo,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
        "top": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          }, 
        },
        "right": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
           getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
    }

    self.actual = getEstimatedSuitCounts.EstimateSuitCounts(self.biddingRelative, self.obj.biddingAbsolute, self.obj.seatingRelative).suitCounts
    self.assertDictEqual(self.expected, self.actual)

def test_open_weakThree(self):
    self.biddingRelative = {
        "left": ['Three Spade'],
        "top": ['pass'],
        "right": ['pass'],
        "bottom": [],
    }

    self.obj = getObject(self.biddingRelative)
    print(self.obj)
    self.expected = {
        "left": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.openWeakThree,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
        "top": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          }, 
        },
        "right": {
          getEstimatedSuitCounts.suits["clubs"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
           getEstimatedSuitCounts.suits["diamonds"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["hearts"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
          getEstimatedSuitCounts.suits["spades"]: {
            "min": getEstimatedSuitCounts.minDefaultValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
    }

    self.actual = getEstimatedSuitCounts.EstimateSuitCounts(self.biddingRelative, self.obj.biddingAbsolute, self.obj.seatingRelative).suitCounts
    self.assertDictEqual(self.expected, self.actual)



