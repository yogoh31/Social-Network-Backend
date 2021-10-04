# Generated by Django 3.2.7 on 2021-10-04 17:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_userfollowing'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('user', 'following_user')},
        ),
    ]
