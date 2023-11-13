from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import TeacherRegistrationForm, StudentForm, WorkForm
from .models import Student, Assignment, Work
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

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    assignments = Assignment.objects.filter(student=student)

    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.student = student
            assignment.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = WorkForm()

    return render(request, 'student_detail.html', {'student': student, 'assignments': assignments, 'form': form})


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    works = Work.objects.filter(student=student)

    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.student = student
            work.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = WorkForm()

    return render(request, 'student_detail.html', {'student': student, 'works': works, 'form': form})

    return render(request, 'student_detail.html', {'student': student, 'works': works, 'form': form})

def edit_assignment(request, assignment_id=None, student_id=None):
    student = get_object_or_404(Student, id=student_id) if student_id else None
    work = get_object_or_404(Work, id=assignment_id) if assignment_id else None

    if request.method == 'POST':
        form = WorkForm(request.POST, instance=work)
        if form.is_valid():
            work = form.save(commit=False)
            work.student = student
            work.save()
            return redirect('student_detail', student_id=student.id)
    else:
        # If assignment_id is None, initialize an empty form for creating a new work
        form = WorkForm(instance=work) if work else WorkForm()

    return render(request, 'edit_assignment.html', {'form': form, 'work': work})