# Generated by Django 3.2.7 on 2021-11-05 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_duty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='career',
            field=models.DateField(blank=True),
        ),
    ]
