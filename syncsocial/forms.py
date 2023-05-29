from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(request=self.request, email=email, password=password)

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('User not found. Please check your email and password.')

        if user is None:
            raise forms.ValidationError('Invalid credentials. Please check your email and password.')

        cleaned_data['user'] = user
        return cleaned_data

class CreateUserForm(UserCreationForm):
    full_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already associated with an account.')

        return email

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'full_name']


class AddFriendsForm(forms.Form):
   email = forms.EmailField()




class AddFreeDatesForm(forms.Form):
   date = forms.DateField()
   time = forms.TimeField()