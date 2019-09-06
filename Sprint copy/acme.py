### Part 1 & 2
import random

""" Making The Product Class as outlined in Instructions """
class Product:
    def __init__(self, name, price=10, weight=20, flammability=.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(100000, 999999)
    
    """ Making the Stealability Function """
    def stealability(self):
        steal_ratio = self.price / self.weight
        if (steal_ratio < .05):
            return 'Not so stealable'
        elif (steal_ratio >= .5) and (steal_ratio < 1.0):
            return 'Kinda stealable'
        else:
            return 'Very Stealable!' 
    
    """ Making the Explode Function """
    def explode(self):
        explode_ratio = self.flammability * self.weight
        if (explode_ratio < 10):
            return '...fizzle.'
        elif (explode_ratio >= 10) and (explode_ratio < 50):
            return '...boom!'
        else:
            return 'BABOOOOM BABAY!!!!'

### part 3
""" Making the BoxingGlove Subclass of Product """
class BoxingGlove(Product):
    def __init__(self, name):
        super.__init__(name, weight=10)
    
    def explode(self):
        return "...it's a glove."
    
    """ Making the Punch Function  """
    def punch(self):
        if (self.weight < 5):
            return 'That tickles.'
        elif (self.weight >= 5) and (self.weight < 15):
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
