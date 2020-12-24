from django.urls import path
from grades.views import deleteCourse
from grades.views import CourseList



app_name = 'grades'

urlpatterns = [
    path("", CourseList.as_view(), name="courseList"),
    path('delete/<str:pk>/', deleteCourse, name='deleteCourse'),
]
