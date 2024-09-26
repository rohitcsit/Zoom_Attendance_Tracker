from django.db import models

class Attendance(models.Model):
    course = models.CharField(max_length=100)
    date = models.DateField()
    conducted_class_time = models.FloatField(default=0)  # Default value added
    time = models.FloatField()

    def __str__(self):
        return f"{self.course} on {self.date}"
