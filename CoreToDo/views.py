from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm   
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login
from .models import *

from .forms import *
# Create your views here.

# def loginTask(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user.is_authenticated:


#     return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        userform = CreateUserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('/')
    else:
        userform = CreateUserForm()

    context = {'userform': userform}
    return render(request, 'register.html', context)

@login_required
def index(request):
    #return HttpResponse("Hello World")
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')
        
    context = {'tasks':tasks, 'form':form}

    return render(request, 'list.html', context)

@login_required
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task) #'instance=task' will show the current list to be updated in new page

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}

    return render(request, 'update_task.html', context)

@login_required
def delete(request,pk):

    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'delete.html', context)