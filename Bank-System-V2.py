# Constants
LIMIT = 500
WITHDRAWAL_LIMIT = 3

# Global variables
balance = 0
statement = ""
num_withdrawals = 0

# Function to perform a deposit
def deposit(value):
    global balance, statement
    if value <= 0:
        print("Operation failed! The value entered is invalid.")
    else:
        balance += value
        statement += f"Deposit: $ {value:.2f}\n"
        print("Deposit successful.")

# Function to perform a withdrawal
def withdraw(value):
    global balance, statement, num_withdrawals
    if value <= 0:
        print("Operation failed! The value entered is invalid.")
    elif value > balance:
        print("Operation failed! You don't have sufficient balance.")
    elif value > LIMIT:
        print("Operation failed! The withdrawal amount exceeds the limit.")
    elif num_withdrawals >= WITHDRAWAL_LIMIT:
        print("Operation failed! Maximum number of withdrawals exceeded.")
    else:
        balance -= value
        statement += f"Withdrawal: $ {value:.2f}\n"
        num_withdrawals += 1
        print("Withdrawal successful.")

# Function to display the balance statement
def display_balance():
    print("\n================ STATEMENT ================")
    print("No transactions made." if not statement else statement)
    print(f"\nBalance: $ {balance:.2f}")
    print("============================================")

# Main program function
def main():
    while True:
        option = input(
            """
            [d] Deposit
            [w] Withdraw
            [b] Balance
            [q] Quit

            => """
        )

        if option == "d":
            value = float(input("Enter the deposit amount: "))
            deposit(value)
        elif option == "w":
            value = float(input("Enter the withdrawal amount: "))
            withdraw(value)
        elif option == "b":
            display_balance()
        elif option == "q":
            break
        else:
            print("Invalid operation, please select the desired operation again.")

if __name__ == "__main__":
    main()
