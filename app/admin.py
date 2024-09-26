from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'date', 'time', 'conducted_class_time')  # Updated list_display
    search_fields = ('course',)  # You can customize this as needed

admin.site.register(Attendance, AttendanceAdmin)
