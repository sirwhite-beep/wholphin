from django.contrib import admin
from . models import Complaint, Enrol, Enroldetail

admin.site.register(Complaint)
admin.site.register(Enrol)
admin.site.register(Enroldetail)
# Register your models here.
