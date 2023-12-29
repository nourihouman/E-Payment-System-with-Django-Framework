""""import essential libraries"""
from django.db import models

class converting_currency(models.Model):
    """
    this class is just for visualization purposes and it does not serve any functionality in this project
               class displays below fields in database
              :param: from_currency, to_currency, rate
              :return:  table in database

              """
    from_currency=models.CharField(max_length=10)
    to_currency=models.CharField(max_length=10)
    rate=models.DecimalField(max_digits=8,decimal_places=3,default='1')
