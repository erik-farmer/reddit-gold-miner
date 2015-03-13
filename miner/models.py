from django.db import models

class GoldMeasure(models.Model):
  timestamp = models.IntegerField()
  value = models.IntegerField()