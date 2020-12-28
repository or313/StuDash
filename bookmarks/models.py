from django.db import models
from grades.models import Course
# descripition- Users are related to certain courses.
# for each course, the user is able to create relevant bookmarks
# each bookmark stores url, name and last visit date in order to enable potential future filtering


class Bookmark (models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    url = models.URLField(max_length=200)
    urlname = models.CharField(max_length=30)
    last_view_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.urlname

    @classmethod
    def add_bookmark(cls, course, url, urlname):
        """Creates new bookmark"""
        bm = Bookmark(course=course, url=url, urlname=urlname)
        bm.save()
        pass

    @classmethod
    def remove_bookmark(cls, bm):
        '''deleted bookmark'''
        bm.delete()
        pass

    @classmethod
    def course_feed(cls):
        """Get the list of bookmarks to display on a Course page
        return: A QuerySet containing all the bookmarks
        ordered from the newest to the oldest added
        """
        return cls.objects.order_by('-last_view_date')
