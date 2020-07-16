class CheckingAccount:
    def __init__(self, firstName, lastName, address, acctNo, balance = 0): #initiates object with given parameters
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.acctNo = acctNo
        self._balance = balance #_balance makes it a private attribute
        
    def deposit(self, credit):
        if type(credit) in [int]: #tested for whole numbers only ie. does not take cents
            self._balance += credit #keeping high cohesion, the methods simply do only what they need to
            
    def withdraw(self, debit):
        if type(debit) in [int]:
            self._balance -= debit
        
    def getBalance(self):
        return "Your current balance is: ${}".format(self._balance)
        
    def getReceipt(self):
        report = "Receipt-\nName: {0} {1}\nAddress: {2}\nAccount Number: {3}\nCurrent Balance: ${4}".format(self.firstName, self.lastName, self.address, self.acctNo, self._balance)
        return report
    
def driver(): #this is the simple driver application that runs methods that the user may call
    myAcct = CheckingAccount("Jane", "Doe", "1234 N 1st St, CityTown CA 90000", 573829201437) #instantiates CheckingAccount object

    myAcct.deposit(100) #credits the account

    print(myAcct.getBalance()) #checks balance

    myAcct.withdraw(99) #debits account

    print(myAcct.getBalance())

    print(myAcct.getReceipt()) #prints receipt
    
    

driver()