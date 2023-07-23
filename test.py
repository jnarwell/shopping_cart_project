import unittest
import index
import random

class ShoppingItemsTest(unittest.TestCase):
    def test_get_item(self):
        new_item = 'apple'
        assert index.get_item(new_item)[0] == 'apple'
        self.assertAlmostEqual( index.get_item(new_item)[1], (round(random.uniform(2,10),2)), delta=8)
    
    # def test_get_cart(self):
    #     index.cart.append('apple')
    #     index.cart.append('apple')
    #     index.cart.append('apple')
    #     index.cart.append('oranges')
    #     print(index.get_cart())
    #     assert index.get_cart() == [{'name': 'apple', 'price': 5.16, 'quantity': 3}, {'name': 'oranges', 'price': 5.97, 'quantity': 1}]
    #     index.cart = []

if __name__ == '__main__':
    unittest.main()