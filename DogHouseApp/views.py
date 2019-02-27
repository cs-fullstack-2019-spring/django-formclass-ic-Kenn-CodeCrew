from django.shortcuts import render
from django.http import HttpResponse
from .forms import HouseLoanForm, DogAdoption


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

    if(request.method == 'POST'):
        print(request.POST)
        context = {"name": request.POST["name"]}
        return render(request, "DogHouseApp/loanResults.html", context)
    else:
        newForm = HouseLoanForm()
        context = {
            "newForm": newForm,
        }
        return render(request, "DogHouseApp/loan.html", context)


def dog(request):

    newForm = DogAdoption()

    context = {
        "newForm": newForm
    }

    return render(request, "DogHouseApp/dogApplication.html", context)


def dogResults(request):
    print(request.POST)
    return HttpResponse("Look in server console")