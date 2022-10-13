from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class course_tbl(models.Model):
    course_name = models.CharField(max_length=225)
    fee = models.IntegerField()

    def __str__(self):
        return self.course_name

class student_tbl(models.Model):
    course = models.ForeignKey(course_tbl, on_delete=models.CASCADE, null=True)
    student_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    joining_date=models.DateField()
    phone_number=models.CharField(max_length=12)

    def __str__(self):
        return self.student_name

class staff_tbl(models.Model):
    staff=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    staff_address=models.CharField(max_length=255)
    gender=models.CharField(max_length=150)
    staff_phone=models.CharField(max_length=12)
    image = models.ImageField(upload_to="image/", null=True)

    def __str__(self):
        return self.image