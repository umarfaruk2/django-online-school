from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


class RegisterView(FormView):
    template_name = 'accounts/signup.html'
    form_class = RegisterForm

    def form_valid(self, form):
        form.save()
        return redirect('login')


def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST) 
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username = user_name, password = user_password)

                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = AuthenticationForm() 
        return render(request, 'accounts/login.html', {'form': form})
    else:
        return redirect('home')


def userLogout(request):
    logout(request)
    return redirect('login')