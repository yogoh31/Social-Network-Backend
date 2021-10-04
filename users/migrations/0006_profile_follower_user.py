# Generated by Django 3.2.7 on 2021-10-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_privacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follower_user',
            field=models.ManyToManyField(related_name='followers', to='users.Profile'),
        ),
    ]