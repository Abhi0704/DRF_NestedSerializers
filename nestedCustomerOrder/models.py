from django.db import models

# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=11)

class Order(models.Model):
    product = models.CharField(max_length=20)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer,related_name='order', on_delete=models.CASCADE)
