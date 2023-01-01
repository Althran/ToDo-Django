from django.forms import ModelForm, TextInput

from .models import TaskTodo


class AddTasksFrom(ModelForm):
    class Meta:
        model = TaskTodo
        fields = ('text', )
        widgets = {
            'text': TextInput(
                attrs={
                    'name': 'text',
                    'id': 'text',
                    'type': 'text',
                    'placeholder': 'Enter task here',
                    'required': True
                }
            )
        }
