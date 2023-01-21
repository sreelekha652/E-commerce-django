from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    confirm_password=models.CharField(max_length=100,null=True,blank=True)

class adcontact(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)

class itemcart(models.Model):
    product=models.CharField(max_length=100,null=True,blank=True)

    quantity=models.CharField(max_length=100,null=True,blank=True)
    totalprice=models.CharField(max_length=100,null=True,blank=True)


