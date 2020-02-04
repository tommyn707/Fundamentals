
class User:
    def __init__(self, first_name, last_name, balance=150):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.transactions = []
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(+amount)
        return amount
    def withdrawal(self, amount, limit=500):
        if self.balance - amount > 0 and amount <= limit:
            self.balance -= amount
            self.transactions.append(-amount)
            return amount
        else:
            return 'Your withdrawal amount is ${} which exceeds your account limit! You have:' \
                   '\n${}. Your withdrawal limit is {}'.format(amount, self.balance, limit)
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_balance(self):
        return self.balance

a = User('Guido van', 'Rossum')
print('first name =', a.get_first_name())
print('last name =', a.get_last_name())
print('account balance =', a.get_balance())
print('withdrawal =', a.withdrawal(50))
print('account balance =', a.get_balance())
