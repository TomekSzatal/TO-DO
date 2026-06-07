from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from To_Do_app.forms import TaskForm
from To_Do_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("To_Do_app:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("To_Do_app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("To_Do_app:task-list")


def toggle_status(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk)
        task.accepted = not task.accepted
        task.save()
    return redirect("To_Do_app:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("To_Do_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("To_Do_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("To_Do_app:tag-list")