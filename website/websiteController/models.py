from django.db import models
from django.forms import ModelForm

# Create your models here.
class Palaute(models.Model):
    nimi = models.CharField(max_length=50)
    palaute = models.TextField(max_length=1000)
    sposti = models.EmailField(max_length=150)

    def __str__(self):
        return self.palaute