from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request


class CreateUserForm(UserCreationForm):
    full_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'full_name']


class AddFriendsForm(forms.Form):
   email = forms.EmailField()




class AddFreeDatesForm(forms.Form):
   date = forms.DateField()