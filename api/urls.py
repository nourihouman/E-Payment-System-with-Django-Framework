"import essential libraries:"
from django.urls import path, include
from api import views

"""define url routes for functions of view"""
urlpatterns=[
    path('', views.conversionlist.as_view()),
    path('currency-rate/',views.conversionlist.as_view()),
    #path('api/convert_currency/<int:pk>/')
    path('convert_currency/<str:from_currency>/<str:to_currency>/<amount>/', views.convert_currency, name='convert_currency')

]