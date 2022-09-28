import datetime
from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import TaskForm
from todolist.models import Task


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!'
            )
            return redirect('todolist:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todos'))
            response.set_cookie('username', username)
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau password salah!')
    context = {}
    return render(request,'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_todos(request):
    data = Task.objects.filter(user = request.user)
    context = {'username': request.COOKIES['username'],
               'last_login': request.COOKIES['last_login'],
               'todos': data,
              }
    return render(request,'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form_listener = form.save(commit=False)
            form_listener.user = request.user
            form_listener.save()
            return HttpResponseRedirect(reverse('todolist:show_todos'))
        else:
            messages.info(request,'Terjadi kesalahan saat menyimpan data!')
    context = {'form': form}
    return render(request, 'create.html',context)

@login_required(login_url='/todolist/login/')
def delete(request, id):
    task = Task.objects.get(
        user = request.user,
        id = id
    )
    task.delete()

    return redirect('todolist:show_todos')