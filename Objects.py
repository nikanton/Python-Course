class ComplexNumber(object):
    def __init__(self, real=0, imaginary=0):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                             self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real -
                             self.imaginary * other.imaginary,
                             self.real * other.imaginary +
                             self.imaginary * other.real)

    def __div__(self, other):
        ab = other.real ** 2 + other.imaginary ** 2
        return self * ComplexNumber(other.real / ab,
                                    -other.imaginary / ab)

    def __str__(self):
        if(self.real != 0 and self.imaginary > 0):
            return '{0:.2f} + {1:.2f}i'.format(self.real, self.imaginary)
        elif(self.real != 0 and self.imaginary == 0):
            return '{0:.2f}'.format(self.real)
        elif(self.real != 0 and self.imaginary < 0):
            return '{0:.2f} - {1:.2f}i'.format(self.real, -self.imaginary)
        elif(self.real == 0 and self.imaginary > 0):
            return '{0:.2f}i'.format(self.imaginary)
        elif(self.real == 0 and self.imaginary == 0):
            return '0.00'
        elif(self.real == 0 and self.imaginary < 0):
            return '{0:.2f}i'.format(self.imaginary)

class Stack(object):
    def __init__(self, a):
        self.stack = []
        self.stack.extend(a)
    def push(self, a):
        self.stack.append(a)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[len(self.stack) - 1]
    def __len__(self):
        return len(self.stack)
    def __str__(self):
        s = ''
        for x in self.stack:
            s += str(x) + ' '
        return s