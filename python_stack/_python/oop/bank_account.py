#
# Bank Account Class
#
# Objectives
# Practice writing classes
#
# As we continue thinking about our banking application, we realize that it would be more
# accurate to assign a balance not to the user directly, but that in the real world, users
# have accounts, and accounts have balances. This gives us the idea that maybe an account is
# its own class! But as we stated, it is not completely independent of a class;
# accounts only exist because users open them.
#
# For this assignment, don't worry about putting any user information in the BankAccount class.
# We'll take care of that in the next lesson!
#
# Let's first just get some more practice writing classes by writing a new BankAccount class.
# In the next lesson, we'll tie our User and BankAccount classes together.
#
# The BankAccount class should have a balance. When a new BankAccount instance is created,
# if an amount is given, the balance of the account should initially be set to that amount;
# otherwise, the balance should start at $0. The account should also have an interest rate,
# saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation.
# (Hint: when using default values in parameters, the order of parameters matters!)
#
# The class should also have the following methods:
#
# deposit(self, amount) - increases the account balance by the given amount
#
# withdraw(self, amount) - decreases the account balance by the given amount if there are
# sufficient funds; if there is not enough money, print a message "Insufficient funds:
# Charging a $5 fee" and deduct $5
#
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
#
# This means we need a class that looks something like this:
###################################################################################################


class BankAccount:
    # Default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Assessing $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance: {}".format(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

####################################################################################################
#
# Create a BankAccount class with the attributes interest rate and balance
# Add a deposit method to the BankAccount class
# Add a withdraw method to the BankAccount class
# Add a display_account_info method to the BankAccount class
# Add a yield_interest method to the BankAccount class
# Create 2 accounts
# To the first account, make 3 deposits and 1 withdrawal,
# then calculate interest and display the account's info all in one line of code (i.e. chaining)
#
# To the second account, make 2 deposits and 4 withdrawals,
# then calculate interest and display the account's info all in one line of code (i.e. chaining)
#
####################################################################################################


# Create 2 accounts
# To the first account, make 3 deposits and 1 withdrawal,
# then calculate interest and display the account's info all in one line of code (i.e. chaining)

account1 = BankAccount(0.01, 100).deposit(
    100).deposit(300).deposit(100).withdraw(250).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals,
# then calculate interest and display the account's info all in one line of code (i.e. chaining)
account2 = BankAccount(0.05, 1000).deposit(2000).deposit(1000).withdraw(
    150).withdraw(50).withdraw(250).withdraw(50).display_account_info()
