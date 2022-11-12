
#from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile


# class UserCreationFormss(UserCreationForm):
#     username= forms.CharField(label='الاسم ')
#     first_name= forms.CharField(label='الاسم الاول')
#     last_name= forms.CharField(label='الاسم الاخير')
#     email= forms.EmailField(label='البريد الالكتروني')
#     password1= forms.CharField(label='كلمة السر',widget=forms.PasswordInput(),min_length=8)
#     password2= forms.CharField(label='ناكيد كلمة السر ',widget=forms.PasswordInput(),min_length=8)

#     class Meta :
#         model = User
#         feilds = ('username','first_name','last_name','email','password1','password2')


class Login_Form(forms.Form):
    username = forms.CharField(label='الاسم')
    password = forms.CharField(label='كلمة المرور',widget=forms.PasswordInput())
    class Meta :
        model = User
        feilds = ('username','password')


class UpdateUserForm(forms.ModelForm):
    first_name= forms.CharField(label='الاسم الاول')
    last_name= forms.CharField(label='الاسم الاخير')
    email= forms.EmailField(label='البريد الالكتروني')
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email')

class UpdateProfile(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('name','subtitle', 'address',
                'address_detail','number_phone', 'working_hours',
                'waiting_time','who_i', 'price',
                'facebook','twitter', 'google',
                'type_of_person','doctor', 'image',
                'Specialist_doctor')        