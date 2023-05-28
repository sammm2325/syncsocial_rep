from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
   email = forms.EmailField()
   password = forms.CharField(widget=forms.PasswordInput)


class CreateUserForm(UserCreationForm):
    name = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name']

class AddFriendsForm(forms.Form):
   email = forms.EmailField()


class AddFreeDatesForm(forms.Form):
   date = forms.DateField()
   time = forms.TimeField()
