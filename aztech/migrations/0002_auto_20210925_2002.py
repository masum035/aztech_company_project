# Generated by Django 3.2.7 on 2021-09-25 14:02

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('aztech', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwarecompany',
            name='company_address',
            field=models.TextField(blank=True, max_length=256, null=True, verbose_name='company-office-address'),
        ),
        migrations.AlterField(
            model_name='softwarecompany',
            name='company_phone',
            field=phone_field.models.PhoneField(max_length=31, verbose_name='company-official-phone-number'),
        ),
    ]