# Generated by Django 4.2.19 on 2025-02-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickmeapp', '0003_alter_vehicle_allow_daily_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='allow_daily',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='seating_capacity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicleimage',
            name='image',
            field=models.ImageField(upload_to='vehicles/'),
        ),
    ]
