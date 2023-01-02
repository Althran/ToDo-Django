from django.views.generic import ListView, DeleteView, UpdateView, DetailView

from .forms import AddTasksFrom
from .models import TaskTodo


class ContextMixin:
    context = {
        'site_title': 'ToDo Django',
    }


class TaskView(ContextMixin, DetailView):
    model = TaskTodo
    template_name = 'core/task_page.html'
    context_object_name = 'addtask'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskView, self).get_context_data()
        context.update(self.context)
        return context


class MainView(ContextMixin, ListView):
    model = TaskTodo
    template_name = 'core/main_page.html'
    context_object_name = 'tasks'
    form_class = AddTasksFrom

    def get_queryset(self):
        return TaskTodo.objects.all()

    def get(self, request, *args, **kwargs):
        return super(MainView, self).get(request=request)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        context['add_tasks_form'] = AddTasksFrom()
        return context

    def post(self, request):
        form = AddTasksFrom(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request=request)


class DeleteTaskView(DeleteView):
    model = TaskTodo
    success_url = '/'
    template_name = 'core/task_delete.html'


class UpdateTaskView(UpdateView):
    model = TaskTodo
    fields = ['status']
    template_name = 'core/status_update_form.html'


class EditTaskView(UpdateView):
    model = TaskTodo
    fields = ['text']
    template_name = 'core/update_form.html'
