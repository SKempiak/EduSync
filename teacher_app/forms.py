from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TeacherRegistrationForm(UserCreationForm):
    # Add any additional fields you need for teacher registration
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

from .models import Student

from .models import Work

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'description', 'grade']  # Adjust based on your Work model fields
