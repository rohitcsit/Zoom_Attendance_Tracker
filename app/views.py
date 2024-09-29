from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Attendance, Student, UpcomingSession  # Import UpcomingSession model




from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Attendance, Student, UpcomingSession

# Other existing views...



# Login view
def login_view(request):
    if request.method == 'POST':
        id_number = request.POST.get('idNumber')
        password = request.POST.get('password')

        # Try to authenticate user
        try:
            student = Student.objects.get(id_number=id_number)
            if student.password == password:
                request.session['student_id'] = student.id_number  # Store student ID in session
                return redirect('index')  # Redirect to the table page
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        except Student.DoesNotExist:
            messages.error(request, "Student not found.")

    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    if 'student_id' in request.session:
        # Fetch all attendance records from the database
        attendances = Attendance.objects.all()

        # Fetch upcoming sessions from the database
        sessions = UpcomingSession.objects.all()

        # Prepare data for Plotly
        courses = [attendance.course for attendance in attendances]
        conducted_classes = [attendance.conducted_time for attendance in attendances]
        attended_classes = [attendance.Attended_Time for attendance in attendances]

        # Fetch unique courses for the query form
        unique_courses = set(attendance.course for attendance in attendances)  # Get unique course names

        # Pass data to the template
        return render(request, 'index.html', {
            'attendances': attendances,
            'courses': courses,
            'conducted_classes': conducted_classes,
            'attended_classes': attended_classes,
            'sessions': sessions,  # Pass sessions to the template
            'unique_courses': unique_courses,  # Pass unique courses to the template
        })
    else:
        # Redirect to login if not authenticated
        return redirect('login')