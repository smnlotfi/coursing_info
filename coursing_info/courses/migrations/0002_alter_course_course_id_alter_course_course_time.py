# Generated by Django 4.0.3 on 2022-04-07 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_time',
            field=models.CharField(max_length=100),
        ),
    ]
