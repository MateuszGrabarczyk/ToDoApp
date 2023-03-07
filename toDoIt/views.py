from django.shortcuts import render
from django.http import HttpResponse

from toDoIt.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "toDoIt/index.html", {'tasks':tasks})
