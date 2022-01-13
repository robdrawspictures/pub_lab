from src.pub import Pub
from src.drink import Drink

drink1 = Drink("Stella", 5.00, 5)
pub1 = Pub("The Lion", 200.00)

print(pub1.name)
pub1.add_drink(drink1)
print(len(pub1.drinks))
pub1.create_drink_stock()
print(pub1.drink_stock)
# new_drink = {"name" : "Guinness", "price" : 6, "units" : 5}
# pub1.drink_stock.append(new_drink)
# print(pub1.drink_stock)
pub1.change_stock_value("Stella", 10.00)
print(pub1.drink_stock)