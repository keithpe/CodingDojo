
class User:		# declare a class and give it name User
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        self.accounts = []
        print("***** Created account for '{}'c *****".format(self.name))

    def open_account(self):
        self.accounts.append(BankAccount())
        print("***** Opened new account for '{}' *****.".format(self.name))
        return self

    # takes an argument that is the amount of the deposit
    def make_deposit(self, amount, account):
        # the specific user's account increases by the amount of the value received
        print(
            "***** Deposit for '{}', into account: '{}', ".format(self.name, account), end='')
        self.accounts[account].deposit(amount)
        return self

    # adding the withdrawal method.
    def make_withdrawal(self, amount, account):
        # The specific user's account decreases the user's balance by the amount specified
        print("***** Withdrawal for '{}', from account: '{}', ".format(self.name, account), end='')
        self.accounts[account].withdraw(amount)
        return self

    # Add a display_user_balance method to the User class.
    def display_user_balance(self):
        print("***** Balance info for '{}' *****".format(self.name))
        if len(self.accounts) > 0:
            for account in range(0, len(self.accounts), 1):
                print("Account:{}: ".format(account), end='')
                self.accounts[account].display_account_info()
        else:
            print('No Accounts Found')
        print("***** End of Balance info for '{}' *****".format(self.name))
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
bobby.open_account()
bobby.open_account()
bobby.make_deposit(100, 0)
bobby.make_deposit(200, 1)
bobby.display_user_balance()
bobby.make_withdrawal(50, 1)
bobby.display_user_balance()


'''
***** S A M P L E     O U T P U T *****

***** Created account for 'Robert Anderson'c *****
***** Opened new account for 'Robert Anderson' *****.
***** Opened new account for 'Robert Anderson' *****.
***** Deposit for 'Robert Anderson', into account: '0', Deposit: $100
***** Deposit for 'Robert Anderson', into account: '1', Deposit: $200
***** Balance info for 'Robert Anderson' *****
Account:0: Balance: $100
Account:1: Balance: $200
***** End of Balance info for 'Robert Anderson' *****
***** Withdrawal for 'Robert Anderson', from account: '1', Withdrawal: $50
***** Balance info for 'Robert Anderson' *****
Account:0: Balance: $100
Account:1: Balance: $150
***** End of Balance info for 'Robert Anderson' *****
'''
