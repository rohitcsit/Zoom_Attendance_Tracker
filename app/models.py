from django.db import models

class Student(models.Model):
    id_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords (you can use Django's default hashers)
    
    def __str__(self):
        return self.id_number

class Attendance(models.Model):
    course = models.CharField(max_length=100)
    date = models.DateField()
    conducted_time = models.FloatField()
    Attended_Time = models.FloatField()

    def __str__(self):
        return f"{self.course} on {self.date}"

class UpcomingSession(models.Model):
    course = models.CharField(max_length=100)
    session_date = models.DateField()
    duration = models.FloatField()  # Duration in hours
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return f"{self.course} - {self.session_date}"
