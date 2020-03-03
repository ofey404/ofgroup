'''
@Author: Ofey Chan
@Date: 2020-03-03 16:50:33
@LastEditors: Ofey Chan
@LastEditTime: 2020-03-03 20:06:53
@Description: Shared class of ofgroup package.
@Reference: 
'''

import prettytable

def hello():
    """Print a hello message"""
    print("Hello, I'm ofgroup!")
    return True

class FiniteGroup():
    """Group with finite number of element."""

    def __init__(self, allElements: list):
        """Args:
          allElements: All elements of the group.
                       Identity(e) should be placed on [0].
        """
        self.allElements = allElements
        self.e = allElements[0]

    def findConjugateClass(self, element):
        """Find conjugate class that contains the element.
        Args:
          element: Given group element.
                   Should be in `allElements` list of this group object.

        Returns:
          A tuple contains all elements of conjugate class.
          Won't promise element in argument goes first.
          eg: (element, [otherElement1, Element2, ...])
        """
        conjugateClass = []
        for testElement in self.allElements:
            # test if `testElement` is `element`'s conjugate.
            for g in self.allElements:
                # find whether any element g could fulfill `g_i = g * g_j * g^-1`
                if element == g * (testElement * self.inverseElement(g)):
                    conjugateClass.append(element)
                    break
        return conjugateClass

    def findAllConjugateClass(self):
        """Find all conjugate class of this group object.
        Repeatedly call `findConjugateClass()` method.
        Choose the first remain element each time.

        Returns:
          A 2D tuple contains all conjugate classes,
          each class's all elements placed in the same tuple.
          eg: (
              (Class1Element1, Class1Element2, ...),
              (Class2Element1, Class2Element2, ...),
              ...
          )
        """
        remainElements = self.allElements.copy()
        allConjugateClasses = []
        while remainElements:
            testElement = remainElements[0]
            conjugateClass = self.findConjugateClass(testElement)
            allConjugateClasses.append(conjugateClass)
            for elementToDelete in conjugateClass:
                # prevent elements in this conjugate class from being chosen again.
                del remainElements[remainElements.index(elementToDelete)]
            
    def inverseElement(self, element):
        """Return inverse element in this group of the given element.
        Args:
          element: Given group element.
                   Should be in `allElements` list of this group object.
                   
        Returns:
          The inverse element of given element.

        Raises:
          Exception: If no inverse element is found.
        """
        for testElement in self.allElements:
            if element * testElement == self.e:
                return testElement
        raise Exception("No inverse Element of element:\n{}".format(element))

    def printMultiplicationTable(self):
        """Print multiplication table of current group object.
        Call `__str__()` method of element.
        Use prettytable package to format.
        """
        table = prettytable.PrettyTable()
        table.field_names = ["\\"] + list(map(str, self.allElements))
        for leftElement in self.allElements:
            table.add_row(
                [str(leftElement)] + 
                [str(leftElement*rightElement) for rightElement in self.allElements]
                )
        print(table)