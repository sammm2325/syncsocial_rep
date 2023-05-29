from django.shortcuts import render, redirect
from .models import User, FreeDate
from .forms import LoginForm, CreateUserForm, AddFriendsForm, AddFreeDatesForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
   # Logic for the home page
   return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def createuser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')  # Get the email from the form data
            first_name, last_name = full_name.split(' ', 1)
            user.first_name = first_name
            user.last_name = last_name
            user.username = email  # Set the email as the username
            user.email = email  # Set the email
            user.save()
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'createuser.html', {'form': form})

def add_friends(request):
   if request.method == 'POST':
       # Logic for handling add friends form submission
       form = AddFriendsForm(request.POST)
       if form.is_valid():
           # Add friends to the current user based on the form data
           # Redirect to appropriate page after adding friends
           pass
   else:
       form = AddFriendsForm()
   return render(request, 'addfriends.html', {'form': form})

def add_free_dates(request):
   if request.method == 'POST':
       # Logic for handling add free dates form submission
       form = AddFreeDatesForm(request.POST)
       if form.is_valid():
           # Add free dates for the current user based on the form data
           # Redirect to appropriate page after adding free dates
           pass
   else:
       form = AddFreeDatesForm()
   return render(request, 'addfreedates.html', {'form': form})

def notifications(request):
   # Logic for the notifications page
   return render(request, 'notifications.html')
