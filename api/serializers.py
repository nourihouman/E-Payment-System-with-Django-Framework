from rest_framework import serializers
from .models import converting_currency


class convert_currencySerializer(serializers.ModelSerializer):
    """
     optional part without any functionality in the project
               class displays below fields in database
              :param: all field in model
              :return:  None

              """
    class Meta:
        model=converting_currency
        fields= '__all__'
