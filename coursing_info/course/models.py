from turtle import mode
from unicodedata import category
from django.db import models

# Create your models here.


class course_category(models.Model):
    category_title=models.CharField(max_length=50)
    def __str__(self):
        return self.category_title

class course(models.Model):
    courses_title=models.CharField(max_length=50)
    courses_online=models.BooleanField()
    course_video=models.CharField(max_length=200)
    courses_date=models.CharField(max_length=100)
    courses_teacher_name=models.CharField(max_length=100)
    course_teacher_rezume=models.CharField(max_length=100)
    course_id=models.IntegerField()
    course_time=models.IntegerField()
    course_targets=models.CharField(max_length=200)
    course_sections=models.CharField(max_length=1000)
    course_learning_manager=models.CharField(max_length=50)
    course_contact_number_1=models.CharField(max_length=50)
    course_contact_number_2=models.CharField(max_length=50)
    course_category=models.ForeignKey(course_category,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.courses_title

