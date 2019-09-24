from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from smartsetup.models import (UserProfile,ChartCategory,ChartSubCategory)
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserProfileForm(forms.ModelForm):
    # image = forms.ImageField(required=False)
    # signature = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = (
            'job_description',
            'city',
            'website',
            'phone',
            'image',
            'signature',
        )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=256, help_text='Required. Inform a valid email address.')
    # description = forms.Textarea(queryset=UserProfile.objects.select_related())

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2',)

class EditProfileForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label= ("Password"),
    help_text= ("Raw passwords are not stored, so there is no way to see "
                "this user's password, but you can change the password "
                "using <a href=\"password\">this form</a>."))
    class Meta:
        model = User
        # exclude = () this can be used to specify fields to exclude'
        fields = ('email','first_name','last_name',)

class ChartCategoryForm(forms.ModelForm):
    class Meta:
        model = ChartCategory
        fields = ('category_code','category_name')

class ChartSubCategoryForm(forms.ModelForm):
    class Meta:
        model = ChartSubCategory
        fields = ('category_code','sub_category_code','sub_category_name','notes')
