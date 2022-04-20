from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from doit.forms import TaskForm
from doit.models import Tag, Task


def index(request):
    return render(request, "doit/task_list.html")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("doit:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("doit:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("doit:tag-list")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "doit/task_list.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "doit/task_form.html"
    success_url = reverse_lazy("doit:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "doit/task_form.html"
    success_url = reverse_lazy("doit:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    template_name = "doit/task_confirm_delete.html"
    success_url = reverse_lazy("doit:task-list")
