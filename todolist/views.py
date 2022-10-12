import datetime
from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from todolist.models import Task
from todolist.forms import TaskForm


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
    return render(request,'todolist_ajax.html', context)

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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
@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user=user, 
            title=title, 
            description=description
        )
        return JsonResponse({
            'error': False, 
            'msg':'Successful'
        })

@login_required(login_url='/todolist/login/')
def delete(request, id):
    # task = Task.objects.get(
    #     user = request.user,
    #     id = id
    # )
    # task.delete()
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=id, user=request.user)
        task.delete()

    # return redirect('todolist:show_todos')
    return JsonResponse({'error': False})

@login_required(login_url='/todolist/login/')
def update(request, id):
    # task = Task.objects.get(
    #     user = request.user,
    #     id = id
    # )
    # task.is_finished = not task.is_finished
    # task.save()
    # return redirect(
    #     'todolist:show_todos'
    # )
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=id, user=request.user)
        task.is_finished = not task.is_finished
        task.save()

        return JsonResponse({'error': False})