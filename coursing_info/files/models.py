from django.db import models
import os

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.name}{ext}"
    return f"{final_name}"




class First(models.Model):
	name = models.CharField(max_length=100)
	image = models.FileField(upload_to=upload_image_path)

    