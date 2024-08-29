class BankAccount:
    def __init__(self, accountHolder):
        self._balance = 0
        self._name = accountHolder

        with open(self._name + 'BankLedger.txt', 'w') as ledgerFile:
            ledgerFile.write('Balance is 0\n')

    def deposit(self, amount):
        if amount <= 0:
            return
        self._balance += amount

        with open(self._name + 'BankLedger.txt', 'a') as ledgerFile:
            ledgerFile.write('Deposit ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return

        self._balance -= amount
        with open(self._name + 'BankLedger.txt', 'a') as ledgerFile:
            ledgerFile.write('Withdraw ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')


acct = BankAccount('Alice')
acct.deposit(120)
acct.withdraw(40)

acct._balance = 1000000000
acct.withdraw(1000)

acct._name = 'Bob'
acct.withdraw(1000)
