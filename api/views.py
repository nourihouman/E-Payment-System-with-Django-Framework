""""import essential libraries"""
import decimal
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework import generics
from .models import converting_currency
from .serializers import convert_currencySerializer


class conversionlist(generics.ListCreateAPIView):
    """
    optional part without any functionality
              :param: serializer_class
              :return:  None
              """
    serializer_class = convert_currencySerializer
    def get_queryset(self):
        queryset= converting_currency.objects.all()
        return queryset


class conversion_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    one option is that consider these field as a return and param None. I used the second option which is:
               class displays below fields in database
              :param: sender, recipient, amount, timestamp,transfer_type, reference
              :return:  table in database

              """
    serializer_class = convert_currencySerializer
    queryset = converting_currency.objects.all()




@csrf_protect
def convert_currency(request,from_currency, to_currency, amount):
    """
              function converts 3 types of currency
             :param: request, from_currency, to_currency, amount
             :return:  amount in form of json
             """
    amount = decimal.Decimal(amount)
    rate = {'GBP': decimal.Decimal(1), 'USD': decimal.Decimal(1.2), 'EUro': decimal.Decimal(1.14)}
    if from_currency not in rate or to_currency not in rate:
        error_message = 'One or both currencies are not supported'
        response_data = {'error': error_message}
        return JsonResponse(response_data,status=400)
    else:
        if from_currency != 'GBP':
            amount = amount / rate[from_currency]
            amount = amount * rate[to_currency]
        else:
            amount = amount * rate[to_currency]

    return JsonResponse(round(amount,2),safe=False)
