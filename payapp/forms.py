from django import forms



class TransactionForm(forms.Form):
    """
              class creates fields
             :param:  recipient, amount,reference
             :return:  None

             """
    recipient = forms.CharField(max_length=20, required=True, label="recipient")
    amount = forms.DecimalField(required=True, min_value=1, max_value=10000)
    reference=forms.CharField(max_length=10,required=True,label='reference')

    def clean(self):
        # Running all cleaning checks
        cleaned_data = super().clean()
        recipient = cleaned_data.get("recipient")
        amount = cleaned_data.get("amount")

    class Meta:
        fields = ['recipient', 'amount','reference']


class MoneyRequestForm(forms.Form):
    """
              class displays creates below fields
             :param:  requester, amount, reference
             :return:  table in database

             """
    requester = forms.CharField(max_length=20, required=True, label="recipient")
    amount = forms.DecimalField(required=True, min_value=1, max_value=10000)
    reference=forms.CharField(max_length=10,required=True,label="reference")

    class Meta:
        fields = ['requester', 'amount','reference']
