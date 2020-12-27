from django.contrib import messages
import django_tables2 as tables
from django_tables2 import SingleTableView
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from grades.models import Course
from grades.forms import NewCourseForm
from django_tables2.utils import A
from django.shortcuts import redirect





class CourseListTable(tables.Table):
    class Meta:
        model = Course
        exclude = ("id", "user")
    delete = tables.LinkColumn("grades:deleteCourse", text='Delete', args=[A('id')], attrs={'a': {'class': 'btn'}})



def deleteCourse(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect("grades:courseList")



class CourseList(LoginRequiredMixin, SingleTableView, FormView):
    login_url = '/accounts/log-in'
    model = Course
    all_data = model.objects.all()
    template_name = "course_list.html"
    form_class = NewCourseForm
    table_class = CourseListTable
    success_url = "/courses"

    def form_valid(self, form):
        user = self.request.user
        newCourse = Course()
        newCourse.course_name = form.cleaned_data["course_name"]
        newCourse.credinitials = form.cleaned_data["credinitials"]
        newCourse.user = user
        newCourse.save()

        messages.success(self.request, "Course was added succesfuly")

        return super(CourseList, self).form_valid(form)

    def get_queryset(self):
        qs = Course.objects.filter(user_id=self.request.user)
        return qs

