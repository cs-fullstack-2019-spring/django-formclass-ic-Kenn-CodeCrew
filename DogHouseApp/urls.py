from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('oldForm/', views.loanForm, name="loanForm"),
    path('gotHouseInfo/', views.gotHouseInfo, name="gotHouseInfo"),
    path('newForm/', views.loan, name="loan"),
]