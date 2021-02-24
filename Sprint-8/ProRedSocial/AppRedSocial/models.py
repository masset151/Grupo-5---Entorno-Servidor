from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class User(models.Model):
    id_user = models.IntegerField(primary_key=True,max_length=100,unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264,unique=True)
    nick =  models.CharField(unique=True,max_length=30)
    

    def __int__(self):
        return self.id_user
