from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(AgeGroupDetails)
admin.site.register(Covid_19_India)
admin.site.register(HospitalBedsIndia)
admin.site.register(ICMRTestingLabs)
admin.site.register(IndividualDetails)
admin.site.register(Population_India_Census2011)
admin.site.register(StatewiseTestingDetails)