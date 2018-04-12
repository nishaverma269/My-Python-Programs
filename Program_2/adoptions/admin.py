from django.contrib import admin

# Register your models here.
from .models import ArrestData

@admin.register(ArrestData)
class ArrestDataAdmin(admin.ModelAdmin):
    list_display = ['_id', 'PK', 'CCR', 'AGE', 'GENDER', 'RACE', 'ARRESTTIME', 'ARRESTLOCATION', 'OFFENSES', 'INCIDENTLOCATION', 'INCIDENTNEIGHBORHOOD', 'INCIDENTZONE', 'INCIDENTTRACT', 'COUNCIL_DISTRICT', 'PUBLIC_WORKS_DIVISION', 'X', 'Y']

#password is n*******3