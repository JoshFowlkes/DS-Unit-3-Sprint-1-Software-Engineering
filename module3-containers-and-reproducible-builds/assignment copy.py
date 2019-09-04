class Customer:
	def __init__(self,first,last,mobile,monthly):
		self.first = first
		self.last = last
		self.mobile = mobile
		self.monthly = monthly
	def annual(self):
		self.salary = self.monthly*12
		return'{0} {1}'.format(self.first, self.salary)



class Employee:
	def __init__(self, first, last, pay):
		self.first = first	
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@yahooooooooligans.com'
    # full name will print... the full name lol
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

employee1 = Employee('Escanor', 'Meliodas', 1000000000000)

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    @property
    def real(self):
        return self.r

    @property
    def imaginary(self):
        return self.i

    @property
    def value(self):
        return [self.r, self.i]  # an array makes more sense

    def __add__(self, other):
        return [self.r + other.r, self.i + other.i]


x = Complex(3.0, -4.5)
print('x is: ', x.value)
y = Complex(5, 5)
print('y is: ', y.value)
c = x + y
print('x + y = ', c)	
d = x - y
print('x - y =', d)

