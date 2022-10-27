from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    text = "This is the Home page"
    return HttpResponse(text)

def calculatorView(request) :
    text = "This is the calculator Page"
    return HttpResponse(text)

def liftTypeView(request) :
    text = "This is the lift page"
    return HttpResponse(text)

def bodyTypeView(request) :
    text = "This is the body type page"
    return HttpResponse(text)

def crudTableView(request) :
    text = "This is the crud table"
    return HttpResponse(text)
