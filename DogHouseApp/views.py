from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Working on more forms")

def loanForm(request):

    context = {

    }

    return render(request, "DogHouseApp/index.html", context)