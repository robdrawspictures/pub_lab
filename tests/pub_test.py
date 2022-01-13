import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Lion", 200.00)
        self.drink1 = Drink("Stella", 5.00, 5)
        self.drink2 = Drink("Smirnoff", 3.50, 10)
        self.person = Customer("Rob", 50.00, 33)
        self.person2 = Customer("Wee Jim", 1.00, 8)
        self.food1 = Food("burger", 7.50, 5)
        self.food2 = Food("pizza", 10.00, 10)

    def test_pub_has_name(self):
        self.assertEqual("The Lion", self.pub.name)

    def test_check_till_amount(self):
        self.assertEqual(200.00, self.pub.till)

    def test_till_empty(self):
        self.pub.increase_till(50)
        self.assertEqual(250.00, self.pub.till)

    def test_add_drink(self):
        self.pub.add_drink(self.drink1)
        self.pub.add_drink(self.drink2)
        self.assertEqual(2, self.pub.drinks_count())

    def test_check_drink_name(self):
        self.pub.add_drink(self.drink1)
        self.assertEqual("Stella", self.pub.drinks[0].name)

    def test_check_customer_age(self):
        test1 = self.pub.check_customer_age(self.person)
        self.assertTrue(test1)
        test2 = self.pub.check_customer_age(self.person2)
        self.assertFalse(test2)

    def test_sell_drink(self): 
        self.pub.sell_drink(self.person, self.drink1)
        self.assertEqual(205.00, self.pub.till)
        self.assertEqual(45.00, self.person.wallet)

    def test_sale_denied(self): 
        self.pub.sell_drink(self.person2, self.drink1)
        self.assertEqual(200.00, self.pub.till)
        self.assertEqual("Sale denied. Oot ma pub.", self.pub.sell_drink(self.person2, self.drink1))

    def test_customer_inebriation(self):
        self.pub.sell_drink(self.person, self.drink1)
        self.assertEqual(5, self.person.inebriation)
        self.pub.sell_drink(self.person, self.drink2)
        self.assertEqual(15, self.person.inebriation)

    def test_customer_too_drunk(self):
        self.pub.sell_drink(self.person, self.drink2)
        self.pub.sell_drink(self.person, self.drink2)
        self.assertEqual("Sale denied. Oot ma pub.", self.pub.sell_drink(self.person, self.drink2))

    def test_customer_broke(self):
        self.pub.sell_food(self.person, self.food2)
        self.pub.sell_food(self.person, self.food2)
        self.pub.sell_food(self.person, self.food2)
        self.pub.sell_food(self.person, self.food2)
        self.pub.sell_food(self.person, self.food2)
        self.assertEqual("We're not a soup kitchen. Oot ma pub.", self.pub.sell_food(self.person, self.food2))

    def test_sell_food(self):
        self.pub.sell_food(self.person, self.food2)
        self.assertEqual(40.00, self.person.wallet)
        self.assertEqual(-10, self.person.inebriation)
        self.assertEqual(210.00, self.pub.till)

    def test_drink_stock(self):
        self.pub.add_drink(self.drink1)
        self.pub.add_drink(self.drink2)
        self.pub.create_drink_stock()
        self.assertEqual(2, len(self.pub.drink_stock))
        self.assertEqual({"name" : "Stella", "price" : 5.00, "units" : 5}, self.pub.drink_stock[0])


    def test_change_stock_value(self):
        self.pub.add_drink(self.drink2)
        self.pub.add_drink(self.drink1)
        self.pub.create_drink_stock()
        self.assertEqual(2, len(self.pub.drink_stock))
        self.pub.change_stock_value("Stella", 6.00)
        self.assertEqual(6.00, self.pub.drink_stock[1]["price"])