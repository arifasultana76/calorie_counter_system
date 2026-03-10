from django.shortcuts import render, redirect
from Calorie_Counter_app.forms import *
from Calorie_Counter_app.models import *
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Sum


@login_required
def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'auth/changepassword.html', {'form': form})

@login_required
def logout_page(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    user = request.user
    
    weight = user.weight or 0
    height = user.height or 0
    age = user.age or 0

    bmr = 0

    if weight > 0 and height > 0 and age > 0:
        if user.gender == 'Male':
            bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
        else:
            bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

    user_entries = CalorieEntryModel.objects.filter(user=user)

    total_consumed = user_entries.aggregate(Sum('calories_consumed'))['calories_consumed__sum'] or 0

    context = {
        'bmr': round(bmr, 2),
        'total_consumed': total_consumed,
        'user': user,
    }

    return render(request, 'master/home.html', context)

@login_required
def add_calorie_entry(request):
    form = CalorieForm()
    if request.method == 'POST':
        form = CalorieForm(request.POST)
        if form.is_valid():
            calorie_entry = form.save(commit=False)
            calorie_entry.user = request.user
            calorie_entry.save()
            return redirect('home')

    return render(request, 'master/form.html', {'form': form})

@login_required
def view_calorie_entries(request):
    entries = CalorieEntryModel.objects.filter(user=request.user).order_by('-date')
    return render(request, 'calorie/calorie.html', {'entries': entries})




    









