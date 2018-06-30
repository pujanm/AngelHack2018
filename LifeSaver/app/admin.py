from django.contrib import admin
from .models import Victim, HospitalUser, Hospitals, Disaster
# Register your models here.
admin.site.register(Victim)
admin.site.register(HospitalUser)
admin.site.register(Disaster)
admin.site.register(Hospitals)
