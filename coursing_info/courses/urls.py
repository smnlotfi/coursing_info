from django.urls import path
from .views import index,courses_show,upload_course,logindef,showlinks,exit
from files.views import home

urlpatterns = [
    path('index',index,name='index'),
    path('',logindef,name='login'),
    path('uploading',upload_course,name='uploading'),
    path('upload',home,name='home'),
    path('manage_<str:course_learning_manager>/<str:course_id>',courses_show),
    path('showlinks',showlinks,name='showlinks'),
    path('exit',exit,name='exit'),
]