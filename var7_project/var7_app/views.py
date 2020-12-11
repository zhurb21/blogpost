from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import CreateUserForm, TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from .filters import TaskFilter

# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request,'Account was created for ' + username)
            return redirect ('login')

    context = {'form': form}
    return render(request, 'var7_app/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'username or password is not correct')

    context = {}
    return render(request, 'var7_app/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['user'])
def userPage(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('user')

    myFilter = TaskFilter(request.GET, queryset = tasks)
    tasks = myFilter.qs
    context = {'tasks': tasks, 'form': form, 'myFilter': myFilter}
    return render(request, 'var7_app/user.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['user'])
def contactPage(request):
    context ={}
    return render(request, 'var7_app/contact.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['user'])
def aboutPage(request):
    context = {}
    return render(request, 'var7_app/about.html', context)

@login_required(login_url = 'login')
@admin_only
def homePage(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('home')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'var7_app/main.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'var7_app/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('home')

    context = {'item': item}
    return render(request, 'var7_app/delete.html', context)