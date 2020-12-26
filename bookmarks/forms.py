from django import forms
from bookmarks.models import Bookmark
from grades.models import Course


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('course', 'url', 'urlname')
        course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label=None)
