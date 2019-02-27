from django.shortcuts import render
from django.http import HttpResponse
from .forms import HouseLoanForm


# Create your views here.
def index(request):
    return HttpResponse("Working on more forms")

def loanForm(request):
    newForm = HouseLoanForm()

    context = {
        "newForm": newForm
    }

    return render(request, "DogHouseApp/index.html", context)


def gotHouseInfo(request):
    print(request.POST)
    print(request.POST["name"])
    return HttpResponse("Got House Info")


def loan(request):
    newForm = HouseLoanForm()
    context = {
        "newForm": newForm,
    }
    return render(request, "DogHouseApp/loan.html", context)
