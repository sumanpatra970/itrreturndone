# Generated by Django 4.0.2 on 2022-03-03 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='itrrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FatherName', models.CharField(default='', max_length=100)),
                ('DateOfBirth', models.DateField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=200)),
                ('pan', models.CharField(default='', max_length=500)),
                ('aadhar', models.CharField(default='', max_length=500)),
                ('bankname', models.CharField(default='', max_length=100)),
                ('bankaccount', models.CharField(default='', max_length=1000)),
                ('ifsccode', models.CharField(default='', max_length=100)),
                ('form16', models.FileField(blank=True, default='NA', upload_to='')),
            ],
        ),
    ]
