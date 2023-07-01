menu = """
[d] Deposit
[w] Withdraw
[b] Balance
[q] Quit

=> """

balance = 0
limit = 500
statement = ""
num_withdrawals = 0
WITHDRAWAL_LIMIT = 3

while True:
    option = input(menu)

    if option == "d":
        value = float(input("Enter the deposit amount: "))
        if value <= 0:
            print("Operation failed! The value entered is invalid.")
            continue

        balance += value
        statement += f"Deposit: R$ {value:.2f}\n"

    elif option == "w":
        value = float(input("Enter the withdrawal amount: "))

        if value > balance:
            print("Operation failed! You don't have sufficient balance.")
        elif value > limit:
            print("Operation failed! The withdrawal amount exceeds the limit.")
        elif num_withdrawals >= WITHDRAWAL_LIMIT:
            print("Operation failed! Maximum number of withdrawals exceeded.")
        elif value <= 0:
            print("Operation failed! The value entered is invalid.")
        else:
            balance -= value
            statement += f"Withdrawal: R$ {value:.2f}\n"
            num_withdrawals += 1

    elif option == "b":
        print("\n================ STATEMENT ================")
        print("No transactions made." if not statement else statement)
        print(f"\nBalance: R$ {balance:.2f}")
        print("============================================")

    elif option == "q":
        break

    else:
        print("Invalid operation, please select the desired operation again.")
