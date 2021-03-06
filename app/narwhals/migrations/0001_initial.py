# Generated by Django 2.2.7 on 2019-11-28 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('histologic_grade', models.IntegerField(default=0)),
                ('ml_prediction', models.FloatField(default=0.0)),
                ('pathology_report', models.TextField(default='HyperLink')),
                ('last_modified', models.DateField(auto_now=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='patients', to='narwhals.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='PathologyScan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pathology_Main_Img', models.FileField(upload_to='images/')),
                ('ml_prediction', models.FloatField(default=0.0)),
                ('jpg_file', models.CharField(blank=True, max_length=100, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pathology_images', to='narwhals.Patient')),
            ],
        ),
    ]
