# Generated by Django 4.1.7 on 2023-03-14 16:23

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WindPowerPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('wind_direction', models.DecimalField(decimal_places=2, max_digits=5)),
                ('entity', models.CharField(max_length=100)),
                ('canton', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('altitude', models.IntegerField()),
                ('power_supplied', models.DecimalField(decimal_places=2, max_digits=10)),
                ('zone', models.CharField(choices=[('urban', 'Urban'), ('rural', 'Rural')], max_length=10)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('document', models.FileField(upload_to='documents/')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('last_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolarPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('field_strength', models.DecimalField(decimal_places=2, max_digits=5)),
                ('panel_angle', models.DecimalField(decimal_places=2, max_digits=5)),
                ('entity', models.CharField(max_length=100)),
                ('canton', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zone', models.CharField(choices=[('urban', 'Urban'), ('rural', 'Rural')], max_length=10)),
                ('altitude', models.IntegerField()),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('document', models.FileField(upload_to='documents/')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('last_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
