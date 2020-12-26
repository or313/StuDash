from django.urls import path
from grades.views import deleteCourse
from grades.views import CourseList
from grades.views import Delete_grade
from grades.views import Create_grade


app_name = 'grades'

urlpatterns = [
    path("", CourseList.as_view(), name="courseList"),
    path('delete/<str:pk>/', deleteCourse, name='deleteCourse'),
    path('Create_grade/', Create_grade, name='createGrade'),
    path('Delete_grade/<int:gradeId>/', Delete_grade, name='deleteGrade'),
]
