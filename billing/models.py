from django.db import models

from django.conf import settings

class State(models.TextChoices):
    PAID = "PAID"
    UNPAID = "UNPAID"
    CANCELLED = "CANCELLED"

class Invoice(models.Model):


    User= models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date = models.DateField()
    due_date=models.DateField()
    state = models.CharField(max_length=15, choices= State.choices, default= State.UNPAID)

    def __str__(Self):
        return f" {Self.User}'s invoice"

class ItemLine(models.Model):
    Invoice = models.ForeignKey(to=Invoice, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    texted = models.BooleanField()

                            
                               

# Create your models here.
