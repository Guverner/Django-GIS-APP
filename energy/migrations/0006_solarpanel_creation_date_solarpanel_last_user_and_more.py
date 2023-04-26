# Generated by Django 4.1.7 on 2023-03-30 16:41

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('energy', '0005_alter_solarpanel_canton_alter_solarpanel_entity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solarpanel',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='solarpanel',
            name='last_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solarpanel',
            name='modification_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='windpowerplant',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='windpowerplant',
            name='last_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='windpowerplant',
            name='modification_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='city',
            field=models.CharField(default='grad', max_length=100),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='entity',
            field=models.CharField(choices=[('RS', 'Republika Srpska'), ('FBiH', 'Federacija Bosne i Hercegovine'), ('BD', 'Brčko distrikt')], default='entitet', max_length=50),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='field_strength',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT (0 0)', srid=4326),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='city',
            field=models.CharField(default='grad', max_length=100),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='entity',
            field=models.CharField(choices=[('RS', 'Republika Srpska'), ('FBiH', 'Federacija Bosne i Hercegovine'), ('BD', 'Brčko distrikt')], default='entitet', max_length=50),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT (0 0)', srid=4326),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='power_supplied',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]