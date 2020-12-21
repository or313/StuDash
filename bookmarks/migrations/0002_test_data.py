from bookmarks.models import Bookmark
from grades.models import Course
from django.contrib.auth.models import User
from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):

        user1 = User.objects.create_user(username='Ido', password='123456')
        user2 = User.objects.create_user(username='Amit', password='123456789')
        course1 = Course.objects.create(
            course_name='course3', credinitials='3')
        course2 = Course.objects.create(
            course_name='course2', credinitials='3')
        test_data = [
            (user1, course1, 'https://www.google.com', 'Google'),
            (user1, course1, 'https://www.ynet.co.il', 'Ynet'),
            (user1, course2, 'https://www.facebook.com', 'Facebook'),
            (user2, course2, 'https://www.facebook.com', 'Facebook'),
        ]

        with transaction.atomic():
            for user, course, url, urlname in test_data:
                Bookmark(user=user, course=course, url=url, urlname=urlname).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
