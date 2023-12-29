'import essentail libraries :'
from django.db import models
from django.contrib.auth.models import User



class Transcation(models.Model):
    """
    one option is that consider these field as a return and param None. I used the second option which is:
               class displays below fields in database
              :param: sender, recipient, amount, timestamp,transfer_type, reference
              :return:  table in database

              """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transactions')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=3)
    timestamp = models.DateTimeField(auto_now_add=True)
    Transfer_Type = (
        ('send', 'Send'),
        ('request', 'Request'))

    transfer_type = models.CharField(max_length=10, choices=Transfer_Type, default='')
    reference = models.CharField(max_length=100, null=False, default='')


class Request(models.Model):
    """
              class displays below fields in database
             :param: Transfer_Status, requester, sender, amount,timestamp, approved,declined,approved at,reference
             :return:  table in database

             """
    Transfer_Status = (
        ('successful', 'successful'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled')
    )
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfer_receiver')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfer_sender')
    amount = models.DecimalField(max_digits=8, decimal_places=3)
    timestamp = models.DateTimeField(auto_now_add=True)
    declined = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(null=True, blank=True)
    reference = models.CharField(max_length=100, null=False, default='')
    transfer_status = models.CharField(max_length=10,default='pending')


