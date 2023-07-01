from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Teacher, Schedule, Activity

def get_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    data = {
        'id': teacher.id,
        'name': teacher.name,
        'email': teacher.email,
    }
    return JsonResponse(data)

def get_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    data = {
        'id': schedule.id,
        'teacher_id': schedule.teacher.id,
        'date': schedule.date.strftime('%Y-%m-%d'),
    }
    return JsonResponse(data)

def get_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    data = {
        'id': activity.id,
        'schedule_id': activity.schedule.id,
        'name': activity.name,
        'duration': str(activity.duration),
    }
    return JsonResponse(data)
