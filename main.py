from rent.Bicycle import Bicycle
from rent.PromoFamily import PromoFamily



bicycles = []

bicycleByHour = Bicycle.byHour()
bicycleByDay = Bicycle.byDay()
bicycleByWeek = Bicycle.byWeek()

bicycles.append(bicycleByHour)
bicycles.append(bicycleByDay)
bicycles.append(bicycleByWeek)

for b in bicycles:
    print(b.detail)

promo = PromoFamily()
promo.addProduct(bicycleByDay)
promo.addProduct(bicycleByDay)
promo.addProduct(bicycleByDay)

print(promo.getTotalAmount())

print(promo.applyPercentDiscount(30))

print(promo.applyPercentExtraCharge(10))