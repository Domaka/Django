from email.headerregistry import Address
from operator import length_hint
from django.db import models

# Create your models here.
class school(models.Model):
    name = models.CharField(max_length=23)
    Address = models.CharField(max_length=23)

    def __str__(self) -> str:
          return self.name

class country(models.Model):
        name = models.CharField(max_length=23)

        
    def __str__(self) -> str:
          return self.name