# Generated by Django 4.1.1 on 2022-10-07 10:52

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
            name='course_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=225)),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('joining_date', models.DateField()),
                ('phone_number', models.CharField(max_length=12)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student_auth_app.course_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='staff_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_address', models.CharField(max_length=255)),
                ('confirm_password', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=150)),
                ('staff_phone', models.CharField(max_length=12)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]