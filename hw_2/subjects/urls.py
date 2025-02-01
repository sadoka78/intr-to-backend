
from django.urls import path
from .views import courses_list, course_detail

urlpatterns = [
    path('', courses_list),
    path('<int:course_id>/', course_detail),
]