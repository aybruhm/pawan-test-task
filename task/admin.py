# Django Imports
from django.contrib import admin

# Own Imports
from task.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "date_created")
    list_filter = ("completed", "date_created")
