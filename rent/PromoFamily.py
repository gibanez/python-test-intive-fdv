from rent import PromotionError
from rent.Promotion import Promotion




class PromoFamily(Promotion):

    def validate(self):
        total = len(self.products)
        if 2 < total and 6 > total:
            return True
        return False

    def getTotalAmount(self):
        if self.validate():
            return self.applyPercentDiscount(30)
        raise PromotionError