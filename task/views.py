# Django Imports
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

# Own Imports
from task.models import Todo
from task.forms import TodoForm
from task.selectors import get_note


@login_required(login_url="/auth/login/")
def home(request: HttpRequest) -> HttpResponse:
    todos = Todo.objects.only("title", "description")
    return render(request, "task/list-tasks.html", {"todos": todos})


@login_required(login_url="/auth/login/")
def create_todo(request: HttpRequest):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully created todo!")
            return redirect("task:home")

        messages.error(request, "Creation of todo failed!")
        return HttpResponseRedirect()

    return render(request, "task/create-task.html", {"form": form})


@login_required(login_url="/auth/login/")
def view_note(request, pk: int) -> HttpResponse:
    note = get_note(pk)
    return render(request, "task/view-note.html", {"note": note, "pk": pk})


@login_required(login_url="/auth/login/")
def update_note(request, pk):
    note = get_note(pk)
    form = TodoForm(instance=note)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=note)
        if form.is_valid():
            form.save()

            messages.success(request, "Successfully updated todo!")
            return redirect("task:home")

        messages.error(request, "Update of todo failed!")
        return HttpResponseRedirect("task:update_note")
    return render(request, "task/update-note.html", {"form": form})


@login_required(login_url="/auth/login/")
def delete_note(request: HttpRequest, pk: int):
    todo = get_note(pk)
    todo.delete()

    messages.success(request, "Successfully deleted todo!")
    return HttpResponseRedirect("/todos/")
