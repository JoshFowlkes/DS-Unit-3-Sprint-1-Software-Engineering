### Part 5
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def setUp(self):
        """Set's up the tests methods"""
        self.product = Product('Test Product')

    def test_default_product_price(self):
        """Test default product price being 10."""
        self.assertEqual(self.product.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        self.assertEqual(self.product.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being 1/2."""
        self.assertEqual(self.product.flammability, 0.5)

    def test_default_stealability(self):
        """Test default stealability() being 'Kinda stealable.'"""
        self.assertEqual(self.product.stealability(), 'Kinda stealable.')

    def test_default_explode(self):
        """Test default explode() being '...boom!'"""
        self.assertEqual(self.product.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """Make sure you can impress Sr. Data Scientists"""

    def setUp(self):
        """Set's up the tests methods"""
        self.products = generate_products()

    def test_default_num_products(self):
        """Test default number of products from generate_products() is 30"""
        self.assertEqual(len(self.products), 30)

    def test_legal_names(self):
        """Test product names are legal or not"""
        for product in self.products:
            name = product.name.split()
            self.assertIn(name[0], ADJECTIVES)
            self.assertIn(name[1], NOUNS)


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
