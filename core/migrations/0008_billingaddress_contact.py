# Generated by Django 2.2.4 on 2021-01-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200510_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='contact',
            field=models.IntegerField(null=True),
        ),
    ]
