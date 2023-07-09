from django.db import models

class Teacher(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=30)

class Schedule(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

class Activity(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    # picture = models.ImageField(upload_to='activity_pictures/')