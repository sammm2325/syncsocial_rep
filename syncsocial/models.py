from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField('self', blank=True)

class FreeDate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()