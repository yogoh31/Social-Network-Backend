# Generated by Django 3.2.7 on 2021-10-10 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
