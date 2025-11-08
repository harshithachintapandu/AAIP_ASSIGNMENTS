# EXAMPLE OF INCORRECT FUNCTION - Missing colon (Syntax Error)
def add(a, b):
    return a + b


# EXAMPLE OF LOGIC ERROR - Infinite Loop
def count_down_incorrect(n):
    """
    INCORRECT VERSION - Causes infinite loop!
    Logic Error: Increments n instead of decrementing it.
    If n starts as non-negative, it will always be >= 0, causing infinite iteration.
    """
    while n >= 0:
        print(n)
        n += 1  # ERROR: Should be n -= 1 (decrement, not increment)


# CORRECTED VERSION - Fixed Logic Error
def count_down_correct(n):
    """
    CORRECT VERSION - Properly counts down from n to 0.
    Fixed: Changed n += 1 to n -= 1 to decrement the counter.
    """
    while n >= 0:
        print(n)
        n -= 1  # CORRECT: Decrements n to count down


class BankAccount:
    
    def __init__(self, account_number, account_holder, initial_balance=0.0):
       
        self.account_number = account_number
        self.account_holder = account_holder
        
        # Validate initial balance
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = float(initial_balance)
    
    def deposit(self, amount):
       
        if amount <= 0:
            print("Error: Deposit amount must be positive!")
            return False
        
        self.balance += amount
        print(f"Deposit successful! Amount deposited: ${amount:.2f}")
        return True
    
    def withdraw(self, amount):
      
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"Error: Insufficient balance! Current balance: ${self.balance:.2f}")
            return False
        
        self.balance -= amount
        print(f"Withdrawal successful! Amount withdrawn: ${amount:.2f}")
        return True
    
    def get_balance(self): 
        return self.balance
    
    def display_balance(self):
        print(f"\nAccount Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")
    
    def display_account_info(self):
        print("\n" + "=" * 50)
        print("ACCOUNT INFORMATION")
        print("=" * 50)
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("=" * 50)


if __name__ == "__main__":
    print("=" * 60)
    print("LOGIC ERROR DEMONSTRATION - Infinite Loop")
    print("=" * 60)
    print("\nProblem: count_down_incorrect() function has a logic error")
    print("Error: Uses n += 1 (increment) instead of n -= 1 (decrement)")
    print("Result: Infinite loop because n never decreases, always stays >= 0")
    print("\n" + "-" * 60)
    print("CORRECTED VERSION DEMONSTRATION:")
    print("-" * 60)
    
    # Demonstrate the correct version
    print("\nCounting down from 5 using CORRECT version:")
    count_down_correct(5)
    
    print("\n" + "=" * 60)
    print("WARNING: Do not run count_down_incorrect() - it will cause infinite loop!")
    print("=" * 60)
    print("\n" + "=" * 60)
    print("BANK ACCOUNT MANAGEMENT SYSTEM")
    print("=" * 60)
    
    try:
        # Create a bank account
        print("\nCreating new bank account...")
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder name: ")
        
        initial_balance_input = input("Enter initial balance (press Enter for $0.00): ")
        initial_balance = float(initial_balance_input) if initial_balance_input else 0.0
        
        # Initialize bank account
        account = BankAccount(account_number, account_holder, initial_balance)
        print("\nAccount created successfully!")
        account.display_account_info()
        
        # Menu-driven program
        while True:
            print("\n" + "-" * 60)
            print("MENU:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Display Account Info")
            print("5. Exit")
            print("-" * 60)
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                amount = float(input("Enter amount to deposit: $"))
                account.deposit(amount)
                account.display_balance()
            
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: $"))
                account.withdraw(amount)
                account.display_balance()
            
            elif choice == "3":
                balance = account.get_balance()
                print(f"\nCurrent Balance: ${balance:.2f}")
            
            elif choice == "4":
                account.display_account_info()
            
            elif choice == "5":
                print("\nThank you for using Bank Account Management System!")
                print("\n" + "=" * 60)
                print("CODE ANALYSIS:")
                print("=" * 60)
                print("""
LOGIC ERROR ANALYSIS - INFINITE LOOP:
--------------------------------------
PROBLEM IDENTIFIED:
- Function: count_down_incorrect(n)
- Error: Uses n += 1 (increment) instead of n -= 1 (decrement)

WHY IT CAUSES INFINITE LOOP:
1. Loop condition: while n >= 0
2. If n starts as 0 or positive (e.g., n = 5)
3. Inside loop: n += 1 increments n (5 → 6 → 7 → 8 → ...)
4. n never decreases, so condition n >= 0 is always True
5. Loop never terminates → INFINITE LOOP

HOW TO FIX:
- Change: n += 1
- To: n -= 1
- This decrements n, eventually making n < 0, terminating the loop

EXAMPLE:
--------
Incorrect:  n = 5 → 6 → 7 → 8 → ... (infinite)
Correct:    n = 5 → 4 → 3 → 2 → 1 → 0 → -1 (stops)

PREVENTION TIPS:
----------------
1. Always verify loop variable changes in the correct direction
2. Ensure loop condition can eventually become False
3. Test with small values first
4. Use debugging to trace variable values
5. For countdown loops, use decrement (n -= 1 or n = n - 1)

CLASS STRUCTURE:
----------------
1. __init__ (Constructor):
   - Initializes account with account_number, account_holder, and balance
   - Validates initial_balance to prevent negative values
   - Uses encapsulation to store account data as instance variables
   - Default parameter allows creating account with zero balance

2. deposit(amount):
   - Validates deposit amount (must be positive)
   - Updates balance by adding deposit amount
   - Provides user feedback on success
   - Returns boolean for programmatic success checking

3. withdraw(amount):
   - Validates withdrawal amount (must be positive)
   - Checks for sufficient balance before withdrawal
   - Prevents overdraft (withdrawal > balance)
   - Updates balance by subtracting withdrawal amount
   - Provides user feedback on success/failure

4. get_balance():
   - Getter method to retrieve current balance
   - Provides controlled access to balance attribute
   - Returns float value of balance

5. display_balance():
   - Formats and displays balance information
   - Shows account holder and account number
   - User-friendly output format

6. display_account_info():
   - Displays complete account information
   - Formatted output for account summary

KEY CONCEPTS:
-------------
1. ENCAPSULATION:
   - Account data (balance, account_number, account_holder) is stored as instance variables
   - Methods provide controlled access to account data
   - Prevents direct modification of balance without validation

2. DATA VALIDATION:
   - All methods validate input before processing
   - Prevents invalid operations (negative deposits, overdraft, etc.)
   - Provides error messages for invalid operations

3. METHOD DESIGN:
   - Each method has a single responsibility
   - Methods return boolean values for success/failure
   - User-friendly error messages

4. OOP PRINCIPLES:
   - Encapsulation: Data and methods bundled together
   - Abstraction: Hides implementation details
   - Data hiding: Balance accessed through methods

TIME COMPLEXITY:
----------------
- deposit(): O(1) - Constant time operation
- withdraw(): O(1) - Constant time operation
- get_balance(): O(1) - Constant time operation
- All operations are constant time, making them efficient

SPACE COMPLEXITY:
-----------------
- O(1) - Only stores account data (3 attributes)
- No additional data structures required

RECOMMENDATIONS:
----------------
- Consider adding transaction history
- Add interest calculation functionality
- Implement account type (savings/checking)
- Add password/pin protection
- Implement account locking after failed attempts
                """)
                break
            
            else:
                print("Invalid choice! Please enter a number between 1-5.")
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please enter valid numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

