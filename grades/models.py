from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Course (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='%(class)s_student', null=True, blank=True)
    course_name = models.CharField(max_length=50)
    credinitials = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.course_name

    @classmethod
    def addCourse(cls, user, course_name, credinitials):
        newCourse = Course()
        newCourse.user = user
        newCourse.course_name = course_name
        newCourse.credinitials = credinitials
        newCourse.save()
        return newCourse

    @classmethod
    def removeCourse(cls, courseID):
        Course.objects.filter(id=courseID).delete()


class Semester(models.TextChoices):
    Winter = 'A',
    Spring = 'B',
    Summer = 'C'


class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0)
    semester = models.CharField(max_length=1, choices=Semester.choices)
    year = models.IntegerField(default=0)

    @classmethod
    def addGradeUserCourse(cls, courseID, grade, semester, year):
        newGrade = Grade()
        newGrade.course = courseID
        newGrade.grade = grade
        newGrade.semester = semester
        newGrade.year = year
        newGrade.save()
        return newGrade

    @classmethod
    def removeGrade(cls, gradeID):
        Grade.objects.filter(id=gradeID).delete()
