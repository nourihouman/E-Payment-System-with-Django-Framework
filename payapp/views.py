""""import essential libraries :"""
import datetime
import json

from django.db import transaction
from django.views.decorators.csrf import csrf_protect
from _decimal import Decimal
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Transcation, Request
from .forms import TransactionForm, MoneyRequestForm
from register.models import User_Profile
from notifications.signals import notify
import requests
from django.contrib.auth.decorators import login_required



def get_response(endpoint):
    """
                 function hits the api app url.
                :param: endpoint
                :return:  dictionary by deserializing the json format
                """
    url=f"http://localhost:8000/webapps2023/api/{endpoint}/"
    response=requests.get(url)
    return json.loads(response.content)


@login_required(login_url='/webapps2023/')
@csrf_protect
def money_transfer(request):
    """
                function transfers money from sender to recipient
               :param: request: http request object received by function
               :return:  form
               :return:   payment/profile.html: a rendered template
               """
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            recipient_username = form.cleaned_data['recipient']
            amount = form.cleaned_data['amount']
            reference=form.cleaned_data['reference']

            if request.user.username==recipient_username:
                form.add_error('recipient','You can not transfer to your own account')
                return render(request, 'payment/profile.html', {'form': form})
            try:

                recipient_user = User.objects.get(username=recipient_username)
                recipient_User_Profile = User_Profile.objects.get(user_id=recipient_user.pk)

            except User.DoesNotExist:
                form.add_error(None, 'Recipient username does not exist')
                return render(request, 'payment/profile.html', {'form': form})

            sender_profile = User_Profile.objects.get(user=request.user)
            try:
                with transaction.atomic():
                    if sender_profile.balance < amount:
                        form.add_error('amount', 'Insufficient balance')
                        return render(request, 'payment/profile.html', {'form': form})

                    # original amount
                    sender_profile.balance -= amount
                    sender_profile.save()

                    # converted amount for recipient

                    converted_amount=get_response(f"convert_currency/{sender_profile.Currency_type}/{recipient_User_Profile.Currency_type}/{amount}")
                    recipient_User_Profile.balance += Decimal(converted_amount)
                    recipient_User_Profile.save()

                    Transcation.objects.create(sender=request.user, recipient=recipient_user, amount=amount,
                                       transfer_type='send',reference=reference)
                    messages.success(request, 'Money transfered successfully')
                    return redirect('/webapps2023/profile/')
            except:
                form.add_error(None, 'Transaction cannot be proceeded.')
                return render(request, 'payment/profile.html', {'form': form})
    else:
        form = TransactionForm()

    return render(request, 'payment/profile.html', {'form': form})


@login_required(login_url='/webapps2023/')
@csrf_protect
def transcation_history(request):
    """
                function displays user's 10 transaction in each page.
               :param: request: http request object recivied by function
               :return:  trabsaction_table.html: rendered template for displaying
               :return:  new_page : paginated list of transactions

               """
    user = auth.get_user(request)
    transaction_history = Transcation.objects.filter(sender_id=user.pk)
    multiple_pages=Paginator(transaction_history,10)
    page_num=request.GET.get('page')
    new_page=multiple_pages.get_page(page_num)
    return render(request, 'payment/transaction_table.html', {'new_page': new_page})



@login_required(login_url='/webapps2023/')
@csrf_protect
def request_money(request):
    """
                function displays user's money request.
               :param: request: http request object recivied by function
               :return:  payment/request_money.html: rendered template for displaying request
               :return:  form : fields that contain objects

               """
    if request.method == 'POST':

        form = MoneyRequestForm(request.POST)

        if form.is_valid():
            requester = form.cleaned_data['requester']
            amount = form.cleaned_data['amount']
            reference=form.cleaned_data['reference']
            try:
                requester = User.objects.get(username=requester)
            except User.DoesNotExist:
                form.add_error('requester', 'Recipient username does not exist')
                return render(request, 'payment/request_money.html', {'form': form})

            if requester == request.user:
                form.add_error('requester', 'Unknown inquiry')
            else:

                request_object = Request(requester=requester, sender=request.user,
                                         amount=amount, reference=reference,timestamp=datetime.datetime.now(),
                                         )
                request_object.save()
                notify.send(sender=request.user,recipient=requester,verb='has requested money from you',
                            level='INFO', public=False)
                messages.success(request, 'Money request sent successfully')
                return redirect('homepage')

        else:
            form = MoneyRequestForm(request.POST)
    else:
        form = MoneyRequestForm()
    return render(request, 'payment/request_money.html', {'form': form})


#@login_required
@csrf_protect
def request_response_table(request):
    """
              :param: request: http request object recivied by function
              :return:  money_request
              :return: payment/request_response/html: render template for showing request response

              """
    requests = Request.objects.filter(requester=request.user)
    return render(request, 'payment/request_response.html', {'money_requests': requests})



@login_required(login_url='/webapps2023/')
def accept_request(request):
    """
               function displays user's response to money request from other users
              :param: request: http request object recivied by function
              :return:  None

              """

    if request.method == 'GET':
        request_id = request.GET.get('request_id')
        action = request.GET.get('action')
        money_request = Request.objects.get(id=request_id)
        if request_id and action:
            if action == 'accept':
                if money_request.requester == request.user:
                    money_request.approved = True
                    money_request.approved_at = timezone.now()

                    requester_profile = User_Profile.objects.get(user=money_request.requester)
                    sender_profile = User_Profile.objects.get(user=money_request.sender)

                    converted_amount = get_response(f"convert_currency/{sender_profile.Currency_type}/{requester_profile.Currency_type}/{money_request.amount}")

                    if requester_profile.balance >= Decimal(converted_amount):
                        sender_profile.balance += money_request.amount
                        sender_profile.save()

                        #money_request.new_amount = convert_currency(sender_profile.Currency_type, requester_profile.Currency_type,money_request.amount)

                        requester_profile.balance -= Decimal(converted_amount)
                        requester_profile.save()

                        Transcation.objects.create(sender=money_request.requester, recipient=money_request.sender,
                                                   amount=converted_amount, transfer_type='request')
                        money_request.transfer_status = 'successful'
                        money_request.save()

                    else:
                        messages.error(request, 'Insufficient balance')
                else:
                    messages.error(request, 'unknown request')
            elif action == 'decline':
                money_request.declined = True
                money_request.transfer_status = 'cancelled'
                money_request.save()
            return redirect('/webapps2023/homepage/')

    else:
        messages.error(request, 'Invalid request')
    return None

















