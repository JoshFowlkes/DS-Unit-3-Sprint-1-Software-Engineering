### Part 5
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        product1 = ('Escanor', 50, 7, 1.3, 123456)
        self.assertEqual(product1.name, 'Escanor')

    def test_explode(self):
        product2 = ('Meliodas', 50, 100, 2.5, 987654)
        self.assertEqual = (product2.explode(), '...boom!')

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        self.assertIn(f'{random.sample(adjectives)} {random.sample(nouns)}', 
                        'Portable Mousetrap')

if __name__ == '__main__':
    unittest.main()




### Part 7

'''
Question 1:
An import part of code reviews is mostly having that additional set of eyes to examine
and debug one's code. I've experienced instances on more than one occasion in which 
I had a simple typo in my code such as not having something like ".py" at the end of 
a file name and it caused hours of searching and headache. Only to have it easily solved 
by another set of eyes that was able to spot the typot immediately. So in short, spotting
 easy to miss mistakes is one huge benefit from code reviews.

Question 2:
Containers help in that they package up all the code and software and dependencies in
one computer enviornment. Because of this, something like Docker would help us because it 
is in a sense 'portable' in nature, and very simply put, saves us a lot of headaches 
especially as we dive deeper into these larger scale projects that have numerous packages
running with all sorts of dfferent dependencies. 
'''
