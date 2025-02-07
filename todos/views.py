from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm

# GET todos/ (Список задач)
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todolist.html', {'todos': todos})

# GET todos/:id (Детали задачи)
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/tododetail.html', {'todo': todo})

# POST todos/ (Добавление задачи)
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todoform.html', {'form': form})

# DELETE todos/:id/delete (Удаление задачи)
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')
