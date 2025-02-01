from django.urls import path
from .views import students_list, student_detail

urlpatterns = [
    path('', students_list),
    path('<int:student_id>/', student_detail),
]