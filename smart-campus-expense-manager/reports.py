from pathlib import Path
from datetime import datetime
from analytics import Analytics


class ReportGenerator:
    def __init__(self, expenses, budget):
        self.expenses = expenses
        self.budget = budget

    def generate(self):
        analytics = Analytics(self.expenses)
        total = analytics.9total()
        average = analytics.average()
        category_totals = analytics.category_totals()

        reports_dir = Path(__file__).resolve().parent / "data"
        reports_dir.mkdir(exist_ok=True)

        file_name = f"expense_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        report_path = reports_dir / file_name

        lines = [
            "SMART CAMPUS EXPENSE & BUDGET MANAGER",
            "=" * 45,
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            f"Total Expenses : ₹{total:.2f}",
            f"Budget         : ₹{self.budget:.2f}",
            f"Remaining      : ₹{self.budget - total:.2f}",
            f"Average Expense: ₹{average:.2f}",
            "",
            "CATEGORY-WISE SUMMARY",
            "-" * 25,
        ]

        if category_totals:
            for category, amount in sorted(category_totals.items()):
                lines.append(f"{category}: ₹{amount:.2f}")
        else:
            lines.append("No expenses recorded.")

        lines.extend([
            "",
            "EXPENSE DETAILS",
            "-" * 25,
        ])

        for expense in self.expenses:
            lines.append(
                f"#{expense['id']} | {expense['date']} | "
                f"{expense['category']} | ₹{expense['amount']:.2f} | "
                f"{expense['description']}"
            )

        report_path.write_text("\n".join(lines), encoding="utf-8")
        return report_path
