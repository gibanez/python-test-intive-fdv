from rent.Product import Product

class Promotion():
    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)

    def getAmount(self):
        amount = 0
        for prod in self.products:
            amount += prod.getAmount()
        return amount

    def applyPercentDiscount(self, percent):
        ratio = 1 - (percent/100)
        return self.getAmount() * ratio

    def applyPercentExtraCharge(self, percent):
        ratio = 1 + (percent / 100)
        return self.getAmount() * ratio
