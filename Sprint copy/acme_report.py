### Part 4
from random import randint, sample, uniform
from acme import Product

""" Making lists of adjectives and nouns to be used as names """
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

""" Generate Products functions """
def generate_products(n=30):
    products = []

    """ Making a for loop to make each individual product """
    for _ in list(range(n)):
        products = Product(name=(f'{random.sample(ADJECTIVES)} {random.sample(NOUNS)}')),
                        price = random.randint(5,100),
                        weight = random.randint(5,100),
                        flammability = random.uniform(0.0, 2.5),
                        identifier = random.randint(100000,999999))
    return products

""" Making inventory report function """
def inventory_report(products):
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    
    """ Unique product names is len of names """
    unique_product_names = len(products.name)
    print('Unique product names:', unique_product_names)

    """ Using mean() to find average of each then printing each one out """
    average_price = mean(products.price)
    print('Average price:', average_price)

    average_weight = mean(products.weight)
    print('Average weight:', average_weight)

    average_flammability = mean(products.flammability)
    print('Average flammability:', average_flammability)

if __name__ == '__main__':
    inventory_report(generate_products())
