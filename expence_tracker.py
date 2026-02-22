import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self,file_path = "JSON_files/Expense_Tracker.json"):
        self.filename = file_path
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.expense = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename,"r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("File is Corrupted. Resetting the File.")
            return []

    def save_expense(self):
        with open(self.filename, "w") as file:
            json.dump(self.expense, file, indent= 4)

    def add_expense(self, name, amount, expense_category, description):
        try:
            expense = {
                "id" : max([e['id'] for e in self.expense], default=0)+1,
                "name": name,
                "amount": float(amount),
                "category": expense_category,
                "description": description,
                "date": datetime.now().strftime("%d-%m-%Y")
            }
            self.expense.append(expense)
            self.save_expense()
            return "Data Added Successfully"
        except ValueError:
            return "Data Addition failed."

    def view_by_category(self,expense_category):
        return [i for i in self.expense if i['category'] == expense_category]

    def view_all(self):
        return self.expense

    def total_expense_by_category(self, expense_category):
        return sum(i['amount'] for i in self.expense if i['category'].lower() == expense_category.lower())

    def total_expense(self):
        return sum(i['amount'] for i in self.expense)

    def delete_expense(self, name):
        self.expense = [i for i in self.expense if i['name'] != name]
        self.save_expense()

def main():
    tracker = ExpenseTracker()
    def pretty_print(expense_data):
        for e in expense_data:
            print("-" * 30)
            print(f"""
            id = {e['id']}
            name = {e['name']}
            amount = {e['amount']}
            category = {e['category']}
            description = {e['description']}
            date = {e['date']}
            """)
            print("-" * 30)
    while True:
        print("""Select a Option from Below:
            1. Add_expense
            2. View_by_Category
            3. View_All
            4. Expense_by_Category
            5. Total_Expense
            6. Delete_Expense
            7. Exit
            """)
        action = input("choose: ").lower().strip()
        if action == "add_expense":
            name = input("Please Enter the Name of the Expense: ").strip().lower()
            amount = input("Please State the Amount: ")
            category_of_expense = input("Please Enter the Category of the Expense: ").strip().lower()
            description = input("Please Enter a small Description of the Expense: ").strip().lower()
            tracker.add_expense(name, amount, category_of_expense, description)
        elif action == 'view_by_category':
            category_of_expense = input("Please Enter the Category of the Expense: ").strip().lower()
            expense = tracker.view_by_category(category_of_expense)
            pretty_print(expense) if expense else print("No Value found with that category.")
        elif action == "view_all":
            expense = tracker.view_all()
            pretty_print(expense) if expense else print("No Value found with that category.")
        elif action == "expense_by_category":
            category_of_expense = input("Please Enter the Category of the Expense: ").strip().lower()
            print(tracker.total_expense_by_category(category_of_expense))
        elif action == "total_expense":
            print(tracker.total_expense())
        elif action == "delete_expense":
            name = input("Please Enter the Name of the Expense: ").strip().lower()
            tracker.delete_expense(name)
        elif action == "exit":
            print("Thank You for using our app")
            break
        else:
            print("Enter a Valid Input from Below Options.")

main()