from django.db import models

# Create your models here.
from django.db import models


class StatsMessage(models.Model):
    customerId = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=8, decimal_places=3)
    uuid = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
