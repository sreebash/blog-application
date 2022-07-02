from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm, LoginForm


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Your have signup successfully!')
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Login Successfully!')
        return response


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.warning(request, 'User deleted successfully!')
    return redirect('accounts:user_list')
