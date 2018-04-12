from django.db import models

# Create your models here.
class ArrestData(models.Model):
    _id = models.TextField()
    PK = models.TextField()
    CCR = models.TextField()
    AGE = models.TextField()
    GENDER = models.TextField()
    RACE = models.TextField()
    ARRESTTIME = models.TextField()
    ARRESTLOCATION = models.TextField()
    OFFENSES = models.TextField()
    INCIDENTLOCATION = models.TextField()
    INCIDENTNEIGHBORHOOD = models.TextField()
    INCIDENTZONE = models.TextField()
    INCIDENTTRACT = models.TextField()
    COUNCIL_DISTRICT = models.TextField()
    PUBLIC_WORKS_DIVISION = models.TextField()
    X = models.TextField()
    Y = models.TextField()

  
# class Pet(models.Model):
#     SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
#     name = models.CharField(max_length=100)
#     breed = models.CharField(max_length=30, blank=True)
#     description = models.TextField()
#     sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
#     submission_date = models.DateTimeField()
#     age = models.IntegerField(null=True)
#     vaccinations = models.ManyToManyField('Vaccine', blank=True)

# class Vaccine(models.Model):
#     name = models.CharField(max_length=50)