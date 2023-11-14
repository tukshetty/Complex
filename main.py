"""
The module defines functionalities for basic complex number operations.
"""

import math

class ImagOp:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, num):
        return ImagOp(self.real + num.real, self.imag + num.imag)

    def __sub__(self, num):
        return ImagOp(self.real - num.real, self.imag - num.imag)

    def __mul__(self, num):
        # (a+bi)*(c+di) = (ac - bd) + (ad + bc)i
        mulReal = (self.real * num.real) - (self.imag * num.imag)
        mulImag = (self.real * num.imag) + (self.imag * num.real)
        return ImagOp(mulReal, mulImag)

    def __truediv__(self, num):
        # (a+bi) / (c+di) = (ac + bd) / (c^2 + d^2) + (bc - ad)i / (c^2 + d^2)
        deno = num.real**2 + num.imag**2
        divReal = (((self.real * num.real) + (self.imag * num.imag))/ deno)
        divImag = (((self.imag * num.real) - (self.real * num.imag)) / deno)
        return ImagOp(divReal, divImag)

    def magnitude(self):
        absolute = math.sqrt((self.real**2) + (self.imag**2))
        return absolute

    def conj(self):
        return ImagOp(self.real, -self.imag)  

    def phase(self):
        #c = a + bj is denoted c: c = arctanb/a.
        return math.atan2(self.imag, self.real)

    def polar(self):
        phi = math.atan2(self.imag, self.real)
        r = math.sqrt((self.real**2) + (self.imag**2))
        return (r, phi)

    def rect_form(self):
        phi = math.atan2(self.imag, self.real)
        r = math.sqrt((self.real**2) + (self.imag**2))
        return ImagOp((r*math.cos(phi)), (r*math.sin(phi)))

     # TODO: Implement further functionalities such as exponential, pi, logarithmic and trignometric functionalities.
    def exp(self):
        return ImagOp()

    


    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
