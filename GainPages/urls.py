from django.urls import path
from .views import aboutPageView, indexPageView, calculatorView, liftTypeView, bodyTypeView, crudTableView


urlpatterns = [
    path("about/", aboutPageView, name="about"),
    path('', indexPageView, name='index'),
    path("calculators/", calculatorView, name="calculators"),
    path("lifts/", liftTypeView, name="lifts"),
    path("bodyTypes/", bodyTypeView, name="bodyTypes"),
    path("crudTable/", crudTableView, name="crudTable"),
]