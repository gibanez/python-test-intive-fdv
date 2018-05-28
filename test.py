import unittest

from rent.Bicycle import Bicycle
from rent.Product import Product


def fun(x):
    return x + 1

def logger(data):
    print(data)

class RentTest(unittest.TestCase):

    def test_createProduct(self):
        prod = Product(1, 2, 'producto prueba')
        logger(prod)
        self.assertEqual(prod.getAmount(), 1)
        self.assertEqual(prod.detail, 'producto prueba')
        print(prod.getAmount())
        print(prod.detail)

    def test_product_coverage(self):
        prod = Product(1, 2, 'producto prueba')
        logger(prod)
        print(prod.getAmount())

    def test_bicycleByHour(self):
        print(Bicycle.byHour())
        bicycle = Bicycle.byHour()
        self.assertEqual(bicycle.getAmount(), 5)
        self.assertEqual(bicycle.detail, 'Rent bicycle: 1 hour')

    
    def test_bicycleByDay(self):
        bicycle = Bicycle.byDay()
        self.assertEqual(bicycle.getAmount(), 20)
        self.assertEqual(bicycle.detail, 'Rent bicycle: 1 hour')

    def test_bicycleByDay(self):
        bicycle = Bicycle.byWeek()
        self.assertEqual(bicycle.getAmount(), 60)
        self.assertEqual(bicycle.detail, 'Rent bicycle: 1 week')

    def test_createProduct(self):
        prod = Product(1, 2, 'producto prueba')
        self.assertEqual(prod.getAmount(), 1)
        self.assertEqual(prod.amount, 1)
        self.assertEqual(prod.detail, 'producto prueba')
        self.assertEqual(prod.hours, 2)
