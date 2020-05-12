# TODO: Finish these four items and then move on to the rest of the OOP section.
#       Continue to do it as a list (array), not a dictionary.
# NINJA BONUS: Add the inflation method to the Store class
# NINJA BONUS: Add the set_clearance method to the Store class
# NINJA BONUS: Modularize your code into 3 separate files
# SENSEI BONUS: Update the product class to give each product a unique id.
#               Update the sell_product method to accept the unique id.


class Store:		# declare a class and give it name Store
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    def show_products(self):
        print("\n**** Store: {} sells these products: ".format(self.name))
        if len(self.products) == 0:
            print("     -- No products in inventory --")
        else:
            for product in range(0, len(self.products), 1):
                print("item: {} - ".format(product), end='')
                self.products[product].print_info()

        print("**** End of Inventory for Store: {} ****\n".format(self.name))
        return self

    def add_product(self, name, price, category):
        # Takes a product and adds it to the store
        print("Adding: {}, price: ${}, category: {}".format(
            name, price, category))
        self.products.append(Products(name, price, category))
        return self

    def sell_product(self, product):
        # Removes a product from the store's list of products
        # Product is the array index
        # First print the product info for this item.
        print("Selling item: {} - ".format(product), end='')
        self.products[product].print_info()
        # Then remove it from this store's list of products.
        del self.products[product]
        return self

    def inflation(self, percent_increase):
        # Increases the price of each product by the percent_increase
        # given (use the method you wrote in the Product class!)
        print("\n**** Storewide Inflation Calculation ****")
        for product in range(0, len(self.products), 1):
            print("Inflation updating item {} - ".format(product))
            print("Old price: ", end='')
            self.products[product].print_info()
            self.products[product].update_price(percent_increase, True)
            print("New price: ", end='')
            self.products[product].print_info()
        print("**** End Inflation Calculation ****")
        return self

    def set_clearance(self, category, percent_discount):
        # Updates all the products matching the given category by reducing
        # the price by the percent_discount given (use the method you wrote
        # in the Product class!)
        print("\n**** Storewide Clearance Calculation ****")
        for product in range(0, len(self.products), 1):
            if self.products[product].category == category:
                print(
                    "Setting clearance price for item: {} - ".format(product), end='')
                self.products[product].print_info()
                self.products[product].update_price(0.10, False)
        print("*** End of Storewide Clearance Calculation ***")
        return self


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


store_165 = Store("Castle Rock")
store_165.show_products()
store_165.add_product("Shovel", 35.50, "Garden Supplies")
store_165.add_product("Rake", 15.50, "Garden Supplies")
store_165.add_product("Lawn Sprinkler", 25.50, "Garden Supplies")
store_165.show_products()
store_165.sell_product(1)
store_165.show_products()
store_165.inflation(.10)
store_165.show_products()
store_165.set_clearance("Garden Supplies", 0.10)
store_165.show_products()
