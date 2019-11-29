from django.db import models

# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    occupant_no = models.IntegerField()
    # admin = models.ForeignKey(User)
    
    
class User(models.Model):
    name = models.CharField(max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood)
    email=models.CharField(max_length =60)
    
    
class Business(models.Model):
    business_name= models.CharField(max_length =30)
    user= models.ForeignKey(User)
    neighbourhood=models.ForeignKey(Neighbourhood)
    business_email=models.EmailField()
    
