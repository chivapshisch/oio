from django.db import models

class Cars(models.Model):
    type = models.CharField(max_length= 200)
    number = models.CharField(max_length= 6)
    price = models.IntegerField()
    
