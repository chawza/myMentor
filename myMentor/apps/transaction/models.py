from django.db import models

# Create your models here.

class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=10, choices=[
        ('course', 'Course'),
        ('subs', 'Subscription')
    ])
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('unpaid', 'unpaid'),
        ('paid', 'paid')
    ])
    payment = models.CharField(max_length=20)
