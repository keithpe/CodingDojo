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
        pass


myUser = User("Keith Peterson", "kpeterson@mil.com")

print('myUser.name', myUser.name)
print('myUser.email', myUser.email)
print('myUser.balance', myUser.account_balance)
myUser.make_deposit(500)
myUser.display_user_balance()
myUser.make_withdrawal(250)
myUser.display_user_balance()
