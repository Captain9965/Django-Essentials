# Generated by Django 4.0.6 on 2022-08-04 06:43

from django.db import migrations, models
import modelApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('modelApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemodels',
            name='engine_capacity',
            field=models.IntegerField(validators=[modelApp.models.validate_engine_capacity]),
        ),
    ]
