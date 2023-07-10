# Django Imports
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Own Imports
from task.models import Todo
from task.forms import TodoForm
from task.selectors import get_note


@login_required(login_url="/auth/login/")
def home(request: HttpRequest) -> HttpResponse:
    todo_list = Todo.objects.only("title", "description").filter(
        user=request.user
    )

    paginator = Paginator(todo_list, 2)
    page = request.GET.get("page", 1)

    try:
        todos = paginator.page(page)
    except PageNotAnInteger:
        todos = paginator.page(1)
    except EmptyPage:
        todos = paginator.page(paginator.num_pages)

    return render(
        request,
        "task/list-tasks.html",
        {"todos": todos, "page": page},
    )


@login_required(login_url="/auth/login/")
def create_todo(request: HttpRequest):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()

            messages.success(request, "Successfully created todo!")
            return redirect("task:home")

        messages.error(request, "Creation of todo failed!")
        return HttpResponseRedirect()

    return render(request, "task/create-task.html", {"form": form})


@login_required(login_url="/auth/login/")
def view_note(request: HttpRequest, pk: int) -> HttpResponse:
    note = get_note(pk, request.user)
    return render(request, "task/view-note.html", {"note": note, "pk": pk})


@login_required(login_url="/auth/login/")
def update_note(request: HttpRequest, pk: int):
    note = get_note(pk, request.user)
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
    todo = get_note(pk, request.user)
    todo.delete()

    messages.success(request, "Successfully deleted todo!")
    return HttpResponseRedirect("/todos/")
