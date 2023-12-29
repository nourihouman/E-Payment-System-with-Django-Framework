"""import essential libraries: """
from django.urls import path, include
from . import views

"""defining routes path"""

urlpatterns = [
    path('profile/', views.money_transfer, name='profile'),
    path('profile/transcation-history/',views.transcation_history,name='transaction-history'),
    path('request-money/', views.request_money, name='request-money'),
    #path('user-notification/', views.user_notification, name='user-notification')
    path('notifications/', include('notifications.urls'))
    ]