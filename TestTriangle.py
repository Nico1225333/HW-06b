
import unittest
from triangle import classifyTriangle


class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right')

    def testEquilateralA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    def testEquilateralB(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral')

    def testEquilateralMaximum(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral')

    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isoceles')

    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isoceles')

    def testIsoscelesC(self):
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles')

    def testScaleneA(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    def testScaleneB(self):
        self.assertEqual(classifyTriangle(6, 4, 5), 'Scalene')

    def testNotTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def testNotTriangleB(self):
        self.assertEqual(classifyTriangle(3, 2, 1), 'NotATriangle')

    def testNotTriangleC(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle')

    def testNotTriangleD(self):
        self.assertEqual(classifyTriangle(200, 1, 1), 'NotATriangle')

    def testZeroA(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput')

    def testZeroB(self):
        self.assertEqual(classifyTriangle(4, 0, 5), 'InvalidInput')

    def testZeroC(self):
        self.assertEqual(classifyTriangle(4, 5, 0), 'InvalidInput')

    def testNegativeA(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'InvalidInput')

    def testNegativeB(self):
        self.assertEqual(classifyTriangle(4, -1, 5), 'InvalidInput')

    def testAboveMaximumA(self):
        self.assertEqual(classifyTriangle(201, 5, 5), 'InvalidInput')

    def testAboveMaximumB(self):
        self.assertEqual(classifyTriangle(5, 201, 5), 'InvalidInput')

    def testFloatInputA(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')

    def testFloatInputB(self):
        self.assertEqual(classifyTriangle(3, 4.5, 5), 'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
