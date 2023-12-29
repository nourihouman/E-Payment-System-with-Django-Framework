"""webapps2023 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, re_path
from django.contrib import admin
from django.urls import include, path
from register import views as register_views
from payapp import views as payapp_views
from django.views.generic import RedirectView

import notifications.urls

urlpatterns = [
    path('webapps2023/admin/',include('admin.urls')),
    path('',RedirectView.as_view(url='webapps2023/')),
    path('webapps2023/', include('register.urls')),
    path('register/', register_views.register_user, name='webapps2023/sign-up'),
    path('login/', register_views.login_user, name='webapps2023/login'),
    path('logout/', register_views.logout_user, name='logout'),
    path('webapps2023/homepage/', register_views.homepage,name='homepage'),
    path('webapps2023/profile/', payapp_views.money_transfer, name='profile'),
    path('webapps2023/transcation-history/',payapp_views.transcation_history,name='transaction-history'),
    path('webapps2023/request-money/', payapp_views.request_money, name='request-money'),
    path('webapps2023/request-response/', payapp_views.request_response_table, name='request-response'),
    path('webapps2023/accept_request/', payapp_views.accept_request, name='request-accept'),
    #path('user-notification/', payapp_views.user_notification, name='user-notification'),
    re_path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('webapps2023/api/', include('api.urls')),



]
