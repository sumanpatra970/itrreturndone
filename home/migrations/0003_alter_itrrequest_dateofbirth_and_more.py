# Generated by Django 4.0.2 on 2022-03-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_itrrequest_form16'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itrrequest',
            name='DateOfBirth',
            field=models.DateField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='itrrequest',
            name='FatherName',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='itrrequest',
            name='aadhar',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='itrrequest',
            name='bankaccount',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='itrrequest',
            name='bankname',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='itrrequest',
            name='city',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='itrrequest',
            name='ifsccode',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='itrrequest',
            name='pan',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='itrrequest',
            name='state',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
