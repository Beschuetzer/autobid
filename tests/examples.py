
import unittest

#this is the name of the function
class NameOfFunctionBeingTested(unittest.TestCase):
    
    #this is how you name a test case (must start with 'test_')
    def test_caseName(self):
        self.assertTrue(True)

    #comparing equality of valu
    def test_sumSuccess(self):
        #do some things to get the actual
        actual = sum([1,3,4])
        expected = 8
        self.assertEqual(actual, expected)

    def test_sumFail(self):
        #do some things to get the actual
        actual = sum([1,3,4])
        expected = 7
        self.assertEqual(actual, expected)

    #comparing boolean True
    def test_isEven(self):
        #do some things to get the actual
        numberToTest = 6
        actual = numberToTest % 2 == 0
        self.assertTrue(actual)

    #comparing boolean False
    def test_isEvenFalse(self):
        #do some things to get the actual
        numberToTest = 7
        actual = numberToTest % 2 == 0
        self.assertFalse(actual)

    #comparing lists
    def test_isSameList(self):
        self.assertListEqual([1,2], [1,2])

    def test_isSameListFail(self):
        self.assertListEqual([1,2], [1,2,3])


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

