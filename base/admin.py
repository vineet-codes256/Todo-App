from django.contrib import admin
from .models import Task

admin.site.register(Task)
# Compare this snippet from todo_list/base/urls.py:
