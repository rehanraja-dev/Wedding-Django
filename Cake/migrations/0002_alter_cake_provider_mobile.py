# Generated by Django 4.1.6 on 2023-03-20 15:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake_provider',
            name='mobile',
            field=models.CharField(default='9155007890', max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
