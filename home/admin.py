from django.contrib import admin

# Register your models here.
from .models import itrrequest

class itrreq(admin.ModelAdmin):
    list_display = ['FatherName','DateOfBirth','state','city','pan','aadhar','bankname','bankaccount','ifsccode','form16']

admin.site.register(itrrequest,itrreq)