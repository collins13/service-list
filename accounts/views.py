from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data["password"]
            )  # call `set_password(...)` with "raw password"
            new_user.save()
            # messages.info(
            #     request, "Thanks for registering. You are now logged in.")
            # new_user = authenticate(username=form.cleaned_data['username'],
            #                         password=form.cleaned_data['password'],
            #                         )
            login(request, new_user)
            return redirect('profile')
    else:
        form = RegisterForm()
        return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user is not None)
            if user is not None:
                login(request, user)
                # redirect to a success page
                return redirect('profile')
        else:
            # return redirect('login')
            pass
            # return an 'invalid login' error message
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
