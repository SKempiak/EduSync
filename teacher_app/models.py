from django.db import models
from django.contrib.auth.models import User


# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add any additional teacher-related fields

class Student(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    @classmethod
    def create_student(cls, teacher, name):
        student = cls(teacher=teacher, name=name)
        student.save()
        return student

class Assignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    text_data = models.TextField()



class Work(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    grade = models.IntegerField(default=100)

    def __str__(self):
        return self.title