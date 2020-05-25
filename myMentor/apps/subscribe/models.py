from django.db import models
from apps.transaction.models import Transaction
from apps.user.models import User

# Create your models here.

class Subscription(models.Model):
    subID = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subType = models.CharField(max_length=10, choices=[
        ('monthly', 'Monthly'),
        ('anually', 'Anually')
    ])
    period = models.IntegerField()
