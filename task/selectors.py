# Django Imports
from django.http import Http404
from django.contrib.auth.models import User

# Own Imports
from task.models import Todo


def get_note(note_id: int, user: User) -> Todo:
    """
    This selector function raises a 404 exception
    if a note is not found, otherwise return the note.

    :param note_id: The id of the note
    :type note_id: int

    :return: The note
    :rtype: Todo
    """
    try:
        note = Todo.objects.get(id=note_id, user=user)
    except Todo.DoesNotExist:
        raise Http404("Not does not exist!")
    return note
