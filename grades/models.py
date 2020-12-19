from django.db import models
from django.conf import settings
# Each user can add, modify or remove course from is list
# Each course contains coures id(default by Django), name, credinitials and grade


class Course (models.Model):
    course_name = models.CharField(max_length=50)
    credinitials = models.IntegerField(default=2)


class Grade(models.Model):
    SEMESTER_NAME = (
        ('A', 'Winter'),
        ('B', 'Spring'),
        ('C', 'Summer'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_student')
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    grade = models.IntegerField(default=0)
    semester = models.CharField(max_length=1, choices=SEMESTER_NAME)
    year = models.IntegerField(default=0)

    @classmethod
    def addGradeUserCourse(cls, user, courseID, grade, semester, year):
        newGrade = Grade.object.create()
        newGrade.user = user
        newGrade.course = courseID
        newGrade.grade = grade
        newGrade.semester = semester
        newGrade.year = year
        return newGrade

    @classmethod
    def removeCourse(cls, courseID):
        Course.object.filter(id=courseID).delete()
        pass


