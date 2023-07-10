# Django Imports
from django.db import models


class Todo(models.Model):
    """Database schema for todos table."""

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Todos"
        db_table = "todos"
        ordering = ["-date_created"]
