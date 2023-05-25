from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User, FreeDate
from .forms import LoginForm, CreateUserForm, AddFriendsForm, AddFreeDatesForm

def home(request):
    # Logic for the home page
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect the user to the desired page (e.g., home.html)
            return redirect('home')
        else:
            # Handle invalid login credentials (e.g., display an error message)
            return render(request, 'login.html', {'error': 'Invalid email or password.'})
    else:
        return render(request, 'login.html')

def create_user(request):
    if request.method == 'POST':
        # Logic for handling create user form submission
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Create a new user based on the form data
            # Redirect to appropriate page after user creation
            pass
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
