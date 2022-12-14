from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Fone(models.Model):
    carName = models.CharField(max_length=255, default="Car Name")
    carModel = models.CharField(max_length=255, default="Car Model")
    carFactory = models.CharField(max_length=255, default="Factory")
    driver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ratingDriver = models.IntegerField()
    trophyDriver = models.IntegerField()
    founder = models.CharField(max_length=256, default="Founder")

    def __str__(self):
        return self.carName


class Circuits(models.Model):
    circuits_Name = models.CharField(max_length=255, default="circuits Name")
    circuits_length = models.CharField(max_length=255, default="circuits length")
    circuits_laps = models.CharField(max_length=255, default="circuits laps")
    circuits_distance = models.IntegerField()
    circuits_speed = models.IntegerField()
    circuits_city = models.CharField(max_length=256, default="circuits city")

    def __str__(self):
        return self.circuits_Name
