
class BankAccount:
    def __init__(self, first_name, middle_name, last_name, balance = 100):

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.balance = balance


        

    def check_balance(self):
        print(self.balance)

    def withdraw(self, funds):
        if self.balance <= funds:
            print("Sorry, not enough funds.")
            return
        self.balance -= funds

    def deposit(self, funds):
        self.balance += funds



first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")

bank_account = BankAccount(first_name, middle_name, last_name)
print("Thanks for the deposit. Your account is now activated!")






while True:

    print("1. Check Balance, 2. Withdraw, 3. Deposit, 4. Quit")
    user_input = input("Enter an option here:  ")


    if user_input == "4":
        print("Thank you!")
        break
    elif user_input == "1":
        pass
    elif user_input == "2":
        withdraw_amount = int(input("How much would you like to withdraw?  "))
        bank_account.withdraw(withdraw_amount)
    elif user_input == "3":
        deposit_amount = int(input("How much would you like to deposit?  "))
        bank_account.deposit(deposit_amount)


    print("Balance: ", bank_account.balance)
    
        







