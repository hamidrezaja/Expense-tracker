from django.shortcuts import render,redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
# Create your views here.
def index(request):
    if request.method=='POST':
        expense=ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
    expenses=Expense.objects.all()
    total_expenses=expenses.aggregate(Sum('amount'))
    expense_form=ExpenseForm()
    return render(request,'myapp/index.html',{"expense_form":expense_form,"expenses":expenses,'total_expenses':total_expenses})
def edit(request,id):
    expense=Expense.objects.get(id=id)
    expense_form=ExpenseForm(instance=expense)
    if request.method=='POST':
        form=ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'myapp/edit.html',{"expense_form":expense_form})
def delete(request,id):
    expense=Expense.objects.get(id=id)
    expense.delete()
    return redirect('index')
    