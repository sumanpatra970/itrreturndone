from django.db import models

# Create your models here.
class itrrequest(models.Model):
    FatherName = models.CharField(max_length=100,default="",blank=False)
    DateOfBirth = models.DateField(max_length=100,blank=False,default="")
    state = models.CharField(max_length=100,blank=False,default="")
    city = models.CharField(max_length=200,default="",blank=False)
    pan = models.CharField(max_length=500,default="",blank=False)
    aadhar = models.CharField(max_length=500,default="",blank=False)
    bankname = models.CharField(max_length=100,default="",blank=False)
    bankaccount = models.CharField(max_length=1000,default="",blank=False)
    ifsccode = models.CharField(max_length=100,default="",blank=False)
    form16 = models.FileField(upload_to='media/',default="NA",blank=True)
