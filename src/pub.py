# from customer import Customer

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

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

    def sell_drink(self, customer, drink):
        customer.wallet -= drink.price
        self.till += drink.price
