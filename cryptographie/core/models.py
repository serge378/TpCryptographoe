from django.db import models

# Create your models here.


class Resultat(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    r = models.IntegerField()
    solution = models.BooleanField()
