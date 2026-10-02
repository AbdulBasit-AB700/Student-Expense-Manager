# ============================================
# Student Expense & Budget Manager
# Built with Python
# ============================================

FILE_NAME = "expenses.txt"


# --------------------------------------------
# Load expenses from file
# --------------------------------------------
def load_expenses():
    expenses = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split("|")

                    if len(parts) == 3:
                        name = parts[0]
                        amount = float(parts[1])
                        category = parts[2]

                        expense = {
                            "name": name,
                            "amount": amount,
                            "category": category
                        }

                        expenses.append(expense)

    except FileNotFoundError:
        pass

    return expenses


# --------------------------------------------
# Save expenses to file
# --------------------------------------------
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:

        for expense in expenses:
            file.write(
                f"{expense['name']}|"
                f"{expense['amount']}|"
                f"{expense['category']}\n"
            )


# --------------------------------------------
# Set Budget
# --------------------------------------------
def set_budget():
    while True:
        try:
            budget = float(input("Enter your budget: Rs. "))

            if budget < 0:
                print("Budget cannot be negative.")
            else:
                print(f"Budget set successfully: Rs. {budget:.2f}")
                return budget

        except ValueError:
            print("Please enter a valid number.")


# --------------------------------------------
# Add Expense
# --------------------------------------------
def add_expense(expenses):

    name = input("Enter expense name: ").strip()

    if name == "":
        print("Expense name cannot be empty.")
        return

    while True:
        try:
            amount = float(input("Enter amount: Rs. "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    category = input("Enter category: ").strip()

    if category == "":
        category = "Other"

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense added successfully!")


# --------------------------------------------
# View Expenses
# --------------------------------------------
def view_expenses(expenses):

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    print("\n========== EXPENSE HISTORY ==========")

    for i, expense in enumerate(expenses, start=1):

        print(
            f"{i}. {expense['name']} | "
            f"Rs. {expense['amount']:.2f} | "
            f"{expense['category']}"
        )

    print("=====================================")


# --------------------------------------------
# Calculate Total Expenses
# --------------------------------------------
def calculate_total(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# --------------------------------------------
# Show Total Expenses
# --------------------------------------------
def show_total(expenses):

    total = calculate_total(expenses)

    print(f"\nTotal Expenses: Rs. {total:.2f}")


# --------------------------------------------
# Show Remaining Balance
# --------------------------------------------
def show_remaining_balance(expenses, budget):

    total = calculate_total(expenses)

    remaining = budget - total

    print(f"\nBudget: Rs. {budget:.2f}")
    print(f"Total Expenses: Rs. {total:.2f}")
    print(f"Remaining Balance: Rs. {remaining:.2f}")

    if remaining < 0:
        print("Warning: You have exceeded your budget!")


# --------------------------------------------
# Find Highest Expense
# --------------------------------------------
def highest_expense(expenses):

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\n========== HIGHEST EXPENSE ==========")
    print(f"Name: {highest['name']}")
    print(f"Amount: Rs. {highest['amount']:.2f}")
    print(f"Category: {highest['category']}")
    print("=====================================")


# --------------------------------------------
# Main Menu
# --------------------------------------------
def show_menu():

    print("\n")
    print("========================================")
    print("      STUDENT EXPENSE MANAGER")
    print("========================================")
    print("1. Set Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Total Expenses")
    print("5. Remaining Balance")
    print("6. Highest Expense")
    print("7. Exit")
    print("========================================")


# --------------------------------------------
# Main Program
# --------------------------------------------

expenses = load_expenses()

budget = 0

while True:

    show_menu()

    choice = input("Enter your choice (1-7): ")

    if choice == "1":

        budget = set_budget()

    elif choice == "2":

        add_expense(expenses)

    elif choice == "3":

        view_expenses(expenses)

    elif choice == "4":

        show_total(expenses)

    elif choice == "5":

        show_remaining_balance(expenses, budget)

    elif choice == "6":

        highest_expense(expenses)

    elif choice == "7":

        print("\nThank you for using Student Expense Manager!")
        print("Goodbye!")
        break

    else:

        print("\nInvalid choice. Please select 1-7.")