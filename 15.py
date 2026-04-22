# --- Blueprint 1: The Bank ---
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance 
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds!")
    
    def get_balance(self):
        return self.__balance

 
 
class Employee:
    def __init__(self, name, salary, bank_account_object):
        self.name = name
        self.salary = salary
        # This is Composition: One object holding another object
        self.account = bank_account_object 

    def info(self):
        return f"Employee: {self.name} | Salary: ${self.salary}"

    def receive_paycheck(self):
        # The employee uses the bank account's method to add the money
        self.account.deposit(self.salary)
        print(f"Payday! ${self.salary} has been deposited into {self.name}'s account.")



















# --- EXECUTION (Building the real objects) ---

# 1. First, create a bank account with 1000 initial balance
zains_bank = BankAccount("PK-9988", 1000)

# 2. Create the employee and "link" that bank account to them
e1 = Employee("Zain", 5000, zains_bank)

# 3. Check the balance before payday
print(f"Starting Balance: {e1.account.get_balance()}")

# 4. Run the paycheck method
e1.receive_paycheck()

# 5. Check the balance after payday
print(f"New Balance: {e1.account.get_balance()}")