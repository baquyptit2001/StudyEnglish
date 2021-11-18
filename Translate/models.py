from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Languages(models.Model):
    namelang=CharField(max_length=30)
    code=CharField(max_length=30)
    