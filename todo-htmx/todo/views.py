from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

# Create your views here.


def index(request):
    todos = Task.objects.all()
    context = {"todos": todos}
    return render(request, "todo/index.html", context)


def create(request):
    if request.POST.get("todo_id"):
        todo_id = request.POST.get("todo_id")
        todo = Task.objects.get(id=todo_id)
        todo.title = request.POST.get("todo")
        todo.save()
    else:
        todo_name = request.POST.get("todo")
        todo = Task.objects.create(title=todo_name)
    todos = Task.objects.all()
    context = {"todos": todos}
    return render(request, "todo/index.html", context)


def edit(request, pk):
    todo = Task.objects.get(id=pk)
    print(todo.title)
    return HttpResponse(
        f"""
                        <input type="hidden" value="{todo.id}" name="todo_id" />
                        <input type="text" name="todo" value="{todo.title}" id="input" placeholder="Введите название задания" required />
                        """
    )


def delete(request, pk):
    todo = Task.objects.get(id=pk)
    
    todo.delete()
    todos = Task.objects.all()
    context = {"todos": todos}
    return render(request, "todo/index.html", context)

def status(request, pk ):
    todo = Task.objects.get(id=pk)
    todo.completed = not todo.completed
    todo.save()
    todos = Task.objects.all()
    context = {"todos": todos}
    return render(request, "todo/index.html", context)