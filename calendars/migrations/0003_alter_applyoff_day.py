# Generated by Django 3.2.7 on 2021-10-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0002_alter_applyoff_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyoff',
            name='day',
            field=models.DateField(),
        ),
    ]
