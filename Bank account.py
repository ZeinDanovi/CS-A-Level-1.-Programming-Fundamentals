# Create a Python class for a Bank. 
# Implement a constructor that initializes an empty list to store bank accounts.
#  Create methods to add a new account to the bank, find an account by account number, deposit money into an account, withdraw money from an account, and display all accounts' information. 
# Instantiate more than one object from the class, and show suitable testing.  

# CHALLENGE. 
# Extend the Bank Account class from the previous challenge. 
# Create subclasses for different types of accounts such as SavingsAccount and CheckingAccount. 
# Each subclass should have its own interest rate or fees. Implement methods to calculate interest or apply fees based on account type.


class bank:
    def __init__(self):
        self.bankList = [] #initiate the class with an empty banklist 


    def add(self,accountName,accountNum,accountBalance):  #add function takes in the new bank account details 
        self.accountName = accountName
        self.accountNum = accountNum
        self.accountBalance = accountBalance    


        #checks that account number being added is unique 
        for account in (self.bankList): #cycles through the account numbers 
            if account[1] != accountNum: #if the account is new, checks the next account number 
                continue     
            else:
                print("Account number already exists.")  #otherwise, the account wont be created if it already present 
                break 

        tupleAccount = (accountName,accountNum,accountBalance)   #sets the account details in a tuple 
        (self.bankList).append(tupleAccount)    #the new account is added to the current banklist            


    def find(self,accountNumb):           #method to find an item in the banklist takes in the unique account number 
        for item in (self.bankList):           #checks all the accounts in the banklist 
            if item[1] == accountNumb:              #if an accountnumber is == to the one being searched 
                print(f"your account is found!")               #output message is printed 
                print(f"the name of your account is {self.accountName}") 
                break                                            #breaks from the list 
        
        print("your account was not found in the database")         #output message that account was not found 
 

    def deposit(self,accountNum,accountDepositSum): #deposit method takes in account number and deposit sum
        self.accountNum = accountNum
        self.accountDepositSum = accountDepositSum 

        self.accountBalance = self.accountBalance + accountDepositSum #updates the account balance 
        print(f"after depositing £{accountDepositSum}, your new balance is £{self.accountBalance} ") #prints the new balance after the deposit 


    def withdraw(self,accountNum,accountWithdrawSum): #withdraw method uses the account num and withdraw amount as parameters 
        self.accountNum = accountNum
        self.accountWithdrawSum = accountWithdrawSum

        self.accountBalance = self.accountBalance - accountWithdrawSum #updates the account balance 
        print(f"after withdrawing £{accountWithdrawSum} , your new balance is £{self.accountBalance} ") #prints the new account balance after withdrawn amount 


    def display(self):  #diplay function requires no parameters 
        print(f" here is the current banklist: {self.bankList} ") #outputs all the bank details in the banklist 



    
    
        
        
#test instances from the class:
 
test = bank() #creates an instance of the class 

test.add("malakai", 363, 700) #calls the add method with parameters to add an account to the banklist 
test.add("nathan",266, 1000) 

test.deposit(363, 20) #calls deposit method with sum and account number 

test.withdraw(266,100) #calls withdraw method with the withdraw amount and account number 

test.display()  #calls the display method 