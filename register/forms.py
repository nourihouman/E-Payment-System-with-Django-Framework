""""import essential libraries: """

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from payapp.views import get_response
from .models import User_Profile

class RegistrationForm(UserCreationForm):
    """
              class creates below fields
             :param: email, first_name, last_name, gender, Currency_type
             :return: None
             """
    email=forms.EmailField(required=True)
    first_name=forms.CharField(max_length=150)
    last_name=forms.CharField(max_length=150)
    gender=forms.ChoiceField(choices=User_Profile.GENDER_CHOICES)
    Currency_type=forms.ChoiceField(choices=User_Profile.Currency_CHOICES)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2','gender','Currency_type']


    def save(self):
        user = super(RegistrationForm, self).save()

        # Saving Registration Profile with User, Currency and Balance.
        currency = self.cleaned_data['Currency_type']
        balance = get_response(f"convert_currency/GBP/{currency}/1000")
        User_Profile(user=user,gender=self.cleaned_data['gender'],Currency_type=currency, balance=balance).save()
        return user
