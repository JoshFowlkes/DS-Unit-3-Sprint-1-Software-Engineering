### Part 1 & 2
import random

class Product:
    def __init__(self, name, price=10, weight=20, flammability=.5, identifier=random.randint(100000,999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        self.steal_ratio = self.price / self.weight
        if (self.steal_ratio < .05):
            print('Not so stealable')
        elif (self.steal_ratio > .5) & (self.steal_ratio < 1.0):
            print('Kinda stealable')
        else:
            print('Very Stealable!') 

    def explode(self):
        self.explode_ratio = self.flammability * 10
        if (self.explode_ratio < 10):
            print('...fizzle.')
        elif (self.explode_ratio >= 10) & (self.explode_ratio < 50):
            print('...boom!')
        else:
            print('BABOOOOM BABAY!!!!')

### part 3
class BoxingGlove(Product):
    def __init__(self, name, price, weight = 10, flammability, identifier):
        super().__init__(self, name, price, weight, flammability, identifier)
        super(BoxingGlove, self).explode(print("... it's a glove."))

    def punch(self):
        if (self.weight < 5):
            print('That tickles.')
        elif (self.weight >= 5) & (self.steal_ratio < 15):
            print('Hey that hurt!')
        else:
            print('OUCH!')
