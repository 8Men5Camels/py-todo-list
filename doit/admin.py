from django.contrib import admin

from doit.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_time", "deadline", "done"]
    list_filter = ("done",)
    search_fields = ("content",)


admin.site.register(Tag)
