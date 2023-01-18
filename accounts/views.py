from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from service_listing.decorators import verified_user_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
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
            context = {
                'id': new_user.id,
                'name': new_user.email
            }
            send_custom_email(request.POST['email'], context)
            login(request, new_user)
            return redirect('profile')
    else:
        form = RegisterForm()
        return render(request, 'accounts/signup.html', {'form': form})


@login_required
# @verified_user_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, 'welcome!')
            return redirect('profile')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def verified(request):
    return render(request, 'accounts/verified.html')


def send_custom_email(to_email, context):
    subject = 'Custom Email Subject'
    html_message = render_to_string('mails/account.html', context)
    from_email = 'sender@example.com'
    send_mail(subject, '', from_email, [to_email], html_message=html_message)


def email(request):
    return render(request, 'mails/account.html')
