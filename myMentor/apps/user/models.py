from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female')
    ])

class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    field = models.CharField(max_length=30)
    price = models.FloatField()
    numberSession = models.IntegerField()
    subType = models.CharField(max_length=5, choices=[
        ('on', 'Online'),
        ('off', 'Offline')
    ])
