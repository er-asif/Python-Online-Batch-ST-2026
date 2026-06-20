"""
Write a python program to create a class with name ‘Bank’. In Bank class take
three instance variables acno, name and balance. Create a parameterized
constructor to initialize instance variables. Now create following methods in
Bank class:-
i. deposit() – This method is used to deposit() money in account.
ii. withdraw() – This method is used to withdraw money from account
after checking balance.
iii. enquiry():- This method provide balance enquiry
"""


class Bank:
    def __init__(self, acno, name, balance):
        self.acno = acno
        self.name = name
        self.balance = balance
        print("Account created successfully")

    def deposit(self, acno, amt):
        if self.acno == acno:
            self.balance += amt
            print(f"{amt} has been credited to you account. Now available balance is {self.balance}")
        else:
            print("Invalid account number")

    def withdraw(self, acno, amt):
        if self.acno == acno:
            if self.balance >= amt:
                self.balance -= amt
                print(f"{amt} has been debited from your account. Now  available balance is {self.balance}")
            else:
               print("Insufficient balance") 
        else:
            print("Invalid account number")
    
    def enquiry(self, acno):
        if self.acno == acno:
            print("Name = ", self.name)
            print("Acount Number =", self.acno)
            print("Total balance = ", self.balance)
        else:
            print("Invalid account number")

obj = Bank(1001, "Mohammad Asif", 3000)

while True:
    print("""
        Press 1 for deposit
        Press 2 for withdraw
        Press 3 for enquiry
        Press 4 for exit
        """)
    ch = int(input("Enter your choice "))
    if ch == 1:
        acno = int(input("Enter account number ")) 
        amt = int(input("Enter amoount for deposite "))
        obj.deposit(acno, amt)
    elif ch == 2:
        acno = int(input("Enter account number ")) 
        amt = int(input("Enter amoount for withdrawl "))
        obj.withdraw(acno, amt)
    elif ch == 3:
        acno = int(input("Enter account number ")) 
        obj.enquiry(acno)
    elif ch == 4:
        break
    else:
        print("Invalid choice")