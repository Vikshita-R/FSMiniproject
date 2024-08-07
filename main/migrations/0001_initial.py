# Generated by Django 5.0.7 on 2024-07-20 13:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CIE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cie', models.IntegerField()),
                ('sub_code', models.CharField(max_length=100)),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=100)),
                ('usn', models.CharField(max_length=100)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(null=True)),
                ('attendance', models.CharField(max_length=50, null=True)),
                ('cie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cie')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
