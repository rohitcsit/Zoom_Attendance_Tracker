from django.shortcuts import render
from .models import Attendance

# Create your views here.
def index(request):
    attendances = Attendance.objects.all()
    return render(request, 'index.html', {'attendances': attendances})

