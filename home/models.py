from django.db import models

# Create your models here.
class itrrequest(models.Model):
    FatherName = models.CharField(max_length=100,default="",blank=False,null=True)
    DateOfBirth = models.DateField(max_length=100,blank=False,default="",null=True)
    state = models.CharField(max_length=100,blank=False,default="",null=True)
    city = models.CharField(max_length=200,default="",blank=False,null=True)
    pan = models.CharField(max_length=500,default="",blank=False,null=True)
    aadhar = models.CharField(max_length=500,default="",blank=False,null=True)
    bankname = models.CharField(max_length=100,default="",blank=False,null=True)
    bankaccount = models.CharField(max_length=1000,default="",blank=False,null=True)
    ifsccode = models.CharField(max_length=100,default="",blank=False,null=True)
    form16 = models.FileField(upload_to='',default="Upload form 16 here",blank=True)
