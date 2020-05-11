
class User:		# declare a class and give it name User
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value received
        print(self.name)
        self.account.deposit(amount)
        return self

    # adding the withdrawal method.
    def make_withdrawal(self, amount):
        # The specific user's account decreases the user's balance by the amount specified
        print(self.name)
        self.account.withdraw(amount)
        return self

    # Add a display_user_balance method to the User class.
    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self

    # transfer_money(self, other_user, amount) -
    # def transfer_money(self, other_user, amount):
    #     # have this method decrease the user's balance by the amount and
    #     # add that amount to other other_user's balance
    #     self.account_balance -= amount
    #     other_user.account_balance += amount
    #     return self


class BankAccount:
    # Default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit: ${}".format(amount))
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("Withdrawal: ${}".format(amount))
        else:
            print("Insufficient funds: Assessing $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance: ${}".format(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


bobby = User("Robert Anderson", "r_anderson@email.com")
bobby.make_deposit(100)
bobby.make_deposit(100)
bobby.display_user_balance()
bobby.make_withdrawal(50)
bobby.display_user_balance()
