from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    weight = models.IntegerField()
    full_name_owner = models.CharField(max_length=255)
    year_of_issue = models.DateField()

