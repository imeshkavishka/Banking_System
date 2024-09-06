from random import randrange

class Bank:
    def __init__(self):
        self.accounts = {} # Create a blank dictionary at first to hold account numbers and amounts.

    def menu(self):#Display the main menu
        print()
        print("01-Create an account")
        print("02-Check balance")
        print("03-Deposit money")
        print("04-Withdraw money")
        print("05-Transfer money")
        print("06-Exit")
        print()

    def create_account(self):# The process for making a new account
        accno = randrange(10000, 21000)#Generate a random account number 
        balance = float(input("Enter the amount for deposit: "))# Request the user's initial deposit amount.
        if balance <= 0: # Verify that the initial deposit amount is higher.
            print("\nPlease enter a positive amount!")
            return
        self.accounts[accno] = balance# Display the account details
        print("\nAccount created successfully.")
        print("Account Number: ", accno)
        print("Balance: Rs. ", balance)

    def check_balance(self):# Check an account's balance 
        accno = int(input("Enter your account number: "))# Request the user's account number
        if accno not in self.accounts: # Verify that the account is real.
            print("\nThis account does not exist!")
            return
        balance = self.accounts[accno]# Display the account balance
        print("\nYour balance: Rs. ", balance)
    
    def deposit(self):#Deposit money into an account
        accno = int(input("Enter your account number: ")) 
        if accno not in self.accounts: # Verify that the account is real.
            print("\nThis account does not exist!")
            return
        amount = float(input("Enter the deposit amount: ")) 
        if amount <= 0: # Check if the deposit amount is positive
            print("\nPlease enter a positive amount!")
            return       
        self.accounts[accno] += amount#Update the account balance      
        print("\nMoney deposited successfully.") # Display the updated balance
        print("Your updated balance: Rs. ", self.accounts[accno])

    def withdraw(self): # To withdraw money from an account        
        accno = int(input("Enter your account number: "))#Get account number form the user     
        if accno not in self.accounts:# Verify that the account is real.
            print("\nThis account does not exist!")
            return
       
        amount = float(input("Enter the withdrawal amount: ")) # Request the user's withdrawal amount.
       
        if amount <= 0: #Check if the withdrawal amount is positive
            print("\nPlease enter a positive amount!")
            return
        
        if amount > self.accounts[accno]:# Check that the account has enough money in it.
            print("\nInsufficient balance!")
            return
        
        self.accounts[accno] -= amount#update account balance       
        print("\nWithdrawal successful.")#print update balance
        print("Your updated balance: Rs. ", self.accounts[accno])

    
    def transfer(self):# To transfer money between two accounts      
        from_acc = int(input("Enter your account number: ")) # Get the account number of the sender from the user       
        if from_acc not in self.accounts: # Verify that the sender's account is active
            print("\nThis account does not exist!")
            return      
        to_acc = int(input("Enter the receiver's account number: "))#Get the account number of the reciver from the user
        if to_acc not in self.accounts: # Check that the recipient's account is active.
            print("\nThe receiver's account does not exist!")
            return       
        amount = float(input("Enter the transfer amount: "))#Get transfer amount from the user      
        if amount <= 0:#Check if the transfer amount is positive
            print("\nPlease enter a positive amount!")
            return        
        if amount > self.accounts[from_acc]:# Check that the sender has enough money.
            print("\nInsufficient balance!")
            return       
        self.accounts[from_acc] -= amount #Transfer the money 
        self.accounts[to_acc] += amount       
        print("\nTransfer successful.")#Display the updated balance of the sender
        print("Your updated balance: Rs.", self.accounts[from_acc])
    
    def main(self):# Main method of operating the banking system
        while True:            
            self.menu()#Display main menu           
            choice = input("Enter your choice (1-6): ")#Get user's choice
            print()
           
            if choice == '1':# Based on the user's selection, carry out the relevant action.
                self.create_account()
            elif choice == '2':
                self.check_balance()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                self.withdraw()
            elif choice == '5':
                self.transfer()
            elif choice == '6':
                print("Thank you for using our banking system.")
                break
            else:
                print(" choice is Invalid! Please enter a number between 1 and 6.")

bank = Bank()# Create an instance of the Bank class
bank.main()#Run the banking system

