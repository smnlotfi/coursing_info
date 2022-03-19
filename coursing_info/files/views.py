from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import First

@login_required(login_url='login')
def home(request):
	infos = First.objects.all()
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			First(name=form.cleaned_data['name'], image=(request.FILES['image'])).save()
			return redirect('uploading')
	else:
		form = ImageForm()
	return render(request, 'upload.html', {'form':form, 'infos':infos})