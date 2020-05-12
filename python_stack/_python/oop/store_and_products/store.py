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
        print("Store: {} sells these products: ".format(
            self.name), end='')
        for i in range(0, len(self.products), 1):
            print(self.products[i]+', ', end='') if i < len(
                self.products)-1 else print(self.products[i]+'. ')

        return self

    def add_product(self, new_product):
        # Takes a product and adds it to the store
        self.products.append(new_product)
        return self

    def sell_product(self, product):
        # Removes a product from the store's list of products
        self.products.remove(product)
        return self


class Products:		# declare a class and give it name Products
    def __init__(self, name=None, price=None, category=None):
        self.name = name
        self.price = price
        self.category = category

    def print_info(self):
        # print the name of the product, its category, and its price.
        print("Product: {}, Category: {}, Price: {}".format(
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


rake = Products("Ultimate Rake", 35.50, "Garden")
shovel = Products("Ultimate Shovel", 55.50, "Garden")
hammer = Products("Golden Shovel", 155.50, "Garden")
rake.print_info()
shovel.print_info()
hammer.print_info()

hammer.update_price(0.10, True)
hammer.print_info()

store_165 = Store("Castle Rock", ["Ultimate Rake"])
store_165.show_products()
store_165.add_product("Ultimate Shovel")
store_165.add_product("Golden Shovel")
store_165.show_products()
store_165.sell_product("Golden Shovel")
store_165.show_products()
