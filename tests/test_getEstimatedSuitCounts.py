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

class OneBidOpportunity(unittest.TestCase):
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

  def test_respond_major_different_suit(self):
    self.biddingRelative = {
        "left": ['One Spade'],
        "top": ['pass'],
        "right": ['Two Heart'],
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
            "min": getEstimatedSuitCounts.openMajorMinValue,
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

  def test_respond_major_same_suit(self):
    self.biddingRelative = {
        "left": ['One Spade'],
        "top": ['pass'],
        "right": ['Two Spade'],
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
            "min": getEstimatedSuitCounts.respondingMinValue,
            "expected": getEstimatedSuitCounts.expectedValue,
          },
        },
    }

    self.actual = getEstimatedSuitCounts.EstimateSuitCounts(self.biddingRelative, self.obj.biddingAbsolute, self.obj.seatingRelative).suitCounts
    self.assertDictEqual(self.expected, self.actual)

  def test_respond_minor_different_suit(self):
    self.biddingRelative = {
        "left": ['One Spade'],
        "top": ['pass'],
        "right": ['Two Club'],
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
            "min": getEstimatedSuitCounts.openMinorMinValue,
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

  def test_respond_minor_same_suit(self):
    self.biddingRelative = {
        "left": ['One Diamond'],
        "top": ['pass'],
        "right": ['Two Diamond'],
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
            "min": getEstimatedSuitCounts.respondingMinValue,
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
              "min": getEstimatedSuitCounts.openWeakTwoMinValue,
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
  
  def test_open_weakTwo_2(self):
      self.biddingRelative = {
          "bottom": ['One Spade'],
          "left": ['Two Heart'],
          "top": ['pass'],
          "right": ['pass'],
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
              "min": getEstimatedSuitCounts.openWeakTwoMinValue,
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
              "min": getEstimatedSuitCounts.openWeakThreeMinValue,
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

  def test_respond_takeout_double(self):
      self.biddingRelative = {
          "bottom": ['One Diamond'],
          "left": ['Double'],
          "top": ['pass'],
          "right": ['One Heart'],
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
              "min": getEstimatedSuitCounts.forcedResponseMinValue,
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

  def test_respond_partner_opening_NT(self):
      self.biddingRelative = {
          "bottom": ['pass'],
          "left": ['One No Trump'],
          "top": ['Pass'],
          "right": ['One Heart'],
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
              "min": getEstimatedSuitCounts.openMajorMinValue,
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

  def test_respond_two_club(self):
      self.biddingRelative = {
          "bottom": ['pass', 'pass'],
          "left": ['Two Club', 'Two Spade'],
          "top": ['Pass', 'pass'],
          "right": ['Two Heart', 'Two Club'],
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
              "min": getEstimatedSuitCounts.forcedResponseMinValue,
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

class TwoBidOpportunities(unittest.TestCase): 
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

  #TODO: need more 2nd suit or 3rd suit cases?
  #what about if pass first, then bid second?
  #Maybe we just need a function that gets if the player being analyzed was the first person on that team to say that suit/NT, if so then they are considered to have opening length in suit/NT?
  #does right have more than 4 min or just more expected (5-6)?
  def test_pass_then_bid(self):
    self.biddingRelative = {
        "right": ['One Club', 'Two Club', 'Three Club'],
        "bottom": ['pass', 'pass'],
        "top": ['pass', 'Two Heart'],
        "left": ['One Diamond', 'Two Spade'],
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
            "min": getEstimatedSuitCounts.forcedResponseMinValue,
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
  


