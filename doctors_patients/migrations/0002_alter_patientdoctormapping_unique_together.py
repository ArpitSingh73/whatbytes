# Generated by Django 5.2 on 2025-04-13 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
        ('doctors_patients', '0001_initial'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='patientdoctormapping',
            unique_together={('patient', 'doctor')},
        ),
    ]
