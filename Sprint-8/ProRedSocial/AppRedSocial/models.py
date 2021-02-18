from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264,unique=True)
    nick =  models.CharField(unique=True,max_length=30)
    

    def __str__(self):
        return self.nick
