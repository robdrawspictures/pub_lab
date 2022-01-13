class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.drink_stock = []

    def add_drink(self, drink):
        self.drinks.append(drink)

    # def get_drink_name(self, name):
    #     found = []
    #     for drink in self.drinks:
    #         if drink.name == name:
    #             return drink.name

    # def get_drink_price(self, name):
    #     found = []
    #     for drink in self.drinks:
    #         if drink.name == name:
    #             return drink.price

    def drinks_count(self):
        return len(self.drinks)

    def increase_till(self, amount):
        self.till += amount

    def check_customer_age(self, customer):
        if customer.age >= 21:
            return True
        else:
            return False

    # ^ This function isn't needed because I rolled it into
    # the one below, but I kept it for testing purposes.

    def sell_drink(self, customer, drink):
        if customer.age < 21 or customer.inebriation >= 20 or customer.wallet < drink.price:
             return "Sale denied. Oot ma pub."
        else:
            customer.wallet -= drink.price
            customer.inebriation += drink.units
            self.till += drink.price

    def sell_food(self, customer, food):
        if customer.wallet < food.price:
            return "We're not a soup kitchen. Oot ma pub."
        else:
            customer.wallet -= food.price
            customer.inebriation -= food.rejuvenation_level
            self.till += food.price

    def create_drink_stock(self):
        drinktionary = []
        for drink in self.drinks:
            drinktionary.append({"name" : drink.name, "price" : drink.price, "units" : drink.units})
        self.drink_stock = drinktionary

    def change_stock_value(self, name, new_price):
        for drink in self.drink_stock:
            if drink["name"] == name:
                drink["price"] = new_price
