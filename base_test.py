"""
TestScript to verify different functionalities for Complex number operations. 
'TestComplex' consists of multiple functions each verifying the complex operations.
Addition : testAdd ; Subtraction : testSub ; Multiplication: testMul; Division : TestDiv; 
Modulus : TestMod; Conjugate : testConj ; Phase : testPhase 
An example complex numbers, comp1 = 2+3i and comp2 = 1+4i is used for verification
"""
from Imaginary import ImagOp
import unittest
import cmath

class TestComplex(unittest.TestCase):
    def setUp(self):
        self.comp1 = ImagOp(5, 11)
        self.comp2 = ImagOp(3, 6)
    #
    def testAdd(self):
        #Addition
        CompSum = self.comp1 + self.comp2
        #print("Addition", str(CompSum))
        self.assertEqual(str(CompSum), "8 + 17i")

    def testSub(self):
        #Substraction
        CompSub = self.comp1 - self.comp2
        #print("Subtraction : ", str(CompSub))
        self.assertEqual(str(CompSub), "2 + 5i")

    def testMul(self):
        #multiplication
        CompMul = self.comp1 * self.comp2
        #print("Multiplication : ", str(CompMul))
        self.assertEqual(str(CompMul), "-51 + 63i")

    def testDiv(self):
        #Division
        CompDiv = self.comp1 / self.comp2
        #print("Division : ", str(CompDiv))
        self.assertAlmostEqual(CompDiv.real, 1.8, places=2)
        self.assertAlmostEqual(CompDiv.imag, 0.07, places=2)

    def testConj(self):
        #Conjugate
        CompConj = self.comp1.conj()
        CompConj2 = self.comp2.conj()
        #print("Conjugate fr comp1 : ", str(CompConj))
        #print("Conjugate fr comp2 : ", str(CompConj2))
        self.assertEqual(str(CompConj), "5 - 11i")
        self.assertEqual(str(CompConj2), "3 - 6i")

    def testMag(self):
        #Modulus
        CompMag = self.comp1.magnitude()
        #print("Magnitude", str(CompMag))
        self.assertAlmostEqual(CompMag, 12.083, places=2)

    def testPhase(self):
        CompPhase = self.comp1.phase()
        #z = cmath.phase(complex(2,3))
        #print("Phase", str(CompPhase))
        self.assertAlmostEqual(CompPhase, cmath.phase(complex(5,11)), places=2)

    def testPolar(self):
        CompPolar = self.comp1.polar()
        #print("My Polar", str(CompPolar))
        #print(cmath.polar(complex(5,11)))
        self.assertAlmostEqual(CompPolar, cmath.polar(complex(5,11)), places=2) 

    def testRect(self):
        CompRect = self.comp1.rect_form()
        #print("My Rect", str(CompRect))
        #print(cmath.rect(12.083045973594572, 1.1441688336680205))

    #TODO : Add more tests accordig to the "main" file.
    #def test___(self):
     #   self.assertEqual()

    #TODO : Error Handling especially divide by 0 error and other Assertion errors
       # try and except

if __name__ == '__main__':
    unittest.main()

