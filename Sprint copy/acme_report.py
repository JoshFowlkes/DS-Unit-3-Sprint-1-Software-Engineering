### Part 4

from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30):
    products = []

    for _ in list(range(n)):
        products = Product(name=(f'{random.sample(ADJECTIVES)} {random.sample(NOUNS)}')),
                        price = random.randint(5,100),
                        weight = random.randint(5,100),
                        flammability = random.uniform(0.0, 2.5),
                        identifier = random.randint(100000,999999))

    return products


def inventory_report(products):
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')

    unique_product_names = len(products.name)
    print('Unique product names:', unique_product_names)

    average_price = mean(products.price)
    print('Average price:', average_price)

    average_weight = mean(products.weight)
    print('Average weight:', average_weight)

    average_flammability = mean(products.flammability)
    print('Average flammability:', average_flammability)


if __name__ == '__main__':
    inventory_report(generate_products())
