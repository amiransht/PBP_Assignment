from django.urls import path
from todolist.views import delete, register, login_user, logout_user, show_todos, create, delete, update

app_name = 'todolist'

urlpatterns = [
    path('', show_todos, name='show_todos'),
    path('create/', create,  name='create'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<str:id>/', delete, name="delete"),
    path('update/<str:id>/', update, name="update"),
    
]
