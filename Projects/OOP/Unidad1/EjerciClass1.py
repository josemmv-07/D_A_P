# Crea una clase que represente una cuenta bancaria

class banckAccount:
    def __init__(self):
        pass

    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def display(self):
        print(self.name, self.balance)

    def recall(self, amount):
        self.balance -= amount  

    def deposit(self, amount):
        self.balance += amount  

x1 = banckAccount()

x1.set_details("jose", 350)
x1.display()

x1.recall(100)
x1.display()
x1.deposit(200)

x1.display()  

