# Django Imports
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User

# Own Imports
from accounts.forms import UserRegisterForm, AuthenticationForm


def user_register(request: HttpRequest) -> HttpResponse:
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # get fields from form
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # create and save user to database
            user: User = User.objects.create_user(
                username=username, password=password
            )
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect("accounts:login")

        messages.error(request, "Account creation failed!")
        return redirect("accounts:register")

    return render(request, "accounts/sign-up.html", {"form": form})


def user_login(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(None, request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
                messages.success(
                    request, f"Welcome {username}, you are logged in."
                )
                return redirect("task:home")
            messages.error(request, "User login failed!")
            return redirect("accounts:login")

    elif request.method == "GET":
        if request.user.is_authenticated:
            return redirect("task:home")

        return render(request, "accounts/login.html", {"form": form})
