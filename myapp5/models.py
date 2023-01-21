from django.db import models

# Create your models here.
class admindatabase(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    mobile_number = models.IntegerField( null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)
    userid= models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    confirm_password = models.CharField(max_length=30, null=True, blank=True)

class categorydb(models.Model):
    category_name= models.CharField(max_length=30, null=True, blank=True)
    discription= models.CharField(max_length=30, null=True, blank=True)
    image= models.ImageField(upload_to="profile", null=True, blank=True)

class productdb(models.Model):
    category= models.CharField(max_length=30, null=True, blank=True)
    productname = models.CharField(max_length=30,null=True, blank=True)
    productprice_per_kg = models.IntegerField(null=True, blank=True)
    product_quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)


