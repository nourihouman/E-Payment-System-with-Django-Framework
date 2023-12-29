"""import essential libraries:"""
from django.urls import path
from . import views

"""define routes for functions of view"""
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout')
]
