from dataclasses import dataclass
from


class Customer:

    def __init__(self,
                 first_name:str,
                 last_name:str,
                 phone:int,
                 email:str,
                 address:str,
                 balance:0):
        
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.__balance = balance


    def update_balance(self, type, amount):
        """updates the balance for deposit or credit transactions"""
        if type == 'deposit':
            self.__balance += amount
        else:
            self.__balance -= amount

    @classmethod
    def update_history(cls, date, type, amount):
        """ updates the transaction history"""
        cls.history[f'{date}'] = {'type':type, 'amount':amount}


    def get_balance(self):


@dataclass
class Bank:

    customers = dict[]


    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass


    def deposit(self, amount):
        pass


    def withdrawal(self, amount):
        pass


    def view_history(self, amount):
        pass


    def sign_up(self, **kwargs):
        pass


    Wema = Bank()

    customer1 