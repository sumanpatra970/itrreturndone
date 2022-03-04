from django.contrib import admin

from .models import itrrequest

class itrreq(admin.ModelAdmin):
    list_display = ['FatherName','DateOfBirth','state','city','pan','aadhar','bankname','bankaccount','ifsccode','form16']

admin.site.register(itrrequest,itrreq)