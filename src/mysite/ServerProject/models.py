from django.db import models

# Create your models here.
class ServerProject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=3000)
    status = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    who_create = models.IntegerField(default=0)
    length = models.IntegerField(default=0)