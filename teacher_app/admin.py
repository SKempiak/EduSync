from django.contrib import admin

# Register your models here.
from .models import Student, Work

admin.site.register(Student)
admin.site.register(Work)