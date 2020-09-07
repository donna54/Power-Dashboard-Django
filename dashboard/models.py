from django.db import models

# Create your models here.

class AgeGroupDetails(models.Model):
    agegroup = models.CharField(max_length=6)
    totalcases = models.IntegerField()
    percentage = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Covid_19_India(models.Model):
    date = models.CharField(max_length=10)
    time = models.TimeField()
    state = models.CharField(max_length=20)
    confirmed_indian_national = models.CharField(max_length=10)
    confirmed_foreign_national = models.CharField(max_length=10)
    cured = models.CharField(max_length=10)
    deaths = models.CharField(max_length=10)
    confirmed = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class HospitalBedsIndia(models.Model):
    state = models.CharField(max_length=30)
    numPrimaryHealthCenters_HMIS = models.CharField(max_length=10)
    numCommunityHealthCenters_HMIS = models.CharField(max_length=10)
    numSubDistrictHospitals_HMIS = models.CharField(max_length=10)
    numDistrictHospitals_HMIS = models.CharField(max_length=10)
    totalPublicHealthFacilities_HMIS = models.CharField(max_length=10)
    numPublicBeds_HMIS = models.CharField(max_length=10)
    numRuralHospitals_NHP18 = models.CharField(max_length=10)
    numRuralBeds_NHP18 = models.CharField(max_length=10)
    numUrbanHospitals_NHP18 = models.CharField(max_length=10)
    numUrbanBeds_NHP18 = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class ICMRTestingLabs(models.Model):
    lab = models.TextField()
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class IndividualDetails(models.Model):
    pid = models.CharField(max_length=10)
    government_id = models.CharField(max_length=10)
    diagnosed_date = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)
    detected_city = models.CharField(max_length=20)
    detected_district = models.CharField(max_length=20)
    detected_state = models.CharField(max_length=20)
    nationality = models.CharField(max_length=10)
    current_status = models.CharField(max_length=10)
    status_change_date = models.CharField(max_length=10)
    notes = models.TextField()

    def __str__(self):
        return self.name

class Population_India_Census2011(models.Model):
    state = models.CharField(max_length=20)
    population = models.CharField(max_length=10)
    rural_population = models.CharField(max_length=10)
    urban_population = models.CharField(max_length=10)
    area = models.CharField(max_length=20)
    density = models.CharField(max_length=20)
    gender_ratio = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class StatewiseTestingDetails(models.Model):
    date = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    totalsamples = models.CharField(max_length=10)
    negative = models.CharField(max_length=10)
    positive = models.CharField(max_length=10)

    def __str__(self):
        return self.name