# Django Imports
from django import forms

# Own Imports
from task.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "description", "completed")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Title of task",
                    "class": "form-control",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "placeholder": "Description of task",
                    "class": "form-control",
                }
            ),
            "completed": forms.CheckboxInput(
                attrs={
                    "placeholder": "Completed task?",
                    "class": "form-control required checkbox form-control-checkbox",
                }
            ),
        }
