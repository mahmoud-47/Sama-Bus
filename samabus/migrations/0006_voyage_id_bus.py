# Generated by Django 3.1.5 on 2021-03-16 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samabus', '0005_bus_place_max'),
    ]

    operations = [
        migrations.AddField(
            model_name='voyage',
            name='id_bus',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='samabus.bus'),
        ),
    ]