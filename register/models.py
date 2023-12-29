"import essentials libraries:"
from django.db import models
from django.contrib.auth.models import User


class User_Profile(models.Model):
    """
              class creates below fields in database
             :param: user, gender, Currency_type, balance
             :return: table in database

             """
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Currency_CHOICES = (
        ('GBP','UK Pounds'),
        ('USD','US Dollars'),
        ('EUro','EUro')

    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Currency_type=models.CharField(max_length=10,choices=Currency_CHOICES,default='GBP')
    balance=models.DecimalField(max_digits=10,decimal_places=2,default=1000.00)
