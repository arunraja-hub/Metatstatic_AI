# Generated by Django 2.2.7 on 2019-11-28 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('narwhals', '0003_auto_20191125_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='patients', to='narwhals.Doctor'),
        ),
        migrations.AlterField(
            model_name='patientimage',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_image', to='narwhals.Patient'),
        ),
    ]
