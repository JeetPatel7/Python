
class bank: 
    def __init__(self,bal,accno):
        self.balance = bal
        self.accountno = accno

    def credit(self,amount):
        self.balance = self.balance - amount
        print(f'{amount} is credited')

    
    def debit(self,amount):
        self.balance = self.balance + amount
        print(f'{amount} is debited')    


acc1 = bank(1000,1234)
acc1.credit(100)
print(acc1.balance)