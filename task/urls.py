# Django Imports
from django.urls import path

# Own Imports
from task import views


app_name = "task"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_todo, name="create_note"),
    path("<int:pk>/", views.view_note, name="view_note"),
    path("<int:pk>/edit/", views.update_note, name="edit_note"),
    path("<int:pk>/delete/", views.delete_note, name="delete_note"),
]
