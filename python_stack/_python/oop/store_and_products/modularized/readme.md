# Modularized Store and Products assignment

# Objectives

- Practice creating classes
- Practice associations between classes
- Practice modularizing code

# Goals

These files included 'Modularizing' the project. I've created a main.py that has all the calls to
the store class.

I've moved the Products class to the products.py file.

I've moved the Store class to the store.py file, and imported the products module into the store module.

I've added lines to main.py to import the classes from store.py and products.py.

Here are the rest of the assignment requirements:

# Assignment: Store & Products

# Objectives:

- Practice creating classes
- Practice associations between classes
- Practice modularizing code

Start by creating a Store class that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.

Next, create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.

### Let's give some methods to our Product class:

- update_price(self, percent_change, is_increased) - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.

- print_info(self) - print the name of the product, its category, and its price.

### Let's also give some methods to our Store class:

- add_product(self, new_product) - takes a product and adds it to the store

- sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.

- inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)

- set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)

* [x] Prevent PacMan from leaving the maze or going through the walls.

* [x] Create a Store class with 2 attributes
* [x] Create a Product class with 3 attributes
* [x] Add the print_info method to the Product class
* [x] Add the update_price method to the Product class
* [x] Add the add_product method to the Store class
* [x] Add the sell_product method to the Store class
* [x] Test out your classes by creating an instance of the Store and a few instances of the Product class, add those instances to the store instance, and then test out the methods.
* [x] NINJA BONUS: Add the inflation method to the Store class
* [x] NINJA BONUS: Add the set_clearance method to the Store class
* [x] NINJA BONUS: Modularize your code into 3 separate files
* [ ] SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.
