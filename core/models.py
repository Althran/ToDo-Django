from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class TaskTodo(models.Model):

    text = models.CharField(
        max_length=250,
        verbose_name='text'
    )

    status = models.BooleanField(
        default=False,
        verbose_name='status'
    )

    date_created = models.DateTimeField(
        default=now,
        verbose_name='date created'
    )

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('tasks')

    class Meta:
        db_table = 'todo_tasks'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ('date_created', )
