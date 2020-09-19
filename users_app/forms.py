from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterFrom(UserCreationForm):
  email = forms.EmailField()
  first_name = forms.CharField()
  last_name = forms.CharField(required=False)
  

  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2'] # fields to be showen
 

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField(required=False)
  username = forms.CharField(required=False)
  class Meta:
    model = User
    fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
  image = forms.ImageField(required=False)
  class Meta:
    model = Profile
    fields = ['image']

