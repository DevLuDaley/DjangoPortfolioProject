from django.contrib import admin
from .models import Job

# adding jobs to admin site/page
admin.site.register(Job)
