from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=100)
    collegecatagory = models.CharField(max_length=50)
    ccode = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos')
    banner = models.ImageField(upload_to='banners')
    about = models.TextField()
    city = models.CharField(max_length=50)
    address = models.TextField()
    website = models.URLField(max_length=200)
    gmaplink = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    mobile = models.BigIntegerField()
    ad_banner1 = models.ImageField( upload_to=('adsection1'))
    ad_2 = models.ImageField( upload_to=('adsection2'))
    ad_footer1 = models.ImageField( upload_to=('adsection4'))
    date_updated = models.DateTimeField(auto_now=True)
class Coursedetails(models.Model):
    ccode1 = models.CharField(max_length=50)
    coursetype = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
class Collegecatagories(models.Model):
    catagory = models.CharField(max_length=50)
    catagorylogo = models.ImageField(upload_to='catagorylogos')
