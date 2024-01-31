# console based personal budget tracker 

import json
import os


def main():
    budget_data = load_data()

    while True:
        print("\n Budget Tracker ")
        
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. View Expenses")
        print("5. Display Summary")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_income(budget_data)
            
        elif choice == "2":
            add_expense(budget_data)

        elif choice == "3":
            total_income, total_expenses, balance = calculate_budget(budget_data)
            print("\n Budget Calculation ")
            print(f"Total Income: {total_income}")
            print(f"Total Expenses: {total_expenses}")
            print(f"Balance Remain: {balance}\n")

        elif choice == "4":
            view_expenses(budget_data)

        elif choice == "5":
            view_summary(budget_data)

        elif choice == "6":
            print("Exit Budget Tracker.")
            break

        else:
            print("Invalid input. enter number between 1 to 6.")




def add_income(data):
    
    amount = float(input("Enter income amount: "))

    data["income"].append({ "amount": amount})
    save_data(data)
    print("Income added successfully!")



def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))

    data["expenses"].append({"category": category, "amount": amount})
    save_data(data)
    print("Expense added successfully!")



def calculate_budget(data):
    total_income = sum(entry["amount"] for entry in data["income"])
    total_expenses = sum(entry["amount"] for entry in data["expenses"])

    balance = total_income - total_expenses
    return total_income, total_expenses, balance



def view_expenses(data):
    expense_categories = set(entry["category"] for entry in data["expenses"])
    
    print("\n Expense Analysis ")
    for category in expense_categories:
        total_amount = sum(entry["amount"] for entry in data["expenses"] if entry["category"] == category)
        print(f"{category}: {total_amount}")



def view_summary(data):

    total_income = sum(entry["amount"] for entry in data["income"])
    total_expenses = sum(entry["amount"] for entry in data["expenses"])
    balance = total_income - total_expenses

    print("\n Budget Summary ")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Balance Remaining: {balance}\n")




def load_data():
    if os.path.exists("budget_data.json"):
        with open("budget_data.json", "r") as file:
            return json.load(file)
    else:
        return {"income": [], "expenses": []}




def save_data(data):
    with open("budget_data.json", "w") as file:
        json.dump(data, file, indent=2)



if __name__ == "__main__":
    main()





