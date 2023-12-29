"""import essential libraries :"""
from django.shortcuts import render, redirect
from notifications.admin import Notification
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from .models import User_Profile
from notifications.models import Notification



@csrf_protect
def homepage(request):
    """
              function displays context in homepage
             :param: request
             :return:  'registration/home.html': for rendering context
             :return: user, converted_amount, currency_type, notification
             """
    user = auth.get_user(request)

    if not user.is_anonymous:
        balance_profile = User_Profile.objects.get(user=user)
        balance = balance_profile.balance
        Currency_type=balance_profile.Currency_type

        return render(request, 'registration/home.html', {'user': user, 'balance': balance,'currency_type':Currency_type ,'notification': Notification.objects.filter(recipient=user)
                                                          })
    else:
        return render(request, 'registration/home.html')



@csrf_protect
def register_user(request):
    """
              function displays register form
             :param: request
             :return:  'registration/sign-up.html': for rendering context
             :return: register_user
             """
    if request.method == 'POST':
        my_form = RegistrationForm(request.POST)

        if my_form.is_valid():
            user = my_form.save()
            login(request, user)
            return redirect('homepage')
        else:
            my_form.add_error(None, 'unsuccessful registration. Invalid information')
    else:
        my_form = RegistrationForm()
    return render(request, 'registration/sign-up.html', {'register_user': my_form})



@csrf_protect
def login_user(request):
    """
              function displays login form
             :param: request
             :return:  'registration/login.html': for rendering context
             :return: login_user
             """
    if request.method == 'POST':
        new_form = AuthenticationForm(request, data=request.POST)
        if new_form.is_valid():
            username = new_form.cleaned_data.get('username')
            password = new_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_authenticated and user.is_superuser:
                    return redirect('admin-homepage')
                else:
                     messages.info(request, f"you are now logged in as {username}")
                     return redirect('homepage')
            else:
                new_form.add_error(None, 'invalid username or password')
        else:
            new_form.add_error(None, 'invalid username or password')
    else:
        new_form = AuthenticationForm()

    return render(request, 'registration/login.html', {'login_user': new_form})


#@login_required
@requires_csrf_token
def logout_user(request):
    """
              function logs the users out
             :param: request
             :return:  webapps2023 page

             """
    logout(request)
    return redirect('/webapps2023/')
