from django.contrib import admin
from .models import Attendance, Student, UpcomingSession  # Import the new UpcomingSession model

# Customize the display for the Attendance model
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'date', 'conducted_time', 'Attended_Time')
    search_fields = ('course',)

# Customize the display for the Student model (optional)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id_number',)

# Customize the display for the UpcomingSession model
class UpcomingSessionAdmin(admin.ModelAdmin):
    list_display = ('course', 'session_date', 'duration')
    search_fields = ('course',)

# Register both models
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(UpcomingSession, UpcomingSessionAdmin)  # Register the UpcomingSession model
