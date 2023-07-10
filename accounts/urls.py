from django.urls import path
from .views import (
    user_register,
    user_login,
)

app_name = "accounts"

urlpatterns = [
    path("register/", user_register, name="register"),
    path("login/", user_login, name="login"),
]
