from django.http import HttpResponse
from django.shortcuts import render
import csv, io
from .models import *
from django.template import RequestContext
from numpy import nan
from pandas import read_csv
from sklearn.impute import SimpleImputer

def index(request):
    template = "home.html"
    agegroupdetails = AgeGroupDetails.objects.all()
    covid19india = Covid_19_India.objects.all()
    hospitalbedsindia = HospitalBedsIndia.objects.all()
    icmrtestinglabs = ICMRTestingLabs.objects.all()
    individualdetails = IndividualDetails.objects.all()
    populationindiacensus2011 = Population_India_Census2011.objects.all()
    statewisetestingdetails = StatewiseTestingDetails.objects.all()

    prompt = {
        'agegroupdetails': agegroupdetails,
        'covid19india': covid19india,
        'hospitalbedsindia': hospitalbedsindia,
        'icmrtestinglabs': icmrtestinglabs,
        'individualdetails': individualdetails,
        'populationindiacensus2011': populationindiacensus2011,
        'statewisetestingdetails': statewisetestingdetails,
    }

    return render(request, template, prompt)

def agegroupdetails_upload(request):
    template = "home.html"

    csv_file = request.FILES['file']
    dataset = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(dataset)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = AgeGroupDetails.objects.update_or_create(
            agegroup = column[1],
            totalcases = column[2],
            percentage = column[3]
        )
    context = {}
    return render(request, template, context)

def covid_19_india_upload(request):
    template = "home.html"
    
    csv_file = request.FILES['file']
    dataset = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(dataset)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = Covid_19_India.objects.update_or_create(
            date = column[1],
            time = column[2],
            state = column[3],
            confirmed_indian_national = column[4],
            confirmed_foreign_national = column[5],
            cured = column[6],
            deaths = column[7],
            confirmed = column[8]
        )
    context = {}
    return render(request, template, context)

def hospitalbedsindia_upload(request):
    template = "home.html"

    csv_file = request.FILES['file']
    dataset = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(dataset)
    next(io_string)

    dataset = read_csv(io_string, header=None)
    values = dataset.values

    imputer = SimpleImputer(missing_values=nan, strategy="median")
    imputer.fit(values[:,4:5])
    values[:,4:5] = imputer.transform(values[:,4:5])

    for column in values:
        _, created = HospitalBedsIndia.objects.update_or_create(
            state = column[1],
            numPrimaryHealthCenters_HMIS = column[2],
            numCommunityHealthCenters_HMIS = column[3],
            numSubDistrictHospitals_HMIS = column[4],
            numDistrictHospitals_HMIS = column[5],
            totalPublicHealthFacilities_HMIS = column[6],
            numPublicBeds_HMIS = column[7],
            numRuralHospitals_NHP18 = column[8],
            numRuralBeds_NHP18 = column[9],
            numUrbanHospitals_NHP18 = column[10],
            numUrbanBeds_NHP18 = column[11]
        )

    context = {}
    return render(request, template, context)

def icmrtestinglabs_upload(request):
    template = "home.html"

    csv_file = request.FILES['file']
    dataset = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(dataset)
    next(io_string)
    for column in csv.reader(io_string, quotechar='"'):
        _, created = ICMRTestingLabs.objects.update_or_create(
            lab = column[0],
            address = column[1],
            pincode = column[2],
            city = column[3],
            state = column[4],
            type = column[5]
        )
    context = {}
    return render(request, template, context)

def individualdetails_upload(request):
    template = "home.html"

    csv_file = request.FILES['file']
    dataset = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(dataset)
    next(io_string)
    for column in csv.reader(io_string, quotechar='"'):
        _, created = IndividualDetails.objects.update_or_create(
            pid = column[0],
            government_id = column[1],
            diagnosed_date = column[2],
            age = column[3],
            gender = column[4],
            detected_city = column[5],
            detected_district = column[6],
            detected_state = column[7],
            nationality = column[8],
            current_status = column[9],
            status_change_date = column[10],
            notes = column[11]
        )
    context = {}
    return render(request, template, context)

def populationindiacensus2011_upload(request):
    template = "home.html"

    csv_file = request.FILES['file']
    dataset = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(dataset)
    next(io_string)
    for column in csv.reader(io_string, quotechar='"'):
        _, created = Population_India_Census2011.objects.update_or_create(
            state = column[1],
            population = column[2],
            rural_population = column[3],
            urban_population = column[4],
            area = column[5],
            density = column[6],
            gender_ratio = column[7]
        )
    context = {}
    return render(request, template, context)

def statewisetestingdetails_upload(request):
    template = "home.html"

    csv_file = request.FILES['file']
    dataset = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(dataset)
    next(io_string)

    dataset = read_csv(io_string, header=None)
    values = dataset.values

    imputer = SimpleImputer(missing_values=nan, strategy="most_frequent")
    imputer.fit(values[:,3:5])
    values[:,3:5] = imputer.transform(values[:,3:5])

    for column in values:
        _, create = StatewiseTestingDetails.objects.update_or_create(
            date = column[0],
            state = column[1],
            totalsamples = column[2],
            negative = column[3],
            positive = column[4]
        )
    context = {}
    return render(request, template, context)