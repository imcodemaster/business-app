from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profile


class UserRegisterForm(UserCreationForm):
	
	first_name = forms.CharField(max_length = 30 , help_text='Enter First Name ** Middle Name also (if any)')
	last_name = forms.CharField(max_length = 30 , help_text='Enter Last Name')
	email = forms.EmailField(help_text='Enter Your Email to get Activate link ')
	
	

	class Meta:
		model = User
		fields = ["username", "first_name" , "last_name", "email" , "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [ 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta : 
		model = Profile
		fields = [  'image' ,'signature_image', 'company_name' , 'domicile' , 'gender' ,
		 'nationality' ,  'mobile' , 'house_no' , 'address' , 'city' ,
		 'state' , 'postal_code' , 'blood_group' , 'skill' ]

