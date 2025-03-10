# Generated by Django 5.0.7 on 2024-10-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrationapp', '0002_patientslist_delete_patientlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Register_Number', models.CharField(max_length=20, unique=True)),
                ('Name', models.CharField(max_length=100)),
                ('Time', models.CharField(max_length=100)),
                ('Reason', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='PatientsList',
        ),
    ]
