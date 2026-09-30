import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from analytics import Analytics
from budget_manager import BudgetManager
from expense_manager import ExpenseManager


def sample_expenses():
    return [
        {
            "id": 1,
            "date": "2026-09-27",
            "category": "Food",
            "amount": 120.0,
            "description": "Lunch",
        },
        {
            "id": 2,
            "date": "2026-09-27",
            "category": "Travel",
            "amount": 80.0,
            "description": "Bus",
        },
        {
            "id": 3,
            "date": "2026-09-27",
            "category": "Food",
            "amount": 200.0,
            "description": "Dinner",
        },
    ]


class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.expenses = sample_expenses()
        self.analytics = Analytics(self.expenses)

    def test_total(self):
        self.assertEqual(self.analytics.total(), 400.0)

    def test_average(self):
        self.assertAlmostEqual(self.analytics.average(), 400.0 / 3)

    def test_largest(self):
        self.assertEqual(self.analytics.largest_expense()["amount"], 200.0)

    def test_category_totals(self):
        result = self.analytics.category_totals()
        self.assertEqual(result["Food"], 320.0)
        self.assertEqual(result["Travel"], 80.0)

    def test_budget_status(self):
        manager = BudgetManager(500.0)
        self.assertEqual(manager.get_status(300.0), "Within Budget")
        self.assertEqual(manager.get_status(450.0), "Near Budget Limit")
        self.assertEqual(manager.get_status(600.0), "Budget Exceeded")

    def test_next_id(self):
        manager = ExpenseManager(self.expenses)
        self.assertEqual(manager._next_id(), 4)


if __name__ == "__main__":
    unittest.main()
