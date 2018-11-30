from django.shortcuts import render
from .forms import TodoForm
from .models import Todo
from django.shortcuts import redirect

# Create your views here.
def add_todo(request):
    if request.method == 'POST':
        todo = Todo(user_id = request.user)
        form = TodoForm(request.POST, instance=todo)
        form.save()
        return redirect('/all-todos')
    else:
        form = TodoForm
    return render(request, 'todo/add-todo.html', {'form': form})


def show_all_todos(request):
    todos = Todo.objects.filter(user_id = request.user.id)
    context = {'todos' : todos}
    return render(request, 'index.html' , context)


def edit_todo(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        form.save()
        return redirect('/all-todos')
    else:
        form = TodoForm(instance = todo)
    context = {'form' : form}
    return render(request, 'todo/edit-todo.html', context)

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    return redirect('/all-todos')

def home(request):
    return render(request, 'frontpage.html', {})

