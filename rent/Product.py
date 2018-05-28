from rent.ProductInterface import ProductInterface


class Product(ProductInterface):

    def __init__(self, amount, hours, detail):
        self.detail = detail
        self.hours = hours
        self.amount = amount

    def getAmount(self):
        return self.amount

