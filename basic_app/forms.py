from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,GithubUsers,Contact

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')

class GithubUsersForm(forms.ModelForm):
    class Meta():
        model=GithubUsers
        fields=('git_username',)

class ContactForm(forms.ModelForm):
    class Meta():
        model=Contact
        fields=('contact_message',)
