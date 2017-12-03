import cmath

class Complex():
    real=0
    imag=0

    def __init__(self, x, y):
        self.real = x
        self.imag = y

    def module(self):
        return ((self.real ** 2 + self.imag ** 2) ** (1 / 2))

    def add(a, b):
        new_real=a.real+b.real
        new_imag=a.imag+b.imag
        return Complex(new_real,new_imag)

    def sub(a, b):
        new_real = a.real - b.real
        new_imag = a.imag - b.imag
        return Complex(new_real, new_imag)

    def mul(a, b):
        new_real = a.real * b.real - a.imag * b.imag
        new_imag = a.imag * b.real + a.real + b.imag
        return Complex(new_real, new_imag)

    def div(a, b):
        try:
            new_real = (a.real * b.real + a.imag * b.imag)/(b.real**2+b.imag**2)
            new_imag = (a.imag * b.real - a.real + b.imag)/(b.real**2+b.imag**2)
            return Complex(new_real, new_imag)
        except ZeroDivisionError:
            print("zero division")

    def print_compex(self):
        if(self.real == 0):
            return "%di" %self.imag
        elif(self.imag == 0):
            return "%d" %self.real
        else:
            return "%d+%di" %(self.real, self.imag)


a = Complex(1,2)
b = Complex(2,2)

print("Complex1: ", a.print_compex())
print("Complex2: ", b.print_compex())

add = Complex.add(a,b)
sub = Complex.sub(a,b)
mul = Complex.mul(a,b)
div = Complex.div(a,b)

print("Modules: ", a.module(), b.module())
print("Add: ", add.print_compex())
print("Sub: ", sub.print_compex())
print("Mul: ", mul.print_compex())
print("Div: ", mul.print_compex())

