class Complex :
    def __init__(self, a, b) :
        self.a = a
        self.b = b 
    def display(self) :
        if self.b < 0 :
            print(self.a,self.b,"i")
        else :
            print(self.a,"+",self.b,"i")

    def __add__(self, target) :
        return Complex(self.a + target.a, self.b + target.b)
    def __sub__(self, target) :
        return Complex(self.a - target.a, self.b - target.b)
    def modulus(self) :
        return ((self.a)**2 +(self.b)**2)**0.5
    def multiply(self, target) :
        return Complex((self.a)*(target.a) - (self.b)*(target.b), (self.a)*(target.b) + (self.b)*(target.a))
    
    def conjugate(self) :
        return Complex(self.a, -1 * self.b)
    def inverse(self) :
        return Complex((self.a)/(self.modulus())**2, (-1)*(self.b)/(self.modulus())**2)
x = Complex(1, 2)
y = Complex(2,-3)
x.display()
(x+y).display()
(x-y).display()
x.multiply(y).display()
print(x.modulus())
x.conjugate().display()
x.inverse().display()
