from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from toDoIt.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "toDoIt/index.html", {'tasks':tasks})

class TaskDetail(DetailView):
	model = Task

class TaskCreate(CreateView):
	model = Task
	fields = ['title', 'description']
	success_url = reverse_lazy('tasks')
	template_name = "toDoIt/task_create.html"

class TaskUpdate(UpdateView):
	model = Task
	fields = ['title', 'description', 'active']
	success_url = reverse_lazy('tasks')
	template_name = "toDoIt/task_update.html"

class TaskDelete(DeleteView):
	model = Task
	context_object_name = 'task'
	success_url = reverse_lazy('tasks')
	template_name = "toDoIt/task_delete.html"