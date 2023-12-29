
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class admin_RegistrationForm(UserCreationForm):
    """
              class creates below fields
             :param: email, username
             :return: None
             """
    email=forms.EmailField(required=True)
    username=forms.CharField(max_length=150)

    class Meta:
        model=User
        fields=['username','email','password1','password2','is_superuser','is_staff']


