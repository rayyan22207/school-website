from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            # Set the team_head field to request.user
            team = form.save(commit=False)
            team.team_head = request.user
            team.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = TeamForm()

    return render(request, 'create_team.html', {'form': form})

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def org_team(request):
    org_t = Org_team.objects.all()
    return render(request, 'org_t.html', {'org_t': org_t})