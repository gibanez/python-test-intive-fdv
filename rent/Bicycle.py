from rent.Product import Product

class Bicycle():
    @staticmethod
    def byHour():
        return Product(5, 1, 'Rent bicycle: 1 hour')
    @staticmethod
    def byDay():
        return Product(20, 24, 'Rent bicycle: 1 day')
    @staticmethod
    def byWeek():
        return Product(60, 24*7, 'Rent bicycle: 1 week')