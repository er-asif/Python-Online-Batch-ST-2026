# Encapsulation

class Bank:
    def __init__(self, name, acno, balance):
        self.__name = name # Private
        self.__acno = acno # Private
        self.__balance = balance # Private 

    def get_name(self):
        print("Name =", self.__name)
    def get_acno(self):
        print("Acc No. =", self.__acno)
    def get_balance(self):
        print("Balance =", self.__balance)
     
obj = Bank("John Doe", 1001, 5000)

obj.get_name()
obj.get_acno()
obj.get_balance()