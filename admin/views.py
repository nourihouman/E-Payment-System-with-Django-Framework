"""import essential libraries: """

from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from payapp.models import Transcation, Request
from register.models import User_Profile
from .forms import admin_RegistrationForm



@csrf_protect
def admin_homepage(request):
    """
              function displays homepage
             :param: request
             :return:  'registration/home.html', admin/home.html: for rendering context
             :return: user
             """
    user = auth.get_user(request)
    if request.user.is_superuser:
        return render(request, 'admin/home.html', {'user': user})
    else:
        return render(request, 'registration/home.html')





@csrf_protect
def overseas_account(request):
    """
              function displays users' information
             :param: request
             :return:  'admin/userinfo.html ': for rendering context
             :return: register_user
             """
    if request.user.is_superuser and request.user.is_authenticated:
        user_info=User_Profile.objects.all().select_related('user')
        multiple_pages=Paginator(user_info,10)
        page_num=request.GET.get('page')
        new_page_information=multiple_pages.get_page(page_num)

        return render(request, 'admin/userinfo.html', {'new_page_information':  new_page_information})
    else:
        messages.warning(request,'You do not have permission to access admin pages')
        return redirect('homepage')



@csrf_protect
def overseas_transaction(request):
    """
              function displays users' transactions
             :param: request
             :return:  'admin/traninfo.html': for rendering context
             :return: new_page_transaction
             """
    if request.user.is_superuser and request.user.is_authenticated:
        tran_info=Transcation.objects.all().select_related('sender','recipient')
        multiple_pages=Paginator(tran_info,10)
        page_num=request.GET.get('page')
        new_page_transaction=multiple_pages.get_page(page_num)

        return render(request, 'admin/traninfo.html', {'new_page_transaction':new_page_transaction})
    else:
        messages.warning(request,'You do not have permission to access admin pages')
    return redirect('homepage')



@csrf_protect
def overseas_request(request):
    """
              function displays users' money requests
             :param: request
             :return:  'admin/requestinfo.html': for rendering context
             :return: new_page
             """
    if request.user.is_superuser and request.user.is_authenticated:
        request_info=Request.objects.all().select_related('requester','sender')
        multiple_pages=Paginator(request_info,10)
        page_num=request.GET.get('page')
        new_page=multiple_pages.get_page(page_num)

        return render(request, 'admin/requestinfo.html', {'new_page':new_page})
    else:
        messages.warning(request,'You do not have permission to access admin pages')
    return redirect('homepage')


@user_passes_test(lambda user: user.is_superuser,login_url='/webapps2023/homepage')
@login_required(login_url='/webapps2023/')
@csrf_protect
def admin_register(request):
    """
              function registers new superuser
             :param: request
             :return:  'admin/sign-up.html': for rendering context
             :return: register_admin
             """
    if request.method == 'POST':
        my_form = admin_RegistrationForm(request.POST)
        if my_form.is_valid():
            user = my_form.save()
            user.is_superuser=True
            user.is_staff=True
            user.save()
            return redirect('admin-homepage')
    else:
        #messages.info(request, 'unsuccessful registration. Invalid information')
        my_form = admin_RegistrationForm()
    return render(request, 'admin/sign-up.html', {'register_admin': my_form})