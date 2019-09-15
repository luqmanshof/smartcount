from django.shortcuts import render,redirect
from smartsetup.forms import (
    SignUpForm,
    EditProfileForm
)
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from smartsetup.models import UserProfile

@login_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'smartsetup/signup.html',{'form':form})

@login_required
def list_signup(request):
    users = User.objects
    return render(request, 'smartsetup/list_signup.html',{'users':users})

@login_required
def edit_signup(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            # return redirect('home')
            users = User.objects
            return render(request, 'smartsetup/list_signup.html',{'users':users})

    else:
        form = EditProfileForm(instance=request.user)
        userprofiles = UserProfile.objects.all()
        args = {'form':form,'userprofiles':userprofiles}
        return render(request,'smartsetup/edit_signup.html',args)

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = PasswordChangeForm()
#         return render(request,'registration/change_password.html',{'form':form})
