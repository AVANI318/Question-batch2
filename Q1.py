class BankAccount:
    def deposit(self):
        amount = int(input("Enter your amount to be deposited on savings account: "))
        if amount > 0:
            self.dep = amount
            print("The deposited amount is:", self.dep)
        else:
            print("Invalid amount entered.")
    def withdraw(self):
        self.withdr = int(input("Enter your amount to be withdrawn: "))
        if self.withdr > self.dep:
            print("There is not enough money in your bank account..retry")
        else:
            print("Cash withdrawn:", self.withdr)
    def balance(self):
        self.bal = self.dep - self.withdr
        print("The balance amount is:", self.bal)


class SavingsAccount(BankAccount):
    def interest(self):
        if hasattr(self, 'bal') and self.bal > 1:
            self.intrst = self.bal * 0.04   
            print("Savings Account Balance Amount:", self.bal)
            print("Interest amount:", self.intrst)
        else:
            print("Balance not available to calculate interest.")

class CurrentAccount:
    def currentdeposit(self):
        self.curamt=int(input("Enter the amount for your current account: "))
        if self.curamt>1:
            print("the amount deposited in your current account is: ",self.curamt)
        else:
            print("the amount should be atleast rupees 1")
    def currentwithdraw(self):
        self.withdraw=int(input("enter the amount to be withdrawed: "))
        if self.withdraw>10:
            print("the amount withdrawed: ",self.withdraw)
        else:
            print("atleast withdraw 10 rupees")
    def currentbalance(self):
        self.curbal=self.curamt-self.withdraw
        print("the balance amount in your current account is: ",self.curbal)

obj = SavingsAccount()
obj.deposit()
obj.withdraw()
obj.balance()
obj.interest()
obj=CurrentAccount()
obj.currentdeposit()
obj.currentwithdraw()
obj.currentbalance()