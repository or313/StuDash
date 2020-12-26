from django.contrib import messages
import django_tables2 as tables
from django_tables2 import SingleTableView
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from grades.forms import NewCourseForm
from django_tables2.utils import A
from django.shortcuts import render, redirect
from grades.models import Grade, Course
from grades.forms import GradeForm


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


def Create_grade(request):
    grades = Grade.objects.select_related('course').filter(course__user=request.user)
    courses = Course.objects.all()
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.course = form.cleaned_data['course']
            obj.grade = form.cleaned_data['grade']
            obj.semester = form.cleaned_data['semester']
            obj.year = form.cleaned_data['year']
            obj.save()
            messages.success(request, "Grade saved successfully")
            return redirect('grades:createGrade')
    else:
        form = GradeForm()
        GPA = CalculateGPA(grades, courses)
        form.fields["course"].queryset = Course.objects.filter(user=request.user)
    return render(request, 'grades/grades.html', {
        'grades': grades,
        'form': form,
        'GPA': GPA,
    })


def CalculateGPA(grades, courses):
    sum = 0
    count = 0
    try:
        for grade in grades:
            for course in courses:
                cred = grade.course.credinitials
            sum += grade.grade * cred
            count += cred
        return(sum / count)
    except ZeroDivisionError:
        print("Zero division error")


def Delete_grade(request, gradeID):
    Grade.removeGrade(gradeID)
    messages.success(request, "Grade Deleted!")
    return redirect('grades:createGrade')
