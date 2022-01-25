from django.shortcuts import render
from .models import course,course_category

# Create your views here.

def index(request):
    return render(request,'course/index.html')

def course(request,*args, **kwargs):
    category=kwargs['category']
    title=kwargs['title']
    context={
        "category":category,
        'title':title
    }
    return render(request,'course.html',context)