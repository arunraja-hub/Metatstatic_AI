# Generated by Django 2.2.6 on 2019-10-31 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('narwhals', '0004_auto_20191031_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='histologic_grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='ml_prediction',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='patient',
            name='pathology_report',
            field=models.TextField(default='HyperLink'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='patients', to='narwhals.Doctor'),
        ),
    ]
