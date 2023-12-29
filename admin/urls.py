""""import essential libraries:"""
from django.urls import path
from admin import views
""""define route for functions of view"""
urlpatterns = [
    path('', views.admin_homepage, name='admin-homepage'),
    path('homepage/', views.admin_homepage, name='admin-homepage'),
    path('users-information/', views.overseas_account, name='admin-users-information'),
    path('transaction-information/', views.overseas_transaction, name='admin-transaction-information'),
    path('request-information/', views.overseas_request, name='admin-request-information'),
    path('admin-register/', views.admin_register, name='admin-register')
]
