print("Importing PRODUCTS module")


class Products:		# declare a class and give it name Products
    def __init__(self, name=None, price=None, category=None):
        self.name = name
        self.price = price
        self.category = category

    def print_info(self):
        # print the name of the product, its category, and its price.
        print("Product: {}, Category: {}, Price: {:04.2f}".format(
            self.name, self.category, self.price))
        return self

    def update_price(self, percent_change, is_increased):
        # updates the product's price. If is_increased is True, the price
        # should increase by the percent_change provided. If False, the price
        # should decrease by the percent_change provided.
        if is_increased:
            self.price += (self.price * percent_change)
            print("Product: {} increased by: {}%".format(
                self.name, percent_change*100))
        else:
            self.price -= (self.price * percent_change)

        return self
