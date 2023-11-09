from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import TeacherRegistrationForm, StudentForm, WorkForm
from .models import Student
from django.contrib.auth.decorators import login_required

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('home')  # Redirect to the home page or any other desired page
    else:
        form = TeacherRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


def home_view(request):
    # Implement the logic for your homepage here
    return render(request, 'home.html')


@login_required
def student_widget(request, student_id=None):
    if student_id:
        student = Student.objects.get(id=student_id)
        if request.method == 'POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('teacher_home')
        else:
            form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            student = Student.create_student(request.user, name)  # Pass the logged-in user as the teacher
            return redirect('teacher_home')
    else:
        form = StudentForm()
    
    return render(request, 'student_widget.html', {'form': form, 'student_id': student_id})


@login_required
def teacher_home(request):
    # Retrieve the students created by the logged-in teacher
    students = Student.objects.filter(teacher=request.user)

    # You can now use the 'students' queryset in your template or perform additional logic

    return render(request, 'teacher_home.html', {'students': students})

@login_required
def create_work(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.student = student
            work.save()
            return redirect('teacher_home')
    else:
        form = WorkForm()

    return render(request, 'create_work.html', {'form': form, 'student': student})