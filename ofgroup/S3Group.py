'''
@Author: Ofey Chan
@Date: 2020-03-03 16:51:22
@LastEditors: Ofey Chan
@LastEditTime: 2020-03-03 20:07:17
@Description: Test S3 group in permutation group.
@Reference: 
'''

from .Core import FiniteGroup

class S3GroupElement:
    def getAlias(self) -> str:
        contentString = ",".join(map(str, self.content))
        contentStringToAlias = {
            "1,2,3": "e",
            "2,1,3": "(12)",
            "1,3,2": "(23)",
            "3,2,1": "(31)",
            "2,3,1": "(123)",
            "3,1,2": "(132)"
        }
        return contentStringToAlias[contentString]

    
    def __init__(self, content: list):
        super().__init__()
        self.content = content
        self.alias=self.getAlias()
        
    def __mul__(self, other):
        rightToLeftElement = {}
        for index, leftElement in enumerate(self.content):
            rightToLeftElement[index+1] = leftElement
        return S3GroupElement(content=[rightToLeftElement[rightElement] for rightElement in other.content])

    def __eq__(self, other):
        return self.content == other.content

    def __str__(self):
        return self.alias

class S3Group(FiniteGroup):

    def __init__(self):
        e = S3GroupElement([1, 2, 3])
        a12 = S3GroupElement([2, 1, 3])
        a23 = S3GroupElement([1, 3, 2])
        a31 = S3GroupElement([3, 2, 1])
        a123 = S3GroupElement([2, 3, 1])
        a132 = S3GroupElement([3, 1, 2])
        allS3Elements = [e, a12, a23, a31, a123, a132]
        super().__init__(allS3Elements)
        