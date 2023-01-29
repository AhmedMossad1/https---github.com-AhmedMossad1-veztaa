from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import Login_Form, UpdateUserForm ,UpdateProfile,UserCForms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def doctors_list(request):
    #query Set
    doctors = User.objects.all()
    return render(request ,'user/doctors_list.html', {'doctors':doctors})


def doctors_detail(request,slug):
    #query Set
    doctors_detail = Profile.objects.get(slug = slug)
    return render(request ,'user/doctors_detail.html', {'doctors_detail':doctors_detail})   

def user_login (request):
    if request.method == 'POST':
        form=Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username = username , password = password )
        if user is not None :
            login(request,user)
            return redirect('account:doctors_list')
    else:        
        form =Login_Form()

    return render(request ,'user/login.html', {'form':form})    


def user_signup(request):
    if request.method == 'POST':
        form = UserCForms(request.POST)
        if form.is_valid():
             # Create a new user object but avoid saving it yet
            new_user = form.save(commit = False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
           #Profile.objects.create(user=new_user)
            # username = form.cleaned_data.get('username')
            # password =form.cleaned_data.get('password')
            # user = authenticate(username = username , password = password )
            return render(request,'user/register_done.html',{'new_user': new_user})
    else:       
            form = UserCForms()
    return render(request,'user/signup.html',{'form': form})

    #         login(request,user)
    #         return redirect('account:doctors_list')
    # else:        
    #     form =UserCForms()

    # return render(request ,'user/signup.html', {'form':form})    


@login_required(login_url='account:login')
def myprofile (request):
    return render(request ,'user/myprofile.html', {})


@login_required
def update_profile (request):
    if request.method == 'POST':
        user_form = UpdateUserForm(instance=request.user , data=request.POST)
        profile_form = UpdateProfile(instance=request.user.profile , data=request.POST)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('account:myprofile')

    else:
        user_form = UpdateUserForm(instance=request.user)  
        profile_form =UpdateProfile(instance=request.user.profile)      

    return render(request ,'user/update_profile.html', {'user_form':user_form , 'profile_form':profile_form ,})
