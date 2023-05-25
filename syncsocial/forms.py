from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class CreateUserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField()

class AddFriendsForm(forms.Form):
    email = forms.EmailField()

class AddFreeDatesForm(forms.Form):
    date = forms.DateField()
    time = forms.TimeField()
