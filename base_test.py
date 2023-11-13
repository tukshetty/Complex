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
        self.comp1 = ImagOp(2, 3)
        self.comp2 = ImagOp(1, 4)
    
    def testAdd(self):
        #Addition
        CompSum = self.comp1 + self.comp2
        #print("Addition", str(CompSum))
        self.assertEqual(str(CompSum), "3 + 7i")

    def testSub(self):
        #Substraction
        CompSub = self.comp1 - self.comp2
        #print("Subtraction : ", str(CompSub))
        self.assertEqual(str(CompSub), "1 - 1i")

    def testMul(self):
        #multiplication
        CompMul = self.comp1 * self.comp2
        #print("Multiplication : ", str(CompMul))
        self.assertEqual(str(CompMul), "-10 + 11i")

    def testDiv(self):
        #Division
        CompDiv = self.comp1 / self.comp2
        #print("Division : ", str(CompDiv))
        self.assertAlmostEqual(CompDiv.real, 0.82, places=2)
        self.assertAlmostEqual(CompDiv.imag, -0.29, places=2)

    def testConj(self):
        #Conjugate
        CompConj = self.comp1.conj()
        CompConj2 = self.comp2.conj()
        #print("Conjugate fr comp1 : ", str(CompConj))
        #print("Conjugate fr comp2 : ", str(CompConj2))
        self.assertEqual(str(CompConj), "2 - 3i")

    def testMag(self):
        #Modulus
        CompMag = self.comp1.magnitude()
        #print("Magnitude", str(CompMag))
        self.assertAlmostEqual(CompMag, 3.61, places=2)

    def testPhase(self):
        CompPhase = self.comp1.phase()
        #z = cmath.phase(complex(2,3))
        #print("Phase", str(CompPhase))
        self.assertAlmostEqual(CompPhase, cmath.phase(complex(2,3)), places=2)

if __name__ == '__main__':
    unittest.main()

