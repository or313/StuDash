from django.contrib import messages
import django_tables2 as tables
from django_tables2 import SingleTableView
from django.views.generic import TemplateView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from grades.models import Course
from grades.forms import NewCourseForm
from django.http import HttpResponse
from django_tables2.utils import A
from django.shortcuts import redirect





class CourseListTable(tables.Table):
    class Meta:
        model = Course
        exclude = ("id", )
    delete = tables.LinkColumn("grades:deleteCourse", text='Delete', args=[A('id')], attrs={'a': {'class': 'btn'}})



def deleteCourse(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect("grades:courseList")



class CourseList(LoginRequiredMixin,SingleTableView ,FormView):
    login_url = '/accounts/log-in'
    model = Course
    template_name = "course_list.html"
    form_class = NewCourseForm
    table_class = CourseListTable
    success_url = "/courses"

    def form_valid(self, form):
        user = self.request.user
        newCourse = Course()
        newCourse.course_name = form.cleaned_data["course_name"]
        newCourse.credinitials = form.cleaned_data["credinitials"]
        newCourse.save()

        messages.success(self.request, "Course was added succesfuly")

        return super(CourseList, self).form_valid(form)

