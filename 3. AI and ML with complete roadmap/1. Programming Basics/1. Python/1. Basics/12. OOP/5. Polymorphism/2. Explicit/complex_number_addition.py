class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def shownumber(self):
        print(f"{self.real}i + {self.img}j")

    # Overloading the '+' operator
    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img                # dunder method
        return Complex(newreal, newimg)


# Creating complex numbers
num1 = Complex(1, 3)
num1.shownumber()

num2 = Complex(6, 4)
num2.shownumber()

# Adding two complex numbers
num3 = num1 + num2
num3.shownumber()
