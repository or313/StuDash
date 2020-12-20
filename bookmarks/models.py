from django.db import models
from django.contrib.auth.models import User
from grades.models import Course
# descripition- Users are related to certain courses.
# for each course, the user is able to create relevant bookmarks
# each bookmark stores url, name and last visit date in order to enable potential future filtering


class Bookmark (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='SOME STRING')
    url = models.URLField(max_length=200)
    urlname = models.CharField(max_length=30)
    last_view_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.urlname
