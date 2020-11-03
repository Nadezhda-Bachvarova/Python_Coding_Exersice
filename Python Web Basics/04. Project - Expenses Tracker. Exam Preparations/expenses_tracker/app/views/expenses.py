from django.shortcuts import render, redirect

from app.forms.expenses import ExpenseForm, DeleteExpenseForm
from app.models import Expense


def create_expense_page(request):
    if request.method == 'GET':
        context = {
            'form': ExpenseForm(),
        }
        return render(request, 'expense-create.html', context)
    else:
        form = ExpenseForm(request.POST)   # when click submit button
        if form.is_valid():
            form.save()
            return redirect('home page')
        # else:
        context = {
            'form': form,
        }
        return render(request, 'expense-create.html', context)


def edit_expense_page(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': ExpenseForm(instance=expense),
        }
        return render(request, 'expense-edit.html', context)
    else:
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {
            'expense': expense,
            'form': form,
        }
        return render(request, 'expense-edit.html', context)


def delete_expense_page(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': DeleteExpenseForm(instance=expense),
        }
        return render(request, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect('home page')