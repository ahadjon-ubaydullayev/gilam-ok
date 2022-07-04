from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    full_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=256, blank=True, null=True)
    active = models.BooleanField(default=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Products(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=256, blank=True, null=True)
    active = models.BooleanField(default=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE)


class RawMaterial(models.Model):
    material_name = models.CharField(max_length=256, blank=True, null=True)
    size = models.CharField(max_length=128, blank=True, null=True)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=256, blank=True, null=True)
    active = models.BooleanField(default=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE)