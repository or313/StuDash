import pytest
from django.db.models.query import QuerySet
from bookmarks.models import Bookmark
from django.contrib.auth.models import User
from grades.models import Course


@pytest.mark.django_db
class TestBookmark:
    def test_course_feed(cls):
        '''
        this function tests the bookmarks displayed on the course page
        '''
        out = Bookmark.course_feed()
        assert isinstance(out, QuerySet)
        assert all(isinstance(b, Bookmark) for b in out)
        assert list(out.values_list('user', 'course', 'url', 'urlname')) == [
            (2, 2, 'https://www.facebook.com', 'Facebook'),
            (1, 2, 'https://www.facebook.com', 'Facebook'),
            (1, 1, 'https://www.ynet.co.il', 'Ynet'),
            (1, 1, 'https://www.google.com', 'Google'),
        ]

    def test_add_bookmark(cls):
        course = Course.objects.create(
            course_name="intro 101", credinitials="3")
        user = User.objects.create_user(username='john', password='johnpassword')
        user.save()
        course.save()
        Bookmark.add_bookmark(user, course, 'https://www.youtube.com', 'Youtube')
        new = Bookmark.objects.filter(urlname='Youtube')
        assert list(new.values_list('user', 'course', 'url', 'urlname')) == [
            (3, 3, 'https://www.youtube.com', 'Youtube'),
        ]

    def test_remove_bookmark(cls):
        d = Bookmark.objects.get(pk=1)
        Bookmark.remove_bookmark(d)
        new = Bookmark.objects.all()
        assert list(new.values_list('user', 'course', 'url', 'urlname')) == [
            (1, 1, 'https://www.ynet.co.il', 'Ynet'),
            (1, 2, 'https://www.facebook.com', 'Facebook'),
            (2, 2, 'https://www.facebook.com', 'Facebook')
        ]
