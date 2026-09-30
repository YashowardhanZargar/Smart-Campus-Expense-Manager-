from validators import get_non_empty, get_positive_float, get_valid_date


class ExpenseManager:
    def __init__(self, expenses=None):
        self.expenses = expenses if expenses is not None else []

    def _next_id(self):
        if not self.expenses:
            return 1
        return max(expense["id"] for expense in self.expenses) + 1

    def add_expense_interactive(self):
        date = get_valid_date("Date (YYYY-MM-DD): ")
        category = get_non_empty("Category: ").title()
        amount = get_positive_float("Amount: ₹")
        description = get_non_empty("Description: ")

        expense = {
            "id": self._next_id(),
            "date": date,
            "category": category,
            "amount": amount,
            "description": description,
        }

        self.expenses.append(expense)
        print("Expense added successfully.")

    def display_expenses(self, expenses=None):
        data = self.expenses if expenses is None else expenses

        if not data:
            print("No expenses recorded.")
            return

        print(f"{'ID':<5}{'Date':<13}{'Category':<18}{'Amount':<12}Description")
        print("-" * 75)

        for expense in data:
            print(
                f"{expense['id']:<5}"
                f"{expense['date']:<13}"
                f"{expense['category']:<18}"
                f"₹{expense['amount']:<10.2f}"
                f"{expense['description']}"
            )

    def find_by_id(self, expense_id):
        for expense in self.expenses:
            if expense["id"] == expense_id:
                return expense
        return None

    def update_expense_interactive(self):
        if not self.expenses:
            print("No expenses available to update.")
            return

        self.display_expenses()
        try:
            expense_id = int(input("\nEnter expense ID to update: "))
        except ValueError:
            print("Invalid ID.")
            return

        expense = self.find_by_id(expense_id)
        if expense is None:
            print("Expense not found.")
            return

        print("Press Enter to keep the existing value.")

        date = input(f"Date [{expense['date']}]: ").strip()
        category = input(f"Category [{expense['category']}]: ").strip()
        amount = input(f"Amount [{expense['amount']}]: ").strip()
        description = input(f"Description [{expense['description']}]: ").strip()

        if date:
            validated_date = get_valid_date("New date: ") if False else date
            expense["date"] = validated_date
        if category:
            expense["category"] = category.title()
        if amount:
            try:
                new_amount = float(amount)
                if new_amount <= 0:
                    raise ValueError
                expense["amount"] = new_amount
            except ValueError:
                print("Invalid amount. Existing amount kept.")
        if description:
            expense["description"] = description

        print("Expense updated successfully.")

    def delete_expense_interactive(self):
        if not self.expenses:
            print("No expenses available to delete.")
            return

        self.display_expenses()
        try:
            expense_id = int(input("\nEnter expense ID to delete: "))
        except ValueError:
            print("Invalid ID.")
            return

        expense = self.find_by_id(expense_id)
        if expense is None:
            print("Expense not found.")
            return

        self.expenses.remove(expense)
        print("Expense deleted successfully.")

    def search_expenses_interactive(self):
        keyword = get_non_empty("Enter category/description keyword: ").lower()

        results = []
        for expense in self.expenses:
            if (
                keyword in expense["category"].lower()
                or keyword in expense["description"].lower()
            ):
                results.append(expense)

        if results:
            self.display_expenses(results)
        else:
            print("No matching expenses found.")

    def get_total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense["amount"]
        return total
