from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload-csv', views.agegroupdetails_upload),
    path('upload-covid-19-india', views.covid_19_india_upload),
    path('upload-hospital-beds-india', views.hospitalbedsindia_upload),
    path('upload-icmr-testing-labs', views.icmrtestinglabs_upload),
    path('upload-individual-details', views.individualdetails_upload),
    path('upload-population-census', views.populationindiacensus2011_upload),
    path('upload-statewise-testing-details', views.statewisetestingdetails_upload),
]