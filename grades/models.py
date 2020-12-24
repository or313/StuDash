from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator



class Course (models.Model):
    course_name = models.CharField(max_length=50,unique=True)
    credinitials = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )

    @classmethod
    def addNewCourse(cls, name, credinitials):
        newCourse = Course.objects.create()
        newCourse.course_name = name
        newCourse.credinitials = credinitials
        newCourse.save()
        pass

class Grade(models.Model):
    SEMESTER_NAME = (
        ('A', 'Winter'),
        ('B', 'Spring'),
        ('C', 'Summer'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='%(class)s_student', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, null=True, blank=True)
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

