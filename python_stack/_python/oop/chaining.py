# Chaining

# Objectives: Understand how to chain methods

# Instead of making calls to the User class to execute it's different methods
# Chaining allows us to type the instance of the User class once and chain it's related
# methods together.
#
# So instead of doing this:
# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_deposit(300)
# guido.make_withdrawal(50)
# guido.display_user_balance()
#
# We can do this:
#
# guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

# This is called chaining. In order for this to work, each method must return self.
# By returning self, if we recall how functions work, each method call will now be equal
# to the instance that called it.
#

# Here's my code from user.py. I've modified the methods to return self and modified the
# calls to use chaining.


class User:		# declare a class and give it name User
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        self.account_balance = 0

    # adding the deposit method
    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value received
        self.account_balance += amount
        return self

    # adding the withdrawal method.
    def make_withdrawal(self, amount):
        # The specific user's account decreases the user's balance by the amount specified
        self.account_balance -= amount
        return self

    # Add a display_user_balance method to the User class.
    def display_user_balance(self):
        print("The balance for {} is {}.".format(
            self.name, self.account_balance))
        return self

    # transfer_money(self, other_user, amount) -
    def transfer_money(self, other_user, amount):
        # have this method decrease the user's balance by the amount and
        # add that amount to other other_user's balance
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


# Create 3 instances of the User class
bobby = User("Robert Anderson", "r_anderson@email.com")
teddy = User("Theodora Williamson", "teddy@email.com")
val = User("Valeria Tortellini", "tory@email.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
bobby.make_deposit(100).make_deposit(50).make_deposit(
    250).make_withdrawal(100).display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
teddy.make_deposit(500).make_deposit(350).display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
val.make_deposit(5000).make_withdrawal(100).make_withdrawal(
    300).make_withdrawal(250).display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user
# and then print both users' balances
bobby.transfer_money(val, 100).display_user_balance()
val.display_user_balance()
