from django.db import models
from apps.transaction.models import Transaction
from apps.user.models import User, Subject

# Create your models here.

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    tran_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subeject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ])