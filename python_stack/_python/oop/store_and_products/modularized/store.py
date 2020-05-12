import products

# This message will print when importing THIS module from any other module
print("Importing STORE module")

# Assign Products the products.Products, so we don't have to rewrite
# this class code
Products = products.Products


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
