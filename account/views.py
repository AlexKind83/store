from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")
                return redirect('store:main_page')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы успешно зарегестрированы")
            return redirect('store:main_page')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'account/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return redirect('account:profile')
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'account/profile.html', context)


def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect('store:main_page')
