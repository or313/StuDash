from django import forms


class NewCourseForm(forms.Form):
    course_name = forms.CharField(max_length=100)
    credinitials = forms.IntegerField()
