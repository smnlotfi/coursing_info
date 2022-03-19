from django.db import models
from django.contrib.auth import get_user_model
user=get_user_model()
# Create your models here.
class course(models.Model):
    courses_title=models.CharField(max_length=50)
    courses_online=models.CharField(max_length=100)
    course_video=models.CharField(max_length=8000)
    course_mashaghel_link=models.CharField(max_length=50,blank=True,null=True)
    courses_date=models.CharField(max_length=100)
    courses_teacher_name=models.CharField(max_length=100)
    course_teacher_rezume=models.CharField(max_length=100)
    course_id=models.IntegerField()
    course_time=models.IntegerField()
    course_targets=models.CharField(max_length=1000)
    course_sections=models.CharField(max_length=1000)
    course_learning_manager=models.CharField(max_length=50)
    course_contact_number_1=models.CharField(max_length=50)
    course_contact_number_2=models.CharField(max_length=50)
    course_whatsapp_number=models.CharField(blank=True,null=True,max_length=50)
    course_category=models.CharField(max_length=50,blank=True,null=True)
    course_image=models.CharField(max_length=200,blank=True,null=True)
    course_writer=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    course_link=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.courses_title


