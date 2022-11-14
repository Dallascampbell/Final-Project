from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return render(request, 'GainPages/index.html')

def aboutPageView(request):
    return render(request, 'GainPages/about.html')

def calculatorView(request) :
    return render(request, 'GainPages/calculators.html')

def liftTypeView(request) :
    return render(request, 'GainPages/lifts.html')

def bodyTypeView(request) :
    return render(request, 'GainPages/bodyTypes.html')

def crudTableView(request) :
    return render(request, 'GainPages/crudTable.html')
