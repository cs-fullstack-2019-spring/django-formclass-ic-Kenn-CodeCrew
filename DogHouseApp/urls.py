from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('loanForm/', views.loanForm, name="loanForm"),
    path('gotHouseInfo/', views.gotHouseInfo, name="gotHouseInfo"),
    path('loan/', views.loan, name="loan"),
]