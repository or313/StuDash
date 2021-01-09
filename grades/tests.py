import pytest
from grades.models import Grade, Course
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestGrade:
    def test_addGradeUserCourse(cls):
        user3 = User.objects.create_user(username="idan", password="123456")
        c = Course.addCourse(user=user3, course_name="NLP", credinitials="3")
        Grade.addGradeUserCourse(c, 90, 'A', 2021)
        out = Grade.objects.filter(semester='A')
        assert list(out.values_list('course', 'grade', 'semester', 'year')) == [
            (3, 90, 'A', 2021)
        ]

    def test_removeGrade(cls):
        user3 = User.objects.create_user(username="idan", password="123456")
        c = Course.addCourse(user=user3, course_name="NLP", credinitials="3")
        Grade.addGradeUserCourse(c, 50, 'B', 2020)
        Grade.removeGrade(2)
        out = Grade.objects.all()
        assert list(out.values_list('course', 'grade', 'semester', 'year')) == [
            (3, 50, 'B', 2020),
        ]


@pytest.mark.django_db
class TestCourse:
    def test_addCourse(cls):
        user4 = User.objects.create_user(username="noa", password="123456")
        Course.addCourse(user=user4, course_name="java", credinitials="3")
        out = Course.objects.filter(credinitials='3')
        assert list(out.values_list('user', 'course_name', 'credinitials')) == [
            (1, 'course3', 3),
            (2, 'course2', 3),
            (5, 'java', 3),
        ]

    def test_removeCourse(cls):
        user4 = User.objects.create_user(username="noa", password="123456")
        Course.addCourse(user=user4, course_name="java", credinitials="3")
        Course.removeCourse(3)
        Course.removeCourse(4)
        Course.removeCourse(5)
        out = Course.objects.all()
        assert list(out.values_list('user', 'course_name', 'credinitials')) == [
            (1, 'course3', 3),
            (2, 'course2', 3),

        ]
