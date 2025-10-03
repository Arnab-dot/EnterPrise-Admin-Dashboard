from tkinter.font import names

from django.db import models

from users.models import Organization, CustomUser


# Create your models here.
class Clients(models.Model):
    username=models.CharField(max_length=100)
    user_address=models.CharField(max_length=100)
    dob=models.DateField()
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name="clients")
    phone_no=models.BigIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="clients")
    updated_by = models.ForeignKey(CustomUser, related_name='clients_updated', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Invoice(models.Model):
    status_choices=[
        ("overdue","Overdue"),
        ("paid","Paid"),
        ("draft","Draft"),
        ("sent","Sent")

    ]
    client=models.ForeignKey(Clients,on_delete=models.CASCADE,related_name="invoice_client")
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name="invoice_org")
    due_date=models.DateField()
    status=models.CharField(max_length=10,choices=status_choices,default="draft")
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="invoice_created_by")
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    updated_by = models.ForeignKey(CustomUser, related_name='clients_updated_Invoice', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.username}:{self.amount}:{self.status}"
    