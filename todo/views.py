from django.shortcuts import render
from .models import Todo
from .forms import TodoForm


def create_todo(request):
    form = TodoForm()
    if request.method == "POST":
        print(request.POST)

    return render(request, "todo/create-todo.html", {"form": form})


# Create your views here.
def todo(request):
    # all,get,filter
    # todos = Todo.objects.all()
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)

    return render(request, "todo/todo.html", {"todos": todos})


def view_todo(request, id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)

    return render(request, "todo/view-todo.html", {"todos": todo})
