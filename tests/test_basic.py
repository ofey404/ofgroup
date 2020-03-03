'''
@Author: Ofey Chan
@Date: 2020-03-03 17:02:46
@LastEditors: Ofey Chan
@LastEditTime: 2020-03-03 17:29:54
@Description: 
@Reference: 
'''

from .context import ofgroup

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases"""

    def test_hello(self):
        self.assertTrue(ofgroup.hello(), msg="hello() should return True.")

if __name__ == "__main__":
    unittest.main()