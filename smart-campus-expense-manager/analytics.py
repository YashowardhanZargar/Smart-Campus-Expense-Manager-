class Analytics:
    def __init__(self, expenses):
        self.expenses = expenses

    def total(self):
        total = 0
        for expense in self.expenses:
            total += expense["amount"]
        return total

    def average(self):
        if not self.expenses:
            return 0.0
        return self.total() / len(self.expenses)

    def largest_expense(self):
        if not self.expenses:
            return None

        largest = self.expenses[0]
        for expense in self.expenses[1:]:
            if expense["amount"] > largest["amount"]:
                largest = expense
        return largest

    def category_totals(self):
        totals = {}
        for expense in self.expenses:
            category = expense["category"]
            if category not in totals:
                totals[category] = 0.0
            totals[category] += expense["amount"]
        return totals

    def category_count(self):
        counts = {}
        for expense in self.expenses:
            category = expense["category"]
            counts[category] = counts.get(category, 0) + 1
        return counts

    def sort_by_amount(self, descending=False):
        return sorted(
            self.expenses,
            key=lambda expense: expense["amount"],
            reverse=descending,
        )
