from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Course

def courses_list(request):
    courses = list(Course.objects.values())
    return JsonResponse(courses, safe=False)

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return JsonResponse({
        "id": course.id,
        "title": course.title,
        "text": course.text,
        "author": course.author,
    })

