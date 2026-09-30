import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
EXPENSE_FILE = DATA_DIR / "expenses.json"
BUDGET_FILE = DATA_DIR / "budget.json"


def _ensure_data_directory():
    DATA_DIR.mkdir(exist_ok=True)


def load_expenses():
    _ensure_data_directory()

    if not EXPENSE_FILE.exists():
        return []

    try:
        with EXPENSE_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read expense data. Starting with empty data.")
        return []


def save_expenses(expenses):
    _ensure_data_directory()

    with EXPENSE_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def load_budget():
    _ensure_data_directory()

    if not BUDGET_FILE.exists():
        return 0.0

    try:
        with BUDGET_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return float(data.get("budget", 0.0))
    except (json.JSONDecodeError, OSError, ValueError):
        print("Warning: Could not read budget data. Using ₹0 budget.")
        return 0.0


def save_budget(budget):
    _ensure_data_directory()

    with BUDGET_FILE.open("w", encoding="utf-8") as file:
        json.dump({"budget": budget}, file, indent=4)
