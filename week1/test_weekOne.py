import unittest
import weekOne

class test_addition(unittest.TestCase):
    def test_addition(self):
        assert weekOne.addition(10,3) == 13, "Should be 13"
        assert weekOne.addition(-100,0) == -100, "Should be -100"
        assert weekOne.addition(1.01, 2.99) == 4, "Should be 4"
   

unittest.main()

       

    
