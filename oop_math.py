
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        """To add complex, numbers
        real answer == A.real + B.real
        imaginary answer == A.imaginary + B.imaginary"""
        raise NotImplementedError
        
    def __sub__(self, no):
        """To subtract complex, numbers
        real answer == A.real - B.real
        imaginary answer == A.imaginary - B.imaginary"""
        raise NotImplementedError
        
    def __mul__(self, no):
        """To multiply complex, numbers
        real answer == A.real * B.real - A.imaginary * B.imaginary
        imaginary answer == A.real * B.imaginary + A.imaginary * B.real"""
        raise NotImplementedError

    def __truediv__(self, no):
        """To divide complex, numbers
        Get the conjugate of A == A.real, -A.imaginary
        Multiply A/B by the conjugate conjuage
        new_A == A * conjugate
        new_B == B * conjugate
        real answer == new_A.real / new_B.real
        imaginary answer == new_A.imaginary / new_B.imaginary"""

        raise NotImplementedError
    
    def __eq__(self, other): 
        if not isinstance(other, Complex):
            # don't attempt to compare against unrelated types
            raise ValueError("Both classes need to be Complex")

        return self.real == other.real and self.imaginary == other.imaginary


def test_add():
    a = Complex(2, 3) 
    b = Complex(3, 4)
    
    assert a + b == Complex(5, 7)

    assert a - b == Complex(-1, -1)

    assert a * b == Complex(-6, 17)

    assert a / b == Complex(0.72, 0.04)