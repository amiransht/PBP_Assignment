from unicodedata import name
from django.urls import path
from todolist.views import delete, register, login_user, logout_user, show_todos, create, delete, update, show_json, create_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todos, name='show_todos'),
    path('create/', create,  name='create'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>/', delete, name="delete"),
    path('update/<int:id>/', update, name="update"),
    path('json/', show_json, name="show_json"),
    path('add/', create_ajax, name="create_ajax"),
]
