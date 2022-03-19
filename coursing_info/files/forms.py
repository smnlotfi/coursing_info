from django import forms


class ImageForm(forms.Form):
	name = forms.CharField( widget=forms.TextInput(attrs={"class" : "form-control"}),
	label=" فراخوان با چه نامی دخیره شود",)
	image = forms.FileField( widget=forms.FileInput(attrs={"class" : "form-control"}),label=" فایل اکسل مورد نظر را انتخاب کنید")