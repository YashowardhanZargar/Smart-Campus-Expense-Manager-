from expense_manager import ExpenseManager
from budget_manager import BudgetManager
from analytics import Analytics
from reports import ReportGenerator
from storage import load_expenses, save_expenses, load_budget, save_budget
from validators import get_valid_choice
from utils import print_header, pause


def display_menu():
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search Expenses")
    print("6. Set Budget")
    print("7. Budget Status")
    print("8. Expense Analytics")
    print("9. Generate Report")
    print("10. Save Data")
    print("11. Exit")


def add_expense(manager):
    print_header("ADD EXPENSE")
    manager.add_expense_interactive()


def view_expenses(manager):
    print_header("ALL EXPENSES")
    manager.display_expenses()


def update_expense(manager):
    print_header("UPDATE EXPENSE")
    manager.update_expense_interactive()


def delete_expense(manager):
    print_header("DELETE EXPENSE")
    manager.delete_expense_interactive()


def search_expenses(manager):
    print_header("SEARCH EXPENSES")
    manager.search_expenses_interactive()


def set_budget(budget_manager):
    print_header("SET MONTHLY BUDGET")
    budget_manager.set_budget_interactive()


def budget_status(manager, budget_manager):
    print_header("BUDGET STATUS")
    total = manager.get_total_expense()
    budget = budget_manager.get_budget()
    print(f"Budget       : ₹{budget:.2f}")
    print(f"Spent        : ₹{total:.2f}")
    print(f"Remaining    : ₹{budget - total:.2f}")
    print(f"Used         : {budget_manager.get_usage_percentage(total):.2f}%")
    print(f"Status       : {budget_manager.get_status(total)}")


def analytics_menu(manager):
    print_header("EXPENSE ANALYTICS")
    analytics = Analytics(manager.expenses)

    print(f"Total Expense      : ₹{analytics.total():.2f}")
    print(f"Average Expense    : ₹{analytics.average():.2f}")

    largest = analytics.largest_expense()
    if largest:
        print(f"Largest Expense    : ₹{largest['amount']:.2f} - {largest['description']}")
    else:
        print("Largest Expense    : No data")

    print("\nCategory-wise Spending:")
    category_data = analytics.category_totals()
    if not category_data:
        print("No data available.")
    else:
        for category, amount in sorted(category_data.items()):
            print(f"  {category:<18} ₹{amount:.2f}")

    print("\nExpenses Sorted by Amount (High to Low):")
    for expense in analytics.sort_by_amount(descending=True):
        print(f"  #{expense['id']} | ₹{expense['amount']:.2f} | {expense['category']} | {expense['description']}")


def generate_report(manager, budget_manager):
    print_header("GENERATE REPORT")
    report = ReportGenerator(manager.expenses, budget_manager.get_budget())
    report_path = report.generate()
    print(f"Report generated successfully: {report_path}")


def save_all(manager, budget_manager):
    save_expenses(manager.expenses)
    save_budget(budget_manager.get_budget())
    print("Data saved successfully.")


def main():
    expenses = load_expenses()
    budget = load_budget()

    manager = ExpenseManager(expenses)
    budget_manager = BudgetManager(budget)

    while True:
        print_header("SMART CAMPUS EXPENSE & BUDGET MANAGER")
        display_menu()

        choice = get_valid_choice("Enter your choice: ", 1, 11)

        if choice == 1:
            add_expense(manager)
        elif choice == 2:
            view_expenses(manager)
        elif choice == 3:
            update_expense(manager)
        elif choice == 4:
            delete_expense(manager)
        elif choice == 5:
            search_expenses(manager)
        elif choice == 6:
            set_budget(budget_manager)
        elif choice == 7:
            budget_status(manager, budget_manager)
        elif choice == 8:
            analytics_menu(manager)
        elif choice == 9:
            generate_report(manager, budget_manager)
        elif choice == 10:
            save_all(manager, budget_manager)
        elif choice == 11:
            save_all(manager, budget_manager)
            print("Thank you for using Smart Campus Expense & Budget Manager.")
            break

        pause()


if __name__ == "__main__":
    main()
