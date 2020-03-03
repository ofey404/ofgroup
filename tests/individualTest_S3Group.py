'''
@Author: Ofey Chan
@Date: 2020-03-03 18:51:04
@LastEditors: Ofey Chan
@LastEditTime: 2020-03-03 20:13:09
@Description: Individual test for S3 Group
    Usage:
    > pwd; python individualTest_S3Group.py           
    /Users/ofey/Code/GroupTheoryCode/Ofey'sGroupPackage/tests
    +-------+-------+-------+-------+-------+-------+-------+
    |   \   |   e   |  (12) |  (23) |  (31) | (123) | (132) |
    +-------+-------+-------+-------+-------+-------+-------+
    |   e   |   e   |  (12) |  (23) |  (31) | (123) | (132) |
    |  (12) |  (12) |   e   | (123) | (132) |  (23) |  (31) |
    |  (23) |  (23) | (132) |   e   | (123) |  (31) |  (12) |
    |  (31) |  (31) | (123) | (132) |   e   |  (12) |  (23) |
    | (123) | (123) |  (31) |  (12) |  (23) | (132) |   e   |
    | (132) | (132) |  (23) |  (31) |  (12) |   e   | (123) |
    +-------+-------+-------+-------+-------+-------+-------+
@Reference: 
'''
from context import ofgroup

s = ofgroup.S3Group()
s.printMultiplicationTable()
