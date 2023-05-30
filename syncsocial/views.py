from django.shortcuts import render, redirect
from .models import  FreeDate, Friend
from django.contrib.auth.models import User
from .forms import LoginForm, CreateUserForm, AddFriendsForm, AddFreeDatesForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def home(request):
   # Logic for the home page
   return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the user from the form
            login(request, user)  # Authenticate and login the user
            return redirect('home')
    else:
        form = LoginForm(request=request, data=request.POST)
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


@login_required
def add_friends(request):
    if request.method == 'POST':
        form = AddFriendsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Check if the friendship already exists
            existing_friendship = Friend.objects.filter(user=request.user, friend__email=email).exists()
            if existing_friendship:
                messages.warning(request, "You have already added this friend.")
            else:
                friend = User.objects.filter(email=email).first()
                if friend:
                    # Create a Friend object to represent the friendship
                    Friend.objects.create(user=request.user, friend=friend)
                    messages.success(request, f"{friend.username} has been added as a friend.")
                else:
                    messages.error(request, "No user found with the provided email.")
            
            return redirect('add_friends')
    else:
        form = AddFriendsForm()
    return render(request, 'addfriends.html', {'form': form})

@login_required
def add_free_dates(request):
    if request.method == 'POST':
        form = AddFreeDatesForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            # Create a FreeDate object for the current user
            FreeDate.objects.create(user=request.user, date=date, time=time)
            messages.success(request, "Free date added successfully.")
            return redirect('add_free_dates')
    else:
        form = AddFreeDatesForm()
    return render(request, 'addfreedates.html', {'form': form})
def notifications(request):
    # Logic for the notifications page
    return render(request, 'notifications.html')