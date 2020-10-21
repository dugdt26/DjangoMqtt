from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class PostMqtt(models.Model):
    temp = models.FloatField()
    hud = models.FloatField()
    pm1 = models.FloatField()
    pm2 = models.FloatField()
    pm3 = models.FloatField()

def __str__(self):
        return f"Temp: {self.temp}, Hud: {self.hud}, Pm1: {self.pm1}, Pm2:{self.pm2}, Pm3:{self.pm3}"