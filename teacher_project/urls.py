"""
URL configuration for teacher_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from teacher_app.views import register_teacher, home_view
from teacher_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', register_teacher, name='registration_signup'),
    path('', home_view, name='home'),
    path('teacher-home/', views.teacher_home, name='teacher_home'),
    path('student-widget/', views.student_widget, name='student_widget'),
    path('student-widget/<int:student_id>/', views.student_widget, name='edit_student_widget'),
    path('create-work/<int:student_id>/', views.create_work, name='create_work'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('edit_assignment/<int:assignment_id>/', views.edit_assignment, name='edit_assignment'),
    path('summary/<int:student_id>/', views.summary, name='summary')
]
