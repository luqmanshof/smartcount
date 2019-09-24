from django.shortcuts import render,redirect,get_object_or_404
from smartsetup.forms import (
    SignUpForm,EditProfileForm,UserProfileForm,ChartCategoryForm,
    ChartSubCategoryForm
)
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from smartsetup.models import UserProfile, ChartCategory, ChartSubCategory
from django.forms.models import model_to_dict

@login_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if form.is_valid() and userprofile_form.is_valid():
            # form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            user = form.save()
            user = userprofile_form.save( instance=request.user.userprofile)

            # login immediately with the created user profile
            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect('dashboard')
    else:
        form = SignUpForm()
        userprofile_form = UserProfileForm()
        return render(request,'smartsetup/signup.html',{'form':form,'userprofile_form':userprofile_form})

@login_required
def list_signup(request):
    users = User.objects.all()
    # fields = model_to_dict(user,fields=['username','first_name','last_name','email'])
    fieldCols = ['User Name','First Name','Last Name','E-Mail']
    return render(request, 'smartsetup/list_signup.html',{'fieldCols':fieldCols,'users':users})
    # return render(request, 'smartsetup/form_list.html',{'fieldCols':fieldCols,'fields':fields})

@login_required
def edit_signup(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        userprofile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        # userprofile_obj = UserProfile.objects.all()

        if form.is_valid() and userprofile_form.is_valid():
            form.save()
            userprofile_form.save()
            # return redirect('home')
            users = User.objects
            return render(request, 'smartsetup/list_signup.html',{'users':users})
    else:
        user = request.user
        form = EditProfileForm(instance=user)
        userprofile_form = UserProfileForm(instance=user.userprofile)
        # form = EditProfileForm(instance=request.user)
        # userprofile_form = UserProfileForm(instance=request.user.userprofile)

        args = {'form':form,'userprofile_form':userprofile_form}
        return render(request,'smartsetup/edit_signup.html',args)

@login_required
@permission_required('smartsetup.can_change_user_profile', raise_exception=True)
def edit_signup_with_pk(request, pk=None):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        userprofile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        # userprofile_obj = UserProfile.objects.all()

        if form.is_valid() and userprofile_form.is_valid():
            form.save()
            userprofile_form.save()
            # return redirect('home')
            users = User.objects
            return render(request, 'smartsetup/list_signup.html',{'users':users})

    else:
        if pk:
            user = User.objects.get(pk=pk)
        else:
            user = request.user
        form = EditProfileForm(instance=user)
        userprofile_form = UserProfileForm(instance=user.userprofile)
        # form = EditProfileForm(instance=request.user)
        # userprofile_form = UserProfileForm(instance=request.user.userprofile)

        args = {'form':form,'userprofile_form':userprofile_form}
        return render(request,'smartsetup/edit_signup.html',args)

@login_required
def chartcategory(request):
    if request.method == 'POST':
        form = ChartCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_chartcategory')
    else:
            form = ChartCategoryForm()
    return render(request,'smartsetup/form.html',{'form':form,'title':'Setup Chart category'})

@login_required
def list_chartcategory(request, pk=None):
    # chartcategory = get_object_or_404(ChartCategory, pk=pk)
    chartcategories = ChartCategory.objects
    fieldCols = ['Category Code','Category Name']

    args ={'fieldCols':fieldCols,'chartcategories':chartcategories}
    return render(request, 'smartsetup/list_chartcategory.html',args)

# @login_required
# def chartcategory_with_pk(request, pk=None):
#     if request.method == 'POST':
#         form = ChartCategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         if pk:
#             chartcategory = ChartCategory.objects.get(pk=pk)
#             form = ChartCategoryForm(instance=chartcategory)
#         else:
#             # chartcategory = request.chartcategory
#             form = ChartCategoryForm()
#     return render(request,'smartsetup/form.html',{'form':form,'title':'Setup Chart category'})


@login_required
def chartsubcategory(request):
    if request.method == 'POST':
        form = ChartSubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_chartsubcategory')
    else:
            form = ChartSubCategoryForm()
    return render(request,'smartsetup/form.html',{'form':form,'title':'Setup Chart category'})


@login_required
def list_chartsubcategory(request, pk=None):
    chartcategories = ChartSubCategory.objects
    fieldCols = ['Account Code','Account Name','Notes','Category']
    # chartcategoriesMain = UserProfileForm(instance=user.userprofile)
    args ={'fieldCols':fieldCols,'chartcategories':chartcategories}
    return render(request, 'smartsetup/list_chartsubcategory.html',args)

@login_required
def financialperformance(request):
    revenues = ChartSubCategory.objects.filter(category_code_id=1)
    expenses = ChartSubCategory.objects.filter(category_code_id=2)

    args = {'revenues':revenues,'expenses':expenses}
    return render (request, 'smartsetup/financialperformance.html',args)

@login_required
def financialposition(request, pk=None):
    curr_assets = ChartSubCategory.objects.filter(category_code_id=3)
    curr_liabilities = ChartSubCategory.objects.filter(category_code_id=5)
    noncurr_assets = ChartSubCategory.objects.filter(category_code_id=4)
    noncurr_liabilities = ChartSubCategory.objects.filter(category_code_id=6)

    args = {'curr_assets':curr_assets,'curr_liabilities':curr_liabilities,
            'noncurr_assets':noncurr_assets,'noncurr_liabilities':noncurr_liabilities}
    return render (request, 'smartsetup/financialposition.html',args)




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
