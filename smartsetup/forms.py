from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from smartsetup.models import UserProfile

class UserProfileForm(forms.ModelForm):
    # description  = forms.CharField(blank=True,max_length=100, default='')
    # city = forms.CharField(max_length=100, default='')
    # website = forms.URLField(default='')
    # phone =   forms.PhoneField(blank=True, help_text='Contact phone number')
    # image = models.ImageField(upload_to='images/profilepix/', blank=True)
    # signature = models.ImageField(upload_to='images/signature/', blank=True)

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
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User

        # def get_queryset(self):
        #     return User.objects.select_related()
        # exclude = () this can be used to specify fields to exclude'
        fields = (
            'email',
            'first_name',
            'last_name',
        )
