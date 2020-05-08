# Create the User class. Add the attributes mentioned in the introduction.
# Include, name, email, account_balance and make_deposit() function.
#
# Add the make_withdrawl method
# Have this method decrease the user's balance by the amount specified
# make_withdrawal(self, amount)


class User:		# declare a class and give it name User
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        self.account_balance = 0

    # adding the deposit method
    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value received
        self.account_balance += amount

    # adding the withdrawal method.
    def make_withdrawal(self, amount):
        # The specific user's account decreases the user's balance by the amount specified
        self.account_balance -= amount

    # Add a display_user_balance method to the User class.
    def display_user_balance(self):
        print("The balance for {} is {}.".format(
            self.name, self.account_balance))

    # transfer_money(self, other_user, amount) -
    def transfer_money(self, other_user, amount):
        # have this method decrease the user's balance by the amount and
        # add that amount to other other_user's balance
        self.account_balance -= amount
        other_user.account_balance += amount


# Create 3 instances of the User class
bobby = User("Robert Anderson", "r_anderson@email.com")
teddy = User("Theodora Williamson", "teddy@email.com")
val = User("Valeria Tortellini", "tory@email.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
bobby.make_deposit(100)
bobby.make_deposit(50)
bobby.make_deposit(250)
bobby.make_withdrawal(100)
bobby.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
teddy.make_deposit(500)
teddy.make_deposit(350)
teddy.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
val.make_deposit(5000)
val.make_withdrawal(100)
val.make_withdrawal(300)
val.make_withdrawal(250)
val.display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user
# and then print both users' balances
bobby.transfer_money(val, 100)
bobby.display_user_balance()
val.display_user_balance()
