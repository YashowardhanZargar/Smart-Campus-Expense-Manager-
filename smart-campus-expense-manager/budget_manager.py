from validators import get_positive_float


class BudgetManager:
    def __init__(self, budget=0.0):
        self.budget = float(budget)

    def set_budget_interactive(self):
        self.budget = get_positive_float("Enter monthly budget: ₹")
        print(f"Monthly budget set to ₹{self.budget:.2f}")

    def get_budget(self):
        return self.budget

    def get_usage_percentage(self, total_spent):
        if self.budget <= 0:
            return 0.0
        return (total_spent / self.budget) * 100

    def get_status(self, total_spent):
        if self.budget <= 0:
            return "Budget not set"
        if total_spent > self.budget:
            return "Budget Exceeded"
        if total_spent == self.budget:
            return "Budget Fully Used"
        if self.get_usage_percentage(total_spent) >= 80:
            return "Near Budget Limit"
        return "Within Budget"
