from rent.Product import Product
from rent.ProductInterface import ProductInterface


class ProductError(ProductInterface):
    def __init__(self, amount, hours, detail):
        self.detail = detail
        self.hours = hours
        self.amount = amount

prod = Product(1, 2, 'producto prueba')
print(prod.getAmount())

prodError = ProductError(1, 2, 'producto prueba')
try:
    prodError.getAmount()
except Exception:
    pass
