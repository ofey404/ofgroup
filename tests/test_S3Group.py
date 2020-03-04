from .context import ofgroup

import unittest

class S3GroupTestSuite(unittest.TestCase):
    """S3Group.py's test cases"""

    def test_printableMultiplicationTable(self):
        s = ofgroup.S3Group()
        self.assertEqual(
"""+-------+-------+-------+-------+-------+-------+-------+
|   \   |   e   |  (12) |  (23) |  (31) | (123) | (132) |
+-------+-------+-------+-------+-------+-------+-------+
|   e   |   e   |  (12) |  (23) |  (31) | (123) | (132) |
|  (12) |  (12) |   e   | (123) | (132) |  (23) |  (31) |
|  (23) |  (23) | (132) |   e   | (123) |  (31) |  (12) |
|  (31) |  (31) | (123) | (132) |   e   |  (12) |  (23) |
| (123) | (123) |  (31) |  (12) |  (23) | (132) |   e   |
| (132) | (132) |  (23) |  (31) |  (12) |   e   | (123) |
+-------+-------+-------+-------+-------+-------+-------+""",
        str(s.printableMultiplicationTable())
        )



if __name__ == "__main__":
    unittest.main()