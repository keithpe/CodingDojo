# SENSEI BONUS: Update the product class to give each product a unique id.
#               Update the sell_product method to accept the unique id.

import store

store_165 = store.Store("Castle Rock")
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
