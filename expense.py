import datetime

# List to store expenses
expenses = []

# Function to add a new expense
def add_expense():
    print("\n---- Add New Expense ----")
    try:
        date_str = input("Enter date (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        category = input("Enter category (e.g., Food, Travel, Shopping): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        expense = {
            "date": date,
            "category": category.capitalize(),
            "amount": amount,
            "description": description
        }

        expenses.append(expense)
        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid input. Please try again.\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.\n")
    else:
        print("\n---- All Expenses ----")
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. Date: {exp['date']} | Category: {exp['category']} | Amount: ${exp['amount']} | Description: {exp['description']}")
        print()

# Function to calculate total by category
def total_by_category():
    print("\n---- Total Expenses by Category ----")
    category = input("Enter category to calculate total: ").capitalize()
    total = sum(exp["amount"] for exp in expenses if exp["category"] == category)
    print(f"Total spent in {category}: ${total:.2f}\n")

# Function to delete an expense
def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        num = int(input("Enter expense number to delete: "))
        if 1 <= num <= len(expenses):
            deleted = expenses.pop(num - 1)
            print(f"Deleted expense: {deleted['description']} (${deleted['amount']})\n")
        else:
            print("Invalid entry number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

# Main menu
def main():
    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total by Category")
        print("4. Delete an Expense")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the program
if __name__ == "__main__":
    main()
