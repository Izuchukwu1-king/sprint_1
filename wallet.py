class Wallet:
# First thing to run when we make a new class outline user-provided
# input values her.
# Parameters with default values assigned are optional
    def __init__(self, initial_amount = 0):
# Save the user-provided initial_amount as an attribute
# self refers to whatever object I'm working with

        self.balance = initial_amount

        #SPEND CASH METHOD
    def spend_cash(self, amount):
            if self.balance < amount:
                return "not enough money"
            else:
                self.balance = self.balance - amount
                return f"remaining balance:{self.balance}"
    def add_cash(self, amount):
                 self.balance = self.balance + amount
                 return f"new balance of:{self.balance}"



# __repr__method
# changes how the "object" looks whent it is printed out
# the presence of the self keyword allows me to acess or modify
# class attributes within this function
def __repr__(self):
          return f"Wallet with balance of: ${self.balance}"


 
    
if __name__ == '__main__':
     wallet1 = Wallet(50)
     print(wallet1)
     print(wallet1.balance)
    #wallet1 = Wallet(100)
    #wallet2 = Wallet(50)
    #wallet3 = Wallet(3000)
    #print(wallet1.add_cash(60))
    #print(wallet1.spend_cash(180))
    #print(wallet1.spend_cash(120))

    #print(wallet1.balance)
    #print(wallet2.balance)
    #print(wallet3.balance)
        