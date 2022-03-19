from django.http import HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import course
from openpyxl.descriptors.base import Length
from openpyxl import Workbook
from openpyxl import load_workbook,worksheet
from django.contrib.auth.models import User
import os


# Create your views here.
@login_required(login_url='login')
def index(request):
    return redirect('home')

def courses_show(request,*args,**kwargs):
    course_id=kwargs['course_id']
    course_learning_manager=kwargs['course_learning_manager']
    selected_course=course.objects.filter(course_id=course_id,course_learning_manager=course_learning_manager).first()
    context={
        'course':selected_course,
    }
    return render(request,'course.html',context)


@login_required(login_url='login')
def upload_course(request):
    context={}
    if (request.POST or None):
        file_name=request.POST['file_name']     
        if os.path.exists(f'media/{file_name}.xlsx')==True:
            wb=Workbook()
            wb = load_workbook(filename = f'media/{file_name}.xlsx')
            sheet = wb['Sheet1']
            sheetlenght=len(sheet['A'])
            l=2
            data=[]
            links=[]
            while l<=sheetlenght:
                createcourse=course.objects.create(
                courses_title=sheet['A'+str(l)].value,
                courses_online=sheet['B'+str(l)].value,
                course_video=sheet['C'+str(l)].value,
                course_mashaghel_link=sheet['D'+str(l)].value,
                courses_date=sheet['E'+str(l)].value,
                courses_teacher_name=sheet['F'+str(l)].value,
                course_teacher_rezume=sheet['G'+str(l)].value,
                course_id=sheet['H'+str(l)].value,
                course_time=sheet['I'+str(l)].value,
                course_targets=sheet['J'+str(l)].value,
                course_sections=sheet['K'+str(l)].value,
                course_learning_manager=sheet['L'+str(l)].value,
                course_contact_number_1=sheet['M'+str(l)].value,
                course_contact_number_2=sheet['N'+str(l)].value,
                course_whatsapp_number=sheet['O'+str(l)].value,
                course_category=sheet['P'+str(l)].value,
                course_image=sheet['Q'+str(l)].value,
                course_writer=request.user
                
            )
                data.append(createcourse)
                links.append(sheet['P'+str(l)].value+'/'+sheet['A'+str(l)].value+'/'+str(sheet['H'+str(l)].value))
                context={
                    'msg':'فراخوان ها با موفقیت ایجاد شده اند.'
                }
                l=l+1 
            return redirect('showlinks')
        else:
         context={
            'msg':'فایل مورد نظر یافت نشد'
            } 

    return render(request,'uploading.html',context)


def logindef(request):
   if request.user.is_authenticated:
        return redirect('home')
   else:
    msg=''
    if(request.POST or None):
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request,User)
            msg='شما با موفقیت وارد شدید'  
            return redirect('home')          
        else:
            msg='نام کاربری یا رمز ورود اشتباه میباشد!'

    context={
        'msg':msg
    }
    return render(request,'login.html',context)


def exit(request):
    if request.user.is_authenticated:
        logout(request)
        print(request.user)
    return redirect('login')




def showlinks(request):
    selectallcourse=course.objects.all()
    print(selectallcourse)
    context={
        'courses':selectallcourse
    }
    return render(request,'showlinks.html',context)