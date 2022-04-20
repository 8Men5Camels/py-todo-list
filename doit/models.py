from django.db import models
from django.views import generic


class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=500)
    created_time = models.TimeField(auto_now_add=True)
    deadline = models.TimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to="Tag", related_name="tasks")

    class Meta:
        ordering = ["created_time"]

    def __str__(self):
        return f"{self.content}: {self.created_time} - {self.deadline} - {self.done}"
