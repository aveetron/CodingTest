from django.urls import path 
from todo import views

urlpatterns = [
    path('add-todo/', views.add_todo, name='add-todo'),
    path('all-todos/', views.show_all_todos, name='show-all-todos'),
    path('edit-todo/<todo_id>/', views.edit_todo, name='edit-todo'),
    path('delete-todo/<todo_id>/', views.delete_todo, name='delete-todo'),
    path('',views.home , name='home'),
]
