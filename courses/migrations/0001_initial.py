# Generated by Django 4.2.4 on 2023-09-03 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=100, unique=True)),
                ('course_description', models.TextField(max_length=400)),
                ('course_banner', models.ImageField(blank=True, upload_to='photos/courses')),
                ('course_price', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('course_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.department')),
                ('course_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
