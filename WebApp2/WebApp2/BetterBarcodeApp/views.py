from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Mytodo
from .forms import TodoForm


# Create your views here.
from .models import *
from .forms import CreateUserForm

def loginpage(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'BetterBarcodeApp/login.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'BetterBarcodeApp/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'BetterBarcodeApp/Dashboard.html')

def studentinput(request):
    return render(request, 'BetterBarcodeApp/Studentinput.html')

def scanner(request):
    return render(request, 'BetterBarcodeApp/Scanner.html')

def alltodos(request):
    tasks = Mytodo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'BetterBarcodeApp/alltodo.html', {'tasks': tasks, 'form': form})

def deleteItem(request, pk):
    task = Mytodo.objects.get(id = pk)
    task.delete()
    return redirect('alltodo')

def updateItem(request, pk):
    todo = Mytodo.objects.get(id=pk)
    updateForm = TodoForm(instance = todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance = todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltodo')
    return render(request, 'BetterBarcodeApp/updateItem.html', {'todo':todo, 'updateform': updateForm})

