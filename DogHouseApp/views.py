from django.shortcuts import render
from django.http import HttpResponse
from .forms import HouseLoan


# Create your views here.
def index(request):
    return HttpResponse("Working on more forms")

def loanForm(request):
    newForm = HouseLoan()

    context = {
        "newForm": newForm
    }

    return render(request, "DogHouseApp/index.html", context)


def gotHouseInfo(request):
    return HttpResponse("Got House Info")