# Generated by Django 3.2.7 on 2021-11-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('tags', '0001_initial'), ('tags', '0002_alter_tag_name'), ('tags', '0003_auto_20211011_0158'), ('tags', '0004_alter_tag_name'), ('tags', '0005_auto_20211011_0208'), ('tags', '0006_auto_20211011_0211'), ('tags', '0007_alter_tag_name')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
