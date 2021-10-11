from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# from django.db.models.deletion import CASCADE

# Create your models here.
class Term(models.Model):
    term_name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.term_name
    
class Vocabulary(models.Model):
    word = models.CharField(max_length=100)
    define = models.CharField(max_length=100)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.word
        