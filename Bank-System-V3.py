# Necessary imports for the code
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime


# Client class represents a generic client
class Client:
    def __init__(self, address):
        # Initializes a client with an address and an empty list of accounts
        self.address = address
        self.accounts = []

    # Performs a transaction on an account
    def perform_transaction(self, account, transaction):
        transaction.register(account)

    # Adds an account to the client's list of accounts
    def add_account(self, account):
        self.accounts.append(account)


# Person class inherits from Client and represents an individual
class Person(Client):
    def __init__(self, name, date_of_birth, cpf, address):
        # Initializes a person with additional information (name, date of birth, CPF) and calls the Client constructor
        super().__init__(address)
        self.name = name
        self.date_of_birth = date_of_birth
        self.cpf = cpf


# Account class represents a generic account
class Account:
    def __init__(self, number, client):
        # Initializes an account with zero balance, a number, agency, associated client, and an empty history
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()

    # Class method to create a new account
    @classmethod
    def new_account(cls, client, number):
        return cls(number, client)

    # Properties to retrieve account information
    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history

    # Performs a withdrawal from the account
    def withdraw(self, value):
        if value <= 0:
            print("\n@@@ Operation failed! The provided value is invalid. @@@")
            return False

        if value > self.balance:
            print("\n@@@ Operation failed! You do not have sufficient balance. @@@")

        else:
            self._balance -= value
            print("\n=== Withdrawal successful! ===")
            return True

    # Performs a deposit into the account
    def deposit(self, value):
        if value <= 0:
            print("\n@@@ Operation failed! The provided value is invalid. @@@")
            return False

        self._balance += value
        print("\n=== Deposit successful! ===")
        return True


# CheckingAccount class inherits from Account and represents a checking account with limits
class CheckingAccount(Account):
    def __init__(self, number, client, limit=500, withdrawal_limit=3):
        # Initializes a checking account with additional limits and calls the Account constructor
        super().__init__(number, client)
        self.limit = limit
        self.withdrawal_limit = withdrawal_limit

    # Overrides the withdraw method to apply limits
    def withdraw(self, value):
        if value > self.limit:
            print(
                "\n@@@ Operation failed! The withdrawal amount exceeds the limit. @@@"
            )

        elif (
            len([t for t in self.history.transactions if t["type"] == "Withdrawal"])
            >= self.withdrawal_limit
        ):
            print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

        else:
            return super().withdraw(value)

        return False

    # Overrides the __str__ method to provide a string representation of the checking account
    def __str__(self):
        return f"""\
            Agency:\t{self.agency}
            Account:\t{self.number}
            Holder:\t{self.client.name}
        """


# History class records account transactions
class History:
    def __init__(self):
        # Initializes the history with an empty list of transactions
        self._transactions = []

    # Property to retrieve the list of transactions
    @property
    def transactions(self):
        return self._transactions

    # Adds a transaction to the history
    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


# Abstract Transaction class represents a generic transaction
class Transaction(ABC):
    # Abstract properties to get the transaction value and register the transaction
    @property
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def register(self, account):
        pass


# Withdrawal class inherits from Transaction and represents a withdrawal transaction
class Withdrawal(Transaction):
    def __init__(self, value):
        self._value = value

    # Property to get the withdrawal value
    @property
    def value(self):
        return self._value

    # Registers a withdrawal on the account and adds it to the history
    def register(self, account):
        success_transaction = account.withdraw(self.value)

        if success_transaction:
            account.history.add_transaction(self)


# Deposit class inherits from Transaction and represents a deposit transaction
class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    # Property to get the deposit value
    @property
    def value(self):
        return self._value

    # Registers a deposit into the account and adds it to the history
    def register(self, account):
        success_transaction = account.deposit(self.value)

        if success_transaction:
            account.history.add_transaction(self)
