from app.models import Profile, Expense


def calculate_budget_left(profile, expenses):
    expenses_cost = sum(expense.price for expense in expenses)
    budget_left = profile.budget - expenses_cost
    return budget_left

