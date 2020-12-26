from django import forms
from grades.models import Grade


class NewCourseForm(forms.Form):
    course_name = forms.CharField(max_length=100)
    credinitials = forms.IntegerField()


# Create the form class
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('course', 'grade', 'semester', 'year')
