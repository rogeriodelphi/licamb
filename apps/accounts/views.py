from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# from .forms import UserForm, UserProfileForm, UserFormChangeInformation
# from .models import UserProfile


def user_login(request):
    template_name = 'accounts/user_login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', '/cadastros/vacinas/site/'))
        else:
            messages.error(request, "Usuário ou senha inválidos!")
    return render(request, template_name, {})